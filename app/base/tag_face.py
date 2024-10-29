import face_recognition
import cv2

# Load the image file.
image = face_recognition.load_image_file("./images/identification-1.jpg")
#image = face_recognition.load_image_file("../../images/family-1-dad-1.jpg")
#image = face_recognition.load_image_file("../images/family_2.jpg")
face_locations = face_recognition.face_locations(image)

# Convert image to image format BGR (used by OpenCV)
image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# Draw a rectangle around the faces in the image using OpenCV.
for face_location in face_locations:
    top, right, bottom, left = face_location
    cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 1)

# Get original dimensions
height, width = image_bgr.shape[:2]
aspect_ratio = width / height

# Resize the image to fit the screen or set a specific size
desired_width = 1440  # Set your desired width
#desired_height = 900  # Set your desired height
desired_height = int(desired_width / aspect_ratio)
resized_image = cv2.resize(image_bgr, (desired_width, desired_height))

# Show the image with the faces detected.
#cv2.imshow('Faces detected', image_bgr)
cv2.imshow('Faces detected', resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
