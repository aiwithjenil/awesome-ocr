from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch
import sys

def run_trocr(image_path):
    """
    Run Microsoft TrOCR on an image.
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        # Using base model for printed text
        processor = TrOCRProcessor.from_pretrained('microsoft/trocr-base-printed')
        model = VisionEncoderDecoderModel.from_pretrained('microsoft/trocr-base-printed').to(device)

        image = Image.open(image_path).convert("RGB")
        pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)

        generated_ids = model.generate(pixel_values)
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]

        print(f"--- TrOCR Result for {image_path} ---")
        print(generated_text)
        print("-" * 40)
        
        return generated_text
    except Exception as e:
        print(f"Error running TrOCR: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python trocr_ocr.py <image_path>")
    else:
        run_trocr(sys.argv[1])
