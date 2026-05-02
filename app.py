from flask import Flask, render_template
from src.preprocess import load_data, clean_data, encode_data
from src.train_model import train_model
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():

    # Load dataset
    df = load_data("data/churn.csv")

    # Clean data
    df = clean_data(df)

    # Encode data
    df = encode_data(df)

    # Train model
    model, X_test, y_test = train_model(df)

    # Predict
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Report
    report = classification_report(y_test, y_pred)

    return render_template(
        "index.html",
        accuracy=round(accuracy * 100, 2),
        report=report
    )

if __name__ == "__main__":
    app.run(debug=True)