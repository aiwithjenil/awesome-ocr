import subprocess
import sys
import os

def run_nougat(pdf_path, output_dir="output"):
    """
    Run Meta's Nougat on a PDF file using the CLI.
    """
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        print(f"--- Running Nougat on {pdf_path} ---")
        
        # Nougat is typically run via CLI
        command = [
            "nougat",
            pdf_path,
            "--out", output_dir,
            "--checkpoint", "facebook/nougat-base"
        ]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Nougat completed successfully.")
            print(f"Output saved in {output_dir}")
        else:
            print(f"Nougat failed with error: {result.stderr}")
            
        print("-" * 40)
        
    except Exception as e:
        print(f"Error running Nougat: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python nougat_ocr.py <pdf_path>")
    else:
        run_nougat(sys.argv[1])
