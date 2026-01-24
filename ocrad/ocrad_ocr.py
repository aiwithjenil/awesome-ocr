import subprocess
import sys

def run_ocrad(image_path):
    """
    Run GNU Ocrad on an image using the CLI.
    """
    try:
        print(f"--- Running Ocrad on {image_path} ---")
        
        # Ocrad is a classic GNU OCR engine
        command = ["ocrad", image_path]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Ocrad Result:")
            print(result.stdout)
        else:
            print(f"Ocrad failed: {result.stderr}")
            
        print("-" * 40)
        
    except Exception as e:
        print(f"Error running Ocrad: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ocrad_ocr.py <image_path>")
    else:
        run_ocrad(sys.argv[1])
