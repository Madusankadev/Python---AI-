#Image represntation in Data Array

import numpy as np
import cv2

#each image contain pixels
#black and white image => black 0 & white 1

while True:
    frame = np.zeros([250, 250], dtype=np.uint8)
    # cv2.imshow('Black Frame', frame)

    halfBW = np.ones([500, 500, 3], dtype=np.uint8)
    halfBW[:,250:] = [255, 0, 0]
    halfBW[:, :250] = [0, 0, 255]
    print(halfBW)
    cv2.imshow('Half', halfBW)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

