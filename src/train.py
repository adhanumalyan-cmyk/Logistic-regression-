
# ==========================================
# IRIS FLOWER CLASSIFICATION
# Using Logistic Regression
# ==========================================


# STEP 1: Import required libraries

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score

from sklearn.metrics import confusion_matrix

from sklearn.metrics import classification_report

import joblib

# STEP 2: Load the Kaggle dataset

df = pd.read_csv("../data/Iris.csv")


# STEP 3: Display first 5 rows

print("\n--- FIRST 5 ROWS ---")
print(df.head())


# STEP 4: Check dataset shape

print("\n--- DATASET SHAPE ---")
print(df.shape)


# STEP 5: Display column names

print("\n--- COLUMN NAMES ---")
print(df.columns)


# STEP 6: Check data types

print("\n--- DATA TYPES ---")
print(df.dtypes)


# STEP 7: Display dataset information

print("\n--- DATASET INFORMATION ---")
df.info()


# STEP 8: Statistical summary

print("\n--- STATISTICAL SUMMARY ---")
print(df.describe())


# STEP 9: Check missing values

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())


# STEP 10: Check duplicate records

print("\n--- DUPLICATE RECORDS ---")
print(df.duplicated().sum())


# STEP 11: Check species distribution

print("\n--- SPECIES DISTRIBUTION ---")
print(df["Species"].value_counts())


# STEP 12: Separate input features (X) and target (y)

X = df.drop(["Id", "Species"], axis=1)

y = df["Species"]


print("\n--- INPUT FEATURES (X) ---")
print(X.head())

print("\n--- TARGET (y) ---")
print(y.head())

print("\nX Shape:", X.shape)
print("y Shape:", y.shape)


# STEP 13: Split dataset into training and testing data

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


print("\n--- TRAIN TEST SPLIT ---")
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)


# STEP 14: Create Logistic Regression model

model = LogisticRegression(max_iter=200)


# STEP 15: Train the model

model.fit(X_train, y_train)


# STEP 16: Display training status

print("\n--- MODEL TRAINING ---")
print("Logistic Regression model trained successfully!")


y_pred = model.predict(X_test)

# STEP 18: Display actual and predicted values

print("\n--- MODEL PREDICTIONS ---")

# STEP 17: Predict using testing data

print("Actual Species:")
print(y_test.values)

print("\nPredicted Species:")
print(y_pred)

#STEP 19 : Calculate model accuracy

accuracy = accuracy_score(y_test , y_pred)

print("\n ---MODEL ACCURACY ---")
print("Accuracy:",accuracy * 100,"%")


# STEP 20: Calculate Confusion Matrix

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=model.classes_
)

# Convert confusion matrix into a readable table
cm_df = pd.DataFrame(
    cm,
    index=model.classes_,
    columns=model.classes_
)

print("\n--- CONFUSION MATRIX ---")
print(cm_df)


#STEP 21 : Generate Classification report

report = classification_report(y_test,y_pred)

print("\n --- classification report ---")

print(report)


# STEP 22: Save the trained model

joblib.dump(model, "../models/iris_model.pkl")

print("\n--- MODEL SAVING ---")
print("Model saved successfully!")