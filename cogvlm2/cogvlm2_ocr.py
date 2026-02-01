import torch
from PIL import Image
from transformers import AutoModelForCausalLM, LlamaTokenizer
import sys

def run_cogvlm2(image_path):
    """
    Run CogVLM2 on an image.
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        model_id = "THUDM/cogvlm2-llama3-chat-19b"
        
        tokenizer = LlamaTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B-Instruct")
        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
            device_map="auto"
        ).eval()

        image = Image.open(image_path).convert("RGB")
        
        query = "Extract all the text from this image."
        inputs = model.build_conversation_input_ids(tokenizer, query=query, history=[], images=[image])
        inputs = {k: v.to(device) for k, v in inputs.items()}
        
        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=1024)
            outputs = outputs[:, inputs['input_ids'].shape[1]:]
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        print(f"--- CogVLM2 Result for {image_path} ---")
        print(response)
        print("-" * 40)
        
        return response
    except Exception as e:
        print(f"Error running CogVLM2: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cogvlm2_ocr.py <image_path>")
    else:
        run_cogvlm2(sys.argv[1])
