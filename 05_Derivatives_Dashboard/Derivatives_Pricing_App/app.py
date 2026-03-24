import streamlit as st
import plotly.graph_objects as go
import numpy as np
from scipy.stats import norm

def black_scholes_european(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

def monte_carlo_pricing(S, K, T, r, sigma, iterations=10000):
    dt = T
    Z = np.random.standard_normal(iterations)
    ST = S * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z)
    payoffs = np.maximum(ST - K, 0)
    return np.exp(-r * T) * np.mean(payoffs)

st.set_page_config(page_title="Option Pricing Calculator", layout="wide")
# AI generated 
st.markdown("""
    <style>
    .block-container { padding-top: 5rem !important; }
    .main { background-color: #0e1117; color: #e0e6ed; }
    div[data-testid="stVerticalBlock"] > div:has(div.stMetric) {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 20px;
    }
    [data-testid="stSidebar"] { display: none; }
    [data-testid="stMetricValue"] { font-family: 'Inter', sans-serif; font-weight: 700; color: #6366f1 !important; }
    [data-testid="stMetricLabel"] { text-transform: uppercase; letter-spacing: 1px; font-size: 0.8rem; color: #94a3b8; }
    .main-header {
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 2rem;
        color: #e0e6ed; 
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="main-header">Options Pricing Dashboard: Black-Scholes vs Monte Carlo</h1>', unsafe_allow_html=True)
st.markdown("---")

st.markdown("### Input Parameters")
row1_1, row1_2, row1_3, row1_4 = st.columns(4)

with row1_1:
    S = st.number_input("Asset Price (S)", value=100.0)
    K = st.number_input("Strike Price (K)", value=105.0)

with row1_2:
    T = st.slider("Time to Maturity (Years)", 0.1, 5.0, 1.0)
    r = st.slider("Risk-Free Rate", 0.0, 0.2, 0.05)

with row1_3:
    sigma = st.slider("Market Volatility", 0.01, 1.0, 0.2)
    iters = st.select_slider("Monte Carlo Iterations", options=[1000, 10000, 50000, 100000], value=10000)

with row1_4:
    st.write("")
    st.write("")
    if st.button("Recalculate", use_container_width=True):
        st.rerun()

st.markdown("---")

bs_price = black_scholes_european(S, K, T, r, sigma)
mc_price = monte_carlo_pricing(S, K, T, r, sigma, iters)
error = abs(bs_price - mc_price)

col_res1, col_res2 = st.columns([1, 2])

with col_res1:
    st.markdown("#### Valuation Results")
    st.metric("Black-Scholes Model", f"$ {bs_price:.2f}")
    st.metric("Monte Carlo Simulation", f"$ {mc_price:.2f}")
    st.metric("Absolute Difference", f"{error:.5f}")
    st.warning(f"Model Convergence: {100 - (error/bs_price*100):.2f}%")

with col_res2:
    st.markdown("#### Convergence Analysis")
    iters_list = [1000, 5000, 10000, 50000, 100000]
    prices = [monte_carlo_pricing(S, K, T, r, sigma, i) for i in iters_list]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=iters_list, y=[bs_price]*len(iters_list), 
                             mode='lines', name='Black-Scholes (Theory)', 
                             line=dict(color='#ef4444', width=2, dash='dot')))
    fig.add_trace(go.Scatter(x=iters_list, y=prices, 
                             mode='lines+markers', name='Monte Carlo (Simulation)', 
                             line=dict(color='#6366f1', width=4)))
    
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=0, r=0, t=10, b=0),
        height=400,
        xaxis=dict(showgrid=False, title="Number of Iterations"),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.05)', title="Option Price"),
        legend=dict(orientation="h", yanchor="bottom", y=-0.3, xanchor="center", x=0.5),
        template="plotly_dark"
    )
    st.plotly_chart(fig, use_container_width=True)
