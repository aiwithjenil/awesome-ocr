import subprocess
import sys
import os

def run_olmocr(pdf_path, output_dir="output"):
    """
    Run olmOCR on a PDF file using the CLI.
    """
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        print(f"--- Running olmOCR on {pdf_path} ---")
        
        # olmOCR is typically run via CLI to process PDFs into clean text/markdown
        command = [
            "python", "-m", "olmocr.pipeline.analyze",
            "--input", pdf_path,
            "--output", output_dir
        ]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("olmOCR completed successfully.")
            print(f"Output saved in {output_dir}")
        else:
            print(f"olmOCR failed with error: {result.stderr}")
            
        print("-" * 40)
        
    except Exception as e:
        print(f"Error running olmOCR: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python olmocr_ocr.py <pdf_path>")
    else:
        run_olmocr(sys.argv[1])
