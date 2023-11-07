from module.identify_table import Table_Img
import cv2, os

path = [
    "img-test/1.png",
    "img-test/2.png"
]

img = Table_Img(os.path.abspath(path[1]))
print(img.find_point_intersect())

