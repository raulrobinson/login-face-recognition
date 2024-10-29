import cv2
from insightface.app import FaceAnalysis

# Initialize the BuffaloL model (change the providers according to your hardware).
app = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])

# Prepare the model for the execution.
app.prepare(ctx_id=0)

# Capture the video stream.
video_capture = cv2.VideoCapture(0)  # Webcam 0 embedded in the laptop.

while True:

    # Read the frame from the webcam.
    ret, frame = video_capture.read()

    # Check if the frame was captured.
    if not ret:
        print("Error accessing the camera")
        break

    # Convert the frame to RGB for the Buffalo model.
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the face detection.
    faces = app.get(frame_rgb)

    # Draw rectangles around the detected faces.
    for face in faces:
        box = face.bbox.astype(int)
        top, right, bottom, left = box[1], box[2], box[3], box[0]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Show the frame in an OpenCV window.
    cv2.imshow('Face detect in real-time', frame)

    # Exit the loop when the 'q' key is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows.
video_capture.release()
cv2.destroyAllWindows()
