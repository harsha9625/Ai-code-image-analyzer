# AI Code Image Analyzer  
### Scratch → Python Logic Interpreter with AI Error Detection

---

## Overview

AI Code Image Analyzer is a research-oriented Flask web application that interprets programming logic from uploaded images and converts it into executable Python code. The system is designed to understand Scratch-style block programming as well as handwritten Python code using AI reasoning.

The application simulates intelligent automated grading pipelines by extracting logic, detecting syntax or reasoning issues, generating corrected code, and saving structured evaluation outputs.

This project demonstrates how modern AI systems can bridge visual programming environments with text-based languages, enabling automated analysis and educational tooling.

---

## Motivation

Students and learners frequently submit programming work as screenshots, block-based diagrams, or handwritten notes. Traditional evaluation workflows struggle to process such visual input efficiently.

This project explores how AI-driven reasoning pipelines can:

- Interpret visual programming logic
- Convert block-based programs into Python
- Identify logical and structural issues
- Provide corrected solutions
- Automate evaluation workflows

The system mirrors real-world intelligent grading and AI-assisted development platforms.

---

## Core Capabilities

- Scratch-style block logic interpretation
- Handwritten Python code understanding
- Python code generation from visual logic
- Syntax and logical error detection
- Structured JSON result formatting
- Automated result persistence
- Interactive web-based upload interface
- Secure API integration
- Modular backend architecture

---

## System Architecture

### 1. Image Processing Layer
Uploads and encodes user images into a format suitable for AI analysis.

### 2. AI Reasoning Engine
Uses a language model to interpret visual logic, translate it into Python, and evaluate correctness.

### 3. Evaluation Pipeline
Identifies errors, explains issues, and produces corrected code.

### 4. Structured Output Layer
Stores results in JSON format for reproducibility and analysis.

### 5. Web Interface
Provides an interactive upload and visualization workflow.

---

## Project Structure

project/
│
├── app.py                  → Flask backend + AI pipeline  
├── templates/              → Upload interface  
├── test_images/            → Sample input images  
├── outputs/                → Saved JSON analysis results  
├── .env                    → Secure API key storage  
└── README.md               → Documentation  

---

## Processing Workflow

1. User uploads an image containing programming logic.  
2. Image is encoded and sent to the AI reasoning engine.  
3. Scratch-style logic is translated into Python code.  
4. Logical or syntax issues are detected.  
5. Corrected Python code is generated.  
6. Structured JSON output is saved and displayed.

---

## Installation & Setup

### Install Dependencies

pip install flask openai pillow python-dotenv

### Configure API Key

Create a `.env` file:

OPENAI_API_KEY=your_api_key_here

### Run Application

python app.py

Open browser:

http://127.0.0.1:5000

---

## Example Output Structure

{
  "cropped_image": "loop decreasing variable",
  "extracted_code": "while x > 10: x -= 2",
  "errors": [],
  "corrected_code": "while x > 10: x -= 2"
}

---

## Learning Outcomes

This project demonstrates:

- AI-assisted visual code interpretation  
- Scratch-to-Python translation pipelines  
- Structured evaluation frameworks  
- JSON-based output management  
- Secure API integration  
- Web backend architecture  
- Automated grading concepts  

---

## Applications

- Intelligent educational grading systems  
- Scratch-to-text code translators  
- Automated debugging assistants  
- AI learning tools  
- Research prototypes in visual programming  
- Code evaluation pipelines  

---

## Research Relevance

The system models how AI can reason about visual programming structures and convert them into formal representations. It explores multimodal reasoning, evaluation pipelines, and automated feedback — core themes in AI-assisted programming research.

---

## Security Practices

- API keys stored using environment variables  
- `.env` excluded from version control  
- Structured output validation  
- Controlled execution pipeline  

---

## Limitations

- Scratch interpretation depends on visual clarity  
- Complex nested logic may require tuning  
- AI reasoning latency varies with input complexity  

---

## Future Enhancements

- Batch image processing  
- Syntax highlighting visualization  
- Error line highlighting  
- Scratch-to-flowchart visualization  
- Offline OCR preprocessing  
- Model fine-tuning  
- Deployment dashboard  
- Evaluation analytics  

---

## Purpose

The project serves as an exploration into AI-driven interpretation of visual programming, bridging block-based educational tools with formal programming environments.

---

## Author

Harsha Vardhan  
AI Systems • Visual Programming • Automated Evaluation Research

---

## License

This project is intended for educational and research purposes.