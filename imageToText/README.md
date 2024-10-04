**Requirements**

Install the required libraries:
```
pip install pytesseract Pillow
```
Make sure you have Tesseract installed on your system:


* Windows:

Download from [here](https://github.com/tesseract-ocr/tesseract/wiki)

* Linux (Ubuntu):
```
sudo apt install tesseract-ocr
```

* macOS:
```
brew install tesseract
```

**How It Works:**
Pillow (PIL) loads the image.
pytesseract processes the image to extract text.
