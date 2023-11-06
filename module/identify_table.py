import cv2



def preprocess(img):
    #chuyển sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #chuyển sang ảnh nhị phân
    thresh, img_bin = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    img_bin = 255-img_bin

    return img_bin
