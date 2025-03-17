# NutriScope-AI: Intelligent Food Analysis & Wellness Advisor

## Overview
NutriScope-AI is an advanced food analysis system that leverages AI to assess the nutritional content of food items based on images provided by the user. The system provides detailed breakdowns of calorie count, macronutrients (carbohydrates, proteins, and fats), vitamins, and essential minerals. Additionally, it suggests suitable exercises based on the food intake to help users maintain a balanced diet and fitness plan.

## Features
- **Food Image Analysis**: Upload an image of your meal, and the AI will recognize the food items and extract nutritional information.
- **Nutrient Breakdown**: Provides detailed calorie counts and nutrient compositions, including vitamins and minerals.
- **Health & Exercise Recommendations**: Suggests personalized exercises based on dietary intake.
- **User-Friendly Interface**: Built using Streamlit for an interactive experience.

## Workflow
1. **User Uploads Food Image**
   - Supported formats: JPEG, JPG, PNG.
   - The image is processed using the `Pillow` library to ensure compatibility.

2. **AI Model Processes the Image**
   - The image is sent to `google-generativeai` (Gemini API) for food recognition and nutrient analysis.
   - AI extracts essential nutritional information, including calorie count, macronutrients, vitamins, and minerals.

3. **Nutritional Breakdown & Health Insights**
   - The system provides a structured breakdown of the food’s nutritional composition.
   - Generates personalized exercise suggestions based on the identified food and its calorie content.

4. **Interactive User Interface**
   - Results are displayed in an easy-to-read format using `streamlit`.
   - Users receive actionable insights to maintain a balanced diet and fitness regimen.

## Installation
To set up NutriScope-AI locally, follow these steps:
```sh
# Clone the repository
git clone https://github.com/RajIIITR/NutriScope-AI-Intelligent-Food-Analysis-Wellness-Advisor.git
cd NutriScope-AI-Intelligent-Food-Analysis-Wellness-Advisor

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Requirements
Ensure you have the following dependencies installed:
```sh
streamlit
python-dotenv==1.0.1
Pillow==9.5.0
google-generativeai==0.0.2
```

## Usage
Run the application with the following command:
```sh
streamlit run app.py
```

## Deployment
NutriScope-AI is also available online. Try it here: [NutriScope-AI Deployment](#) *(https://nutriscope-ai.streamlit.app/)*
