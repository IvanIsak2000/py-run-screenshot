import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
image = Image.open("photo.png")
# string = pytesseract.image_to_string(image)

pytesseract.pytesseract.tesseract_cmd = r"full path to the exe file"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

text = pytesseract.image_to_string(image, config='--psm 11')
# печатаем
print(text)
