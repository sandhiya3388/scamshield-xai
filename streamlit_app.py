import streamlit as st

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# HEADER
# =========================================================

st.title("🛡️ ScamShield AI")
st.subheader("Explainable Scam Detection System")

st.write(
    "Analyze a transaction, identify suspicious indicators, "
    "and understand why the transaction was classified as risky."
)

st.divider()

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🛡️ ScamShield")

st.sidebar.write(
    "An Explainable AI prototype for detecting suspicious "
    "financial transactions."
)

st.sidebar.info(
    "The system does not only provide a risk score. "
    "It explains the factors that contributed to the decision."
)

st.sidebar.markdown("### Risk Levels")
st.sidebar.write("🟢 0–30 : Low Risk")
st.sidebar.write("🟠 31–60 : Suspicious")
st.sidebar.write("🔴 61–100 : High Risk")

# =========================================================
# TRANSACTION INPUT
# =========================================================

st.header("💳 Transaction Details")

# Quick demo first
st.subheader("🎯 Quick Demo")

demo = st.selectbox(
    "Choose a sample transaction",
    [
        "Custom Transaction",
        "🔴 Suspicious Transaction",
        "🟢 Normal Transaction",
        "🟠 Moderately Suspicious Transaction"
    ]
)

# Default values
default_amount = 25000
default_usual = 3000
default_beneficiary = "Yes"
default_time = 2
default_link = "Yes"
default_failed = 2

if demo == "🟢 Normal Transaction":
    default_amount = 1500
    default_usual = 3000
    default_beneficiary = "No"
    default_time = 14
    default_link = "No"
    default_failed = 0

elif demo == "🟠 Moderately Suspicious Transaction":
    default_amount = 7000
    default_usual = 3000
    default_beneficiary = "Yes"
    default_time = 14
    default_link = "No"
    default_failed = 1

# =========================================================
# INPUT COLUMNS
# =========================================================

col1, col2 = st.columns(2)

with col1:

    amount = st.number_input(
        "💰 Transaction Amount (₹)",
        min_value=0,
        value=default_amount,
        step=500
    )

    usual_amount = st.number_input(
        "📊 User's Usual Transaction Amount (₹)",
        min_value=0,
        value=default_usual,
        step=500
    )

    new_beneficiary = st.selectbox(
        "👤 New Beneficiary?",
        ["No", "Yes"],
        index=1 if default_beneficiary == "Yes" else 0
    )

with col2:

    transaction_hour = st.slider(
        "🕐 Transaction Time",
        0,
        23,
        default_time
    )

    suspicious_link = st.selectbox(
        "🔗 Suspicious Link Associated?",
        ["No", "Yes"],
        index=1 if default_link == "Yes" else 0
    )

    failed_attempts = st.number_input(
        "⚠️ Previous Failed Attempts",
        min_value=0,
        max_value=10,
        value=default_failed
    )

st.divider()

# =========================================================
# ANALYZE BUTTON
# =========================================================

