# pylint: disable=no-member

import cv2
import numpy as np

img = cv2.imread('Square-circle.png', 0)



kernelCr=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(11,11))

kernelSq=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))


circleErosion=cv2.erode(img,kernelCr,iterations=2)
# the hole in the middle of the image increases in size as the border shrinks.
# erosion using a disk shaped structuring element will tend to round concave boundaries
#but will preserve the shape of convex boundaries.

squareErosion=cv2.erode(circleErosion,kernelSq,iterations=1)


cv2.imshow('squareErosion', squareErosion)

#the image took a slightly squared shape 

cv2.imwrite( "circle-square-erode.png", squareErosion );




cv2.waitKey()

