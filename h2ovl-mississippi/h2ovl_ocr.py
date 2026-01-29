import torch
from transformers import AutoModel, AutoTokenizer
from PIL import Image
import sys

def run_h2ovl(image_path):
    """
    Run H2OVL-Mississippi on an image.
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_id = "h2oai/h2ovl-mississippi-2b"
        
        model = AutoModel.from_pretrained(model_id, trust_remote_code=True, torch_dtype=torch.bfloat16).to(device).eval()
        tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

        image = Image.open(image_path).convert("RGB")
        
        question = "Extract all the text from this image."
        res = model.chat(tokenizer, image, question)

        print(f"--- H2OVL-Mississippi Result for {image_path} ---")
        print(res)
        print("-" * 40)
        
        return res
    except Exception as e:
        print(f"Error running H2OVL-Mississippi: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python h2ovl_ocr.py <image_path>")
    else:
        run_h2ovl(sys.argv[1])
