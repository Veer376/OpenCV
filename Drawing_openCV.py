import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((512,512,3), np.uint8)
# cv.line(img,(100,0),(0,100),(255,0,0),5)
# cv.rectangle(img,(15,25),(200,150),(0,255,45),3)
cv.circle(img,(447,63), 63, (0,0,255), 1)
font = cv.FONT_HERSHEY_TRIPLEX
text = 'Aryaveer'
text_size, _ = cv.getTextSize(text, font, 3, 2)
text_x = 20
text_y = 250
cv.putText(img, text, (text_x, text_y), font, 3, (255, 255, 255), 2, cv.LINE_AA)
rectangle_color = (255, 255, 255)
rectangle_thickness = 2
rectangle_padding = 10
rectangle_width = text_size[0] + 2 * rectangle_padding
rectangle_height = text_size[1] + 2 * rectangle_padding
cv.rectangle(img, (text_x - rectangle_padding, text_y - rectangle_height - rectangle_padding),
             (text_x + rectangle_width + rectangle_padding, text_y + rectangle_padding),
             rectangle_color, rectangle_thickness)
cv.imshow("Line", img)
if cv.waitKey(0) == ord("s"):
    cv.release()
    cv.destroyAllWindows()