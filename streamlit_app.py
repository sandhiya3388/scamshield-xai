import streamlit as st
import pandas as pd
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="ScamShield AI",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# LANGUAGE SETTINGS
# =========================================================

LANGUAGES = {
    "English 🇬🇧": "en",
    "தமிழ் 🇮🇳": "ta",
    "हिन्दी 🇮🇳": "hi",
    "తెలుగు 🇮🇳": "te",
    "മലയാളം 🇮🇳": "ml"
}

TEXT = {

    "en": {
        "title": "🛡️ ScamShield AI",
        "subtitle": "Explainable AI Scam Detector",
        "description": "Analyze a financial transaction and understand why it may be suspicious.",
        "language": "🌐 Language",
        "about": "About ScamShield",
        "about_text": "ScamShield analyzes transaction behaviour and identifies suspicious indicators.",
        "transaction": "💳 Transaction Details",
        "demo": "🎯 Quick Demo",
        "custom": "Custom Transaction",
        "suspicious": "🔴 Suspicious Transaction",
        "normal": "🟢 Normal Transaction",
        "moderate": "🟠 Moderately Suspicious Transaction",
        "amount": "💰 Transaction Amount (₹)",
        "usual": "📊 User's Usual Transaction Amount (₹)",
        "beneficiary": "👤 New Beneficiary?",
        "time": "🕐 Transaction Time",
        "link": "🔗 Suspicious Link Associated?",
        "failed": "⚠️ Previous Failed Attempts",
        "yes": "Yes",
        "no": "No",
        "analyze": "🔍 ANALYZE TRANSACTION",
        "risk": "🚨 Risk Assessment",
        "risk_score": "Risk Score",
        "risk_factors": "Risk Factors",
        "status": "Status",
        "high": "HIGH RISK",
        "medium": "SUSPICIOUS",
        "low": "LOW RISK",
        "xai": "🤖 Explainable AI",
        "xai_text": "The system explains which transaction features contributed to the risk score.",
        "contribution": "📊 Risk Contribution",
        "contribution_text": "Each bar shows how strongly a factor contributed to the overall risk.",
        "summary": "📋 Risk Factor Summary",
        "why": "🔎 Why Was This Transaction Flagged?",
        "action": "🛡️ Recommended Action",
        "hold": "HOLD TRANSACTION",
        "verify": "VERIFY TRANSACTION",
        "proceed": "TRANSACTION CAN PROCEED",
        "history": "🕘 Recent Analysis History",
        "download": "📥 Download Analysis Report",
        "pipeline": "🧠 Explainable AI Pipeline",
        "factor": "Factor",
        "score": "Score",
        "level": "Risk Level",
        "explanation": "Explanation",
        "no_factors": "No suspicious indicators were detected.",
        "high_reason": "Multiple suspicious indicators were detected together. Their combined contribution increased the overall risk.",
        "medium_reason": "Some unusual transaction behaviour was detected. Verification is recommended.",
        "low_reason": "No major suspicious indicators were detected in this transaction.",
        "unusual_amount": "Unusual Transaction Amount",
        "higher_amount": "Higher Than Usual Amount",
        "new_beneficiary": "New Beneficiary",
        "suspicious_link": "Suspicious Link",
        "unusual_time": "Unusual Transaction Time",
        "failed_attempt": "Previous Failed Attempt",
        "multiple_failed": "Multiple Failed Attempts"
    },

    "ta": {
        "title": "🛡️ ScamShield AI",
        "subtitle": "Explainable AI Scam Detector",
        "description": "Transaction-ஐ ஆய்வு செய்து அது ஏன் சந்தேகத்திற்குரியது என்பதை அறியலாம்.",
        "language": "🌐 மொழி",
        "about": "ScamShield பற்றி",
        "about_text": "ScamShield transaction behaviour-ஐ ஆய்வு செய்து சந்தேகத்திற்குரிய காரணிகளை கண்டறிகிறது.",
        "transaction": "💳 Transaction விவரங்கள்",
        "demo": "🎯 Quick Demo",
        "custom": "Custom Transaction",
        "suspicious": "🔴 சந்தேகத்திற்குரிய Transaction",
        "normal": "🟢 சாதாரண Transaction",
        "moderate": "🟠 மிதமான சந்தேக Transaction",
        "amount": "💰 Transaction Amount (₹)",
        "usual": "📊 வழக்கமான Transaction Amount (₹)",
        "beneficiary": "👤 புதிய Beneficiary?",
        "time": "🕐 Transaction நேரம்",
        "link": "🔗 சந்தேகத்திற்குரிய Link உள்ளதா?",
        "failed": "⚠️ முந்தைய Failed Attempts",
        "yes": "ஆம்",
        "no": "இல்லை",
        "analyze": "🔍 TRANSACTION-ஐ ANALYZE செய்",
        "risk": "🚨 Risk Assessment",
        "risk_score": "Risk Score",
        "risk_factors": "Risk Factors",
        "status": "நிலை",
        "high": "அதிக ஆபத்து",
        "medium": "சந்தேகத்திற்குரியது",
        "low": "குறைந்த ஆபத்து",
        "xai": "🤖 Explainable AI",
        "xai_text": "எந்த transaction காரணிகள் risk score-க்கு பங்களித்தன என்பதை system விளக்குகிறது.",
        "contribution": "📊 Risk Contribution",
        "contribution_text": "ஒவ்வொரு காரணியும் risk-க்கு எவ்வளவு பங்களித்தது என்பதை chart காட்டுகிறது.",
        "summary": "📋 Risk Factor Summary",
        "why": "🔎 இந்த Transaction ஏன் Flag செய்யப்பட்டது?",
        "action": "🛡️ பரிந்துரைக்கப்படும் நடவடிக்கை",
        "hold": "TRANSACTION-ஐ நிறுத்தவும்",
        "verify": "TRANSACTION-ஐ சரிபார்க்கவும்",
        "proceed": "TRANSACTION தொடரலாம்",
        "history": "🕘 சமீபத்திய Analysis History",
        "download": "📥 Analysis Report Download",
        "pipeline": "🧠 Explainable AI Pipeline",
        "factor": "காரணம்",
        "score": "Score",
        "level": "Risk Level",
        "explanation": "விளக்கம்",
        "no_factors": "சந்தேகத்திற்குரிய காரணிகள் எதுவும் கண்டறியப்படவில்லை.",
        "high_reason": "பல சந்தேகத்திற்குரிய காரணிகள் கண்டறியப்பட்டுள்ளன. அவற்றின் மொத்த பங்களிப்பு risk-ஐ அதிகரித்துள்ளது.",
        "medium_reason": "சில வழக்கத்திற்கு மாறான transaction behaviour கண்டறியப்பட்டுள்ளது. சரிபார்ப்பு பரிந்துரைக்கப்படுகிறது.",
        "low_reason": "இந்த transaction-ல் முக்கியமான சந்தேகத்திற்குரிய காரணிகள் எதுவும் இல்லை.",
        "unusual_amount": "வழக்கத்திற்கு மாறான Transaction Amount",
        "higher_amount": "வழக்கத்தை விட அதிக Amount",
        "new_beneficiary": "புதிய Beneficiary",
        "suspicious_link": "சந்தேகத்திற்குரிய Link",
        "unusual_time": "வழக்கத்திற்கு மாறான நேரம்",
        "failed_attempt": "முந்தைய Failed Attempt",
        "multiple_failed": "பல Failed Attempts"
    },

    "hi": {
        "title": "🛡️ ScamShield AI",
        "subtitle": "Explainable AI Scam Detector",
        "description": "Transaction का विश्लेषण करें और समझें कि वह suspicious क्यों है।",
        "language": "🌐 भाषा",
        "about": "ScamShield के बारे में",
        "about_text": "ScamShield transaction behaviour का विश्लेषण करके suspicious indicators पहचानता है।",
        "transaction": "💳 Transaction Details",
        "demo": "🎯 Quick Demo",
        "custom": "Custom Transaction",
        "suspicious": "🔴 Suspicious Transaction",
        "normal": "🟢 Normal Transaction",
        "moderate": "🟠 Moderately Suspicious Transaction",
        "amount": "💰 Transaction Amount (₹)",
        "usual": "📊 सामान्य Transaction Amount (₹)",
        "beneficiary": "👤 नया Beneficiary?",
        "time": "🕐 Transaction Time",
        "link": "🔗 Suspicious Link?",
        "failed": "⚠️ Previous Failed Attempts",
        "yes": "हाँ",
        "no": "नहीं",
        "analyze": "🔍 TRANSACTION ANALYZE करें",
        "risk": "🚨 Risk Assessment",
        "risk_score": "Risk Score",
        "risk_factors": "Risk Factors",
        "status": "स्थिति",
        "high": "HIGH RISK",
        "medium": "SUSPICIOUS",
        "low": "LOW RISK",
        "xai": "🤖 Explainable AI",
        "xai_text": "System बताता है कि किन transaction features ने risk score बढ़ाया।",
        "contribution": "📊 Risk Contribution",
        "contribution_text": "Chart दिखाता है कि प्रत्येक factor ने risk में कितना योगदान दिया।",
        "summary": "📋 Risk Factor Summary",
        "why": "🔎 Transaction Flag क्यों हुआ?",
        "action": "🛡️ Recommended Action",
        "hold": "TRANSACTION HOLD करें",
        "verify": "TRANSACTION VERIFY करें",
        "proceed": "TRANSACTION आगे बढ़ सकता है",
        "history": "🕘 Recent Analysis History",
        "download": "📥 Analysis Report Download करें",
        "pipeline": "🧠 Explainable AI Pipeline",
        "factor": "Factor",
        "score": "Score",
        "level": "Risk Level",
        "explanation": "Explanation",
        "no_factors": "कोई suspicious indicator नहीं मिला।",
        "high_reason": "कई suspicious indicators एक साथ मिले। इनके combined contribution ने risk बढ़ाया।",
        "medium_reason": "कुछ unusual transaction behaviour मिला। Verification recommended है।",
        "low_reason": "इस transaction में कोई major suspicious indicator नहीं मिला।",
        "unusual_amount": "Unusual Transaction Amount",
        "higher_amount": "Higher Than Usual Amount",
        "new_beneficiary": "New Beneficiary",
        "suspicious_link": "Suspicious Link",
        "unusual_time": "Unusual Transaction Time",
        "failed_attempt": "Previous Failed Attempt",
        "multiple_failed": "Multiple Failed Attempts"
    },

    "te": {
        "title": "🛡️ ScamShield AI",
        "subtitle": "Explainable AI Scam Detector",
        "description": "Transaction-ஐ analyze செய்து அது ஏன் suspicious என்பதை அறியுங்கள்.",
        "language": "🌐 భాష",
        "about": "ScamShield గురించి",
        "about_text": "ScamShield transaction behaviour-ஐ ஆய்வு செய்து suspicious indicators-ஐ கண்டறிகிறது.",
        "transaction": "💳 Transaction వివరాలు",
        "demo": "🎯 Quick Demo",
        "custom": "Custom Transaction",
        "suspicious": "🔴 Suspicious Transaction",
        "normal": "🟢 Normal Transaction",
        "moderate": "🟠 Moderately Suspicious Transaction",
        "amount": "💰 Transaction Amount (₹)",
        "usual": "📊 సాధారణ Transaction Amount (₹)",
        "beneficiary": "👤 కొత్త Beneficiary?",
        "time": "🕐 Transaction Time",
        "link": "🔗 Suspicious Link ఉందా?",
        "failed": "⚠️ Previous Failed Attempts",
        "yes": "అవును",
        "no": "కాదు",
        "analyze": "🔍 TRANSACTION ANALYZE చేయండి",
        "risk": "🚨 Risk Assessment",
        "risk_score": "Risk Score",
        "risk_factors": "Risk Factors",
        "status": "స్థితి",
        "high": "HIGH RISK",
        "medium": "SUSPICIOUS",
        "low": "LOW RISK",
        "xai": "🤖 Explainable AI",
        "xai_text": "ఏ transaction features risk score ను పెంచాయో system వివరిస్తుంది.",
        "contribution": "📊 Risk Contribution",
        "contribution_text": "ప్రతి factor risk కు ఎంత contribution చేసిందో chart చూపిస్తుంది.",
        "summary": "📋 Risk Factor Summary",
        "why": "🔎 ఈ Transaction ఎందుకు Flag అయింది?",
        "action": "🛡️ Recommended Action",
        "hold": "TRANSACTION HOLD చేయండి",
        "verify": "TRANSACTION VERIFY చేయండి",
        "proceed": "TRANSACTION కొనసాగించవచ్చు",
        "history": "🕘 Recent Analysis History",
        "download": "📥 Analysis Report Download",
        "pipeline": "🧠 Explainable AI Pipeline",
        "factor": "Factor",
        "score": "Score",
        "level": "Risk Level",
        "explanation": "Explanation",
        "no_factors": "Suspicious indicators ఏవీ గుర్తించబడలేదు.",
        "high_reason": "Multiple suspicious indicators ఒకేసారి గుర్తించబడ్డాయి. వాటి combined contribution risk ను పెంచింది.",
        "medium_reason": "కొంత unusual transaction behaviour గుర్తించబడింది. Verification recommended.",
        "low_reason": "ఈ transaction లో major suspicious indicators ఏవీ లేవు.",
        "unusual_amount": "Unusual Transaction Amount",
        "higher_amount": "Higher Than Usual Amount",
        "new_beneficiary": "New Beneficiary",
        "suspicious_link": "Suspicious Link",
        "unusual_time": "Unusual Transaction Time",
        "failed_attempt": "Previous Failed Attempt",
        "multiple_failed": "Multiple Failed Attempts"
    },

    "ml": {
        "title": "🛡️ ScamShield AI",
        "subtitle": "Explainable AI Scam Detector",
        "description": "ഒരു transaction പരിശോധിച്ച് അത് എന്തുകൊണ്ട് suspicious ആണെന്ന് മനസ്സിലാക്കുക.",
        "language": "🌐 ഭാഷ",
        "about": "ScamShield കുറിച്ച്",
        "about_text": "ScamShield transaction behaviour പരിശോധിച്ച് suspicious indicators കണ്ടെത്തുന്നു.",
        "transaction": "💳 Transaction വിവരങ്ങൾ",
        "demo": "🎯 Quick Demo",
        "custom": "Custom Transaction",
        "suspicious": "🔴 Suspicious Transaction",
        "normal": "🟢 Normal Transaction",
        "moderate": "🟠 Moderately Suspicious Transaction",
        "amount": "💰 Transaction Amount (₹)",
        "usual": "📊 സാധാരണ Transaction Amount (₹)",
        "beneficiary": "👤 പുതിയ Beneficiary?",
        "time": "🕐 Transaction Time",
        "link": "🔗 Suspicious Link ഉണ്ടോ?",
        "failed": "⚠️ Previous Failed Attempts",
        "yes": "അതെ",
        "no": "ഇല്ല",
        "analyze": "🔍 TRANSACTION ANALYZE ചെയ്യുക",
        "risk": "🚨 Risk Assessment",
        "risk_score": "Risk Score",
        "risk_factors": "Risk Factors",
        "status": "സ്ഥിതി",
        "high": "HIGH RISK",
        "medium": "SUSPICIOUS",
        "low": "LOW RISK",
        "xai": "🤖 Explainable AI",
        "xai_text": "ഏത് transaction features ആണ് risk score വർധിപ്പിച്ചതെന്ന് system വിശദീകരിക്കുന്നു.",
        "contribution": "📊 Risk Contribution",
        "contribution_text": "ഓരോ factor-വും risk-ലേക്ക് എത്ര contribution നൽകിയെന്ന് chart കാണിക്കുന്നു.",
        "summary": "📋 Risk Factor Summary",
        "why": "🔎 ഈ Transaction എന്തുകൊണ്ട് Flag ചെയ്തു?",
        "action": "🛡️ Recommended Action",
        "hold": "TRANSACTION HOLD ചെയ്യുക",
        "verify": "TRANSACTION VERIFY ചെയ്യുക",
        "proceed": "TRANSACTION തുടരാം",
        "history": "🕘 Recent Analysis History",
        "download": "📥 Analysis Report Download ചെയ്യുക",
        "pipeline": "🧠 Explainable AI Pipeline",
        "factor": "Factor",
        "score": "Score",
        "level": "Risk Level",
        "explanation": "Explanation",
        "no_factors": "Suspicious indicators കണ്ടെത്തിയില്ല.",
        "high_reason": "Multiple suspicious indicators ഒരുമിച്ച് കണ്ടെത്തി. അവയുടെ combined contribution risk വർധിപ്പിച്ചു.",
        "medium_reason": "ചില unusual transaction behaviour കണ്ടെത്തി. Verification recommended.",
        "low_reason": "ഈ transaction-ൽ major suspicious indicators കണ്ടെത്തിയില്ല.",
        "unusual_amount": "Unusual Transaction Amount",
        "higher_amount": "Higher Than Usual Amount",
        "new_beneficiary": "New Beneficiary",
        "suspicious_link": "Suspicious Link",
        "unusual_time": "Unusual Transaction Time",
        "failed_attempt": "Previous Failed Attempt",
        "multiple_failed": "Multiple Failed Attempts"
    }
}

