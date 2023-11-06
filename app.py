from module import identify_table
import cv2, os

path = [
    "img-test/1.png",
    "img-test/2.png"
]

img = cv2.imread(os.path.abspath(path[0]))
cv2.imshow("Font", img)
cv2.waitKey()

img = identify_table.preprocess(img)

cv2.imshow("Back", img)
cv2.waitKey()