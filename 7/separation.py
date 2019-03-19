import cv2

import numpy as np

img = cv2.imread('circle_and_lines.png', 0)

kernelDisk=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

circles=cv2.morphologyEx(img, cv2.MORPH_OPEN, kernelDisk)


cv2.imshow('Your circles separated', circles)

(contours, _) = cv2.findContours(circles.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#number of circles in the image

print(len(contours))


cv2.waitKey()