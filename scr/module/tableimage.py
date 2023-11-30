import cv2
import numpy as np
import os

# tìm biên
def image_bin(img):
    # Chuyển ảnh sang ảnh xám (grayscale)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Áp dụng Gaussian Blur để làm mờ ảnh, giúp loại bỏ nhiễu
    blur_image = cv2.GaussianBlur(img_gray, (5, 5), 0)

    thresh, img_bin = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    return 255 - img_bin

#Xác địch các vector đường thẳng.
def lines(img):
    img_bin = image_bin(img)

    # Sử dụng Hough Line Transform để tìm các đoạn thẳng
    lines = cv2.HoughLinesP(img_bin, 1, np.pi / 180, threshold=30, minLineLength=100, maxLineGap=5)

    print(lines)
    # lọc ra các đường ngang và dọc
    h_line = [line[0].tolist() for line in lines if abs(line[0][1] - line[0][3])<10]
    v_line = [line[0].tolist() for line in lines if abs(line[0][0] - line[0][2])<10]

    return h_line, v_line

def group_lines(lines, thin_thresh, k = 1):
    new_lines = []

    while len(lines) > 0:
        thresh = sorted(lines, key=lambda x: x[k])[0]

        slines = [line for line in lines if thresh[k] - thin_thresh <= line[k] <= thresh[k] + thin_thresh]
        lines = [line for line in lines if thresh[k] - thin_thresh > line[k] or line[k] > thresh[k] + thin_thresh]

        lis = []
        for line in slines:
            lis.append(line[k-1])
            lis.append(line[k+1])
        new_lines.append([min(lis) - 4*thin_thresh, max(lis) + 4*thin_thresh, thresh[k]])
    return new_lines



if __name__== "__main__":
    img_path = os.path.abspath(r"scr\data_test\Input\img_table\2.jpg")
    print(img_path)
    img = cv2.imread(img_path)

    h_lines, v_lines = lines(img)
    horizontal_lines = group_lines(h_lines, img.shape[1]//120)
    vertical_lines = group_lines(v_lines, img.shape[1]//120, 2)

    cv2.imshow("bien", image_bin(img))
    cv2.waitKey()

    for h in horizontal_lines:
       cv2.line(img, [h[0]*2, h[2]*2], [h[1]*2, h[2]*2], (255, 0, 0), 2, 1, 1)

    for v in vertical_lines:
       cv2.line(img, [v[2]*2, v[0]*2], [v[2]*2, v[1]*2], (0, 0, 255), 2, 1, 1)

    cv2.imshow("show", img)
    cv2.waitKey()



