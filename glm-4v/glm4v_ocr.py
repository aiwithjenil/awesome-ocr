import torch
from PIL import Image
from transformers import AutoModelForCausalLM, AutoTokenizer
import sys

def run_glm4v(image_path):
    """
    Run GLM-4V on an image.
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_id = "THUDM/glm-4v-9b"
        
        tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
            trust_remote_code=True,
            device_map="auto"
        ).eval()

        image = Image.open(image_path).convert("RGB")
        
        inputs = tokenizer.apply_chat_template(
            [{"role": "user", "image": image, "content": "Extract all the text from this image."}],
            add_generation_prompt=True,
            tokenize=True,
            return_tensors="pt",
            return_dict=True
        ).to(device)

        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=1024)
            outputs = outputs[:, inputs['input_ids'].shape[1]:]
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        print(f"--- GLM-4V Result for {image_path} ---")
        print(response)
        print("-" * 40)
        
        return response
    except Exception as e:
        print(f"Error running GLM-4V: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python glm4v_ocr.py <image_path>")
    else:
        run_glm4v(sys.argv[1])
