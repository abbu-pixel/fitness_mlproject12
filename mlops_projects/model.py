from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(X, y):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def save_model(model, filename='sample_house_data.csv'):
    joblib.dump(model, filename)

def load_model(filename='house_price_model.pkl'):
    return joblib.load(filename)

def predict(model, X):
    return model.predict(X)
