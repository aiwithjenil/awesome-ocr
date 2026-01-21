from rapidocr_onnxruntime import RapidOCR
import sys

def run_rapidocr(image_path):
    """
    Run RapidOCR on an image.
    """
    try:
        # Initialize RapidOCR
        engine = RapidOCR()
        
        # Perform OCR
        result, elapse = engine(image_path)
        
        print(f"--- OCR Result for {image_path} ---")
        if result:
            for line in result:
                print(f"Text: {line[1]}, Confidence: {line[2]:.2f}")
        else:
            print("No text detected.")
        print(f"Time elapsed: {elapse}")
        print("-" * 40)
        
        return result
    except Exception as e:
        print(f"Error running RapidOCR: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rapidocr_example.py <image_path>")
    else:
        run_rapidocr(sys.argv[1])
