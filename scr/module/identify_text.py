import pytesseract
import os

tesseract_path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
if not os.path.isfile(tesseract_path):
    with open(os.path.abspath(".\\configs\\tesseract_path.txt"), "r") as f:
        tesseract_path = f.read()
pytesseract.pytesseract.tesseract_cmd = tesseract_path 

def get_text(img):

    # Sử dụng Tessera OCR để nhận diện văn bản từ hình ảnh
    text = pytesseract.image_to_string(img)

    # In ra văn bản đã nhận diện được
    return text;

