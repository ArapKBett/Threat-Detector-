# model_training.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

def train_and_evaluate_model(data, labels, selected_features):
    X_train, X_test, y_train, y_test = train_test_split(data[selected_features], labels, test_size=0.3, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    data = pd.read_csv('processed_data.csv')
    labels = data['label']  # Replace with actual label column
    selected_features = ['feature1', 'feature2', 'feature3']  # Replace with actual selected features
    train_and_evaluate_model(data, labels, selected_features)
  
