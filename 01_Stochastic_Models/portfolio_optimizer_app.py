import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from pypfopt import EfficientFrontier, risk_models, expected_returns

# --- Styling & Constants ---
FIRE_PALETTE = ["#4A0404", "#8B0000", "#B22222", "#E37222", "#E3AFBC", "#FDE2E4"]
DEFAULT_ASSETS = ["AAPL", "MSFT", "AMZN", "NVDA", "GOOGL"]
WSE_ASSETS = ["PKO.WA", "PKN.WA", "PZU.WA", "KGH.WA", "DNP.WA", "ALE.WA", "LPP.WA", "CDR.WA", "PEO.WA", "SPL.WA"]

# --- Helper Functions ---
def calculate_historical_var(data: pd.DataFrame, weights: pd.Series, alpha: float = 0.05) -> float:
    """Calculates historical Value at Risk for a given portfolio."""
    portfolio_returns = (data.pct_change().dropna() * pd.Series(weights)).sum(axis=1)
    return portfolio_returns.quantile(alpha)

@st.cache_data(ttl=86400) # Cache clears every 24h
def get_sp500_tickers() -> list:
    """Scrapes current S&P 500 tickers from Wikipedia."""
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    try:
        return pd.read_html(url)[0]['Symbol'].tolist()
    except Exception:
        return DEFAULT_ASSETS

# --- Page Configuration ---
st.set_page_config(page_title="Pro Quant Terminal", layout="wide", page_icon="🏦")

# Combine datasets for the multiselect widget
sp500_tickers = get_sp500_tickers()
ALL_OPTIONS = sorted(list(set(WSE_ASSETS + sp500_tickers + ["SPY", "QQQ", "GLD"])))

# --- Sidebar Controls ---
st.sidebar.header("Control Panel")
strategy = st.sidebar.radio(
    "Select Optimization Strategy:", 
    ["Max Sharpe Ratio", "Minimum Volatility", "Target Return (15%)"]
)
start_date = st.sidebar.date_input("Historical Data Start Date", value=pd.to_datetime("2021-01-01"))
rf_rate = st.sidebar.slider("Risk-Free Rate (%)", 0.0, 10.0, 2.0, step=0.1) / 100

# --- Main Interface ---
st.title("Quant Asset Management Terminal")
st.markdown("Optimize your portfolio using Modern Portfolio Theory (Markowitz Framework).")

selected_assets = st.multiselect(
    "Select assets for your portfolio (you can type custom tickers, e.g., TSLA):",
    options=ALL_OPTIONS,
    default=["PKO.WA", "AAPL", "MSFT", "CDR.WA"]
)

calculate_btn = st.button("COMPUTE OPTIMAL PORTFOLIO", use_container_width=True)

# --- Core Logic ---
if calculate_btn and selected_assets:
    with st.spinner('Fetching market data and running optimization...'):
        try:
            # Data Fetching
            data = yf.download(selected_assets, start=start_date)['Close']
            
            # Markowitz Parameters
            mu = expected_returns.mean_historical_return(data)
            S = risk_models.sample_cov(data)
            ef = EfficientFrontier(mu, S)
            
            # Strategy Execution
            if strategy == "Max Sharpe Ratio":
                ef.max_sharpe(risk_free_rate=rf_rate)
            elif strategy == "Minimum Volatility":
                ef.min_volatility()
            elif strategy == "Target Return (15%)":
                ef.efficient_return(target_return=0.15)
            
            # Extract Results
            clean_weights = ef.clean_weights()
            perf = ef.portfolio_performance(verbose=False, risk_free_rate=rf_rate)
            var_value = calculate_historical_var(data, clean_weights)

            # --- Results Rendering ---
            c1, c2 = st.columns([1, 2])
            
            with c1:
                st.subheader("Strategy Statistics")
                st.metric("Expected Annual Return", f"{perf[0]:.2%}")
                st.metric("Annual Volatility (Risk)", f"{perf[1]:.2%}")
                st.metric("Sharpe Ratio", f"{perf[2]:.2f}")
                st.metric("Daily Historical VaR (95%)", f"{var_value:.2%}")
                
                # Weights DataFrame rendering
                st.markdown("**Optimal Asset Allocation:**")
                df_weights = pd.DataFrame.from_dict(clean_weights, orient='index', columns=['Weight']).query("Weight > 0")
                df_weights = df_weights.sort_values(by='Weight', ascending=False)
                st.dataframe(df_weights.style.format("{:.2%}"), use_container_width=True)

            with c2:
                st.subheader("Portfolio Structure")
                fig_pie = px.pie(
                    df_weights, names=df_weights.index, values='Weight', 
                    hole=0.4, 
                    template="plotly_dark",
                    color_discrete_sequence=FIRE_PALETTE
                )
                fig_pie.update_layout(margin=dict(l=20, r=20, t=20, b=20))
                st.plotly_chart(fig_pie, use_container_width=True)

            # --- Backtesting Chart ---
            st.divider()
            st.subheader("📉 Historical Equity Curve (Backtest)")
            
            port_returns = (data.pct_change().dropna() * pd.Series(clean_weights)).sum(axis=1)
            cumulative_returns = (1 + port_returns).cumprod()

            fig_bt = px.line(cumulative_returns, labels={'value': 'Capital Multiplier', 'index': 'Timeline'})
            fig_bt.update_traces(
                line_color='#B22222', 
                hovertemplate="Multiplier: %{y:.2f}<extra></extra>"
            )
            fig_bt.update_xaxes(
                dtick="M12", 
                tickformat="%Y", 
                rangeslider_visible=True,
                gridcolor="rgba(255, 255, 255, 0.1)"
            )
            fig_bt.update_layout(
                template="plotly_dark", 
                hovermode="x unified",
                xaxis_title="",
                yaxis_title="Portfolio Value"
            )
            st.plotly_chart(fig_bt, use_container_width=True, config={'displayModeBar': False})

        except Exception as e:
            st.error(f"Optimization Error: Please ensure you selected enough valid assets. Details: {e}")
else:
    if not selected_assets:
        st.info("Please select at least one asset to proceed.")