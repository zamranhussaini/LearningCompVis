import cv2
import os

img = cv2.imread(os.path.join('.','pic','noisy.jpg'))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # cvt to grayscale (its alr grey so idk)

#reduce noise
img_less_noise = cv2.bilateralFilter(gray_img, 9, 75, 75)

#canny edge detection
edges = cv2.Canny(img_less_noise, threshold1=200, threshold2=200)



#Apply thresholding
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
adaptive = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 11, 2)


cv2.imshow('canny', edges)
cv2.waitKey(0)