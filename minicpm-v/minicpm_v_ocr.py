from transformers import AutoModel, AutoTokenizer
import torch
from PIL import Image
import sys

def run_minicpm_v(image_path):
    """
    Run MiniCPM-V on an image.
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_id = "openbmb/MiniCPM-V-2_6" # Example version
        
        model = AutoModel.from_pretrained(model_id, trust_remote_code=True, torch_dtype=torch.bfloat16).to(device).eval()
        tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

        image = Image.open(image_path).convert("RGB")
        
        question = "Extract all the text from this image."
        msgs = [{'role': 'user', 'content': question}]

        res = model.chat(
            image=image,
            msgs=msgs,
            tokenizer=tokenizer,
            sampling=True,
            temperature=0.7
        )

        print(f"--- MiniCPM-V Result for {image_path} ---")
        print(res)
        print("-" * 40)
        
        return res
    except Exception as e:
        print(f"Error running MiniCPM-V: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python minicpm_v_ocr.py <image_path>")
    else:
        run_minicpm_v(sys.argv[1])
