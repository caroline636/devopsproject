import os
import json
from flask import Flask, request, render_template, redirect, url_for
from model_utils import extract_text_from_pdf, score_resume_against_jd

app = Flask(__name__)
DATA_DIR = os.getenv('DATA_DIR', '/app/data')  # mount host volume here

os.makedirs(DATA_DIR, exist_ok=True)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    jd = request.form.get('job_description', '')
    file = request.files.get('resume')
    if not file or file.filename == '':
        return "No file uploaded", 400
    # extract text (assume pdf else read as text)
    filename = file.filename
    if filename.lower().endswith('.pdf'):
        # pdfplumber can accept a file object
        text = extract_text_from_pdf(file)
    else:
        text = file.read().decode('utf-8', errors='ignore')
        if not text:  # if utf-8 fails, try utf-16
            file.seek(0)
            text = file.read().decode('utf-16', errors='ignore')
    score, matches = score_resume_against_jd(text, jd)
    result = {
        'filename': filename,
        'score': score,
        'matches': matches
    }
    # save JSON result (no DB)
    outpath = os.path.join(DATA_DIR, f"{filename}.json")
    with open(outpath, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    return render_template('result.html', result=result, jd=jd, resume_text=text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
