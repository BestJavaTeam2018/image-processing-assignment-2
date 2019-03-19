import cv2
import numpy as np

coins = cv2.imread('coins.png',1)

gray = cv2.cvtColor(coins, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray, 600, 200)

contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

amountOfMoneyCalculated  =0

for element in contours:
    area=cv2.contourArea(element)
    if area>2000:
        cv2.drawContours(coins, element, -1, (255,0,0), 3)
        amountOfMoneyCalculated+=50
    else : 
        cv2.drawContours(coins, element, -1, (0,0,255), 3)
        amountOfMoneyCalculated+=25

cv2.imshow('coins',coins)  

cv2.imwrite( "coins2.png", coins);


print(amountOfMoneyCalculated)


cv2.waitKey()




