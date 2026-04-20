## End to End Machine Learning project
## Overview
This is an end-to-end Machine Learning project that predicts a student's math score based on various demographic and academic factors. It provides a complete pipeline from data ingestion to model training and deployment via a web application.

## Features
- Provides an interactive **Flask Web Application** for user input.
- Takes the following user inputs to make a prediction:
  - Gender
  - Race/Ethnicity
  - Parental Level of Education
  - Lunch Type (Standard or Free/Reduced)
  - Test Preparation Course (Completed or None)
  - Reading Score
  - Writing Score
- Predicts the **Math Score** continuously based on a trained machine learning model.

## Project Structure
- `src/`: Contains the complete modular machine learning pipeline.
  - `components/`: Data ingestion, data transformation, and model training modules.
  - `pipeline/`: Training and prediction pipeline logic.
  - `logger.py` & `exception.py`: Custom logging and exception handling.
- `notebook/`: Jupyter notebooks for **Exploratory Data Analysis (EDA)** and model experimentation.
- `application.py`: The entry point for the Flask web application.
- `templates/`: Contains the HTML templates for the user interface (`index.html`, `home.html`).
- `requirements.txt`: List of all project dependencies.
- `setup.py`: Script to make the project installable as a package.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   cd ML-Project
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask web server:
   ```bash
   python application.py
   ```

2. Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

3. Navigate to the prediction page to enter student details and hit "Predict" to see the expected math score!

## Author
**Priyanshu**  
Email: priyanshuvats8806@gmail.com
