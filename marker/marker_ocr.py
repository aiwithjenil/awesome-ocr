import subprocess
import sys
import os

def run_marker(pdf_path, output_dir="output"):
    """
    Run Marker on a PDF file using the CLI.
    """
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        print(f"--- Running Marker on {pdf_path} ---")
        
        # Marker is typically run via CLI
        command = [
            "marker_single",
            pdf_path,
            "--output_dir", output_dir,
            "--batch_multiplier", "2"
        ]
        
        result = subprocess.run(command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("Marker completed successfully.")
            print(f"Output saved in {output_dir}")
        else:
            print(f"Marker failed with error: {result.stderr}")
            
        print("-" * 40)
        
    except Exception as e:
        print(f"Error running Marker: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python marker_ocr.py <pdf_path>")
    else:
        run_marker(sys.argv[1])
