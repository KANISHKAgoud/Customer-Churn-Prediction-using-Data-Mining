import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    # Convert TotalCharges to numeric
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    df = df.dropna()

    # Convert target column
    df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

    return df

def encode_data(df):
    df = pd.get_dummies(df, drop_first=True)
    return df