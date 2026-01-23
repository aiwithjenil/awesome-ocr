from transformers import AutoModel, AutoTokenizer
import torch
import sys

def run_got_ocr(image_path):
    """
    Run GOT-OCR2.0 on an image.
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_name = 'ucas-haoran/GOT-OCR2_0'
        
        tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        model = AutoModel.from_pretrained(model_name, trust_remote_code=True, low_cpu_mem_usage=True, device_map='auto', use_safetensors=True).eval()

        # Perform OCR
        # type can be 'ocr', 'format', 'plain'
        res = model.chat(tokenizer, image_path, ocr_type='ocr')
        
        print(f"--- GOT-OCR2.0 Result for {image_path} ---")
        print(res)
        print("-" * 40)
        
        return res
    except Exception as e:
        print(f"Error running GOT-OCR2.0: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python got_ocr.py <image_path>")
    else:
        run_got_ocr(sys.argv[1])
