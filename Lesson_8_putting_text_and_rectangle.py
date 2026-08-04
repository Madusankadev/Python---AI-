import cv2

print(cv2.__version__)

width = 640
height = 360

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))

while True:
    _ignore, frame = cam.read()

    #draw rectangle black box size 40x40 pixel
    # frame[140:220, 280:360] = (0, 0, 0)

    cv2.circle(frame, (int(width/2), int(height/2)), 25, (255, 0, 0), 5)

    cv2.putText(frame, "Madhushankha is Boss", (120, 80), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 255), 2)

    cv2.imshow('CAM', frame)
    cv2.moveWindow('CAM', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()