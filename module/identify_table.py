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

    def _lines(self, k):
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, k)
        image = cv2.erode(self.img_bin, kernel, iterations=3)
        lines = cv2.dilate(image, kernel, iterations=3)

        lines = cv2.HoughLinesP(lines, 1, np.pi/180, 30, maxLineGap=250)
        return lines

    def _group_lines(self, lines, thin_thresh, k = 1):
        new_lines = []

        while len(lines) > 0:
            thresh = sorted(lines, key=lambda x: x[0][k])[0][0]

            slines = [line for line in lines if thresh[k] - thin_thresh <= line[0][k] <= thresh[k] + thin_thresh]
            lines = [line for line in lines if thresh[k] - thin_thresh > line[0][k] or line[0][k] > thresh[k] + thin_thresh]

            lis = []
            for line in slines:
                lis.append(line[0][k-1])
                lis.append(line[0][k+1])
            x_min, x_max = min(lis) - int(5*thin_thresh), max(lis) + int(5*thin_thresh)
            
            line = [0,0,0,0]
            line[k] = line[k-2] = thresh[k]
            line[k-1], line[k+1] =x_min, x_max
            new_lines.append(line)
        return new_lines

    def find_horizontal_lines(self):
        kernel_len = self.img_gray.shape[1]//120
        h_lines = self._lines((kernel_len, 1))

        self.horizontal_lines = self._group_lines(h_lines, kernel_len, 1)
        return self.horizontal_lines
    
    def find_vertical_lines(self):
        kernel_len = self.img_gray.shape[1]//100
        v_lines = self._lines((1, kernel_len))

        self.vertical_lines = self._group_lines(v_lines, kernel_len, 2)
        return self.vertical_lines

