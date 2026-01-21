import easyocr
import sys

def run_easyocr(image_path):
    """
    Run EasyOCR on an image.
    """
    try:
        # Initialize the reader (English)
        reader = easyocr.Reader(['en'])
        
        # Perform OCR
        results = reader.readtext(image_path)
        
        print(f"--- OCR Result for {image_path} ---")
        for (bbox, text, prob) in results:
            print(f"[{prob:.2f}] {text}")
        print("-" * 40)
        
        return results
    except Exception as e:
        print(f"Error running EasyOCR: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python easyocr_example.py <image_path>")
    else:
        run_easyocr(sys.argv[1])
