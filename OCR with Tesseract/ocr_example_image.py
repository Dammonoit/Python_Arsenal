from PIL import Image
import pytesseract

image = Image.open("ocr_example.jpg")

text_convert = pytesseract.image_to_string(image, lang = 'eng')

print(text_convert)
