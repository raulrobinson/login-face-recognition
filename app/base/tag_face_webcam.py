import face_recognition
import cv2

# Initialize the webcam for video capture in real-time.
video_capture = cv2.VideoCapture(0)  # The parameter 0 refers to the default webcam.

while True:
    # Capture frame-by-frame from the webcam.
    ret, frame = video_capture.read()

    # If the capture is successful.
    if not ret:
        print("Error al acceder a la cámara")
        break

    # Convert the frame from BGR (OpenCV format) to RGB (face_recognition format).
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect the face locations in the frame.
    face_locations = face_recognition.face_locations(frame_rgb)

    # Drawing rectangles around the faces.
    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 1)

        # Define the label for the detected face.
        label = "face"

        # Obtain the position for the text.
        label_position = (left, top - 10)

        # Draw the text on the image.
        cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Show the frame with the detected faces.
    cv2.imshow('Face detect in real-time', frame)

    # Exit the loop if the 'q' key is pressed.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows.
video_capture.release()
cv2.destroyAllWindows()
