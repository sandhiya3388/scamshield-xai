import streamlit as st
import re
import pandas as pd

st.set_page_config(
    page_title="ScamShield XAI",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# LANGUAGE
# =========================================================

LANG = {
    "English": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "Explainable AI Scam Detection",
        "mode": "Detection Mode",
        "transaction": "💳 Transaction",
        "message": "💬 Message",
        "call": "📞 Call",
        "analyze": "🔍 Analyze",
        "score": "Risk Score",
        "why": "🧠 Why is this suspicious?",
        "chart": "📊 Risk Contribution",
        "action": "🛡️ Recommended Action",
        "safe": "SAFE",
        "suspicious": "SUSPICIOUS",
        "high": "HIGH RISK",
        "safe_action": "No major scam indicators were detected. Stay alert.",
        "suspicious_action": "Verify the sender and details before taking action.",
        "high_action": "Do not proceed. Verify through an official channel.",
        "amount": "Transaction Amount",
        "beneficiary": "New Beneficiary",
        "failed": "Previous Failed Attempts",
        "unusual": "Unusual Transaction Time",
        "tx_link": "Suspicious Link Associated",
        "message_box": "Enter suspicious message",
        "call_box": "Enter call transcript",
        "empty": "Please enter some content first.",
        "about": "This prototype explains which factors increased the scam risk score.",
        "sample": "Try Sample",
        "clear": "Clear",
        "factor": "Risk Factor",
        "points": "Points"
    },

    "தமிழ்": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "விளக்கக்கூடிய AI மோசடி கண்டறிதல்",
        "mode": "கண்டறிதல் வகை",
        "transaction": "💳 பரிவர்த்தனை",
        "message": "💬 குறுஞ்செய்தி",
        "call": "📞 அழைப்பு",
        "analyze": "🔍 ஆய்வு செய்",
        "score": "ஆபத்து மதிப்பெண்",
        "why": "🧠 ஏன் இது சந்தேகமாக உள்ளது?",
        "chart": "📊 ஆபத்து காரணிகளின் பங்களிப்பு",
        "action": "🛡️ பரிந்துரைக்கப்படும் நடவடிக்கை",
        "safe": "பாதுகாப்பானது",
        "suspicious": "சந்தேகத்திற்கிடமானது",
        "high": "அதிக ஆபத்து",
        "safe_action": "முக்கியமான மோசடி அறிகுறிகள் எதுவும் இல்லை. கவனமாக இருங்கள்.",
        "suspicious_action": "நடவடிக்கை எடுப்பதற்கு முன் அனுப்புநர் மற்றும் விவரங்களை சரிபார்க்கவும்.",
        "high_action": "தொடர வேண்டாம். அதிகாரப்பூர்வ வழியில் சரிபார்க்கவும்.",
        "amount": "பரிவர்த்தனை தொகை",
        "beneficiary": "புதிய பயனாளி",
        "failed": "முந்தைய தோல்வியடைந்த முயற்சிகள்",
        "unusual": "வழக்கத்திற்கு மாறான பரிவர்த்தனை நேரம்",
        "tx_link": "பரிவர்த்தனையுடன் தொடர்புடைய சந்தேக இணைப்பு",
        "message_box": "சந்தேகமான செய்தியை உள்ளிடவும்",
        "call_box": "அழைப்பு உரையை உள்ளிடவும்",
        "empty": "முதலில் தகவலை உள்ளிடவும்.",
        "about": "எந்த காரணிகள் ஆபத்து மதிப்பெண்ணை அதிகரித்தன என்பதை இந்த முன்மாதிரி விளக்குகிறது.",
        "sample": "மாதிரி முயற்சி",
        "clear": "அழி",
        "factor": "ஆபத்து காரணி",
        "points": "புள்ளிகள்"
    },

    "Hindi": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "व्याख्यात्मक AI घोटाला पहचान",
        "mode": "पहचान मोड",
        "transaction": "💳 लेन-देन",
        "message": "💬 संदेश",
        "call": "📞 कॉल",
        "analyze": "🔍 विश्लेषण करें",
        "score": "जोखिम स्कोर",
        "why": "🧠 यह संदिग्ध क्यों है?",
        "chart": "📊 जोखिम योगदान",
        "action": "🛡️ सुझाई गई कार्रवाई",
        "safe": "सुरक्षित",
        "suspicious": "संदिग्ध",
        "high": "उच्च जोखिम",
        "safe_action": "कोई बड़ा घोटाला संकेत नहीं मिला। सावधान रहें।",
        "suspicious_action": "कार्रवाई से पहले प्रेषक और विवरण सत्यापित करें।",
        "high_action": "आगे न बढ़ें। आधिकारिक माध्यम से सत्यापित करें।",
        "amount": "लेन-देन राशि",
        "beneficiary": "नया लाभार्थी",
        "failed": "पिछले असफल प्रयास",
        "unusual": "असामान्य लेन-देन समय",
        "tx_link": "संदिग्ध लिंक",
        "message_box": "संदिग्ध संदेश दर्ज करें",
        "call_box": "कॉल ट्रांसक्रिप्ट दर्ज करें",
        "empty": "पहले जानकारी दर्ज करें।",
        "about": "यह प्रोटोटाइप बताता है कि किन कारणों से जोखिम स्कोर बढ़ा।",
        "sample": "नमूना",
        "clear": "साफ करें",
        "factor": "जोखिम कारक",
        "points": "अंक"
    },

    "Telugu": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "వివరణాత్మక AI మోసం గుర్తింపు",
        "mode": "గుర్తింపు విధానం",
        "transaction": "💳 లావాదేవీ",
        "message": "💬 సందేశం",
        "call": "📞 కాల్",
        "analyze": "🔍 విశ్లేషించండి",
        "score": "ప్రమాద స్కోర్",
        "why": "🧠 ఇది ఎందుకు అనుమానాస్పదం?",
        "chart": "📊 ప్రమాద కారణాల సహకారం",
        "action": "🛡️ సూచించిన చర్య",
        "safe": "సురక్షితం",
        "suspicious": "అనుమానాస్పదం",
        "high": "అధిక ప్రమాదం",
        "safe_action": "పెద్ద మోసం సూచనలు కనిపించలేదు. జాగ్రత్తగా ఉండండి.",
        "suspicious_action": "చర్య తీసుకునే ముందు పంపినవారిని మరియు వివరాలను తనిఖీ చేయండి.",
        "high_action": "కొనసాగించవద్దు. అధికారిక మార్గంలో ధృవీకరించండి.",
        "amount": "లావాదేవీ మొత్తం",
        "beneficiary": "కొత్త లబ్ధిదారు",
        "failed": "మునుపటి విఫల ప్రయత్నాలు",
        "unusual": "అసాధారణ లావాదేవీ సమయం",
        "tx_link": "అనుమానాస్పద లింక్",
        "message_box": "అనుమానాస్పద సందేశాన్ని నమోదు చేయండి",
        "call_box": "కాల్ ట్రాన్స్క్రిప్ట్ నమోదు చేయండి",
        "empty": "ముందుగా సమాచారాన్ని నమోదు చేయండి.",
        "about": "ప్రమాద స్కోర్ ఎందుకు పెరిగిందో ఈ ప్రోటోటైప్ వివరిస్తుంది.",
        "sample": "నమూనా",
        "clear": "తొలగించు",
        "factor": "ప్రమాద కారకం",
        "points": "పాయింట్లు"
    },

    "Malayalam": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "വിശദീകരിക്കാവുന്ന AI തട്ടിപ്പ് കണ്ടെത്തൽ",
        "mode": "കണ്ടെത്തൽ രീതി",
        "transaction": "💳 ഇടപാട്",
        "message": "💬 സന്ദേശം",
        "call": "📞 കോൾ",
        "analyze": "🔍 പരിശോധിക്കുക",
        "score": "റിസ്ക് സ്കോർ",
        "why": "🧠 ഇത് സംശയാസ്പദമാകുന്നത് എന്തുകൊണ്ട്?",
        "chart": "📊 റിസ്ക് സംഭാവന",
        "action": "🛡️ ശുപാർശ ചെയ്യുന്ന നടപടി",
        "safe": "സുരക്ഷിതം",
        "suspicious": "സംശയാസ്പദം",
        "high": "ഉയർന്ന അപകടസാധ്യത",
        "safe_action": "പ്രധാനപ്പെട്ട തട്ടിപ്പ് സൂചനകൾ കണ്ടെത്തിയില്ല. ജാഗ്രത പാലിക്കുക.",
        "suspicious_action": "നടപടി എടുക്കുന്നതിന് മുമ്പ് അയച്ചയാളെയും വിവരങ്ങളും പരിശോധിക്കുക.",
        "high_action": "തുടരരുത്. ഔദ്യോഗിക മാർഗത്തിലൂടെ പരിശോധിക്കുക.",
        "amount": "ഇടപാട് തുക",
        "beneficiary": "പുതിയ ഗുണഭോക്താവ്",
        "failed": "മുമ്പത്തെ പരാജയപ്പെട്ട ശ്രമങ്ങൾ",
        "unusual": "അസാധാരണ ഇടപാട് സമയം",
        "tx_link": "സംശയാസ്പദമായ ലിങ്ക്",
        "message_box": "സംശയാസ്പദമായ സന്ദേശം നൽകുക",
        "call_box": "കോൾ ട്രാൻസ്ക്രിപ്റ്റ് നൽകുക",
        "empty": "ആദ്യം വിവരങ്ങൾ നൽകുക.",
        "about": "റിസ്ക് സ്കോർ വർദ്ധിപ്പിച്ച കാരണങ്ങൾ ഈ പ്രോട്ടോടൈപ്പ് വിശദീകരിക്കുന്നു.",
        "sample": "സാമ്പിൾ",
        "clear": "മായ്ക്കുക",
        "factor": "റിസ്ക് ഘടകം",
        "points": "പോയിന്റുകൾ"
    }
}

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🛡️ ScamShield")

