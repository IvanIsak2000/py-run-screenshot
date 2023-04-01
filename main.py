import os
import time

import pytesseract
from PIL import Image, ImageEnhance, ImageFilter, ImageGrab
import autopep8


def main():

    pytesseract.pytesseract.tesseract_cmd = r"full path to the exe file"
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

    def get_text():
        image = ImageGrab.grabclipboard()

        if image == None:
            return None
        else:
            image.save('photo.png')
            return (
                pytesseract.image_to_string(
                    Image.open("photo.png")))  # get text

    def run(text):
        with open('photo_main.py', 'w', encoding='utf-8') as file:
            file.write(text)

        # os.system(
        #     'autopep8 --in-place --aggressive --aggressive photo_main.py')  # pep8, but questioning whether to use this
        os.system('photo_main.py')  # run code

        print(
            '----------------------------------------\nProgram detected this text:\n',
            text)  # info

    try:
        os.remove("photo.png")
        text_from_photo = get_text()
        if text_from_photo != None:
            run(text_from_photo)
        else:
            return print("It's not a photo! ")

    except FileNotFoundError:
        print('Previous screenshot not found, OK')
        text_from_photo = get_text()
        if text_from_photo != None:
            run(text_from_photo)
        else:
            return print("It's not a photo! ")


if __name__ == '__main__':

    main()
    for_exit = input()
