import joblib
import pandas as pd
import numpy as np
import sys

# --- Load Saved Objects ---
# Ensure the paths match where you saved these files
try:
    model = joblib.load('model.joblib')
    scaler = joblib.load('scaler.joblib') # Load the fitted scaler
    # Assuming feature_columns.joblib was saved as suggested earlier
    feature_columns = joblib.load('feature_columns.joblib')
    print("Model, Scaler, and Feature Columns loaded successfully.")
except FileNotFoundError as e:
    print(f"Error loading required files: {e}")
    print("Please ensure 'model.joblib', 'scaler.joblib', and 'feature_columns.joblib' are in the correct directory.")
    sys.exit(1) # Exit the script if files are not found

# --- Define Preprocessing Logic ---
# Define the mapping used for BusinessTravel
business_travel_mapping = {'Non-Travel': 1, 'Travel_Rarely': 2, 'Travel_Frequently': 3}

# Define the categorical columns that were one-hot encoded
categorical_cols = ['MaritalStatus', 'OverTime']

# Manually define the original numerical columns (including mapped BusinessTravel)
# This list should match the columns that were passed to the scaler during training
original_numerical_cols_before_ohe = ['BusinessTravel', 'DailyRate', 'DistanceFromHome', 'Education',
                                    'EnvironmentSatisfaction', 'HourlyRate', 'JobInvolvement', 'JobLevel',
                                    'JobSatisfaction', 'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked',
                                    'PercentSalaryHike', 'PerformanceRating', 'RelationshipSatisfaction',
                                    'StockOptionLevel', 'TotalWorkingYears', 'TrainingTimesLastYear',
                                    'WorkLifeBalance', 'YearsAtCompany', 'YearsInCurrentRole',
                                    'YearsSinceLastPromotion', 'YearsWithCurrManager']


def preprocess_new_data(data_df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocesses new data to be used for prediction.

    Applies the same transformations as used during model training:
    - BusinessTravel mapping
    - One-hot encoding for specified categorical columns
    - Standardization using the loaded scaler
    - Reorders and fills missing columns to match training data features.

    Args:
        data_df: DataFrame containing the raw data to predict.

    Returns:
        DataFrame with preprocessed features, ready for the model.
    """
    # Apply BusinessTravel mapping
    data_df['BusinessTravel'] = data_df['BusinessTravel'].map(business_travel_mapping)

    # Apply one-hot encoding
    data_df_encoded = pd.get_dummies(data_df, columns=categorical_cols)

    # Ensure all columns from training data are present and in the correct order
    # Fill missing columns with 0. This handles cases where a category in training
    # data is not present in the new data.
    data_df_aligned = data_df_encoded.reindex(columns=feature_columns, fill_value=0)

    # Select only the columns that were intended to be scaled
    data_to_scale = data_df_aligned[original_numerical_cols_before_ohe]

    # Apply standardization using the loaded scaler
    data_scaled_values = scaler.transform(data_to_scale)
    data_scaled_df = pd.DataFrame(data_scaled_values, columns=original_numerical_cols_before_ohe, index=data_df_aligned.index)

    # Replace the original numerical columns with the scaled ones in the aligned dataframe
    data_df_aligned[original_numerical_cols_before_ohe] = data_scaled_df


    return data_df_aligned

# --- Prediction Function ---
def predict_employee_attrition(data_df: pd.DataFrame):
    """
    Predicts the likelihood of employee attrition for the given data.

    Args:
        data_df: DataFrame containing the raw employee data.
    """
    # Preprocess the input data
    preprocessed_data = preprocess_new_data(data_df.copy()) # Work on a copy

    # Ensure the columns of preprocessed data match the features the model was trained on
    if not preprocessed_data.columns.equals(pd.Index(feature_columns)):
        print("Error: Input data columns after preprocessing do not match model training features.")
        print("Expected columns:", feature_columns)
        print("Input columns after preprocessing:", preprocessed_data.columns.tolist()
        sys.exit(1) # Exit if columns don't match

    # Make prediction using the loaded model
    try:
        predictions_proba = model.predict_proba(preprocessed_data)
        predicted_class = np.argmax(predictions_proba, axis=1)

        # Map the predicted class to labels
        labels = {0: 'No', 1: 'Yes'}
        predicted_label = [labels[i] for i in predicted_class]

        print("Prediction Results:")
        for i in range(len(data_df)):
            print(f"  Employee {i+1}:")
            print(f"    Probability of Attrition (No/Yes): {predictions_proba[i]}")
            print(f"    Predicted Attrition Status: {predicted_label[i]}")

    except Exception as e:
        print(f"An error occurred during prediction: {e}")
        sys.exit(1) # Exit on prediction error


# --- Example Usage ---
# The code inside this block will only run when the script is executed directly
if __name__ == "__main__":
    # Example data for prediction
    # Make sure the column names and data types match your original data *before* any preprocessing
    example_employee_data = {
       'BusinessTravel': ['Travel_Frequently'],
       'DailyRate': [1444],
       'DistanceFromHome': [1],
       'Education': [4],
       'EnvironmentSatisfaction': [4],
       'HourlyRate': [88],
       'JobInvolvement': [3],
       'JobLevel': [1],
       'JobSatisfaction': [2],
       'MaritalStatus': ['Married'],
       'MonthlyIncome': [2991],
       'MonthlyRate': [5224],
       'NumCompaniesWorked': [0],
       'OverTime': ['Yes'], 
       'PercentSalaryHike': [11],
       'PerformanceRating': [3],
       'RelationshipSatisfaction': [2],
       'StockOptionLevel': [1],
       'TotalWorkingYears': [7],
       'TrainingTimesLastYear': [2],
       'WorkLifeBalance': [3],
       'YearsAtCompany': [6],
       'YearsInCurrentRole': [2],
       'YearsSinceLastPromotion': [3],
       'YearsWithCurrManager': [1],
    }

    # Create a DataFrame from the example data
    example_df = pd.DataFrame(example_employee_data)

    # Run the prediction
    print("--- Running Prediction on Example Data ---")
    predict_employee_attrition(example_df)
