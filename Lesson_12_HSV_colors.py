import cv2
import numpy as np
print(cv2.__version__)

width=640
height=360

evt=0

def MouseClick(event, xPos, yPos, flags, param):
    global clickX
    global clickY
    global evt
    if event==cv2.EVENT_LBUTTONUP:
        evt=event
        clickX=xPos
        clickY=yPos

    if event==cv2.EVENT_RBUTTONUP:
        evt=event
        

cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('cam')
cv2.setMouseCallback('cam', MouseClick)

while True:
    _ignore, frame = cam.read()

    if evt==cv2.EVENT_LBUTTONUP:
        global colorFrame
        colorFrame = np.zeros([250, 250, 3], dtype=np.uint8)
        color= frame[clickY][clickX]
        colorFrame[:, :] = color
        cv2.putText(colorFrame, str(color), (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 1)
        cv2.imshow('color', colorFrame)
        cv2.moveWindow('color', width, 0)
        evt=0

    if evt==cv2.EVENT_RBUTTONUP:
        cv2.destroyWindow('color')
        evt=0

    cv2.imshow('cam', frame)
    cv2.moveWindow('cam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()