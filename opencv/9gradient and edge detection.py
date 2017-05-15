import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)  # frame , datatype
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)  # frame , datatype, x ,y , IDK
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)  # frame ,datatype ,x , y , IDK

    # edge detector
    edges = cv2.Canny(frame,  100 , 200)  # using the canny algo to detect edges! more the number value, less the
    # edges would be shown

    cv2.imshow('laplacian', laplacian)
    cv2.imshow('frame', frame)
    cv2.imshow('sobelx', sobelx)
    cv2.imshow('sobely', sobely)
    cv2.imshow('edges', edges)

    if cv2.waitKey(1) == ord('k'):
        break

cap.release()
cv2.destroyAllWindows()
