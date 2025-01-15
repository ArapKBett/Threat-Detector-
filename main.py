# main.py
import pandas as pd
from preprocessing import load_and_preprocess_data
from feature_selection import select_features
from model_training import train_and_evaluate_model

if __name__ == "__main__":
    file_path = 'path_to_dataset.csv'
    processed_data = load_and_preprocess_data(file_path)
    data = pd.DataFrame(processed_data)
    labels = data['label']  # Replace with actual label column
    selected_features = select_features(data.drop('label', axis=1), labels)
    train_and_evaluate_model(data, labels, selected_features)
  
