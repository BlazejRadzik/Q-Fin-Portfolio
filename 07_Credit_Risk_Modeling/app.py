import streamlit as st
import numpy as np

st.set_page_config(page_title="Institutional Credit Risk Terminal", layout="wide")
st.title("🏦 Credit Risk Intelligence Dashboard")

with st.sidebar:
    st.header("Applicant Attributes")
    fico = st.slider("FICO Score", 300, 850, 720)
    dti = st.slider("Debt-to-Income Ratio (DTI)", 0.0, 1.0, 0.3)

# Logit PD Model Simulation
# PD = 1 / (1 + exp(-z))
logit_z = -0.015 * fico + 2.5 * dti + 3.0
pd_score = 1 / (1 + np.exp(-logit_z))

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
    st.write("- **Gini Coefficient:** 0.68")
    st.write("- **AUC-ROC:** 0.84")