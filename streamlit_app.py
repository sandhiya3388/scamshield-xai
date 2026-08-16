import streamlit as st

st.set_page_config(
    page_title="ScamShield XAI",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ ScamShield")
st.subheader("Explainable AI Scam Detector")

st.write(
    "Enter the transaction details below. "
    "The system will detect suspicious indicators and explain why "
    "the transaction is risky."
)

st.divider()

# -------------------------
# TRANSACTION DETAILS
# -------------------------

st.header("💳 Transaction Details")

amount = st.number_input(
    "Transaction Amount (₹)",
    min_value=0,
    value=25000
)

usual_amount = st.number_input(
    "User's Usual Transaction Amount (₹)",
    min_value=0,
    value=3000
)

new_beneficiary = st.selectbox(
    "Is this a new beneficiary?",
    ["No", "Yes"]
)

transaction_hour = st.slider(
    "Transaction Time (24-hour format)",
    0,
    23,
    14
)

suspicious_link = st.selectbox(
    "Is a suspicious link associated with this transaction?",
    ["No", "Yes"]
)

failed_attempts = st.number_input(
    "Previous Failed Attempts",
    min_value=0,
    max_value=10,
    value=0
)

# -------------------------
# ANALYZE BUTTON
# -------------------------

if st.button("🔍 Analyze Transaction", use_container_width=True):

    risk_score = 0
    reasons = []

    # Amount analysis
    if usual_amount > 0 and amount >= usual_amount * 5:
        risk_score += 30
        reasons.append(
            f"🔴 **Unusual transaction amount:** ₹{amount:,.0f} "
            f"is much higher than the user's usual amount "
            f"of ₹{usual_amount:,.0f}."
        )

    elif usual_amount > 0 and amount >= usual_amount * 2:
        risk_score += 15
        reasons.append(
            f"🟠 **Higher than usual amount:** ₹{amount:,.0f} "
            f"is significantly higher than the usual "
            f"₹{usual_amount:,.0f}."
        )

    # New beneficiary
    if new_beneficiary == "Yes":
        risk_score += 25
        reasons.append(
            "🔴 **New beneficiary:** The receiver was recently "
            "added to the user's account."
        )

    # Suspicious link
    if suspicious_link == "Yes":
        risk_score += 30
        reasons.append(
            "🔴 **Suspicious link detected:** A potentially "
            "dangerous or suspicious link is associated with "
            "the transaction."
        )

    # Unusual time
    if transaction_hour < 6 or transaction_hour >= 23:
        risk_score += 10
        reasons.append(
            f"🟠 **Unusual transaction time:** The transaction "
            f"occurred at approximately {transaction_hour:02d}:00."
        )

    # Failed attempts
    if failed_attempts >= 3:
        risk_score += 15
        reasons.append(
            f"🔴 **Multiple failed attempts:** "
            f"{failed_attempts} previous failed attempts were detected."
        )

    elif failed_attempts > 0:
        risk_score += 5
        reasons.append(
            f"🟠 **Previous failed attempt:** "
            f"{failed_attempts} failed attempt(s) were detected."
        )

    # Maximum score = 100
    risk_score = min(risk_score, 100)

    st.divider()

    # -------------------------
    # RISK RESULT
    # -------------------------

    st.header("🚨 Risk Assessment")

    if risk_score >= 61:

        st.error(
            f"HIGH RISK — {risk_score}%"
        )

        risk_level = "HIGH RISK"

    elif risk_score >= 31:

        st.warning(
            f"SUSPICIOUS — {risk_score}%"
        )

        risk_level = "SUSPICIOUS"

    else:

        st.success(
            f"SAFE — {risk_score}%"
        )

        risk_level = "SAFE"

    # -------------------------
    # EXPLANATION
    # -------------------------

    st.header("🔎 Why was this transaction flagged?")

    if reasons:

        for reason in reasons:
            st.markdown(reason)

    else:

        st.success(
            "No major suspicious indicators were detected."
        )

    # -------------------------
    # XAI SUMMARY
    # -------------------------

    st.header("🤖 Explainable AI Summary")

    if risk_score >= 61:

        st.write(
            f"The transaction is classified as **{risk_level}** "
            f"with a risk score of **{risk_score}%**. "
            "The classification is mainly influenced by multiple "
            "unusual indicators occurring together. "
            "These include transaction amount, beneficiary status, "
            "suspicious links, transaction timing, and previous "
            "failed attempts."
        )

    elif risk_score >= 31:

        st.write(
            f"The transaction is classified as **{risk_level}** "
            f"with a risk score of **{risk_score}%**. "
            "One or more unusual indicators were detected. "
            "The transaction should be verified before proceeding."
        )

    else:

        st.write(
            f"The transaction is classified as **{risk_level}** "
            f"with a risk score of **{risk_score}%**. "
            "No major risk indicators were detected from the "
            "information provided."
        )

    st.info(
        "⚠️ This is a prototype for demonstration purposes. "
        "A real banking system would require validated fraud "
        "detection models and additional security checks."
    )