if st.button(
    "🔍 ANALYZE TRANSACTION",
    use_container_width=True
):

    risk_score = 0
    factors = []

    # =====================================================
    # 1. TRANSACTION AMOUNT
    # =====================================================

    if usual_amount > 0:

        ratio = amount / usual_amount

        if ratio >= 5:

            risk_score += 30

            factors.append({
                "name": "Unusual Transaction Amount",
                "score": 30,
                "level": "HIGH",
                "explanation":
                    f"The transaction amount of ₹{amount:,.0f} "
                    f"is approximately {ratio:.1f} times higher "
                    f"than the user's usual amount of "
                    f"₹{usual_amount:,.0f}."
            })

        elif ratio >= 2:

            risk_score += 15

            factors.append({
                "name": "Higher Than Usual Amount",
                "score": 15,
                "level": "MEDIUM",
                "explanation":
                    f"The transaction amount of ₹{amount:,.0f} "
                    f"is significantly higher than the user's "
                    f"usual amount of ₹{usual_amount:,.0f}."
            })

    # =====================================================
    # 2. NEW BENEFICIARY
    # =====================================================

    if new_beneficiary == "Yes":

        risk_score += 25

        factors.append({
            "name": "New Beneficiary",
            "score": 25,
            "level": "HIGH",
            "explanation":
                "The receiver is newly added. "
                "A newly added beneficiary can increase "
                "the risk of unauthorized transactions."
        })

    # =====================================================
    # 3. SUSPICIOUS LINK
    # =====================================================

    if suspicious_link == "Yes":

        risk_score += 30

        factors.append({
            "name": "Suspicious Link",
            "score": 30,
            "level": "HIGH",
            "explanation":
                "A potentially suspicious link is associated "
                "with the transaction. This may indicate "
                "phishing or fraudulent activity."
        })

    # =====================================================
    # 4. UNUSUAL TIME
    # =====================================================

    if transaction_hour < 6 or transaction_hour >= 23:

        risk_score += 10

        factors.append({
            "name": "Unusual Transaction Time",
            "score": 10,
            "level": "MEDIUM",
            "explanation":
                f"The transaction occurred around "
                f"{transaction_hour:02d}:00, which is an "
                "unusual time for financial activity."
        })

    # =====================================================
    # 5. FAILED ATTEMPTS
    # =====================================================

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

    # Maximum risk score
    risk_score = min(risk_score, 100)

    st.divider()

    # =====================================================
    # RISK ASSESSMENT
    # =====================================================

    st.header("🚨 Risk Assessment")

    if risk_score >= 61:

        risk_level = "HIGH RISK"

        st.error(
            f"🚨 HIGH RISK — {risk_score}/100"
        )

    elif risk_score >= 31:

        risk_level = "SUSPICIOUS"

        st.warning(
            f"⚠️ SUSPICIOUS — {risk_score}/100"
        )

    else:

        risk_level = "LOW RISK"

        st.success(
            f"✅ LOW RISK — {risk_score}/100"
        )

    # =====================================================
    # RISK PROGRESS BAR
    # =====================================================

    st.progress(
        risk_score / 100
    )

    # =====================================================
    # SUMMARY CARDS
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Risk Score",
            f"{risk_score}/100"
        )

    with col2:

        st.metric(
            "Risk Factors",
            len(factors)
        )

    with col3:

        st.metric(
            "Status",
            risk_level
        )

    st.divider()

    # =====================================================
    # EXPLAINABLE AI
    # =====================================================

    st.header("🤖 Explainable AI")

    st.write(
        "The system breaks down the risk score into individual "
        "factors so the user can understand why the transaction "
        "was flagged."
    )

    if factors:

        for factor in factors:

            with st.expander(
                f"🔎 {factor['name']}  |  +{factor['score']} points"
            ):

                st.write(
                    f"**Risk Level:** {factor['level']}"
                )

                st.write(
                    f"**Contribution:** +{factor['score']} points"
                )

                st.write(
                    f"**Why it matters:** "
                    f"{factor['explanation']}"
                )

    else:

        st.success(
            "No suspicious indicators were detected."
        )

    # =====================================================
    # RISK CONTRIBUTION CHART
    # =====================================================

    if factors:

        st.header("📊 Risk Contribution")

        chart_data = {
            factor["name"]: factor["score"]
            for factor in factors
        }

        st.bar_chart(chart_data)

        st.caption(
            "Higher values indicate a stronger contribution "
            "to the overall risk score."
        )

    # =====================================================
    # MAIN AI EXPLANATION
    # =====================================================

    st.header("🔎 Why Was This Transaction Flagged?")

    if risk_score >= 61:

        st.write(
            f"This transaction is classified as **HIGH RISK** "
            f"with a score of **{risk_score}/100**. "
            "Multiple suspicious indicators were detected "
            "together. The combination of unusual transaction "
            "behaviour, beneficiary information, links, timing, "
            "and failed attempts increased the overall risk."
        )

    elif risk_score >= 31:

        st.write(
            f"This transaction is classified as **SUSPICIOUS** "
            f"with a score of **{risk_score}/100**. "
            "Some unusual behaviour was detected. "
            "The transaction should be verified before proceeding."
        )

    else:

        st.write(
            f"This transaction has a **LOW RISK** score of "
            f"**{risk_score}/100**. "
            "No major suspicious indicators were detected "
            "from the provided information."
        )

    # =====================================================
    # RECOMMENDED ACTION
    # =====================================================

    st.header("🛡️ Recommended Action")

    if risk_score >= 61:

        st.error(
            "🛑 HOLD TRANSACTION\n\n"
            "Verify the beneficiary and transaction details "
            "before proceeding."
        )

    elif risk_score >= 31:

        st.warning(
            "⚠️ VERIFY TRANSACTION\n\n"
            "Confirm the recipient and transaction details "
            "before proceeding."
        )

    else:

        st.success(
            "✅ TRANSACTION CAN PROCEED\n\n"
            "No major warning indicators were detected."
        )

    # =====================================================
    # XAI PIPELINE
    # =====================================================

    st.divider()

    st.subheader("🧠 Explainable AI Pipeline")

    st.write(
        "Transaction Data"
        "  →  Risk Indicators"
        "  →  Risk Score"
        "  →  Feature Contributions"
        "  →  Human-Readable Explanation"
    )

    st.caption(
        "ScamShield XAI is a hackathon prototype. "
        "A production banking system would require validated "
        "machine-learning models, secure banking integrations, "
        "and additional fraud-prevention controls."
    )
