import sys
import requests
import pytesseract
from PIL import Image
from io import BytesIO


def get_image(url):
    return Image.open(BytesIO(requests.get(url).content))


if __name__ == '__main__':
    """Tool to test the raw output of pytesseract with a given input URL"""

    print("A simple OCR utility\n")
    url = raw_input("What is the url of the image you would like to analyze?\n")
    image = get_image(url)
    print("The raw output from tesseract with no processing is:\n\n")
    print("-----------------BEGIN-----------------\n")
    print(pytesseract.image_to_string(image) + "\n")
    print("------------------END------------------\n")