# =========================================================
# LANGUAGE SELECTOR
# =========================================================

selected_language = st.sidebar.selectbox(
    "🌐 Language / மொழி",
    list(LANGUAGES.keys())
)

lang = LANGUAGES[selected_language]
T = TEXT[lang]

# =========================================================
# SESSION HISTORY
# =========================================================

if "history" not in st.session_state:
    st.session_state.history = []

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🛡️ " + T["about"])

st.sidebar.write(T["about_text"])

st.sidebar.divider()

st.sidebar.markdown("### Risk Levels")
st.sidebar.write("🟢 0–30 : " + T["low"])
st.sidebar.write("🟠 31–60 : " + T["medium"])
st.sidebar.write("🔴 61–100 : " + T["high"])

# =========================================================
# HEADER
# =========================================================

st.title(T["title"])
st.subheader(T["subtitle"])
st.write(T["description"])

st.divider()

# =========================================================
# TRANSACTION INPUT
# =========================================================

st.header(T["transaction"])
st.subheader(T["demo"])

demo_options = [
    T["custom"],
    T["suspicious"],
    T["normal"],
    T["moderate"]
]

demo = st.selectbox(
    "Demo",
    demo_options,
    label_visibility="collapsed"
)

# =========================================================
# DEFAULT VALUES
# =========================================================

amount = 25000
usual_amount = 3000
beneficiary_default = T["yes"]
time_default = 2
link_default = T["yes"]
failed_default = 2

if demo == T["normal"]:

    amount = 1500
    usual_amount = 3000
    beneficiary_default = T["no"]
    time_default = 14
    link_default = T["no"]
    failed_default = 0

elif demo == T["moderate"]:

    amount = 7000
    usual_amount = 3000
    beneficiary_default = T["yes"]
    time_default = 14
    link_default = T["no"]
    failed_default = 1

# =========================================================
# INPUT COLUMNS
# =========================================================

col1, col2 = st.columns(2)

with col1:

    amount = st.number_input(
        T["amount"],
        min_value=0,
        value=amount,
        step=500
    )

    usual_amount
