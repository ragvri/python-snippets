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

    kernel = np.ones((5, 5), np.uint8)

    erosion = cv2.erode(mask, kernel=kernel, iterations=1)  # it looks for a list of pixels in a given lenght. If
    # the value of one pixel is different from the others, it removes that pixel

    dilation = cv2.dilate(mask, kernel=kernel, iterations=1)  # instead of removing the pixel, it pushes the pixel out

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)  # removed false positives
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)  # removes false negatives

    cv2.imshow('frame', frame)
    # cv2.imshow('erosion', erosion)
    # cv2.imshow('dilation', dilation)
    # cv2.imshow('result', res)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    if cv2.waitKey(1) == ord('k'):
        break

cv2.destroyAllWindows()
cap.release()
