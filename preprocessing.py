# preprocessing.py
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    # Handle missing values
    data.fillna(method='ffill', inplace=True)
    # Encode categorical variables if any
    data = pd.get_dummies(data)
    # Standardize features
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    return data_scaled

if __name__ == "__main__":
    file_path = 'path_to_dataset.csv'
    processed_data = load_and_preprocess_data(file_path)
    pd.DataFrame(processed_data).to_csv('processed_data.csv', index=False)
