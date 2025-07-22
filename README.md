# Employee Salary Predictor

A web application that predicts whether an employee earns more than 50K per year based on their profile details. Built with Streamlit and powered by a machine learning model trained on the Adult Census dataset.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [How to Run](#how-to-run)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Batch Prediction](#batch-prediction)
- [Customization](#customization)
- [License](#license)

---

## Overview

This project provides an interactive web interface to classify employees into two salary classes: earning more than 50K or not, based on their demographic and work-related features. The model is trained on a cleaned and preprocessed version of the Adult Census dataset.

## Features

- Predict salary class for a single employee via sidebar input.
- Batch prediction for multiple employees via CSV upload.
- Downloadable results for batch predictions.
- Clean, modern UI with custom styling.
- Model trained and selected for best accuracy.

## Project Structure

```
.
├── main.py                      # Streamlit web app
├── Employee_salary_prediction.ipynb  # Data cleaning, EDA, and model training
├── best_model.pkl               # Trained ML model
├── adult3.csv                   # Cleaned dataset
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## Dataset

- **Source:** Adult Census Income dataset (UCI Machine Learning Repository)
- **File:** `adult3.csv`
- **Features Used:**
  - `age`
  - `education`
  - `occupation`
  - `hours-per-week`
  - `gender`
- **Target:** `income` (binary: `>50K` or `<=50K`)

## Model Training

- Data cleaning and preprocessing performed in the Jupyter notebook.
- Categorical features encoded using `OneHotEncoder`.
- Numerical features scaled with `StandardScaler`.
- Multiple models evaluated: Logistic Regression, Random Forest, KNN, SVM, Gradient Boosting, and Voting Ensemble.
- **Best Model:** Gradient Boosting Classifier (accuracy ≈ 82.3%)
- The best model is saved as `best_model.pkl` and used in the web app.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd EmployeeSaleryPredictor
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run main.py
   ```

4. **Open your browser:**  
   Visit the local URL provided by Streamlit (usually http://localhost:8501).

## Dependencies

Key dependencies (see `requirements.txt` for full list):

- streamlit
- pandas
- scikit-learn
- joblib
- matplotlib

## Usage

### Single Prediction

- Use the sidebar to input employee details:
  - Age
  - Education Level
  - Job Role
  - Hours per week
  - Gender
- Click **Predict Salary Class** to see the result.

### Batch Prediction

- Go to the "Batch Prediction" section.
- Upload a CSV file with the same columns as the input features.
- View and download the predictions.

## Customization

- To retrain or improve the model, use the Jupyter notebook (`Employee_salary_prediction.ipynb`).
- Update the model by saving a new `best_model.pkl`.

## License

MIT License

---

**Note:**  
- Ensure your input data matches the expected format and categories.
- For any issues or contributions, please open an issue or pull request. 