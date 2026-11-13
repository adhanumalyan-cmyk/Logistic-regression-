
# STEP 25: Prediction with Input Validation

import joblib
import pandas as pd

# Load saved model
model = joblib.load("../models/iris_model.pkl")

print("=== IRIS FLOWER PREDICTION ===")

try:
    # Get measurements from user
    sepal_length = float(input("Enter Sepal Length (cm): "))
    sepal_width = float(input("Enter Sepal Width (cm): "))
    petal_length = float(input("Enter Petal Length (cm): "))
    petal_width = float(input("Enter Petal Width (cm): "))

    # Check whether measurements are positive
    measurements = [
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]

    if any(value <= 0 for value in measurements):
        print("Error: Measurements must be positive numbers.")

    else:
        # Prepare input
        new_flower = pd.DataFrame(
            [measurements],
            columns=[
                "SepalLengthCm",
                "SepalWidthCm",
                "PetalLengthCm",
                "PetalWidthCm"
            ]
        )

        # Predict
        prediction = model.predict(new_flower)

        print("\n--- PREDICTION RESULT ---")
        print("Predicted Species:", prediction[0])

except ValueError:
    print("Error: Please enter valid numeric values!")
