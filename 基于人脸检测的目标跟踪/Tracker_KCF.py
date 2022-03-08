import cv2
import sys

# Set up tracker.
tracker = cv2.TrackerKCF_create()

# Read video
# video = cv2.VideoCapture(0)
video = cv2.VideoCapture("C:/Users/16426/Desktop/py/demo.mp4")
video.set(cv2.CAP_PROP_FRAME_WIDTH,1920)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)
video.set(cv2.CAP_PROP_FPS, 144)

# Exit if video not opened.
if not video.isOpened():
    print("Could not open video")
    sys.exit()

# Read first frame.
ok, frame = video.read()
if not ok:
    print("Cannot read video file")
    sys.exit()

# Face detection
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, None, fx=1, fy=1)
gray = cv2.equalizeHist(gray)
# Loading the face classifier
face_detector = cv2.CascadeClassifier("C:/Users/16426/Desktop/py/opencv-master/data/haarcascades/haarcascade_frontalface_alt.xml")
faces = face_detector.detectMultiScale(gray,1.2, 5)
n_faces = len(faces)
print(n_faces)
bbox = (0, 0, 0, 0)
bbox = faces[0]

# Initialize tracker with first frame and bounding box
tracker.init(frame,tuple(bbox))

while True:
    # Read a new frame
    ok, frame = video.read()
    if not ok:
        break

    # Start timer
    timer = cv2.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(frame)

    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    # Draw bounding box
    if ok:
        # # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 2)
    else:
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100, 340), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 6)

    # Display tracker type on frame
    cv2.putText(frame, "KCF Tracker", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 3, (50, 170, 50), 6)

    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100, 220), cv2.FONT_HERSHEY_SIMPLEX, 3, (50, 170, 50), 6)

    # Display result
    cv2.namedWindow("Tracking", 0)
    cv2.imshow("Tracking", frame)

    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27: break