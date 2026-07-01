import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

def prepare_data(data):
    print("Preparing data for ML model...")
    
    df = data.copy()
    
    df['Days'] = np.arange(len(df))
    
    X = df[['Days']].values
    y = df['Close'].values
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"Training data: {len(X_train)} days")
    print(f"Testing data: {len(X_test)} days")
    
    return X_train, X_test, y_train, y_test, df

def train_model(X_train, y_train):
    print("Training Linear Regression model...")
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    print("Model training complete!")
    return model

def evaluate_model(model, X_test, y_test):
    print("Evaluating model performance...")
    
    y_predicted = model.predict(X_test)
    
    mae = mean_absolute_error(y_test, y_predicted)
    r2 = r2_score(y_test, y_predicted)
    
    print(f"Mean Absolute Error: ${mae:.2f}")
    print(f"R2 Score: {r2:.4f}")
    
    return y_predicted, mae, r2

def predict_future(model, df, days=30):
    print(f"Predicting next {days} days...")
    
    last_day = len(df)
    future_days = np.arange(last_day, last_day + days).reshape(-1, 1)
    future_prices = model.predict(future_days)
    
    print("Future predictions ready!")
    return future_prices

if __name__ == "__main__":
    from data_loader import load_stock_data
    
    data = load_stock_data()
    X_train, X_test, y_train, y_test, df = prepare_data(data)
    model = train_model(X_train, y_train)
    y_predicted, mae, r2 = evaluate_model(model, X_test, y_test)
    future = predict_future(model, df)
    print(f"\nNext 30 days predicted prices:")
    for i, price in enumerate(future.flatten(), 1):
          print(f"Day {i}: ${price:.2f}")