# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import joblib, json
from preprocess import load_and_preprocess

def train_model():
    df = load_and_preprocess()

    # keep only numeric columns (you already did this in preprocess)
    # target
    y = df['Calories']
    X = df.drop(columns=['Calories'])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"✅ Model training complete!")
    print(f"MAE: {mae:.2f} | R²: {r2:.3f}")
    print("📊 Train shape:", X_train.shape, " Test shape:", X_test.shape)

    # save model + columns
    joblib.dump(model, "model.pkl")
    with open("model_columns.json", "w") as f:
        json.dump(list(X.columns), f)

    print("💾 Saved model -> model.pkl")
    print("💾 Saved feature list -> model_columns.json")

if __name__ == "__main__":
    train_model()
