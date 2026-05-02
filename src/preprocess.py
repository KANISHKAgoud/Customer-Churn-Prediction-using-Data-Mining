import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def clean_data(df):

    # Drop unnecessary column
    if 'customerID' in df.columns:
        df = df.drop('customerID', axis=1)

    # Convert TotalCharges to numeric
    if 'TotalCharges' in df.columns:
        df['TotalCharges'] = pd.to_numeric(
            df['TotalCharges'],
            errors='coerce'
        )

    # Remove null values
    df = df.dropna()

    # Convert target column
    if 'Churn' in df.columns:
        df['Churn'] = df['Churn'].map({
            'Yes': 1,
            'No': 0
        })

    return df

def encode_data(df):

    df = pd.get_dummies(df, drop_first=True)

    return df