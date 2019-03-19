# pylint: disable=no-member

import cv2

img = cv2.imread('circle.png', 0)

_,threshold=cv2.threshold(img,90,255,cv2.THRESH_BINARY_INV)

kernelDisk=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,11))

erosion=cv2.erode(threshold,kernelDisk,iterations=2)

cv2.imshow('Your amazing filtered Image', erosion)

cv2.waitKey()
