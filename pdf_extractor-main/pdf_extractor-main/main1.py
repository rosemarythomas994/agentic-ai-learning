from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
import json
from your_module import extract_data_to_json  # Your existing function

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'txt', 'docx'}

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        files = request.files.getlist('files')  # Use 'files' in HTML form
        extract_type = request.form.get('extract_type', 'export')
        results = []

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)

                try:
                    # Call your extraction function (works for PDF, TXT, DOCX; images will use OCR)
                    llm_result = extract_data_to_json(pdf_path=file_path,
                                                     prompt_path=f"templates/{extract_type}_prompt.txt")
                except Exception as e:
                    llm_result = {"error": str(e)}

                results.append({
                    'filename': filename,
                    'ocr_preview': "OCR preview not implemented yet",  # Optionally implement
                    'llm_result': json.dumps(llm_result, indent=2)
                })

        return render_template('output.html', results=results)

    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)
