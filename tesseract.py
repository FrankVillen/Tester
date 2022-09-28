# text recognition
import cv2
import pytesseract

# read image
img = cv2.imread('test2.png')

# configurations
config = ('-l eng --oem 1 --psm 3')

# If you have not configured the tesseract executable in your System variables PATH, include the following.
# pytessercat
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

text = pytesseract.image_to_string(img, config=config)

# print text
text = text.split('\n')
for item in text:
    print(item)
# print(text)
