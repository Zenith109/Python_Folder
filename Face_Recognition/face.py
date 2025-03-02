import cv2
import numpy as np
from fer import FER
import os

# Initialize video capture from the default camera
video = cv2.VideoCapture(0)

# Load the pre-trained face detection model
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Initialize the emotion detector
detector = FER()

# List to store face data
faces_data = []
i = 0

# Create a directory to save the captured faces
if not os.path.exists('captured_faces'):
    os.makedirs('captured_faces')

def get_expression(image):
    """
    Detect emotions in the given image using the FER library.
    Returns a dictionary of emotions if detected, otherwise None.
    """
    result = detector.detect_emotions(image)
    if result:
        return result[0]['emotions']
    return None

while True:
    # Capture frame-by-frame
    ret, frame = video.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale frame
    faces = facedetect.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        # Crop the face from the frame
        crop_img = frame[y:y+h, x:x+w, :]
        
        # Resize the cropped face image
        resized_img = cv2.resize(crop_img, (50, 50))
        
        # Store face data every 10 frames, up to 100 faces
        if len(faces_data) <= 100 and i % 10 == 0:
            faces_data.append(resized_img)
            # Save the face image to disk
            cv2.imwrite(f'captured_faces/face_{len(faces_data)}.jpg', resized_img)
        
        i = i + 1
        
        # Display the number of faces stored on the frame
        cv2.putText(frame, str(len(faces_data)), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
        
        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 50, 255), 1)
        
        # Get the expression of the detected face
        expression = get_expression(crop_img)
        if expression:
            # Find the emotion with the highest score
            max_emotion = max(expression, key=expression.get)
            
            # Display the detected emotion on the frame
            cv2.putText(frame, max_emotion, (x, y-10), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
    
    # Display the resulting frame
    cv2.imshow("Frame", frame)
    
    # Break the loop if 'q' key is pressed
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
video.release()
cv2.destroyAllWindows()