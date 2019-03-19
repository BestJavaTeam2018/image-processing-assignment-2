import cv2

import math

import numpy as np

img = cv2.imread('circle_and_lines.png', 0)

kernelDisk=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

normalKernel=np.ones((4,4), np.uint8)


circles=cv2.morphologyEx(img, cv2.MORPH_OPEN, kernelDisk)


cv2.imshow('Your circles separated', circles)

(contours, _) = cv2.findContours(circles.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#number of circles in the image

print(len(contours))

lines=img-circles

lines=cv2.erode(lines,normalKernel,iterations=1)

cv2.imshow('Your lines separated',lines)

(contours, _) = cv2.findContours(lines.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

numberOfLines= math.ceil(len(contours)/2)

print(numberOfLines)

cv2.waitKey()