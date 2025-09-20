import fitz  # PyMuPDF
import traceback
import pytesseract
from PIL import Image


def ocr_pdf_to_text(pdf_path, output_txt="output.txt"):
    """Extract text from all pages of PDF using OCR and save to a file
    """
    try:
        doc = fitz.open(pdf_path)
        all_text = []

        for i, page in enumerate(doc):
            # Convert each page to image
            pix = page.get_pixmap(dpi=300)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

            # OCR using Tesseract
            text = pytesseract.image_to_string(img, lang="eng")

            # Save per-page text
            page_header = f"\n\n===== PAGE {i+1} =====\n\n"
            all_text.append(page_header + text.strip())

        # Combine all pages into one text string
        full_text = "\n".join(all_text)

        # Save to file
        with open(output_txt, "w", encoding="utf-8") as f:
            f.write(full_text)

        return full_text
    except Exception as e:
        print(traceback.print_exc())
        return ""


def load_text(file_path: str) -> str:
    """Load the full text from a file and return as a string."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
