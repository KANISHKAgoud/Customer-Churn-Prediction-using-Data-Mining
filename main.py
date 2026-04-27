from src.preprocess import load_data, clean_data, encode_data
from src.train_model import train_model
from src.evaluate import evaluate_model

def main():
    df = load_data("data/churn.csv")
    df = clean_data(df)
    df = encode_data(df)

    model, X_test, y_test = train_model(df)
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()