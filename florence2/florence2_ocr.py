from transformers import AutoProcessor, AutoModelForCausalLM
from PIL import Image
import torch
import sys

def run_florence2(image_path):
    """
    Run Microsoft Florence-2 OCR on an image.
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_id = 'microsoft/Florence-2-base'
        
        model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True).to(device)
        processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)

        image = Image.open(image_path).convert("RGB")
        
        # Task: OCR
        prompt = "<OCR>"
        
        inputs = processor(text=prompt, images=image, return_tensors="pt").to(device)
        generated_ids = model.generate(
            input_ids=inputs["input_ids"],
            pixel_values=inputs["pixel_values"],
            max_new_tokens=1024,
            num_beams=3
        )
        
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=False)[0]
        parsed_answer = processor.post_process_generation(generated_text, task=prompt, image_size=(image.width, image.height))

        print(f"--- OCR Result for {image_path} ---")
        print(parsed_answer[prompt])
        print("-" * 40)
        
        return parsed_answer
    except Exception as e:
        print(f"Error running Florence-2: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python florence2_example.py <image_path>")
    else:
        run_florence2(sys.argv[1])
