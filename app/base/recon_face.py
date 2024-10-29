import face_recognition

# Load the image with KNOWN image.
known_image = face_recognition.load_image_file("./images/family-1-dad-1.jpg")

# Load the image with UNKNOWN image.
#unknown_image = face_recognition.load_image_file("./images/family-1-dad-2.jpg")
unknown_image = face_recognition.load_image_file("./images/family-1-mom-2.jpg")

# Obtain the encodings of the faces in the images.
known_encoding = face_recognition.face_encodings(known_image)[0]
unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare the faces.
results = face_recognition.compare_faces([known_encoding], unknown_encoding)

if results[0]:
    print("It's the same person!")
else:
    print("Not the same person.")
