from PIL import Image,ImageEnhance,ImageFilter
from pytesseract import image_to_string

def get_string_from_image(im):
    text = image_to_string(im)
    return text
