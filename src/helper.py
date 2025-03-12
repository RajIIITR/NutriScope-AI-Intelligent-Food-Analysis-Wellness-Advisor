import google.generativeai as genai
import io
from PIL import Image
import os

# Configure the API
def configure_genai():
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY environment variable not set")
    genai.configure(api_key=GOOGLE_API_KEY)

# Function to process image and get response
def get_gemini_response(prompt, image):
    # Ensure API is configured
    configure_genai()
    
    # Load the generative model
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # Prepare the image data
    if image is not None:
        # Convert PIL Image to bytes
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        image_bytes = buffered.getvalue()
        
        # Generate content
        response = model.generate_content([prompt, {'mime_type': 'image/jpeg', 'data': image_bytes}])
        return response.text
    else:
        return "Please upload an image."