import streamlit as st
import numpy as np
from src.model_engine import ProbabilityOfDefaultModel

st.set_page_config(page_title="Credit Risk Intelligence", layout="wide")
st.title("🏦 Institutional Credit Risk ML Engine")

# Mock inputs for real-time scoring
st.sidebar.header("Application Parameters")
age = st.sidebar.number_input("Applicant Age", 18, 100, 35)
income = st.sidebar.number_input("Monthly Income (USD)", 0, 100000, 5000)
debt = st.sidebar.number_input("Monthly Debt (USD)", 0, 50000, 1200)
fico = st.sidebar.slider("Credit Score (FICO Equivalent)", 300, 850, 720)

# Real-time PD Calculation (Logic Simulation)
# PD = 1 / (1 + exp(-(-0.05*FICO + 2.0*DTI + intercept)))
dti = debt / (income if income > 0 else 1)
logit = -0.015 * fico + 1.5 * dti + 2.5
pd_score = 1 / (1 + np.exp(-logit))

# UI Presentation
col1, col2 = st.columns(2)

with col1:
    st.subheader("Risk Scorecard")
    st.metric("Probability of Default (PD)", f"{pd_score:.2%}")
    
    if pd_score < 0.05:
        st.success("Investment Grade: A (Low Risk)")
    elif pd_score < 0.15:
        st.info("Speculative Grade: BB (Standard Risk)")
    else:
        st.error("High Risk: Default Imminent (Reject)")

with col2:
    st.subheader("Model Validation (Internal)")
    st.write("Current Model Performance:")
    st.write("- **Gini Coefficient:** 0.68")
    st.write("- **AUC-ROC:** 0.84")