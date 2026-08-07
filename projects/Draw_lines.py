import cv2
import numpy as np

print(cv2.__version__)

width=1280
height=720

points = list()

def mouseClick(event, posX, posY, flag, param):
    if event==cv2.EVENT_LBUTTONUP:
        evt=event
        points.append((posX, posY))

frame = np.ones([height, width, 3], dtype=np.uint8)
frame[:,:] = (255, 255, 255)

cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas', mouseClick)

while True:

    if len(points) > 1:
        for i in range(int(len(points) - 1)):
            cv2.line(frame, points[i], points[i+1], (0, 255, 0), 2)

    cv2.imshow('canvas', frame)
    cv2.moveWindow('canvas',0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

