# how to launch web cam more faster

import cv2

print(cv2.__version__)

width = 640
height = 360
xPos=int(width/2)
yPos=int(height/2)
radius=int(height/2)
borderThikness=1

def xPosCallback(val):
    global xPos
    xPos=val

def yPosCallback(val):
    global yPos
    yPos=val

def radiusCallback(val):
    global radius
    radius=val

def borderThiknessCallback(val):
    global borderThikness
    borderThikness=val

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) # setup cam codak

cv2.namedWindow('myTrackBar')
cv2.resizeWindow('myTrackBar', 400 , 150)
cv2.moveWindow('myTrackBar', width, 0)
cv2.createTrackbar('xPOs', 'myTrackBar', int(width/2), width, xPosCallback)
cv2.createTrackbar('yPos', 'myTrackBar', int(height/2), height, yPosCallback)
cv2.createTrackbar('Radius', 'myTrackBar', int(height/4), int(height/2), radiusCallback)
cv2.createTrackbar('Thikness', 'myTrackBar', 2, int(height/2), borderThiknessCallback)

while True:
    _ignore, frame = cam.read()

    cv2.circle(frame, (xPos, yPos), radius, (0, 255, 0), borderThikness)

    cv2.imshow('CAM', frame)
    cv2.moveWindow('CAM', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()