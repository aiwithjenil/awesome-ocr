import pytesseract
from PIL import Image
import sys

def run_tesseract(image_path):
    """
    Run Tesseract OCR on an image.
    Requires tesseract-ocr to be installed on the system.
    """
    try:
        # Load the image
        img = Image.open(image_path)
        
        # Perform OCR
        text = pytesseract.image_to_string(img)
        
        print(f"--- OCR Result for {image_path} ---")
        print(text)
        print("-" * 40)
        
        return text
    except Exception as e:
        print(f"Error running Tesseract: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python tesseract_example.py <image_path>")
    else:
        run_tesseract(sys.argv[1])