language = st.sidebar.selectbox(
    "🌐 Language",
    list(LANG.keys())
)

T = LANG[language]

st.sidebar.info(T["about"])

# =========================================================
# TITLE
# =========================================================

st.title(T["title"])
st.caption(T["subtitle"])

mode = st.radio(
    T["mode"],
    [
        T["transaction"],
        T["message"],
        T["call"]
    ],
    horizontal=True
)

# =========================================================
# TEXT ANALYSIS
# =========================================================

def analyze_text(text):

    text = text.lower()

    factors = []

    urgent_words = [
        "urgent",
        "immediately",
        "act now",
        "hurry",
        "otp",
        "pin",
        "password",
        "kyc",
        "account blocked",
        "verify now",
        "இப்போதே",
        "உடனே",
        "அவசரம்",
        "otp",
        "வங்கி",
        "கணக்கு"
    ]

    money_words = [
        "send money",
        "transfer",
        "payment",
        "pay",
        "upi",
        "refund fee",
        "processing fee",
        "பணம்",
        "செலுத்த",
        "கட்டணம்"
    ]

    if any(word in text for word in urgent_words):
        factors.append(
            ("Urgency / sensitive information request", 25)
        )

    if any(word in text for word in money_words):
        factors.append(
            ("Money or payment request", 25)
        )

    if re.search(r"(https?://|www\.|bit\.ly|tinyurl)", text):
        factors.append(
            ("Suspicious link", 30)
        )

    if re.search(r"\b\d{4,6}\b", text):
        factors.append(
            ("Possible OTP / verification code", 20)
        )

    remote_words = [
        "anydesk",
        "teamviewer",
        "remote access",
        "screen share",
        "screen sharing"
    ]

    if any(word in text for word in remote_words):
        factors.append(
            ("Remote access request", 30)
        )

    impersonation_words = [
        "bank officer",
        "police",
        "rbi",
        "income tax",
        "customer care",
        "வங்கி அதிகாரி",
        "போலீஸ்"
    ]

    if any(word in text for word in impersonation_words):
        factors.append(
            ("Possible impersonation", 25)
        )

    if not factors:
        factors.append(
            ("No major suspicious indicator", 0)
        )

    score = min(
        sum(points for _, points in factors),
        100
    )

    return score, factors


