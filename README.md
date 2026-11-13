# Iris Flower Classification 🌸

## Project Overview

Iris Flower Classification is a Machine Learning project that predicts the species of an Iris flower based on four physical measurements.

The project uses the Logistic Regression algorithm to classify flowers into three species:

- Iris-setosa
- Iris-versicolor
- Iris-virginica

## Dataset

Dataset: Kaggle Iris Dataset

- Total records: 150
- Total columns: 6
- Input features: 4
- Target variable: Species
- Classes: 3

### Input Features

1. Sepal Length (cm)
2. Sepal Width (cm)
3. Petal Length (cm)
4. Petal Width (cm)

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib

## Machine Learning Workflow

1. Load the Kaggle dataset.
2. Explore and understand the data.
3. Separate input features and target labels.
4. Split data into training and testing sets.
5. Train the Logistic Regression model.
6. Evaluate using Accuracy, Confusion Matrix and Classification Report.
7. Save the trained model.
8. Predict new flower species using user input.

## Project Structure

```text
Iris_Flower_Classification/
├── data/
│   └── Iris.csv
├── models/
│   └── iris_model.pkl
├── src/
│   ├── train.py
│   └── predict.py
├── docs/
└── README.md
```

## How to Run

### 1. Activate Environment

```bash
conda activate ml_learning
```

### 2. Train the Model

```bash
cd src
python train.py
```

### 3. Predict a New Flower

```bash
python predict.py
```

Enter the four flower measurements when prompted.

## Algorithm

Logistic Regression

## Project Status

Core model training, evaluation, model saving and interactive prediction implemented.

## Future Improvements

- Build a web interface using Streamlit.
- Add input validation and improved error handling.
- Compare multiple Machine Learning algorithms.
- Deploy the model as a web application.# Logistic-regression-
# Logistic-regression-
# Logistic-regression-
# Logistic-regression-
# Logistic-regression-
