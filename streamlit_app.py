import streamlit as st

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="ScamShield XAI",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------

st.title("🛡️ ScamShield AI")
st.subheader("Explainable Scam Detection System")

st.write(
    "Analyze a transaction and understand exactly why it may be risky."
)

st.divider()

# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.header("📌 About ScamShield")

st.sidebar.write(
    "ScamShield analyzes transaction behaviour and identifies "
    "suspicious indicators."
)

st.sidebar.info(
    "The Explainable AI layer shows which factors contributed "
    "to the risk score."
)

# -----------------------------
# TRANSACTION INPUT
# -----------------------------

st.header("💳 Transaction Details")

col1, col2 = st.columns(2)

with col1:

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
        "New Beneficiary?",
        ["No", "Yes"]
    )

with col2:

    transaction_hour = st.slider(
        "Transaction Time",
        0,
        23,
        14
    )

    suspicious_link = st.selectbox(
        "Suspicious Link Associated?",
        ["No", "Yes"]
    )

    failed_attempts = st.number_input(
        "Previous Failed Attempts",
        min_value=0,
        max_value=10,
        value=0
    )

st.divider()

# -----------------------------
# DEMO TRANSACTIONS
# -----------------------------

st.header("🎯 Quick Demo")

demo = st.selectbox(
    "Choose a sample transaction",
    [
        "Custom Transaction",
        "🔴 Example: Suspicious Transaction",
        "🟢 Example: Normal Transaction"
    ]
)

if demo == "🔴 Example: Suspicious Transaction":

    amount = 25000
    usual_amount = 3000
    new_beneficiary = "Yes"
    transaction_hour = 2
    suspicious_link = "Yes"
    failed_attempts = 2

elif demo == "🟢 Example: Normal Transaction":

    amount = 1500
    usual_amount = 3000
    new_beneficiary = "No"
    transaction_hour = 14
    suspicious_link = "No"
    failed_attempts = 0

# -----------------------------
# ANALYSIS
# -----------------------------

if st.button("🔍 Analyze Transaction", use_container_width=True):

    risk_score = 0
    factors = []

    # -------------------------
    # AMOUNT ANALYSIS
    # -------------------------

    if usual_amount > 0:

        ratio = amount / usual_amount

        if ratio >= 5:

            risk_score += 30

            factors.append({
                "name": "Unusual Transaction Amount",
                "score": 30,
                "level": "HIGH",
                "explanation":
                    f"The transaction amount ₹{amount:,.0f} "
                    f"is about {ratio:.1f}× the user's usual "
                    f"amount of ₹{usual_amount:,.0f}."
            })

        elif ratio >= 2:

            risk_score += 15

            factors.append({
                "name": "Higher Than Usual Amount",
                "score": 15,
                "level": "MEDIUM",
                "explanation":
                    f"The transaction amount ₹{amount:,.0f} "
                    f"is significantly higher than the usual "
                    f"amount of ₹{usual_amount:,.0f}."
            })

    # -------------------------
    # BENEFICIARY ANALYSIS
    # -------------------------

    if new_beneficiary == "Yes":

        risk_score += 25

        factors.append({
            "name": "New Beneficiary",
            "score": 25,
            "level": "HIGH",
            "explanation":
                "The receiver is newly added. New beneficiaries "
                "can increase the risk of unauthorized transfers."
        })

    # -------------------------
    # LINK ANALYSIS
    # -------------------------

    if suspicious_link == "Yes":

        risk_score += 30

        factors.append({
            "name": "Suspicious Link",
            "score": 30,
            "level": "HIGH",
            "explanation":
                "A suspicious link is associated with the "
                "transaction and may indicate phishing or fraud."
        })

    # -------------------------
    # TIME ANALYSIS
    # -------------------------

    if transaction_hour < 6 or transaction_hour >= 23:

        risk_score += 10

        factors.append({
            "name": "Unusual Transaction Time",
            "score": 10,
            "level": "MEDIUM",
            "explanation":
                f"The transaction occurred around "
                f"{transaction_hour:02d}:00, which is outside "
                "the user's typical activity period."
        })

    # -------------------------
    # FAILED ATTEMPTS
    # -------------------------

    if failed_attempts >= 3:

        risk_score += 15

        factors.append({
            "name": "Multiple Failed Attempts",
            "score": 15,
            "level": "HIGH",
            "explanation":
                f"{failed_attempts} previous failed attempts "
                "were detected before this transaction."
        })

    elif failed_attempts > 0:

        risk_score += 5

        factors.append({
            "name": "Previous Failed Attempt",
            "score": 5,
            "level": "MEDIUM",
            "explanation":
                f"{failed_attempts} previous failed attempt(s) "
                "were detected."
        })

    risk_score = min(risk_score, 100)

    st.divider()

    # -----------------------------
    # RISK RESULT
    # -----------------------------

    st.header("🚨 Risk Assessment")

    if risk_score >= 61:

        st.error(
            f"🚨 HIGH RISK — {risk_score}/100"
        )

        risk_level = "HIGH RISK"

    elif risk_score >= 31:

        st.warning(
            f"⚠️ SUSPICIOUS — {risk_score}/100"
        )

        risk_level = "SUSPICIOUS"

    else:

        st.success(
            f"✅ LOW RISK — {risk_score}/100"
        )

        risk_level = "LOW RISK"

    # -----------------------------
    # RISK SCORE
    # -----------------------------

    st.progress(risk_score / 100)

    # -----------------------------
    # EXPLAINABLE AI
    # -----------------------------

    st.header("🤖 Explainable AI")

    if factors:

        st.write(
            "The following factors contributed to the risk score:"
        )

        for factor in factors:

            with st.expander(
                f"{factor['name']}  →  +{factor['score']} points"
            ):

                st.write(
                    f"**Risk Level:** {factor['level']}"
                )

                st.write(
                    f"**Why it matters:** {factor['explanation']}"
                )

    else:

        st.success(
            "No major suspicious indicators were detected."
        )

    # -----------------------------
    # MAIN EXPLANATION
    # -----------------------------

    st.header("🔎 Why was this transaction flagged?")

    if risk_score >= 61:

        st.write(
            f"This transaction is classified as **{risk_level}** "
            f"with a risk score of **{risk_score}/100**. "
            "Multiple unusual indicators were detected together. "
            "The combination of these factors increases the "
            "possibility of fraudulent activity."
        )

    elif risk_score >= 31:

        st.write(
            f"This transaction is classified as **{risk_level}** "
            f"with a risk score of **{risk_score}/100**. "
            "Some unusual behaviour was detected, so the "
            "transaction should be verified before proceeding."
        )

    else:

        st.write(
            f"This transaction has a **{risk_level}** score of "
            f"**{risk_score}/100**. No major suspicious indicators "
            "were detected from the information provided."
        )

    # -----------------------------
    # RECOMMENDED ACTION
    # -----------------------------

    st.header("🛡️ Recommended Action")

    if risk_score >= 61:

        st.error(
            "Do not proceed until the beneficiary and transaction "
            "details are verified."
        )

    elif risk_score >= 31:

        st.warning(
            "Verify the beneficiary and transaction details "
            "before proceeding."
        )

    else:

        st.success(
            "No immediate warning indicators were detected. "
            "Continue to follow normal security practices."
        )

    # -----------------------------
    # XAI FLOW
    # -----------------------------

    st.divider()

    st.caption(
        "Transaction Data → Risk Indicators → Risk Score → "
        "Feature Contributions → Human-Readable Explanation"
    )

    st.caption(
        "Prototype for hackathon demonstration."
    )
