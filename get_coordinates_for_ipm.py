import cv2 as cv
import numpy as np
import json

pts = [] 

# get coordinates of mouse click
def click(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        pts.append((x, y))
        print(x, y)
        cv.circle(img, (x, y), 5, (0, 0, 255), -1)
        cv.imshow('image', img)

# load image
img = cv.imread('data/0.png')

# create a window and bind the function to it
cv.namedWindow('image')
cv.setMouseCallback('image', click)
# close the window on keypress
while True:
    cv.imshow('image', img)
    if len(pts) == 4 & cv.waitKey(20):
        break