import re
import json
from doc_utils import ocr_pdf_to_text, load_text
from llm_utils import call_llm

prompt_mapper = {"export" : "export_prompt.txt", "license": "license_prompt.txt" }

def extract_data_to_json(pdf_path, prompt_path):
    print("** Starting data extraction ** ")
    extracted_text = ocr_pdf_to_text(pdf_path=pdf_path)
    assert extracted_text != ""
    print("** Data Extracted **")
    prompt_template = load_text(file_path=prompt_path)
    prompt_ = prompt_template.format(input_data=extracted_text)

    print("Starting LLM Call")
    response_content = call_llm(prompt_)
    pattern = r'<text>(.*?)</text>'
    match = re.search(pattern, response_content, re.DOTALL)
    if match:
        response_content = json.loads(match.group(1))
        print(response_content)
    else:
        print(response_content)
    return response_content

def main(extract_file_type, file_name="ocr test 2.pdf"):
    pdf_file_name = file_name
    prompt_file = prompt_mapper.get(extract_file_type)
    if prompt_file is None:
        print("Invalid file type")
        return False
    pdf_path = f"docs/{pdf_file_name}"
    prompt_path = f"templates/{prompt_file}"
    extract_data_to_json(pdf_path=pdf_path, prompt_path=prompt_path)


if __name__ == "__main__":
    main(extract_file_type="export")
