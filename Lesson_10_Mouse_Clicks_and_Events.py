import cv2

print(cv2.__version__)

cam = cv2.VideoCapture(0)

while True:
    _ignore, frame = cam.read()

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('My Web CAM', grayFrame)
    cv2.moveWindow('My Web CAM', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()