import cv2
import numpy as np

print(cv2.__version__)

width=1280
height=720

points=list()

def mosueClick(event, posX, posY, flags, param):
    global enableDrawing

    if event==cv2.EVENT_LBUTTONDOWN:
        enableDrawing=True

    if event==cv2.EVENT_LBUTTONUP:
        enableDrawing=False

    if enableDrawing and event==cv2.EVENT_MOUSEMOVE:
        points.append((posX, posY))

frame = np.zeros([height, width, 3], dtype=np.uint8)
frame[:,:] = (255, 255, 255)

cv2.namedWindow('canvas')
cv2.setMouseCallback('canvas', mosueClick)

while True:

    if len(points) > 1:
        for i in range(int(len(points)-1)):
            cv2.line(frame, points[i], points[i+1], (0,0,255))
    
    cv2.imshow('canvas', frame)
    cv2.moveWindow('canvas',0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break