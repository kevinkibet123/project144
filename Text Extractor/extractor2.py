import os
import cv2
import pytesseract
from PIL import Image

image_path = r"C:\Users\Your-full-path\to-image.png"

if image_path is None:
    print(f"Check image location and try again")
else:
    image = cv2.imread(image_path)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
gray = cv2.resize(gray,None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
# gray = cv2.GaussianBlur(gray, (5,5),0)#leads to poorer results, but try it first before commenting it out


text_extract = pytesseract.image_to_string(gray)
print("Extracted Text:")
print(text_extract)