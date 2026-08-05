import cv2
import time

width = 1280
height=720

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

fps = 0

lastTime = time.time()
filterdFPS = 30

while True:
    _ignore, frame = cam.read()

    currentTime = time.time()
    fps = 1 / (currentTime-lastTime)
    filterdFPS = filterdFPS*.97+fps*.03

    lastTime=time.time()      

    cv2.rectangle(frame, (0, 0), (200, 50), (255, 0, 255), -1)
    cv2.putText(frame, f"FPS: {round(filterdFPS)}", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
    cv2.imshow('CAMERA', frame)
    cv2.moveWindow('CAMERA',0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()
