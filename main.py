import PyPDF2
from flask import Flask, request, jsonify, render_template
from google import genai
import json 
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
# Ensure your .env file has API_KEY=your_gemini_key
client = genai.Client(api_key=os.getenv("API_KEY"))
MODEL_NAME = 'gemini-2.5-flash'

def extract_text_from_stream(file_stream):
    text = ""
    try:
        reader = PyPDF2.PdfReader(file_stream)
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        print(f"PDF Error: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    # 1. Validate File
    if 'pdf_file' not in request.files:
        return jsonify({"success": False, "error": "No file uploaded"}), 400
    
    file = request.files['pdf_file']
    if file.filename == '':
        return jsonify({"success": False, "error": "No file selected"}), 400

    # 2. Extract Job Description
    job_description = request.form.get('job_description', '')
    if not job_description:
        return jsonify({"success": False, "error": "Job Description is required"}), 400

    # 3. Extract PDF Text
    text = extract_text_from_stream(file)
    if not text:
        return jsonify({"success": False, "error": "Could not read PDF. Ensure it is text-based."}), 400
    
    try:
        # 4. Prompt Gemini
        prompt = f"""
        You are an experienced HR Manager and ATS (Applicant Tracking System) expert. 
        Compare the Resume Text below against the Job Description.

        JOB DESCRIPTION:
        {job_description}

        RESUME TEXT:
        {text}

        You MUST return your response as a valid JSON object with exactly these two keys:
        1. "score": An integer from 0 to 100 representing how well the resume matches the job description.
        2. "analysis": A structured Markdown string. It must include sections for "Strengths", "Missing Keywords", and "Formatting issues". Do not use JSON inside this string, just clean Markdown.
        """
        
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config={
                'response_mime_type': 'application/json'
            }
        )
        
        # 5. Parse Response
        raw_text = response.text.strip()
        
        try:
            data = json.loads(raw_text)
        except json.JSONDecodeError:
            if raw_text.startswith("```json"):
                raw_text = raw_text[7:]
            if raw_text.endswith("```"):
                raw_text = raw_text[:-3]
            data = json.loads(raw_text)
        
        return jsonify({
            "success": True,
            "data": data 
        })

    except Exception as e:
        print(f"AI Error: {e}")
        return jsonify({"success": False, "error": "AI Processing failed. Check server logs."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=8080)