import tensorflow as tf
import os
import PIL
import cv2
import glob
import numpy as np
from tkinter import  *
from PIL import Image, ImageDraw, ImageGrab
def clear_widget():
    global cv
    cv.delete('all')

def activation_event(event):
    global lastx, lasty
    # B1-motion
    cv.bind('<B1-Motion>', draw_lines)
    lastx, lasty = event.x, event.y
def draw_lines(event):
    global lastx, lasty
    x,y= event.x, event.y
    #do the canvas drawings
    cv.create_line((lastx, lasty, x, y), width=8, fill='black', capstyle=ROUND, smooth=True, splinesteps=12)
    lastx, lasty= x,y
def Recognize_Digit():
    global image_number
    predictions=[]
    percentage=[]
    # image_number =0
    filename= f'image_{image_number}.png'
    widget= cv

    # get the widget coordinate
    x=root.winfo_rootx()+widget.winfo_x()
    y=root.winfo_rooty()+widget.winfo_y()
    x1= x+widget.winfo_width()
    y1=y+widget.winfo_height()

    #grab the image, crop it according to my requirement and saved it in png fomat
    ImageGrab.grab().crop((x,y,x1,y1)).save(filename)

    #read the image in color format
    image= cv2.imread(filename, cv2.IMREAD_COLOR)
    # convert the image in grayscale
    gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # applying Otsu thresholding
    ret, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    # find Contour() function helps in extracting the contours from the image
    contours= cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt in contours:
        # Get bounding box and extract ROI
        x,y,w,h= cv2.boundingRect(cnt)
        #create Rectangle
        cv2.rectangle(image, (x,y), (x+w,y+h), (255,0,0), 1)
        top=int(0.05 * th.shape[0])
        bottom= top
        left= int(0.05 * th.shape[1])
        right=left
        th_up= cv2.copyMakeBorder(th, top, bottom, left, right, cv2.BORDER_REPLICATE)
        # Extract the image ROI
        roi= th[y-top: y+h+bottom, x-left:x+w+right]
        #resize roi image to 28*28 pixels image
        img= cv2.resize(roi, (28,28), interpolation=cv2.INTER_AREA)
        print(img.shape)
        img= img.reshape(-1,28*28)
        print(img.shape)
        img=img/255
        pred=model.predict([img])[0]
        final_pred= np.argmax(pred)
        data= str(final_pred)+'  '+ str(int(max(pred)*100))+ '%'

        font=cv2.FONT_HERSHEY_SIMPLEX
        fontScale=0.5
        color= (255,0,0)
        thickness=1
        cv2.putText(image,data,(x,y-5), font, fontScale, color, thickness)
    cv2.imshow('image', image)
    cv2.waitKey(0)



#load model
model=tf.keras.models.load_model('../handwritten.model')

#create a main window first
root=Tk()
root.resizable(0,0)
root.title('Hand written Digit recognition GUI app')

#innitiate few variables
lastx, lasty= None, None
image_number=0

#create canvas for drawing
cv=Canvas(root, width=640, height=480, bg='white')
cv.grid(row=0, column=0, pady=2, sticky=W, columnspan=2)
#Tkinter provide mechanism to let you deal with events
cv.bind('<Button-1>', activation_event)

#Add button and label
btn_save=Button(text='Recognize digit', command=Recognize_Digit)
btn_save.grid(row=2, column=0, pady=1, padx=1)
button_clear= Button(text='Clear Widget', command= clear_widget)
button_clear.grid(row=2, column=1, pady=1, padx=1)


# mainloop() is used when your application is ready to run
root.mainloop()
