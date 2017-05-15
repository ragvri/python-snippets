import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# print(cv2.cvtColor(np.uint8([[0,0,255]]) , cv2.COLOR_BGR2HSV))

# gets the red cap that I have
while True:
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # stands for hue , saturation and value. Chaging bgr to diff type
    # h:0 to 179 S:0 to 255 V=0:255
    lower_red = np.array([150, 150, 50])
    upper_red = np.array([180, 250, 175])
    mask = cv2.inRange(hsv, lower_red, upper_red)  # returns 0 or 1..also 1 maps to white and 0 to black
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((15, 15), np.float32) / (15 * 15)
    smoothed = cv2.filter2D(res, -1, kernel)  # gives a simple avg of our frame

    blur= cv2.GaussianBlur(res, (15,15) , 0) # another way to get smoothening of the color filter No noise in this one!

    median = cv2.medianBlur(res,15)

    cv2.imshow('frame', frame)
    # cv2.imshow('mask', mask)
    cv2.imshow('result', median)
    if cv2.waitKey(1) == ord('k'):
        break

cv2.destroyAllWindows()
cap.release()
