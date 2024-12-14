# # Installing the libraries
# get_ipython().system('pip install cmake')
# get_ipython().system('pip install dlib')
# get_ipython().system('pip install face_recognition')
# # Importing the libraries
# import dlib
# import face_recognition
# import cv2
# import matplotlib.pyplot as plt
# # Reading the image for face detection using the face_recogntion library
# img = face_recognition.load_image_file(r"C:\Users\tushi\Downloads\PythonGeeks\tom cruise.jpg")

# # Displaying the original image
# plt.imshow(img)

# # Extracting the location of the face on the image using the face_locations function
# face = face_recognition.face_locations(img)[0]
# img_copy = img.copy()
# # Creating a bounding box around the detected face
# cv2.rectangle(img_copy, (face[3], face[0]),(face[1], face[2]), (0,255,0), 2)

# # Displaying the result
# plt.imshow(img_copy)

# # Training using the image read and creating encodings
# train_encodings = face_recognition.face_encodings(img)[0]
# train_encodings
# # Validating using the train encodings on another image read
# test = face_recognition.load_image_file(r"C:\Users\tushi\Downloads\PythonGeeks\tom cruise 2.jpg")

# # Creating encodings for the test image and comparing with encodings of the train image.
# test_encode = face_recognition.face_encodings(test)[0]
# print(face_recognition.compare_faces([train_encodings],test_encode))
# # Output for comparison is true
# True
# # Displaying the read image
# plt.imshow(test)

# # Extracting the location of the face on the image using the face_locations function 
# face = face_recognition.face_locations(test)[0]
# img_copy = test.copy()
# # Creating a bounding box around the detected face
# cv2.rectangle(img_copy, (face[3], face[0]),(face[1], face[2]), (0,255,0), 5)
# # Displaying the result
# plt.imshow(img_copy)