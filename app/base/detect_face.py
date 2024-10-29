import face_recognition
import cv2
import os

def load_image(image_path):
    """Load an image from a file path and return it as a numpy array."""
    if os.path.isfile(image_path):
        return face_recognition.load_image_file(image_path)
    else:
        raise FileNotFoundError(f"The image was not found in the path: {image_path}")

def main(image_path):
    # Load the image from the path provided.
    image = load_image(image_path)
    face_locations = face_recognition.face_locations(image)

    # Convert image to image format BGR (used by OpenCV)
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Draw a rectangle around the faces in the image using OpenCV.
    for face_location in face_locations:
        top, right, bottom, left = face_location
        cv2.rectangle(image_bgr, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(image_bgr, 'Rostro', (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show the image with the faces detected.
    cv2.imshow('Detect faces', image_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Change the image path as needed or use user input.
    image_path = input("Please, copy and paste (example: C:\\Users\\rasys\\Documents\\GitLab\\face-recognition-base\\images\\family-1-dad-2.jpg): ")
    try:
        main(image_path)
    except FileNotFoundError as e:
        print(e)