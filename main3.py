import cv2
import numpy 


img=cv2.imread("poster.jpg")
#rocket=img[120:360,400:500]
#img[0:240,500:600]=rocket
texttoshow="I Love Coding At Whitehat Junior"

cv2.putText(img,texttoshow,(20,130),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=0.75,color=(0,0,255))
cv2.imshow("img",img)
cv2.imwrite("Greeting.jpg",img)
cv2.waitKey(0)