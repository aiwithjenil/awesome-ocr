import torch
from transformers import AutoModel, AutoTokenizer
from PIL import Image
import sys

def run_internvl(image_path):
    """
    Run InternVL on an image.
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_id = "OpenGVLab/InternVL2-8B"
        
        model = AutoModel.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
            trust_remote_code=True,
            device_map='auto'
        ).eval()
        
        tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

        image = Image.open(image_path).convert("RGB")
        
        # InternVL specific prompt and chat logic
        question = "<image>\nPlease extract all the text from this image."
        response, history = model.chat(tokenizer, image, question, history=None, return_history=True)

        print(f"--- InternVL Result for {image_path} ---")
        print(response)
        print("-" * 40)
        
        return response
    except Exception as e:
        print(f"Error running InternVL: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python internvl_ocr.py <image_path>")
    else:
        run_internvl(sys.argv[1])
