from PIL import Image
import pytesseract

# Optional: specify the path to the tesseract executable if it's not in your PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example

def extract_text_from_image(image_path):
    """
    Extracts text from the provided image using pytesseract.
    
    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The text extracted from the image.
    """
    try:
        # Open the image file
        img = Image.open(image_path)
        
        # Use pytesseract to extract text
        text = pytesseract.image_to_string(img)
        
        return text.strip()
    
    except Exception as e:
        return f"Error: {e}"

# Example usage
image_path = "path_to_your_image.png"
extracted_text = extract_text_from_image(image_path)
print("Extracted Text:", extracted_text)
