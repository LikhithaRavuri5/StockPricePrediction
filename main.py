from data_loader import load_stock_data
from visualizer import plot_stock_price, plot_predictions
from model import prepare_data, train_model, evaluate_model, predict_future

STOCK_SYMBOL = "TSLA"

def run_pipeline():
    print("\n" + "="*50)
    print("  STOCK PRICE PREDICTION SYSTEM")
    print(f"  Analyzing: {STOCK_SYMBOL}")
    print("="*50 + "\n")

    print("STEP 1: Loading stock data...")
    data = load_stock_data()
    print("✓ Data loaded!\n")

    print("STEP 2: Visualizing price history...")
    plot_stock_price(data, STOCK_SYMBOL)
    print("✓ Graph saved!\n")

    print("STEP 3: Preparing data for ML...")
    X_train, X_test, y_train, y_test, df = prepare_data(data)
    print("✓ Data prepared!\n")

    print("STEP 4: Training ML model...")
    model = train_model(X_train, y_train)
    print("✓ Model trained!\n")

    print("STEP 5: Evaluating model...")
    y_predicted, mae, r2 = evaluate_model(model, X_test, y_test)
    print(f"✓ MAE: ${mae:.2f} | R2 Score: {r2:.4f}\n")

    print("STEP 6: Plotting predictions...")
    plot_predictions(y_test, y_predicted, STOCK_SYMBOL)
    print("✓ Prediction graph saved!\n")

    print("STEP 7: Predicting future prices...")
    future_prices = predict_future(model, df, days=30)
    print("✓ Future predictions ready!\n")

    print("="*50)
    print("  PREDICTION COMPLETE!")
    print(f"  Next 30 days average predicted price:")
    print(f"  ${future_prices.mean():.2f}")
    print("="*50 + "\n")

if __name__ == "__main__":
    run_pipeline()