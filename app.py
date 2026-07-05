import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from data_loader import load_stock_data
from model import prepare_data, train_model, evaluate_model, predict_future

st.set_page_config(
    page_title="Stock Price Prediction",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Stock Price Prediction App")
st.markdown("**Predict future stock prices using Machine Learning!**")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    stock_symbol = st.text_input(
        "Enter Stock Symbol",
        value="TSLA",
        help="Example: TSLA, AAPL, INFY, TCS.NS"
    )

with col2:
    future_days = st.slider(
        "Days to Predict",
        min_value=7,
        max_value=60,
        value=30
    )

analyze_button = st.button("🔍 Analyze Stock", type="primary")

if analyze_button:
    with st.spinner(f"Fetching {stock_symbol} stock data..."):
        import yfinance as yf
        stock = yf.download(stock_symbol, start="2020-01-01", end="2024-01-01")
        stock = stock[['Close']].dropna()

    if len(stock) == 0:
        st.error("Invalid stock symbol! Please try again.")
    else:
        st.success(f"✅ Downloaded {len(stock)} days of data!")

        st.markdown("---")
        st.subheader("📊 Stock Price History")

        fig1, ax1 = plt.subplots(figsize=(12, 5))
        ax1.plot(stock.index, stock['Close'],
                color='blue', linewidth=1.5,
                label=f'{stock_symbol} Closing Price')
        ax1.set_title(f'{stock_symbol} Stock Price History (2020-2024)',
                     fontsize=14, fontweight='bold')
        ax1.set_xlabel('Date')
        ax1.set_ylabel('Price (USD)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig1)

        st.markdown("---")
        st.subheader("🤖 Training ML Model...")

        with st.spinner("Training Linear Regression model..."):
            X_train, X_test, y_train, y_test, df = prepare_data(stock)
            model = train_model(X_train, y_train)
            y_predicted, mae, r2 = evaluate_model(model, X_test, y_test)

        col3, col4 = st.columns(2)
        with col3:
            st.metric("Mean Absolute Error", f"${mae:.2f}")
        with col4:
            st.metric("R2 Score", f"{r2:.4f}")

        st.markdown("---")
        st.subheader("📉 Actual vs Predicted Prices")

        fig2, ax2 = plt.subplots(figsize=(12, 5))
        ax2.plot(y_test, color='blue',
                linewidth=1.5, label='Actual Price')
        ax2.plot(y_predicted, color='red',
                linewidth=1.5, linestyle='dashed',
                label='Predicted Price')
        ax2.set_title(f'{stock_symbol} — Actual vs Predicted',
                     fontsize=14, fontweight='bold')
        ax2.set_xlabel('Days')
        ax2.set_ylabel('Price (USD)')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig2)

        st.markdown("---")
        st.subheader(f"🔮 Next {future_days} Days Prediction")

        future_prices = predict_future(model, df, days=future_days)
        future_flat = future_prices.flatten()

        col5, col6, col7 = st.columns(3)
        with col5:
            st.metric("Starting Price", f"${future_flat[0]:.2f}")
        with col6:
            st.metric("Ending Price", f"${future_flat[-1]:.2f}")
        with col7:
            st.metric("Average Price", f"${future_flat.mean():.2f}")

        fig3, ax3 = plt.subplots(figsize=(12, 4))
        ax3.plot(range(1, future_days + 1), future_flat, color='green', linewidth=2, marker='o', markersize=4, label='Predicted Price')
        ax3.set_title(stock_symbol + ' - Next ' + str(future_days) + ' Days Forecast', fontsize=14, fontweight='bold')
        ax3.set_xlabel('Days from Today')
        ax3.set_ylabel('Predicted Price (USD)')
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        plt.tight_layout()
        st.pyplot(fig3)