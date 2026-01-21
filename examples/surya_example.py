from PIL import Image
from surya.ocr import run_ocr
from surya.model.detection import model as det_model, processor as det_processor
from surya.model.recognition import model as rec_model, processor as rec_processor
import sys

def run_surya(image_path):
    """
    Run Surya OCR on an image.
    """
    try:
        image = Image.open(image_path)
        langs = ["en"] # Replace with your languages
        
        # Load models
        det_m, det_p = det_model.load_model(), det_processor.load_processor()
        rec_m, rec_p = rec_model.load_model(), rec_processor.load_processor()

        # Run OCR
        predictions = run_ocr([image], [langs], det_m, det_p, rec_m, rec_p)
        
        print(f"--- OCR Result for {image_path} ---")
        for page in predictions:
            for line in page.text_lines:
                print(f"Text: {line.text}, Confidence: {line.confidence:.2f}")
        print("-" * 40)
        
        return predictions
    except Exception as e:
        print(f"Error running Surya: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python surya_example.py <image_path>")
    else:
        run_surya(sys.argv[1])
