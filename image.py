
import cv2 as cv
import sys
img = cv.imread("wp9339939-vector-forest-wallpapers.png")
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("here it is", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("swp9339939-vector-forest-wallpapers.png", img)