# Awesome OCR: A Comprehensive Collection of OCR Libraries and Models

This repository serves as a comprehensive collection of code examples and test documents for various Optical Character Recognition (OCR) libraries and State-of-the-Art (SOTA) models. The goal is to provide a practical resource for developers and researchers to compare the performance of different OCR solutions across a range of document complexities, from simple digital text to complex, handwritten, and multi-column layouts.

## Table of Contents
1. [OCR Landscape: Traditional vs. SOTA](#ocr-landscape-traditional-vs-sota)
2. [Repository Structure](#repository-structure)
3. [Test Documents](#test-documents)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)

## OCR Landscape: Traditional vs. SOTA

The field of OCR has evolved significantly, moving from rule-based systems to deep learning models, and now to powerful Vision-Language Models (VLMs) based on the Transformer architecture. This repository includes examples from both traditional and modern approaches.

### Traditional and Open-Source Libraries

These libraries are generally easier to set up and are highly effective for standard OCR tasks.

| Library | Core Technology | Key Strengths | Use Case |
| :--- | :--- | :--- | :--- |
| **Tesseract** | LSTM-based (Traditional) | Most widely used, extensive language support, battle-tested. | Clean, high-quality digital documents. |
| **EasyOCR** | CNN + RNN (CRNN) | Simple to install and use, good multilingual support (80+ languages). | Quick text extraction from images and scanned documents. |
| **PaddleOCR** | PP-OCR (Deep Learning) | Excellent for multilingual and layout-aware OCR, fast, optimized for real-time. | Documents with complex layouts, multi-language text. |
| **RapidOCR** | ONNXRuntime/OpenVINO | Multi-platform, highly portable, and fast. | Edge devices, lightweight applications, cross-platform deployment. |

### State-of-the-Art (SOTA) and Transformer-based Models

These models, often built on the Transformer architecture, excel at complex document understanding, including layout analysis, table extraction, and handling noisy or handwritten text.

| Model | Developer | Core Technology | Key Strengths |
| :--- | :--- | :--- | :--- |
| **Surya** | Datalab | Transformer-based | High-performance document OCR, layout analysis, and reading order detection. |
| **Florence-2** | Microsoft | Vision-Language Model (VLM) | Unified model for various vision tasks, strong performance on complex document understanding. |
| **Qwen2-VL** | Alibaba | Vision-Language Model (VLM) | SOTA performance, strong multimodal capabilities, good for complex layouts. |
| **Chandra** | Datalab | Transformer-based | High-accuracy for complex documents (handwriting, tables, math), outputs structured data (Markdown/JSON). |
| **Dolphin** | ByteDance | Vision-Encoder-Decoder | Universal document parsing, excellent at handling tables and formulas. |
| **LightOnOCR** | LightOn AI | 1B-parameter VLM | Optimized for speed and efficiency, SOTA for its size on document understanding benchmarks. |

## Repository Structure

The repository is now structured with a dedicated folder for each OCR library/model, containing its specific code, requirements, and documentation.

```
awesome-ocr/
├── tesseract/
│   ├── tesseract_ocr.py
│   ├── requirements.txt
│   └── README.md
├── easyocr/
│   ├── easyocr_ocr.py
│   ├── requirements.txt
│   └── README.md
├── paddleocr/
│   ├── paddleocr_ocr.py
│   ├── requirements.txt
│   └── README.md
├── surya/
│   ├── surya_ocr.py
│   ├── requirements.txt
│   └── README.md
├── florence2/
│   ├── florence2_ocr.py
│   ├── requirements.txt
│   └── README.md
├── qwen2vl/
│   ├── qwen2vl_ocr.py
│   ├── requirements.txt
│   └── README.md
├── rapidocr/
│   ├── rapidocr_ocr.py
│   ├── requirements.txt
│   └── README.md
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
| **Simple** | Clean, digital-born documents with standard fonts and single-column layouts. Ideal for testing basic text recognition accuracy. | `sample_digital.pdf` |
| **Medium** | Scanned documents, multi-column layouts, and clear tables. Used to test layout analysis and structured data extraction capabilities. | `scanned_image.pdf`, `table_1.png`, `table_2.png` |
| **Hard** | Low-quality scans, complex forms, and challenging handwritten text. Designed to push the limits of SOTA models. | `handwriting_1.jpg`, `handwriting_2.jpg`, `messy_form.png`, `complex_doc.png` |

## Setup and Installation

### Prerequisites
*   Python 3.8+
*   For Tesseract, the Tesseract OCR engine must be installed on your system (e.g., `sudo apt install tesseract-ocr`).

### Installation
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/awesome-ocr.git
    cd awesome-ocr
    ```
2.  **Install Python dependencies for a specific model:**
    Navigate to the model's directory and install its specific requirements.
    ```bash
    cd tesseract
    pip install -r requirements.txt
    ```
    *Note: Installing dependencies for large VLM models (Florence-2, Qwen2-VL) may require a powerful machine and significant time.*

## Usage

To run an example, navigate to the model's directory and pass the path to a test document (relative to the repository root) to the corresponding script.

**Example: Running EasyOCR on a Medium-difficulty document**

```bash
cd easyocr
python easyocr_ocr.py ../tests/medium/table_1.png
```

**Example: Running PaddleOCR on a Hard-difficulty document**

```bash
cd paddleocr
python paddleocr_ocr.py ../tests/hard/handwriting_1.jpg
```
