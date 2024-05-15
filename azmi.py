import cv2

min_contour_width = 30  
min_contour_height = 30  
offset = 10  
line_height = 550  
matches = []
cars = 0
time_since_last_count = 0  # Initialize the variable here

def get_centroid(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

# Load cascade classifier for cars
car_cascade = cv2.CascadeClassifier('cars.xml')

# Open video file
cap = cv2.VideoCapture('video2.mp4')

cap.set(3, 1920)
cap.set(4, 1080)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1920, 1080))

ret, frame1 = cap.read()
frame2 = frame1.copy()  # Inisialisasi frame2 dengan frame1

while ret:
    d = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        contour_valid = (w >= min_contour_width) and (h >= min_contour_height)

        if not contour_valid:
            continue

        cv2.rectangle(frame1, (x-10, y-10), (x+w+10, y+h+10), (255, 0, 0), 2)
        centroid = get_centroid(x, y, w, h)
        matches.append(centroid)
        cv2.circle(frame1, centroid, 5, (0, 255, 0), -1)
        cx, cy = get_centroid(x, y, w, h)

        if time_since_last_count <= 0:
            for (x, y) in matches:
                if y < (line_height+offset) and y > (line_height-offset):
                    cars += 1
                    matches.remove((x, y))
                    break  # No need for time_since_last_count update here

    # cv2.putText(frame1, "Total Cars Detected: " + str(cars), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 170, 0), 2)

    # Write the frame into the file 'output.avi'
    out.write(frame1)

    cv2.imshow("Vehicle Detection", frame1)

    if cv2.waitKey(1) == 27:
        break

    frame1 = frame2
    ret, frame2 = cap.read()  # Baca frame berikutnya
    time_since_last_count -= 1

# Release everything if job is finished
out.release()
cv2.destroyAllWindows()
cap.release()
