# sip_app.py
import math
import streamlit as st

st.set_page_config(page_title="SIP Calculator", page_icon="📈", layout="centered")

st.title("📈 SIP Calculator")

with st.form("sip_form"):
    col1, col2 = st.columns(2)
    with col1:
        monthly = st.number_input("Monthly Investment (₹)", min_value=0.0, step=100.0, value=5000.0, format="%.2f")
        years   = st.number_input("Years", min_value=0.1, step=0.5, value=10.0, format="%.1f")
    with col2:
        rate    = st.number_input("Annual Return Rate (%)", min_value=0.0, step=0.25, value=12.0, format="%.2f")
        extra_months = st.number_input("Extra Months (optional)", min_value=0, step=1, value=0)

    show_growth = st.checkbox("Show month-wise growth chart", value=True)
    submitted = st.form_submit_button("Calculate")

def compute_sip(monthly, annual_rate_pct, years, extra_months=0):
    """
    Future value of monthly SIP with monthly compounding:
      FV = P * [((1+r)^n - 1) / r] * (1+r)
      r = annual_rate/12, n = years*12 (+ extras)
    """
    if monthly <= 0 or years <= 0 or annual_rate_pct < 0:
        return None, None

    r = (annual_rate_pct / 100.0) / 12.0
    n = int(years * 12) + int(extra_months)

    # month-wise series for optional chart
    balances = []
    bal = 0.0
    for m in range(1, n + 1):
        bal = (bal * (1 + r)) + monthly  # deposit at month end
        balances.append((m, bal))

    if r == 0:
        fv = monthly * n
    else:
        fv = monthly * (((1 + r) ** n - 1) / r) * (1 + r)

    invested = monthly * n
    gain = fv - invested
    summary = {
        "months": n,
        "invested": round(invested, 2),
        "future_value": round(fv, 2),
        "gain": round(gain, 2),
        "monthly": monthly,
        "rate": annual_rate_pct,
        "years": years,
    }
    return summary, balances

if submitted:
    result, series = compute_sip(monthly, rate, years, extra_months)
    if result is None:
        st.error("Please ensure: Monthly > 0, Years > 0, Rate ≥ 0.")
    else:
        st.success("Calculated successfully!")
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Invested", f"₹{result['invested']:,.2f}")
        c2.metric("Future Value", f"₹{result['future_value']:,.2f}")
        c3.metric("Estimated Gain", f"₹{result['gain']:,.2f}")
        st.caption(f"Months: {result['months']}  •  Monthly: ₹{result['monthly']:,.2f}  •  Rate: {result['rate']}%")

        if show_growth and series:
            import pandas as pd
            import matplotlib.pyplot as plt

            df = pd.DataFrame(series, columns=["Month", "Balance"])
            st.dataframe(df.tail(12), use_container_width=True)

            fig, ax = plt.subplots()
            ax.plot(df["Month"], df["Balance"])
            ax.set_xlabel("Month")
            ax.set_ylabel("Balance (₹)")
            ax.set_title("SIP Growth Over Time")
            st.pyplot(fig)

st.markdown("---")
st.caption("Formula uses monthly compounding. FV = P × [((1+r)^n − 1)/r] × (1+r), where r = (annual%/100)/12 and n = months.")
