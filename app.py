from module.identify_table import Table_Img
import cv2, os

path = [
    "img-test/1.png",
    "img-test/2.png"
]

img = Table_Img(os.path.abspath(path[0]))
print(img.find_horizontal_lines())
print(img.find_vertical_lines())
