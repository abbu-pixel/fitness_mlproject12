import pandas as pd
import numpy as np
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from xgboost import XGBRegressor

def main():
    data = pd.read_csv('train.csv')

    target = 'SalePrice'
    features = data.drop(columns=[target])
    y = data[target]

    numeric_features = features.select_dtypes(include=[np.number]).columns.tolist()
    categorical_features = features.select_dtypes(include=['object']).columns.tolist()

    numeric_transformer = SimpleImputer(strategy='median')
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', XGBRegressor(n_estimators=100, max_depth=5, learning_rate=0.1, random_state=42))
    ])

    model.fit(features, y)

    joblib.dump(model, 'xgb_house_price_model.pkl')

    print("Training complete and model saved as 'xgb_house_price_model.pkl'.")

if __name__ == "__main__":
    main()
