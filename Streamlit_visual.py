import streamlit as st
import pandas as pd
from black_scholes import BlackScholes

st.set_page_config(
    page_title = "A Darkend Visual",
    layout = "wide"
)

st.title("Black-Scholes Option Pricing Engine")

st.markdown(
    """
    My name is Peter Wagwan
    """
)

st.markdown("---")

with st.sidebar:
    st.header("Parameters of Model")

    spot = st.number_input(
        "Spot Price",
        min_value = 0.01,
        max_value = 100.0,
        step = 0.5
    )

    strike = st.number_input(
        "Strike Price",
        min_value = 0.01,
        max_value = 100.0,
        step = 0.5
    )

    maturity = st.number_input(
        "Time to Maturity (Years)",
        min_value = 0.01,
        max_value = 1.0,
        step = 0.25
    )

    volatility = st.slider(
        "Volatility",
        min_value = 0.01,
        max_value = 1.0,
        value =0.2
    )

    rate = st.slider(
        "Risk-free Interest Rate",
        min_value = 0.0,
        max_value = 0.2,
        value =0.05,

    )

    model = BlackScholes(
        spot       = spot,
        strike     = strike,
        rate       = rate,
        maturity   = maturity,
        volatility = volatility
    )

call_price = model.call_price()
put_price  = model.put_price()

st.subheader("Option Valuation")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        label = "Call Option Value",
        value = f"{call_price:.2f}"
    )

with col2:
    st.metric(
        label = "Put Option Value",
        value = f"{put_price:.2f}"
    )

st.markdown("---")

st.subheader("Model Inputs")

parameters = pd.DataFrame({
    "Parameters" : [
    " Spot Price ",
    " Strike Price ",
    " Time to Maturity ",
    " Volatility ",
    "Risk - Free Rate "
    ],
    "Value": [
        spot,
        strike,
        maturity,
        volatility,
        rate
    ]
})

st.dataframe(parameters, hide_index = True)