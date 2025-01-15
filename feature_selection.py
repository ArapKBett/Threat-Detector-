# feature_selection.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def select_features(data, labels, num_features=10):
    model = RandomForestClassifier()
    model.fit(data, labels)
    feature_importances = model.feature_importances_
    important_features = sorted(zip(feature_importances, data.columns), reverse=True)[:num_features]
    return [feature[1] for feature in important_features]

if __name__ == "__main__":
    data = pd.read_csv('processed_data.csv')
    labels = data['label']  # Replace with actual label column
    features = select_features(data.drop('label', axis=1), labels)
    print("Selected Features:", features)
  
