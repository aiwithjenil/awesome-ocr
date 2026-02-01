import requests
import sys
import json

def run_umi_ocr(image_path, server_url="http://127.0.0.1:1224/api/ocr"):
    """
    Run Umi-OCR via its HTTP API.
    Note: This requires the Umi-OCR server to be running.
    """
    try:
        with open(image_path, "rb") as f:
            image_data = f.read()
            
        # Umi-OCR API expects base64 or file upload
        # This is a simplified example assuming the server is running locally
        files = {"file": image_data}
        response = requests.post(server_url, files=files)
        
        if response.status_code == 200:
            result = response.json()
            print(f"--- Umi-OCR Result for {image_path} ---")
            print(json.dumps(result, indent=2, ensure_ascii=False))
            print("-" * 40)
            return result
        else:
            print(f"Umi-OCR API failed with status code: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error running Umi-OCR: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python umi_ocr.py <image_path>")
    else:
        run_umi_ocr(sys.argv[1])
