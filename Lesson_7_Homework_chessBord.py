import cv2
import numpy as np

bordSize = int(input("What size your board boss: "))
squreCount = int(input("How many squre need in one row sir: "))

width=bordSize
height=bordSize

numOfCols=squreCount
numOfRows=squreCount

cellWidth = int(width/numOfCols)
cellHeight = int(height/numOfRows)

frame = np.zeros([width, height, 3], dtype=np.uint8)


color = 1

for row in range(numOfRows):
    if row % 2 == 0:
            color=-1
    else:
            color=1
    for col in range(numOfCols):
        frame[int(row*cellHeight): int(row*cellHeight+cellHeight), int(col*cellWidth): int(col*cellWidth+cellWidth)] = [0, 0, 0] if color == -1 else [255, 255, 255]
        color= color*(-1)
    


while True:
    cv2.imshow('BOARD', frame)
    cv2.moveWindow('BOARD', 0, 0)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break