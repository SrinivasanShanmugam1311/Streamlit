import streamlit as st

st.set_page_config(page_title="Simple Interest", page_icon="🧮", layout="centered")
st.title("🧮 Simple Interest Calculator")

with st.form("si_form"):
    col1, col2 = st.columns(2)
    with col1:
        principal = st.number_input("Principal (₹)", min_value=0.0, step=100.0, value=10000.0, format="%.2f")
        years     = st.number_input("Time (Years)", min_value=0.1, step=0.5, value=2.0, format="%.1f")
    with col2:
        rate      = st.number_input("Annual Rate (%)", min_value=0.0, step=0.25, value=8.0, format="%.2f")

    submitted = st.form_submit_button("Calculate")

def compute_si(p, r_pct, t):
    if p <= 0 or r_pct < 0 or t <= 0:
        return None
    si = p * r_pct * t / 100.0
    amt = p + si
    return {
        "principal": round(p, 2),
        "rate": r_pct,
        "years": t,
        "simple_interest": round(si, 2),
        "amount": round(amt, 2),
    }

if submitted:
    res = compute_si(principal, rate, years)
    if res is None:
        st.error("Please ensure: Principal > 0, Years > 0, Rate ≥ 0.")
    else:
        st.success("Calculated successfully!")
        c1, c2 = st.columns(2)
        c1.metric("Simple Interest", f"₹{res['simple_interest']:,.2f}")
        c2.metric("Total Amount (P + SI)", f"₹{res['amount']:,.2f}")
        st.caption(f"P=₹{res['principal']:,.2f}, R={res['rate']}%, T={res['years']} years")
st.markdown("---")
st.caption("Formula: SI = P × R × T / 100; Amount = P + SI.")
