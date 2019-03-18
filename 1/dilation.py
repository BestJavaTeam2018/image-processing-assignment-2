# pylint: disable=no-member

import cv2
import numpy as np

img = cv2.imread('Square-circle.png', 0)
kernel=np.zeros((10,10), np.uint8)


dilation=cv2.dilate(img,kernel,iterations=1)
cv2.imshow('Your amazing filtered Image', dilation)


cv2.waitKey()
