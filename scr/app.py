from module import Table_Img, get_text
import os

img_path = os.path.abspath("data_test\Input\img_table\1.jpg") 

img = Table_Img(img_path)
img.find_cell()

n = len(img.cells)

for x in range(n-1):
    text = get_text(img.cut_img(x, 1))
    print(text)