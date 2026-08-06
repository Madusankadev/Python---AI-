import cv2

print(cv2.__version__)

width=1280
height=720

valX = 20
valY = 10

centerX = int(width/2)
centerY = int(height/2)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    _ignore, frame = cam.read()

    frameROI = frame[int(centerY-60):int(centerY+60), int(centerX-120):int(centerX+120)]
    frameROI_BGR = cv2.cvtColor(cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY), cv2.COLOR_GRAY2BGR)
    frame[int(centerY-60):int(centerY+60), int(centerX-120):int(centerX+120)] = frameROI_BGR

    if (centerX >= 1160 or centerX <= 120):
        valX=valX*(-1)

    if centerY >= 660 or centerY <= 60:
        valY*=(-1)

    centerY+=valY
    centerX+=valX

    cv2.imshow('CAM', frame)
    cv2.moveWindow('CAM', 0,0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()