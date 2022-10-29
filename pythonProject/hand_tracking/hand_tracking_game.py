import mediapipe as mp
import cv2
import time
import handtracking_module
import math
import osascript
import re
pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector= handtracking_module.handDetector()
def change_volume(v):
    # result = osascript.osascript('get volume settings')
    # find = re.findall('output volume:\S+', result[1])
    # find = str(find)
    # find = find.split(':')
    # volume = int(find[1].replace(",']", ''))
    osascript.osascript("set volume output volume {}".format(v))
while True:
    success, img = cap.read()
    img=detector.findHands(img,)
    lst=detector.find_position(img,draw=False)
    if len(lst) !=0:
        (cx4,cy4)=lst[4][1],lst[4][2]
        (cx8,cy8) = lst[8][1], lst[8][2]
        cv2.circle(img, (cx4, cy4), 10, (0, 255, 255), cv2.FILLED)
        cv2.circle(img, (cx8, cy8), 10, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (cx4,cy4),(cx8,cy8), (155,56,133),9)
        length_of_vector=math.sqrt(((cx8-cx4)**2 + (cy8-cy4)**2)) # length from 18 to 372
        OldRange = (372 - 18)
        NewRange = (100 - 0)
        NewValue = (((length_of_vector - 18) * NewRange) / OldRange) + 0
        change_volume(NewValue)
    # print(results.multi_hand_landmarks)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)