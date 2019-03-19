# pylint: disable=no-member

import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('morning.jpg',1)
image2 = cv2.imread('evening.jpg',1)


# Making both images have the same size
resized = cv2.resize(image, (900, 675), interpolation=cv2.INTER_AREA)
resized2 = cv2.resize(image2, (900, 675), interpolation=cv2.INTER_AREA)


# Method 1:
img = cv2.addWeighted(resized2, 0.5, resized, 0.5, 0) 


# Method 2:
lower_white = np.array([220, 220, 220], dtype=np.uint8)
upper_white = np.array([255, 255, 255], dtype=np.uint8)

mask = cv2.inRange(resized, lower_white, upper_white)

res = cv2.bitwise_not(resized,resized, mask)

cv2.imshow('res', res) 

cv2.waitKey()
