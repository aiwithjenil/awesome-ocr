from paddleocr import PaddleOCR
import sys

def run_paddleocr(image_path):
    """
    Run PaddleOCR on an image.
    """
    try:
        # Initialize PaddleOCR (English)
        ocr = PaddleOCR(use_angle_cls=True, lang='en')
        
        # Perform OCR
        result = ocr.ocr(image_path, cls=True)
        
        print(f"--- OCR Result for {image_path} ---")
        for idx in range(len(result)):
            res = result[idx]
            for line in res:
                print(f"Text: {line[1][0]}, Confidence: {line[1][1]:.2f}")
        print("-" * 40)
        
        return result
    except Exception as e:
        print(f"Error running PaddleOCR: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python paddleocr_example.py <image_path>")
    else:
        run_paddleocr(sys.argv[1])
