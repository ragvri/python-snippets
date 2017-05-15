import cv2
import numpy as np

img = cv2.imread('opencv-template-matching.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('opencv-template-for-matching.jpg', cv2.IMREAD_GRAYSCALE)

width, height = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
location = np.where(res >= threshold)

for point in zip(*location[::-1]):  # ::-1 reversed the array to get width , height. Zip returns an iterator
    cv2.rectangle(img, point, (point[0] + width, point[1] + height), (0, 255, 255), 2)

cv2.imshow('detected', img)

cv2.waitKey(0)

cv2.destroyAllWindows()
