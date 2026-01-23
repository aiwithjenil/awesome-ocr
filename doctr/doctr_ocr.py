from doctr.io import DocumentFile
from doctr.models import ocr_predictor
import sys

def run_doctr(image_path):
    """
    Run docTR on an image or PDF.
    """
    try:
        # Load the model
        model = ocr_predictor(pretrained=True)
        
        # Load the document
        if image_path.lower().endswith('.pdf'):
            doc = DocumentFile.from_pdf(image_path)
        else:
            doc = DocumentFile.from_images(image_path)
            
        # Perform OCR
        result = model(doc)
        
        print(f"--- docTR Result for {image_path} ---")
        # Export to JSON or just print text
        json_output = result.export()
        for page in json_output['pages']:
            for block in page['blocks']:
                for line in block['lines']:
                    for word in line['words']:
                        print(word['value'], end=' ')
                    print()
        print("-" * 40)
        
        return result
    except Exception as e:
        print(f"Error running docTR: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python doctr_ocr.py <path_to_file>")
    else:
        run_doctr(sys.argv[1])
