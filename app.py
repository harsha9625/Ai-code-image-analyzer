from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv
import base64
from PIL import Image
import io
import os
import json
from datetime import datetime

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Secure API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# AI instruction prompt
master_prompt = """
You are an advanced code interpreter.

The user uploads an image that may contain Scratch-style block programming or handwritten Python code.

Your job:

1. Understand the logic of the blocks or code.
2. Convert Scratch-style logic into equivalent Python code.
3. Detect logical or syntax issues.
4. Return structured JSON.

Return ONLY JSON:

{
  "cropped_image": "description of visible logic",
  "extracted_code": "interpreted python code",
  "errors": [
    {
      "type": "logic/syntax",
      "line": "line number",
      "code": "problematic code",
      "explanation": "reason + fix"
    }
  ],
  "corrected_code": "final working python code"
}

If no errors exist, return empty list for errors.
Never return null values.
"""

# Encode uploaded image to base64
def encode_image(file_storage):
    image = Image.open(file_storage.stream)
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()


@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files["image"]
    base64_img = encode_image(file)

    try:

        # Call OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": master_prompt},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Analyze this code image."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_img}"
                            },
                        },
                    ],
                },
            ],
        )

        # Safe JSON parsing
        raw_text = response.choices[0].message.content.strip()

        if raw_text.startswith("```"):
            parts = raw_text.split("```")
            if len(parts) >= 2:
                raw_text = parts[1].replace("json", "", 1).strip()

        try:
            structured_json = json.loads(raw_text)
        except Exception as e:
            structured_json = {
                "error": "JSON parse failed",
                "details": str(e),
                "raw_output": raw_text
            }

        # Save JSON output
        os.makedirs("outputs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"outputs/analysis_{timestamp}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(structured_json, f, indent=4)

        return jsonify({
            "message": "Analysis complete",
            "output_file": filename,
            "result": structured_json
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
