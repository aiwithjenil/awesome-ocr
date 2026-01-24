import subprocess
import sys

def run_gocr(image_path):
    """
    Run GOCR on an image using the CLI.
    """
    try:
        print(f"--- Running GOCR on {image_path} ---")
        
        # GOCR is a classic C-based OCR engine
        command = ["gocr", "-i", image_path]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("GOCR Result:")
            print(result.stdout)
        else:
            print(f"GOCR failed: {result.stderr}")
            
        print("-" * 40)
        
    except Exception as e:
        print(f"Error running GOCR: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python gocr_ocr.py <image_path>")
    else:
        run_gocr(sys.argv[1])
