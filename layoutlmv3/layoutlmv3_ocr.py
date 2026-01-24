from transformers import LayoutLMv3Processor, LayoutLMv3ForSequenceClassification
from PIL import Image
import torch
import sys
import pytesseract

def run_layoutlmv3(image_path):
    """
    Run LayoutLMv3 on an image. 
    Note: LayoutLMv3 typically requires an external OCR (like Tesseract) to provide text and bounding boxes.
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=True)
        model = LayoutLMv3ForSequenceClassification.from_pretrained("microsoft/layoutlmv3-base").to(device)

        image = Image.open(image_path).convert("RGB")
        
        # The processor will use Tesseract to get words and boxes if apply_ocr=True
        encoding = processor(image, return_tensors="pt").to(device)
        
        # This example just shows the feature extraction/encoding part
        # LayoutLMv3 is usually fine-tuned for specific tasks like classification or NER
        outputs = model(**encoding)
        
        print(f"--- LayoutLMv3 Processing for {image_path} ---")
        print(f"Detected {len(encoding['input_ids'][0])} tokens.")
        print(f"Model output logits shape: {outputs.logits.shape}")
        print("-" * 40)
        
        return outputs
    except Exception as e:
        print(f"Error running LayoutLMv3: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python layoutlmv3_ocr.py <image_path>")
    else:
        run_layoutlmv3(sys.argv[1])
