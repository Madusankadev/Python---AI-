import cv2

print(cv2.__version__)

width=64
height=36
xPos=0
yPos=0
scale=1

def xPosCallback(val):
    global xPos 
    xPos=val

def yPosCallback(val):
    global yPos
    yPos=val

def scaleCallback(val):
    global scale
    scale=val

cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('myTrackBar')
cv2.createTrackbar('xPos', 'myTrackBar', 0, 1280, xPosCallback)
cv2.createTrackbar('yPos', 'myTrackBar', 0, 720, yPosCallback)
cv2.createTrackbar('scale', 'myTrackBar', 0, 50, scaleCallback)

while True:
    _ignore, frame = cam.read()

    cv2.imshow('camera', frame)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, int(width*scale))
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, int(height*scale))
    cv2.moveWindow('camera', xPos, yPos)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()