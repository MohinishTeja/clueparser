# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 00:21:39 2020

@author: mohin
"""
import cv2
import numpy as np

img = cv2.imread("1.png")
img2=cv2.imread("w.png")

median = cv2.medianBlur(img, 5)
median2=cv2.medianBlur(img2,5)


#cv2.imshow("Original",img)
cv2.imshow("Original2",img2)
cv2.imshow("Median", median)
cv2.imshow("Median",median2)


cv2.waitKey(0)
cv2.destroyAllWindows()