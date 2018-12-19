from flask import Flask, request, jsonify
from io import BytesIO
import requests

app= Flask(__name__)

@app.route('/text', methods = ['POST'])

def text():
    import pytesseract
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    from PIL import Image

    im= Image.open(request.args.get('path', ''))
    text = pytesseract.image_to_string(im, lang='eng')

    return text

app.run(port= '5001')
