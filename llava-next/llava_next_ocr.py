from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration
import torch
from PIL import Image
import sys

def run_llava_next(image_path):
    """
    Run LLaVA-NeXT on an image.
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_id = "llava-hf/llava-v1.6-vicuna-7b-hf"
        
        processor = LlavaNextProcessor.from_pretrained(model_id)
        model = LlavaNextForConditionalGeneration.from_pretrained(model_id, torch_dtype=torch.float16, low_cpu_mem_usage=True).to(device)

        image = Image.open(image_path).convert("RGB")
        
        prompt = "A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions. USER: <image>\nPlease extract all the text from this image. ASSISTANT:"
        
        inputs = processor(prompt, image, return_tensors="pt").to(device)
        
        output = model.generate(**inputs, max_new_tokens=512)
        res = processor.decode(output[0], skip_special_tokens=True)

        print(f"--- LLaVA-NeXT Result for {image_path} ---")
        print(res.split("ASSISTANT:")[-1].strip())
        print("-" * 40)
        
        return res
    except Exception as e:
        print(f"Error running LLaVA-NeXT: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python llava_next_ocr.py <image_path>")
    else:
        run_llava_next(sys.argv[1])