# =========================================================
# TRANSACTION ANALYSIS
# =========================================================

def analyze_transaction(
    amount,
    new_beneficiary,
    failed_attempts,
    unusual_time,
    suspicious_link
):

    factors = []

    if amount >= 50000:
        factors.append(
            ("High transaction amount", 30)
        )

    elif amount >= 20000:
        factors.append(
            ("Higher-than-normal amount", 20)
        )

    if new_beneficiary:
        factors.append(
            ("New beneficiary", 25)
        )

    if failed_attempts >= 2:
        factors.append(
            ("Multiple failed attempts", 15)
        )

    elif failed_attempts == 1:
        factors.append(
            ("Previous failed attempt", 5)
        )

    if unusual_time:
        factors.append(
            ("Unusual transaction time", 10)
        )

    if suspicious_link:
        factors.append(
            ("Suspicious link associated with transaction", 30)
        )

    if not factors:
        factors.append(
            ("No major suspicious indicator", 0)
        )

    score = min(
        sum(points for _, points in factors),
        100
    )

    return score, factors


# =========================================================
# RESULT
# =========================================================

def show_result(score, factors):

    st.divider()

    if score >= 70:

        st.error(
            f"🔴 {T['high']} — {score}/100"
        )

        st.warning(
            T["high_action"]
        )

    elif score >= 40:

        st.warning(
            f"🟠 {T['suspicious']} — {score}/100"
        )

        st.info(
            T["suspicious_action"]
        )

    else:

        st.success(
            f"🟢 {T['safe']} — {score}/100"
        )

        st.info(
            T["safe_action"]
        )

    st.subheader(
        f"📈 {T['score']}"
    )

    st.progress(score / 100)

    # -----------------------------------------------------
    # EXPLANATION
    # -----------------------------------------------------

    st.subheader(T["why"])

    for name, points in factors:

        if points > 0:
            st.write(
                f"🔴 **{name}** → +{points} {T['points']}"
            )

    # -----------------------------------------------------
    # REAL STREAMLIT CHART
    # -----------------------------------------------------

    st.subheader(T["chart"])

    chart_data = pd.DataFrame(
        factors,
        columns=[
            T["factor"],
            T["points"]
        ]
    )

    if chart_data[T["points"]].sum() > 0:

        st.bar_chart(
            chart_data.set_index(T["factor"])
        )

    else:

        st.success(
            T["safe_action"]
        )

    # -----------------------------------------------------
    # RECOMMENDATION
    # -----------------------------------------------------

    st.subheader(T["action"])

    if score >= 70:

        st.error(T["high_action"])

    elif score >= 40:

        st.warning(T["suspicious_action"])

    else:

        st.success(T["safe_action"])


