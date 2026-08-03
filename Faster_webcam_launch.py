# how to launch web cam more faster

import cv2

print(cv2.__version__)

width = 1280
height = 720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) # setup cam codak

while True:
    _ignore, frame = cam.read()
    cv2.imshow('CAM', frame)
    cv2.moveWindow('CAM', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()