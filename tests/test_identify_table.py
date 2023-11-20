dirtest = "data\\test_identify_table" # <===========================


#=======================================================
import sys, os, shutil
path = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path)

#========================================================
input_path = os.path.join(path, dirtest, 'input')
output_path = os.path.join(path, dirtest,'output')
#=======================================================

from module.identify_table import Table_Img
import cv2
list_img_path = [os.path.join(input_path, p) for p in os.listdir(input_path)]

try:
    shutil.rmtree(output_path)
except:
    pass
finally:
    os.mkdir(output_path)

for img_path in list_img_path:
    img = Table_Img(img_path)
    h_line = img.find_horizontal_lines()
    v_line = img.find_vertical_lines()
    
    image = img.img
    color = (0, 0, 255)
    cells,_ = img.cut_cell()
    for cell in cells:
        cv2.rectangle(image, cell[0], cell[1], color, 2)
    cv2.imwrite(os.path.join(output_path,  os.path.basename(img_path)), image)
print("DONE")