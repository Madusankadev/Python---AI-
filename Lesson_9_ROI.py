import cv2

print(cv2.__version__)

width = 640
height = 360

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    _ignore, frame = cam.read()

    frameROI = frame[150:210, 250:390]
    grayFrameROI = cv2.cvtColor(frameROI, cv2.COLOR_BGR2GRAY)
    cv2.imshow('ROI', grayFrameROI)
    cv2.moveWindow('ROI', 650, 0)

    frame[0:60, 0:140] = cv2.cvtColor(grayFrameROI, cv2.COLOR_GRAY2BGR)

    cv2.imshow('CAM', frame)        
    cv2.moveWindow('CAM', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()