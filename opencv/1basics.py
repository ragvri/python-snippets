import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)  # read the image. second parameter is the filter. If we don't
# specify anything it will read it as a colored image but removes the alpha channel which is degree of opaquness

# grayscale- only 1 parameter
# IMREAD_COLOR - b,g,r
# IMREAD_UNCHANGED - b,g,r and alpha

# cv2.imshow('image', img)  #display an image , first parameter is the name of the image, second is the image of the
# file
# cv2.waitKey(0)   # it waits for a key to be pressed. 0 means forever
# cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')  # display image on matplotlib
plt.plot()
plt.show()

cv2.imwrite('watchgray.png', img)  # writeh the image to a new file

# opencv does BGR matplotlib does RGB
