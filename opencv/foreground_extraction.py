import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg', cv2.IMREAD_UNCHANGED)
# plt.imshow(img)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

mask = np.zeros(img.shape[:2], np.uint8)

bgdmodel = np.zeros((1, 65),
                    np.float64)  # creates an array of 1 row and 64 columns all having zeros of type float64bits
fgmodel = np.zeros((1, 65), np.float64)

rectangle = (161, 79, 150, 150)  # x,y of the top left part of the image , x,y of the bottom right part of the image

cv2.grabCut(img, mask, rectangle, bgdmodel, fgmodel, 5, cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

img = img * mask2[:, :, np.newaxis]
plt.imshow(img)
plt.colorbar()
plt.show()
