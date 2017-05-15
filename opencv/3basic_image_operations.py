import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

px = img[55, 55]  # get a pixel of image will give a list of bgr

img[55, 55] = [255, 255, 255]  # change the color of a pixel

# ROI : region of image

roi = img[100:150, 100:150]  # will give a numpy array of bgr values

img[100:150, 100:150] = [255, 255, 255]  # will give a region of white color

watch_face = img[37:111, 107:194]  # can copy and paste a portion of an image to a corner, first is height and then is
# width. To get the cordinates of the watch open the image in paint

img[0:74, 0:87] = watch_face  # since the height and the width of watch_face is 74 and 87 pixels resp

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
