import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Define preprocessing pipeline for numeric and categorical features
def preprocess_data(df):
    numeric_features = ['LotArea', 'OverallQual', 'YearBuilt', 'GrLivArea']  # example features
    categorical_features = ['Neighborhood']

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Fit and transform the data
    X = df[numeric_features + categorical_features]
    X_processed = preprocessor.fit_transform(X)

    return X_processed, preprocessor
