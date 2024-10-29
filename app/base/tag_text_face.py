import cv2
import face_recognition

# Load the image file.
image = face_recognition.load_image_file("./images/family-1-dad-1.jpg")

# Convert image to image format BGR (used by OpenCV)
image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Detect the locations of the faces.
face_locations = face_recognition.face_locations(image)

# If you have names or references for each face (you can generate a list with the references)
references = [f"person_{i + 1}" for i in range(len(face_locations))]

# Draw rectangles and add labels to the image for each face.
for i, face_location in enumerate(face_locations):
    top, right, bottom, left = face_location

    # Draw a rectangle around the face.
    cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 1)

    # Set the reference text for the face (name or reference).
    reference_text = references[i]
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_color = (255, 255, 255)  # White color
    font_thickness = 1

    # Calculate the position to put the text (above the rectangle).
    text_position = (left, top - 10 if top - 10 > 10 else top + 10)

    # Set the text on the image.
    cv2.putText(image_bgr, reference_text, text_position, font, font_scale, font_color, font_thickness)

# Show the image with the faces and references.
cv2.imshow("Rostros detectados", image_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
