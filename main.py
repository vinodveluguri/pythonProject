import cv2
import numpy as py
import face_recognition

imgSony = face_recognition.load_image_file('Images/Sony.jpeg')
imgSony = cv2.cvtColor(imgSony, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgSony)[0]
encodSon = face_recognition.face_encodings(imgSony)[0]
cv2.rectangle(imgSony,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

cv2.imshow('Sony', imgSony)
cv2.waitKey(0)