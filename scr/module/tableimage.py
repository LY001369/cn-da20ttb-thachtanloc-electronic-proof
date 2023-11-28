import cv2
import numpy as np
import os

# tìm biên
def edges_find(img):
    # Chuyển ảnh sang ảnh xám (grayscale)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng Gaussian Blur để làm mờ ảnh, giúp loại bỏ nhiễu
    blur_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Áp dụng Canny Edge Detection để tìm cạnh
    edges = cv2.Canny(blur_image, 50, 150, apertureSize=3)

    return edges

#Xác địch các vector đường thẳng.
def lines(img, k = 1):
    edges = edges_find(img)

    # Sử dụng Hough Line Transform để tìm các đoạn thẳng
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=100, minLineLength=100, maxLineGap=10)

    # lọc ra các đường ngang và dọc
    h_line = [line[0].tolist() for line in lines if line[0][1] == line[0][3]]
    v_line = [line[0].tolist() for line in lines if line[0][0] == line[0][2]]

    return h_line, v_line

def group_lines(lines, thin_thresh, k = 1):
    new_lines = []

    while len(lines) > 0:
        thresh = sorted(lines, key=lambda x: x[0][k])[0][0]

        slines = [line for line in lines if thresh[k] - thin_thresh <= line[0][k] <= thresh[k] + thin_thresh]
        lines = [line for line in lines if thresh[k] - thin_thresh > line[0][k] or line[0][k] > thresh[k] + thin_thresh]

        lis = []
        for line in slines:
            lis.append(line[0][k-1])
            lis.append(line[0][k+1])
        new_lines.append([min(lis) - 4*thin_thresh, max(lis) + 4*thin_thresh, thresh[k]])
    return new_lines

def find_horizontal_lines(img):
    h_lines, thin_thresh = lines(img, 0)

    horizontal_lines = group_lines(h_lines, thin_thresh, 1)
    return horizontal_lines


if __name__== "__main__":
    img_path = os.path.abspath(r"scr\data_test\Input\img_table\1.jpg")
    print(img_path)
    img = cv2.imread(img_path)
    #cv2.imshow("show", img)
    cv2.waitKey()

    h_lines, v_lines = lines(img, 0)
    print(h_lines, "\n-----\n")
    print(v_lines, "\n-----\n")

