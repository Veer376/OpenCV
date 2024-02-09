import cv2 as cv
cap=cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame=cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    flipedimage=cv.flip(frame, 1)
    cv.imshow("frame", flipedimage)
    if cv.waitKey(1)==ord('q'):
        break
cv.release()
cv.destroyAllWindows()