from transformers import AutoModelForCausalLM, AutoTokenizer
from PIL import Image
import torch
import sys

def run_moondream(image_path):
    """
    Run Moondream2 on an image.
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_id = "vikhyatk/moondream2"
        revision = "2024-08-26"
        
        model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True, revision=revision).to(device)
        tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)

        image = Image.open(image_path).convert("RGB")
        enc_image = model.encode_image(image)
        
        res = model.answer_question(enc_image, "Extract all the text from this image.", tokenizer)

        print(f"--- Moondream2 Result for {image_path} ---")
        print(res)
        print("-" * 40)
        
        return res
    except Exception as e:
        print(f"Error running Moondream2: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python moondream_ocr.py <image_path>")
    else:
        run_moondream(sys.argv[1])
