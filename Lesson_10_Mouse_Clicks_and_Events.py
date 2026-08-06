# how to launch web cam more faster

import cv2

print(cv2.__version__)

width = 1280
height = 720
evt=0

def mouseClick(event, xPOs, yPos, flag, param):
    global evt
    global pos
    if event == cv2.EVENT_LBUTTONDOWN:
        evt=event
        pos=(xPOs, yPos)
    if event==cv2.EVENT_LBUTTONUP:
        evt=event
        pos=(xPOs,yPos)
    if event==cv2.EVENT_RBUTTONDOWN:
        evt=event
        pos=(xPOs,yPos)
    if event==cv2.EVENT_RBUTTONUP:
        evt=event
        pos=(xPOs,yPos)

    if event==cv2.EVENT_MOUSEWHEEL:
        print(f"Event: {event}")
        print(f"POSITIONS: x:{xPOs}, y:{yPos}")

    evt=event
    pos=(xPOs, yPos)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG')) # setup cam codak

cv2.namedWindow('CAM')
cv2.setMouseCallback('CAM', mouseClick)

while True:
    _ignore, frame = cam.read()

    if evt==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(frame, pos, 25, (255, 0, 0), 2)
        cv2.putText(frame, "Mouse Left Down",pos, cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0),2)

    if evt==cv2.EVENT_LBUTTONUP:
        cv2.circle(frame, pos, 25, (255, 0, 0), 2)
        cv2.putText(frame, "Mouse Left Up", pos, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255,0), 2)

    if evt==cv2.EVENT_RBUTTONDOWN:
        cv2.putText(frame, "Mouse Right Down", pos, cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0),2)
        cv2.circle(frame, pos, 25, (255,0,0), 2)

    if evt==cv2.EVENT_RBUTTONUP:
        cv2.putText(frame, "Mouse Right Up", pos, cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0),2)
        cv2.circle(frame, pos, 25, (255,0,0),2)

    if evt==cv2.EVENT_LBUTTONDBLCLK:
        print("Mouse left double click")
        cv2.putText(frame, "Left Button Double Clicked", pos, cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0),2)

    if evt==cv2.EVENT_RBUTTONDBLCLK:
        print("Right button double clicked")

    cv2.imshow('CAM', frame)
    cv2.moveWindow('CAM', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()