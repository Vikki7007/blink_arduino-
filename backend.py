from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from PIL import Image
import os

# Set up Flask app
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Configure Gemini API
os.environ['GOOGLE_API_KEY'] = "AIzaSyD3bb1Cbsfd4MCsOhwROP6S-oxshpCerrA"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def send_text_request(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

def image_analysis_request(image_path):
    model = genai.GenerativeModel('gemini-pro-vision')
    image = Image.open(image_path)
    response = model.generate_content(["Analyze the image", image])
    return response.text

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    prompt = data.get("prompt", "")
    response = send_text_request(prompt)
    return jsonify({"response": response})

@app.route('/analyze-image', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
    
    image = request.files['image']
    image_path = "temp.jpg"
    image.save(image_path)
    
    response = image_analysis_request(image_path)
    os.remove(image_path)  # Clean up the saved image
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
