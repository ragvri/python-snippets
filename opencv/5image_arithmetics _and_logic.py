import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('mainlogo.png')

# add = img1 + img2  # shows both the images simultaneosly
# add=cv2.add(img1,img2)  # this one adds the corresponding bgr of the pixels in the two images if >255 then changes
# to 255
# weighted = cv2.addWeighted(img1, 0.6, img2, 0.4,0)
# img1, weight of img1, img2 , weight of img2(should add to 1) , gamma

rows, cols, channels = img3.shape
roi = img1[0:rows, 0:cols]

img3_to_gray = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3_to_gray, 220, 255, cv2.THRESH_BINARY_INV)  # source should be grayscale
# if pixel value is above 220 it is converted to 255. If below 220 then convert to black. cv2.THRESH_BINARY_INV will
# invert this pixel value obtained
mask_inv = cv2.bitwise_not(mask)  # gives pixel value opp of the mask image

# similiary bitwise_and , bitwise_or , bitwise_xor

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)  # creates a black color (0 value) in the region of the symbol
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)  # creates black color in region around the logo

# adding will give the python logo on the graph

dst = cv2.add(img1_bg, img3_fg)
dst = img1[0:rows, 0:cols]

cv2.imshow('img1_bg', img1_bg)
# cv2.imshow('img3_fg', img3_fg)
cv2.imshow('dst', dst)
# cv2.imshow('adf', img3_to_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
