# pylint: disable=no-member

import cv2
import numpy as np

img = cv2.imread('cameraman.png', 0)
kernel=np.ones((5,5), np.uint8)

opening=cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing=cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
cv2.imshow('Your amazing filtered Image', closing)


cv2.waitKey()
