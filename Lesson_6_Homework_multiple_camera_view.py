#Open multiple camera view

import cv2

print(cv2.__version__)

width=1920
height=1080

numOfCol = int(input("Number of Columns: "))
numOfRows = int(input("Number of Rows: "))

frameWidth = int(width / numOfCol)
frameHeight = int(height / numOfRows)

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    _ignore, frame = cam.read()

    for row in range(numOfCol):
        for col in range(numOfCol):
            cv2.imshow(f"CAM_{row}_{col}", frame)
            cv2.moveWindow(f"CAM_{row}_{col}", int(col*frameWidth), int(row*frameHeight))

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cam.release()