import cv2
import numpy as np

class Table_Img():
    def __init__(self, image_path):
        self.img = cv2.imread(image_path)
        self.preprocess()

    def preprocess(self):
        #chuyển sang ảnh xám
        self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
    
        #chuyển sang ảnh nhị phân
        thresh, img_bin = cv2.threshold(self.img_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        self.img_bin = 255-img_bin

        return self.img_gray, self.img_bin

    def _h_lines(self):
        kernel_len = self.img_gray.shape[1]//120
        hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_len, 1))
        image_horizontal = cv2.erode(self.img_bin, hor_kernel, iterations=3)
        horizontal_lines = cv2.dilate(image_horizontal, hor_kernel, iterations=3)

        h_lines = cv2.HoughLinesP(horizontal_lines, 1, np.pi/180, 30, maxLineGap=250)
        return h_lines, kernel_len
    
    def _group_h_lines(self, h_lines, thin_thresh):
        new_h_lines = []

        while len(h_lines) > 0:
            thresh = sorted(h_lines, key=lambda x: x[0][1])[0][0]
            lines = [line for line in h_lines if thresh[1] - thin_thresh <= line[0][1] <= thresh[1] + thin_thresh]
            h_lines = [line for line in h_lines if thresh[1] - thin_thresh > line[0][1] or line[0][1] > thresh[1] + thin_thresh]
            
            x = []
            for line in lines:
                x.append(line[0][0])
                x.append(line[0][2])

            x_min, x_max = min(x) - int(5*thin_thresh), max(x) + int(5*thin_thresh)
            new_h_lines.append([x_min, thresh[1], x_max, thresh[1]])

        return new_h_lines
    
    def horizontal_lines(self):
        h_lines, kernel_len = self._h_lines()
        self.horizontal_lines = self._group_h_lines(h_lines, kernel_len)
        return self.horizontal_lines
