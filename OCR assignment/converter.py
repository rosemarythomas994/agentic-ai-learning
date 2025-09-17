import json
import argparse
import PyPDF2
from pdfminer.high_level import extract_text
import tabula
from PIL import Image
import pytesseract
import fitz  # PyMuPDF for image conversion in OCR fallback
import io

def extract_text_from_pdf(pdf_path, use_ocr=False):
    """Extract text using PyPDF2 or pdfminer, with OCR fallback."""
    text = ''
    if not use_ocr:
        try:
            # Try pdfminer for better layout
            text = extract_text(pdf_path)
            if text.strip():  # If text is found
                return text
        except Exception as e:
            print(f"pdfminer error: {e}")
        
        try:
            # Fallback to PyPDF2
            with open(pdf_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    text += page.extract_text() or ''
            if text.strip():
                return text
        except Exception as e:
            print(f"PyPDF2 error: {e}")
    
    # OCR fallback for image-based PDFs
    print("Falling back to OCR...")
    doc = fitz.open(pdf_path)
    ocr_text = ''
    for page in doc:
        pix = page.get_pixmap(dpi=300)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        ocr_text += pytesseract.image_to_string(img, lang='eng') + '\n'
    doc.close()
    return ocr_text.strip() or 'No text extracted'

def extract_tables_from_pdf(pdf_path):
    """Extract tables using tabula-py."""
    try:
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
        tables_json = [table.to_dict(orient='records') for table in tables]
        return tables_json
    except Exception as e:
        print(f"Table extraction error: {e}")
        return []

def convert_pdf_to_json(pdf_path, output_json='output.json', use_ocr=False):
    """Main function to convert PDF to JSON."""
    text = extract_text_from_pdf(pdf_path, use_ocr)
    tables = extract_tables_from_pdf(pdf_path)
    
    data = {
        'extracted_text': text,
        'extracted_tables': tables
    }
    
    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Conversion complete. JSON saved to {output_json}")
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert PDF to JSON")
    parser.add_argument("pdf_path", help="Path to the input PDF file")
    parser.add_argument("--output", default="output.json", help="Path to output JSON file")
    parser.add_argument("--ocr", action="store_true", help="Force OCR for image-based PDFs")
    args = parser.parse_args()
    
    convert_pdf_to_json(args.pdf_path, args.output, args.ocr)