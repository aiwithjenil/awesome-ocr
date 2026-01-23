import os
import sys
from magic_pdf.data.data_reader_factory import DataReaderFactory
from magic_pdf.model.doc_analyze_by_custom_model import doc_analyze
from magic_pdf.config.enums import SupportedPdfParseMethod

def run_mineru(pdf_path, output_dir="output"):
    """
    Run MinerU (Magic-PDF) on a PDF file.
    """
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Read PDF data
        reader = DataReaderFactory().get_reader(pdf_path)
        pdf_bytes = reader.read()
        
        # Analyze and parse PDF
        # method can be 'auto', 'ocr', 'txt'
        model_json = doc_analyze(pdf_bytes, pdf_path, model_name="layoutlmv3", method=SupportedPdfParseMethod.OCR)
        
        print(f"--- MinerU Analysis for {pdf_path} ---")
        print(f"Detected {len(model_json)} pages/elements.")
        print(f"Results saved to {output_dir}")
        print("-" * 40)
        
        return model_json
    except Exception as e:
        print(f"Error running MinerU: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python mineru_ocr.py <pdf_path>")
    else:
        run_mineru(sys.argv[1])
