from markitdown import MarkItDown
import sys

def run_markitdown(file_path):
    """
    Run Microsoft MarkItDown on a file.
    """
    try:
        md = MarkItDown()
        result = md.convert(file_path)
        
        print(f"--- MarkItDown Result for {file_path} ---")
        print(result.text_content)
        print("-" * 40)
        
        return result.text_content
    except Exception as e:
        print(f"Error running MarkItDown: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python markitdown_ocr.py <file_path>")
    else:
        run_markitdown(sys.argv[1])
