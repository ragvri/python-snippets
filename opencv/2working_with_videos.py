import cv2
import numpy as np
import random

cap = cv2.VideoCapture(0)  # 0 means the first webcam , 1 means the second . To use video file instead, put file path
#  instead of camera number
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # name of file, codec type, resolution
while True:
    ret, frame = cap.read()  # we get a true/false and a frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # making a new frame that is gray scaled
    out.write(frame)
    cv2.imshow('frame2', gray)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cap.release()  # releases the camera. think of it in terms of file. If you modify a file that is alredy opened
# elsewhere we get trouble

cv2.destroyAllWindows()
