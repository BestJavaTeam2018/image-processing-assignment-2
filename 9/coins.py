import cv2
import numpy as np

coins = cv2.imread('coins.png',1)

gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)

# again, try different values here
edged = cv2.Canny(gray, 600, 200)

cv2.imshow('Edges', edged)

contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(contours))

amountOfMoneyCalculated  =0

for element in contours:
    area=cv2.contourArea(element)
    if area>2000:
        amountOfMoneyCalculated+=50
    else :   
        amountOfMoneyCalculated+=25

print(amountOfMoneyCalculated)


cv2.waitKey()




