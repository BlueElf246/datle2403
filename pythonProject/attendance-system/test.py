import face_recognition
import numpy as np
import face_recognition
import cv2
imgEmma=face_recognition.load_image_file('image/emma.jpg')
imgEmma=cv2.cvtColor(imgEmma,cv2.COLOR_BGRA2RGB)

imgTest=face_recognition.load_image_file('image/elle.jpg')
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGRA2RGB)

facLoc= face_recognition.face_locations(imgEmma)[0]
encodeEmma= face_recognition.face_encodings(imgEmma)[0]
cv2.rectangle(imgEmma,(facLoc[1],facLoc[2]),(facLoc[3],facLoc[0]),(255,0,255),2)

facLocTest= face_recognition.face_locations(imgTest)[0]
encodeTest= face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest,(facLocTest[1],facLocTest[2]),(facLocTest[3],facLocTest[0]),(255,0,255),2)

result= face_recognition.compare_faces([encodeEmma],encodeTest)
faceDis= face_recognition.face_distance([encodeEmma],encodeTest)
print(result,faceDis)
cv2.putText(imgTest,f'{result}{faceDis[0]}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
# cv2.imshow('emma',imgEmma)
cv2.imshow('emma',imgTest)
cv2.imshow('elle',imgEmma)
cv2.waitKey(0)