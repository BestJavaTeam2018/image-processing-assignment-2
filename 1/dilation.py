# pylint: disable=no-member

import cv2
import numpy as np

img = cv2.imread('Square-circle.png', 0)

kernelSq=cv2.getStructuringElement(cv2.MORPH_RECT,(11,11))

kernelcircle=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))


dilation=cv2.dilate(img,kernelcircle,iterations=1)
cv2.imshow('using circle structure', dilation)

#convex boundaries will become rounded,
#and concave boundaries will be preserved as they are.


dilation=cv2.dilate(img,kernelSq,iterations=1)
cv2.imshow('using square structure', dilation)

#will dilate the bottom of a region more strongly than the top.



cv2.waitKey()
