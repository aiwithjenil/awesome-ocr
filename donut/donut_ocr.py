from transformers import DonutProcessor, VisionEncoderDecoderModel
from PIL import Image
import torch
import sys
import re

def run_donut(image_path):
    """
    Run Donut (OCR-free Document Understanding) on an image.
    """
    try:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        processor = DonutProcessor.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa")
        model = VisionEncoderDecoderModel.from_pretrained("naver-clova-ix/donut-base-finetuned-docvqa").to(device)

        image = Image.open(image_path).convert("RGB")
        
        # Prepare decoder inputs
        task_prompt = "<s_docvqa><s_question>What is the text in this document?</s_question><s_answer>"
        decoder_input_ids = processor.tokenizer(task_prompt, add_special_tokens=False, return_tensors="pt").input_ids.to(device)

        pixel_values = processor(image, return_tensors="pt").pixel_values.to(device)

        outputs = model.generate(
            pixel_values,
            decoder_input_ids=decoder_input_ids,
            max_length=model.config.decoder.max_position_embeddings,
            pad_token_id=processor.tokenizer.pad_token_id,
            eos_token_id=processor.tokenizer.eos_token_id,
            use_cache=True,
            bad_words_ids=[[processor.tokenizer.unk_token_id]],
            return_dict_in_generate=True,
        )

        sequence = processor.batch_decode(outputs.sequences)[0]
        sequence = sequence.replace(processor.tokenizer.eos_token, "").replace(processor.tokenizer.pad_token, "")
        sequence = re.sub(r"<.*?>", "", sequence, count=1).strip() # remove first task start token
        
        print(f"--- Donut Result for {image_path} ---")
        print(processor.token2json(sequence))
        print("-" * 40)
        
        return sequence
    except Exception as e:
        print(f"Error running Donut: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python donut_ocr.py <image_path>")
    else:
        run_donut(sys.argv[1])
