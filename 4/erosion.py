# pylint: disable=no-member

import cv2
import numpy as np

img = cv2.imread('circle.png', 0)
kernelSq=cv2.getStructuringElement(cv2.MORPH_RECT,(11,1))

kernelCr=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(2,11))

erosion=cv2.erode(img,kernelSq,iterations=1)
erosion=cv2.erode(img,kernelCr,iterations=1)

cv2.imshow('Your amazing filtered Image', erosion)


cv2.waitKey()

