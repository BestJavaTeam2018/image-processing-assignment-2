import cv2
import numpy as np

img = cv2.imread('circle.png', 0)

_,threshold=cv2.threshold(img,90,255,cv2.THRESH_BINARY_INV)

kernel=np.ones((5,5), np.uint8)

erosion=cv2.erode(threshold,kernel,iterations=1)

cv2.imshow('Your amazing filtered Image', threshold)

cv2.waitKey()
