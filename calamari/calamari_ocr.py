import subprocess
import sys

def run_calamari(image_path):
    """
    Run Calamari OCR on an image using the CLI.
    """
    try:
        print(f"--- Running Calamari on {image_path} ---")
        
        # Calamari is typically run via CLI
        # It requires a pre-trained model path
        command = [
            "calamari-predict",
            "--checkpoint", "path/to/model.ckpt",
            "--files", image_path
        ]
        
        print("Note: Calamari requires a specific model checkpoint to run.")
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Calamari completed successfully.")
        else:
            print(f"Calamari failed (likely due to missing model): {result.stderr}")
            
        print("-" * 40)
        
    except Exception as e:
        print(f"Error running Calamari: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python calamari_ocr.py <image_path>")
    else:
        run_calamari(sys.argv[1])
