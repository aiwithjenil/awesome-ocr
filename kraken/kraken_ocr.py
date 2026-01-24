import subprocess
import sys

def run_kraken(image_path):
    """
    Run Kraken OCR on an image using the CLI.
    """
    try:
        print(f"--- Running Kraken on {image_path} ---")
        
        # Kraken is typically run via CLI
        # 'get-it' downloads the default model if not present
        command = [
            "kraken",
            "-i", image_path, "output.txt",
            "binarize", "segment", "ocr"
        ]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Kraken completed successfully.")
            with open("output.txt", "r") as f:
                print(f.read())
        else:
            print(f"Kraken failed with error: {result.stderr}")
            
        print("-" * 40)
        
    except Exception as e:
        print(f"Error running Kraken: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python kraken_ocr.py <image_path>")
    else:
        run_kraken(sys.argv[1])
