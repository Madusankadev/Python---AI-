import cv2

print(cv2.__version__)

width=640
height=360
evt=0
moveEvt=0

def MouseEvent(event, xPOs, yPos, flag, param):

    global evt
    global startPos 
    global endPos
    global movePos
    global moveEvt

    if event==cv2.EVENT_LBUTTONDOWN:
        startPos=(xPOs, yPos)
        evt=event
    if event==cv2.EVENT_LBUTTONUP:
        endPos=(xPOs, yPos)
        if startPos[0] > endPos[0]:
            tmpPos=startPos
            startPos=endPos
            endPos=tmpPos
        evt=event
    if event==cv2.EVENT_RBUTTONUP:
        evt=event
    if event==cv2.EVENT_MOUSEMOVE:
        movePos=(xPOs, yPos)
        moveEvt=event

cam=cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cv2.namedWindow('cam')
cv2.setMouseCallback('cam', MouseEvent)

while True:
    _ignore, frame = cam.read()
    print(f"event before if: {evt}")

  
    if evt==cv2.EVENT_LBUTTONUP:
        cropFrame = frame[startPos[1]:endPos[1], startPos[0]:endPos[0]]
        cv2.imshow('crop', cropFrame)
        cv2.moveWindow('crop', 650, 0)
        cv2.rectangle(frame, (startPos), (endPos), (0,255,0), 2)

    if evt==cv2.EVENT_RBUTTONUP:
        cv2.destroyWindow('crop')
        evt=0

    if evt==cv2.EVENT_LBUTTONDOWN and moveEvt==cv2.EVENT_MOUSEMOVE:
        cv2.rectangle(frame, startPos, movePos, (0, 255, 0), 1)
    cv2.imshow('cam', frame)
    cv2.moveWindow('cam', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()