
# 📄 ResumeAI – ATS Resume Scanner

ResumeAI is a modern, AI-powered tool designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). By analyzing a resume PDF against a specific job description, it provides an instant match score, identifies missing keywords, and offers actionable improvement suggestions using Google's Gemini AI.

---

## ✨ Features

- **Instant Match Score**  
  Get a 0–100% compatibility score based on keyword matching.

- **AI-Powered Analysis**  
  Uses Google Gemini (Generative AI) to understand context, not just simple text matching.

- **Missing Keywords Detection**  
  Identifies critical hard skills, soft skills, and tools mentioned in the job description but missing from your resume.

- **Improvement Suggestions**  
  Actionable advice on how to rephrase resume bullet points.

- **Privacy Focused**  
  Files are processed locally or temporarily; no long-term storage (configurable).

- **Modern UI**  
  Responsive, glassmorphism-inspired design built with Tailwind CSS.

---

## 🛠️ Tech Stack

### Frontend
- HTML5  
- Vanilla JavaScript  
- Tailwind CSS (via CDN)  
- Lucide Icons  

### Backend
- Python 3.x  
- Flask  
- Google GenAI SDK (`google-genai`)  
- PyPDF2 (PDF parsing)  

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher  
- Google Cloud API Key for Gemini AI  

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Sai-11011/ATS-Checker.git
cd ATS-Checker
```
### 2. Install Backend Dependencies

It is recommended to use a virtual environment.

```bash
pip install flask google-genai PyPDF2
```

### 3. Configure API Key

Open `app.py` and replace the placeholder with your actual API key
(**Environment variable is recommended**).

```python
client = genai.Client(api_key="YOUR_ACTUAL_API_KEY")
```

Or using environment variables:

```bash
export GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"
```

---

## ▶️ Running the Application

### Start the Flask Server

```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000/
```

### Open the Frontend

Open `index.html` directly in your browser.

> **Note:**
> If you are serving the HTML file separately (e.g., via Live Server), ensure the `fetch` URL in your JavaScript matches your Flask server address.

---

## 📂 Project Structure

```
resume-ai-scanner/
│
├── main.py # Flask backend application
├── templates/         
│    └──index.html          # Main frontend user interface
├── uploads/            # Temporary storage for uploaded PDFs
└── README.md           # Project documentation
```

---

## 💡 Usage

1. **Upload Resume**
   Drag and drop your PDF resume into the upload zone.

2. **Paste Job Description**
   Copy and paste the full job description you are applying for.

3. **Analyze Resume**
   Click **"Analyze Resume"**.

4. **Review Results**
   Check your ATS score and detailed feedback to improve your resume.

---

## 🤝 Contributing

Contributions are welcome!
Please fork the repository and submit a pull request for any features, improvements, or bug fixes.

---

## 📄 License

This project is licensed under the **MIT License**.
See the `LICENSE` file for details.