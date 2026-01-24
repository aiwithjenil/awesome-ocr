# Awesome OCR: A Comprehensive Collection of OCR Libraries and Models

This repository serves as a comprehensive collection of code examples and test documents for various Optical Character Recognition (OCR) libraries and State-of-the-Art (SOTA) models. The goal is to provide a practical resource for developers and researchers to compare the performance of different OCR solutions across a range of document complexities, from simple digital text to complex, handwritten, and multi-column layouts.

## Table of Contents
1. [OCR Landscape: Traditional vs. SOTA](#ocr-landscape-traditional-vs-sota)
2. [Repository Structure](#repository-structure)
3. [Test Documents](#test-documents)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)

## OCR Landscape: Traditional vs. SOTA

The field of OCR has evolved significantly, moving from rule-based systems to deep learning models, and now to powerful Vision-Language Models (VLMs) based on the Transformer architecture.

### Traditional and Open-Source Libraries

| Library | Core Technology | Key Strengths | Use Case |
| :--- | :--- | :--- | :--- |
| **Tesseract** | LSTM-based | Most widely used, extensive language support. | Clean digital documents. |
| **EasyOCR** | CRNN | Simple to use, 80+ languages supported. | Quick text extraction. |
| **PaddleOCR** | PP-OCR | Excellent for multilingual and layout-aware OCR. | Complex layouts, multi-language. |
| **RapidOCR** | ONNX/OpenVINO | Fast, portable, and lightweight. | Edge devices, cross-platform. |
| **docTR** | Deep Learning | High-performing, accessible, PyTorch/TF support. | General OCR tasks. |
| **Kraken** | Deep Learning | Optimized for historical and non-Latin scripts. | Historical documents. |
| **Calamari** | Deep Learning | High performance on historical documents. | Academic/Historical research. |
| **GOCR** | Feature Extraction | Classic open-source engine, lightweight. | Simple, high-contrast text. |
| **GNU Ocrad** | Feature Extraction | Classic GNU tool, lightweight. | Simple text recognition. |

### SOTA and Transformer-based Models

| Model | Developer | Core Technology | Key Strengths |
| :--- | :--- | :--- | :--- |
| **Surya** | Datalab | Transformer | High-performance OCR and layout analysis. |
| **Florence-2** | Microsoft | VLM | Unified model for vision tasks, strong OCR. |
| **Qwen2-VL** | Alibaba | VLM | SOTA performance, strong multimodal capabilities. |
| **GOT-OCR2.0** | UCAS | Transformer | Unified end-to-end model for diverse OCR tasks. |
| **Nougat** | Meta AI | Transformer | Specialized for scientific PDFs and LaTeX. |
| **MinerU** | OpenDataLab | LayoutLMv3 | High-quality PDF to Markdown/JSON conversion. |
| **Marker** | Vik Paruchuri | Pipeline | Fast, high-accuracy PDF to Markdown. |
| **MarkItDown** | Microsoft | Utility | Lightweight tool for converting various files to MD. |
| **TrOCR** | Microsoft | Transformer | End-to-end Transformer-based OCR. |
| **Donut** | Naver | Transformer | OCR-free document understanding. |
| **LayoutLMv3** | Microsoft | Transformer | Multi-modal Transformer for Document AI. |
| **olmOCR** | AI2 | LLM-based | Clean text extraction from noisy scans. |

## Repository Structure

The repository is structured with a dedicated folder for each OCR library/model, containing its specific code, requirements, and documentation.

```
awesome-ocr/
├── tesseract/
├── easyocr/
├── paddleocr/
├── surya/
├── florence2/
├── qwen2vl/
├── rapidocr/
├── doctr/
├── got-ocr2/
├── nougat/
├── mineru/
├── marker/
├── markitdown/
├── trocr/
├── donut/
├── layoutlmv3/
├── kraken/
├── calamari/
├── gocr/
├── ocrad/
├── olmocr/
├── tests/
│   ├── simple/
│   ├── medium/
│   └── hard/
└── README.md
```

## Test Documents

We have curated a set of test documents categorized by difficulty to provide a robust evaluation environment.

| Category | Description | Files |
| :--- | :--- | :--- |
| **Simple** | Clean, digital-born documents. | `sample_digital.pdf` |
| **Medium** | Scanned documents, multi-column layouts, tables. | `scanned_image.pdf`, `table_1.png`, `table_2.png` |
| **Hard** | Low-quality scans, complex forms, handwriting. | `handwriting_1.jpg`, `handwriting_2.jpg`, `messy_form.png`, `complex_doc.png` |

## Setup and Installation

### Prerequisites
*   Python 3.8+
*   System-level dependencies (e.g., `tesseract-ocr` for Tesseract, `gocr` for GOCR).

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/awesome-ocr.git
    cd awesome-ocr
    ```
2.  **Install dependencies for a specific model:**
    ```bash
    cd <model_folder>
    pip install -r requirements.txt
    ```

## Usage

Navigate to the model's directory and run the script with a test document path.

```bash
cd easyocr
python easyocr_ocr.py ../tests/medium/table_1.png
```
