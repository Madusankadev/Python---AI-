import cv2
import numpy as np

print(cv2.__version__)

width=640
height=360

def hueMinSet(val):
    global hueMin
    hueMin=val

def hueMaxSet(val):
    global hueMax 
    hueMax=val

def satuMinSet(val):
    global satuMin 
    satuMin=val

def satuMaxSet(val):
    global satuMax 
    satuMax=val

def valueMinSet(val):
    global valueMin 
    valueMin=val

def valueMaxSet(val):
    global valueMax 
    valueMax=val

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myTrackbar')
cv2.resizeWindow('myTrackbar', 450, 300)
cv2.moveWindow('myTrackbar', width, 0)
cv2.createTrackbar('Hue Min ', 'myTrackbar', 10, 179, hueMinSet)
cv2.createTrackbar('Hue Max ', 'myTrackbar', 10, 179, hueMaxSet)
cv2.createTrackbar('Satu Min ', 'myTrackbar', 10, 255, satuMinSet)
cv2.createTrackbar('Satu Max ', 'myTrackbar', 10, 255, satuMaxSet)
cv2.createTrackbar('Value Min ', 'myTrackbar', 10, 255, valueMinSet)
cv2.createTrackbar('Value Max ', 'myTrackbar', 10, 255, valueMaxSet)

while True:
    _ignore, frame = cam.read()

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerBound = np.array([hueMin, satuMin, valueMin])
    upperBound = np.array([hueMax, satuMax, valueMax])
    myMask = cv2.inRange(frameHSV, lowerBound, upperBound)
    myObject = cv2.bitwise_and(frame, frame, mask=myMask)

    myMaskSmall = cv2.resize(myMask, (int(width/2), int(height/2)))
    cv2.imshow('mask', myMaskSmall)
    cv2.moveWindow('mask', 0, height)

    myObjectSmall = cv2.resize(myObject, (int(width/2), int(height/2)))
    cv2.imshow('object', myObjectSmall)
    cv2.moveWindow('object', int(width/2), height)

    cv2.imshow('CAM', frame)
    cv2.moveWindow('CAM', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()