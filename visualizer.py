import matplotlib.pyplot as plt

def plot_stock_price(data, symbol="TSLA"):
    print("Drawing stock price graph...")
    
    plt.figure(figsize=(12, 6))
    
    plt.plot(data.index, data['Close'], 
             color='blue', 
             linewidth=1.5,
             label=f'{symbol} Closing Price')
    
    plt.title(f'{symbol} Stock Price History (2020-2024)', 
              fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{symbol}_price_history.png')
    print(f"Graph saved as {symbol}_price_history.png")
    plt.show()

def plot_predictions(actual, predicted, symbol="TSLA"):
    print("Drawing prediction graph...")
    
    plt.figure(figsize=(12, 6))
    
    plt.plot(actual, 
             color='blue', 
             linewidth=1.5,
             label='Actual Price')
    
    plt.plot(predicted, 
             color='red', 
             linewidth=1.5,
             linestyle='dashed',
             label='Predicted Price')
    
    plt.title(f'{symbol} — Actual vs Predicted Stock Price', 
              fontsize=16, fontweight='bold')
    plt.xlabel('Days', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(f'{symbol}_predictions.png')
    print(f"Graph saved as {symbol}_predictions.png")
    plt.show()

if __name__ == "__main__":
    from data_loader import load_stock_data
    data = load_stock_data()
    plot_stock_price(data)