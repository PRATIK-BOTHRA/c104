import numpy as np
import cv2
Black = np.zeros([600,600])
Black[200:400,200:400] = 255
print(Black)
cv2.imshow("Black",Black)
cv2.waitKey(0)