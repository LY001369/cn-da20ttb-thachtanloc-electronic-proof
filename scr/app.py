from module.identify_table import Table_Img
from module.identify_text import get_text

import cv2, os

img = Table_Img(r"D:\LY001369\cn-da20ttb-thachtanloc-electronic-proof\scr\data\test_identify_table\input\1.jpg")
img.cut_cell()

org = (50, 100)  # Tọa độ (x, y) của văn bản
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)  # Màu văn bản (Blue, Green, Red)
thickness = 2
lineType = cv2.LINE_AA

for l in img.img_cells:
    
    text = get_text(l[1])
    print(text)
    cv2.imshow(text, l[1])
cv2.waitKey()

