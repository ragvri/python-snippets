import numpy as np
import cv2

image = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(image, (0, 0), (150, 150), (0, 0, 0),
         15)  # where to draw , starting cordinate , ending cordinate, bgr color of
# line 255,255,255 denotes white, pixels of line
cv2.rectangle(image, (15, 25), (200, 150), (255, 255, 255), 3)  # top left and bottom right cordinates
cv2.circle(image, (100, 20), 55, (255, 0, 0), -1)  # center and the radius , if -1 in linewidth it will fill in

points = np.array([[10, 10], [23, 32], [43, 21]], np.int32)

cv2.polylines(image, [points], True, (0, 255, 0), 3)  # list of points, whether you want to close the polygon

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image, 'open cv', (100, 20), font, 1, (255, 255 , 255), 2, cv2.LINE_AA)  # what to write , position of
# image, font to use , size, color , width of text , IDK
# size of font , color, spacing between the letters

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
