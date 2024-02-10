import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((100,100,3), np.uint8)
# cv.imshow("Black Image", img)
# Draw a diagonal blue line with thickness of 5 px
cv.line(img,(100,0),(0,100),(255,0,0),5)
cv.imshow("Line", img)
if cv.waitKey(0) == ord("s"):
    cv.release()
    cv.destroyAllWindows()