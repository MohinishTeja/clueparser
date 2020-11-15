# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 00:28:45 2020

@author: mohin
"""
import cv2
import numpy as np

img = cv2.imread("w.png")
median = cv2.medianBlur(img, 5)
averaging = cv2.blur(median, (21, 21))
cv2.imshow("Original image", img)
cv2.imshow("Averaging", averaging)

cv2.waitKey(0)
cv2.destroyAllWindows()