from module.identify_table import Table_Img
import cv2, os

path = [
    "img-test/1.png",
    "img-test/2.png"
]

img = Table_Img(os.path.abspath(path[0]))
img.cut_cell()

x, y = 5, 1
cv2.imshow(f"ô {x};{y}", img.cells[x][y])
cv2.waitKey()

