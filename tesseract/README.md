# Tesseract OCR

Tesseract is an open-source OCR engine that has been around since the 1980s and is currently maintained by Google. It is one of the most popular and widely used OCR engines in the world.

## Installation

1. Install the Tesseract engine on your system:
   - **Ubuntu**: `sudo apt install tesseract-ocr`
   - **macOS**: `brew install tesseract`
   - **Windows**: Download the installer from the [official repository](https://github.com/UB-Mannheim/tesseract/wiki).

2. Install the Python wrapper:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

```bash
python tesseract_ocr.py <path_to_image>
```