# =========================================================
# TRANSACTION TAB
# =========================================================

if mode == T["transaction"]:

    st.header(T["transaction"])

    amount = st.number_input(
        T["amount"],
        min_value=0.0,
        value=1000.0,
        step=500.0
    )

    col1, col2 = st.columns(2)

    with col1:

        new_beneficiary = st.checkbox(
            T["beneficiary"]
        )

        unusual_time = st.checkbox(
            T["unusual"]
        )

    with col2:

        failed_attempts = st.number_input(
            T["failed"],
            min_value=0,
            max_value=10,
            value=0,
            step=1
        )

        suspicious_link = st.checkbox(
            T["tx_link"]
        )

    if st.button(
        T["analyze"],
        type="primary",
        use_container_width=True
    ):

        score, factors = analyze_transaction(
            amount,
            new_beneficiary,
            failed_attempts,
            unusual_time,
            suspicious_link
        )

        show_result(
            score,
            factors
        )


# =========================================================
# MESSAGE
# =========================================================

elif mode == T["message"]:

    st.header(T["message"])

    message = st.text_area(
        T["message_box"],
        height=180
    )

    col1, col2 = st.columns(2)

    with col1:

        analyze_message = st.button(
            T["analyze"],
            type="primary",
            use_container_width=True
        )

    with col2:

        sample_message = st.button(
            T["sample"],
            use_container_width=True
        )

    if sample_message:

        message = (
            "Congratulations! You won a prize. "
            "Your account will be blocked. "
            "Click https://example.com and send OTP immediately."
        )

        st.info(message)

        score, factors = analyze_text(
            message
        )

        show_result(
            score,
            factors
        )

    elif analyze_message:

        if not message.strip():

            st.warning(T["empty"])

        else:

            score, factors = analyze_text(
                message
            )

            show_result(
                score,
                factors
            )


# =========================================================
# CALL
# =========================================================

else:

    st.header(T["call"])

    st.info(
        T["call_box"]
    )

    call_text = st.text_area(
        T["call_box"],
        height=220
    )

    col1, col2 = st.columns(2)

    with col1:

        analyze_call = st.button(
            T["analyze"],
            type="primary",
            use_container_width=True
        )

    with col2:

        sample_call = st.button(
            T["sample"],
            use_container_width=True
        )

    if sample_call:

        call_text = (
            "Hello, I am calling from your bank. "
            "Your account will be blocked today. "
            "Please tell me your OTP immediately "
            "and install AnyDesk for verification."
        )

        st.info(call_text)

        score, factors = analyze_text(
            call_text
        )

        show_result(
            score,
            factors
        )

    elif analyze_call:

        if not call_text.strip():

            st.warning(T["empty"])

        else:

            score, factors = analyze_text(
                call_text
            )

            show_result(
                score,
                factors
            )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "🛡️ ScamShield XAI | Hackathon Prototype"
)
