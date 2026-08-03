import cv2

print(cv2.__version__)

width=640
height=350

cam = cv2.VideoCapture(0)

while True:
    _ignore, frame = cam.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('upperLeft', frame)
    cv2.moveWindow('upperLeft', 0, 0)

    cv2.imshow('upperRight', grayFrame)
    cv2.moveWindow('upperRight', width, 0)

    cv2.imshow('bottomLeft', grayFrame)
    cv2.moveWindow('bottomLeft', 0, height)

    cv2.imshow('bottomRight', frame)
    cv2.moveWindow('bottomRight', width, height)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()