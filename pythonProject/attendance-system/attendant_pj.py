import face_recognition
import numpy as np
import face_recognition
import cv2
import os
from datetime import  datetime
path= 'image'
images=[]
classNames=[]
mylist= os.listdir(path)
print(mylist)
for cls in mylist:
    curent=cv2.imread(f'{path}/{cls}')
    images.append(curent)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)
def find_encoding(images):
    encodelist=[]
    for img in images:
        img=cv2.cvtColor(img,cv2.COLOR_BGRA2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist
def mark_attendance(name):
    with open('attendant.csv','r+') as f:
        myDatalist=f.readlines()
        nameList=[]
        for line in myDatalist:
            entry=line.split(', ')
            nameList.append(entry[0])
        if name not in nameList:
            now=datetime.now()
            dtstring= now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, {dtstring}')
encodeListKnow= find_encoding(images)
print('encoding_complete')

cap=cv2.VideoCapture(0)

while True:
    success,img=cap.read()
    imgS= cv2.resize(img,(0,0),None,0.25,0.25)
    imgS= cv2.cvtColor(imgS, cv2.COLOR_BGRA2RGB)

    facesCurframe = face_recognition.face_locations(imgS)

    encodeCurframe = face_recognition.face_encodings(imgS,facesCurframe)

    for encodeFace,FaceLoc in zip(encodeCurframe,facesCurframe):
        matches=face_recognition.compare_faces(encodeListKnow,encodeFace)
        faceDis=face_recognition.face_distance(encodeListKnow,encodeFace)
        print(faceDis)
        matchindex=np.argmin(faceDis)
        if matches[matchindex]:
            name=(classNames[matchindex]).upper()
            print(name)
            y1,x2,y2,x1= FaceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img, (x1,y1), (x2,y2), (255, 0, 255), 2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,123),2)
            mark_attendance(name)
    cv2.imshow('Webcame',img)
    cv2.waitKey(1)


# imgEmma=face_recognition.load_image_file('image/emma.jpg')
# imgEmma=cv2.cvtColor(imgEmma,cv2.COLOR_BGRA2RGB)
#
# imgTest=face_recognition.load_image_file('image/elle.jpg')
# imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGRA2RGB)