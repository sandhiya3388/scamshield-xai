import streamlit as st
import re

st.set_page_config(
    page_title="ScamShield XAI",
    page_icon="🛡️",
    layout="wide"
)

TEXT = {
    "English": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "Explainable AI Scam Detector",
        "about": "ScamShield checks transactions, messages and call transcripts for suspicious patterns.",
        "mode": "Detection Mode",
        "transaction": "Transaction",
        "message": "Message",
        "call": "Call",
        "amount": "Transaction amount",
        "new_beneficiary": "New beneficiary",
        "failed": "Previous failed attempts",
        "night": "Unusual transaction time",
        "link": "Suspicious link present",
        "analyze": "🔍 Analyze",
        "message_input": "Paste the message here",
        "call_input": "Paste the call transcript here",
        "result": "Risk Assessment",
        "why": "Why was this flagged?",
        "contribution": "Risk Contribution",
        "action": "Recommended Action",
        "safe": "SAFE",
        "suspicious": "SUSPICIOUS",
        "critical": "CRITICAL",
        "allow": "You can proceed, but stay alert.",
        "verify": "Verify the sender, beneficiary and details before proceeding.",
        "hold": "Do not proceed. Verify the details through an official channel.",
        "no_risk": "No major suspicious indicators were detected.",
        "empty": "Please enter some text.",
        "call_info": "Paste the caller's words or call transcript here. This prototype checks the text for scam indicators.",
        "footer": "Hackathon prototype — not a bank decision system.",
        "factor_keywords": "Suspicious language or scam keywords",
        "factor_link": "Suspicious or shortened link",
        "factor_otp": "Possible OTP or verification code request",
        "factor_external": "External link detected",
        "factor_remote": "Remote access or pressure pattern",
        "factor_amount_high": "Unusually high transaction amount",
        "factor_amount_medium": "Higher-than-normal transaction amount",
        "factor_new": "New beneficiary",
        "factor_failed": "Previous failed attempts",
        "factor_failed_one": "Previous failed attempt",
        "factor_time": "Unusual transaction time",
        "factor_tx_link": "Suspicious link associated with transaction",
        "factor_none": "No major suspicious indicator"
    },

    "Tamil": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "விளக்கக்கூடிய செயற்கை நுண்ணறிவு மோசடி கண்டறிதல்",
        "about": "பரிவர்த்தனை, குறுஞ்செய்தி மற்றும் அழைப்பு உரையில் சந்தேக அறிகுறிகளை ScamShield கண்டறியும்.",
        "mode": "கண்டறிதல் வகை",
        "transaction": "பரிவர்த்தனை",
        "message": "குறுஞ்செய்தி",
        "call": "அழைப்பு",
        "amount": "பரிவர்த்தனை தொகை",
        "new_beneficiary": "புதிய பயனாளி",
        "failed": "முந்தைய தோல்வியடைந்த முயற்சிகள்",
        "night": "வழக்கத்திற்கு மாறான நேரம்",
        "link": "சந்தேகத்திற்கிடமான இணைப்பு உள்ளது",
        "analyze": "🔍 ஆய்வு செய்",
        "message_input": "குறுஞ்செய்தியை இங்கே உள்ளிடவும்",
        "call_input": "அழைப்பு உரையை இங்கே உள்ளிடவும்",
        "result": "ஆபத்து மதிப்பீடு",
        "why": "இது ஏன் சந்தேகமாகக் கண்டறியப்பட்டது?",
        "contribution": "ஆபத்து காரணிகள்",
        "action": "பரிந்துரைக்கப்படும் நடவடிக்கை",
        "safe": "பாதுகாப்பானது",
        "suspicious": "சந்தேகத்திற்கிடமானது",
        "critical": "மிகவும் ஆபத்தானது",
        "allow": "தொடரலாம். ஆனால் கவனமாக இருங்கள்.",
        "verify": "அனுப்புநர், பயனாளி மற்றும் விவரங்களைச் சரிபார்த்த பிறகு தொடரவும்.",
        "hold": "தொடர வேண்டாம். அதிகாரப்பூர்வ வழியில் விவரங்களைச் சரிபார்க்கவும்.",
        "no_risk": "முக்கியமான சந்தேக அறிகுறிகள் எதுவும் கண்டறியப்படவில்லை.",
        "empty": "உள்ளடக்கத்தை உள்ளிடவும்.",
        "call_info": "அழைப்பில் பேசப்பட்ட வார்த்தைகள் அல்லது அழைப்பு உரையை இங்கே உள்ளிடவும். இந்த முன்மாதிரி மோசடி அறிகுறிகளை ஆய்வு செய்யும்.",
        "footer": "ஹேக்கத்தான் முன்மாதிரி — இது வங்கி முடிவு அமைப்பு அல்ல.",
        "factor_keywords": "சந்தேகமான வார்த்தைகள் அல்லது மோசடி சொற்கள்",
        "factor_link": "சந்தேகமான அல்லது சுருக்கப்பட்ட இணைப்பு",
        "factor_otp": "OTP அல்லது சரிபார்ப்பு குறியீடு கேட்கப்படலாம்",
        "factor_external": "வெளிப்புற இணைப்பு கண்டறியப்பட்டது",
        "factor_remote": "தொலைநிலை அணுகல் அல்லது அழுத்தம் கொடுக்கும் முறை",
        "factor_amount_high": "வழக்கத்திற்கு மாறாக அதிக பரிவர்த்தனை தொகை",
        "factor_amount_medium": "வழக்கத்தை விட அதிகமான பரிவர்த்தனை தொகை",
        "factor_new": "புதிய பயனாளி",
        "factor_failed": "முந்தைய தோல்வியடைந்த முயற்சிகள்",
        "factor_failed_one": "முந்தைய தோல்வியடைந்த முயற்சி",
        "factor_time": "வழக்கத்திற்கு மாறான பரிவர்த்தனை நேரம்",
        "factor_tx_link": "பரிவர்த்தனையுடன் தொடர்புடைய சந்தேக இணைப்பு",
        "factor_none": "முக்கியமான சந்தேக அறிகுறி எதுவும் இல்லை"
    }
}


def has_suspicious_link(text):
    pattern = r"(https?://|www\.|bit\.ly|tinyurl|t\.co/)"
    return bool(re.search(pattern, text.lower()))


def analyze_text(text, lang):
    t = TEXT[lang]
    lower = text.lower()
    factors = []

    keywords = [
        "otp",
        "pin",
        "password",
        "urgent",
        "verify now",
        "account blocked",
        "kyc",
        "click",
        "winner",
        "prize",
        "refund",
        "cashback",
        "remote access",
        "screen share",
        "investment",
        "police",
        "arrest",
        "இப்போதே",
        "ரகசிய",
        "வங்கி",
        "கணக்கு",
        "பரிசு",
        "உடனே",
        "கிளிக்"
    ]

    if any(word in lower for word in keywords):
        factors.append(
            (t["factor_keywords"], 25)
        )

    if has_suspicious_link(text):
        factors.append(
            (t["factor_link"], 30)
        )

    if re.search(r"\b\d{4,6}\b", text):
        factors.append(
            (t["factor_otp"], 20)
        )

    if any(
        x in lower
        for x in [
            "http://",
            "https://",
            "bit.ly",
            "tinyurl"
        ]
    ):
        factors.append(
            (t["factor_external"], 10)
        )

    if any(
        x in lower
        for x in [
            "call me",
            "screen share",
            "remote access",
            "anydesk"
        ]
    ):
        factors.append(
            (t["factor_remote"], 25)
        )

    if not factors:
        factors.append(
            (t["factor_none"], 0)
        )

    score = min(
        sum(points for _, points in factors),
        100
    )

    return score, factors


def analyze_transaction(
    amount,
    new_beneficiary,
    failed_attempts,
    unusual_time,
    suspicious_link,
    lang
):
    t = TEXT[lang]
    factors = []

    if amount >= 50000:
        factors.append(
            (t["factor_amount_high"], 30)
        )

    elif amount >= 20000:
        factors.append(
            (t["factor_amount_medium"], 20)
        )

    if new_beneficiary:
        factors.append(
            (t["factor_new"], 25)
        )

    if failed_attempts >= 2:
        factors.append(
            (t["factor_failed"], 15)
        )

    elif failed_attempts == 1:
        factors.append(
            (t["factor_failed_one"], 5)
        )

    if unusual_time:
        factors.append(
            (t["factor_time"], 10)
        )

    if suspicious_link:
        factors.append(
            (t["factor_tx_link"], 30)
        )

    if not factors:
        factors.append(
            (t["factor_none"], 0)
        )

    score = min(
        sum(points for _, points in factors),
        100
    )

    return score, factors


def show_chart(factors, title):

    st.subheader("📊 " + title)

    max_value = max(
        [points for _, points in factors] + [1]
    )

    for name, points in factors:

        if points > 0:
            width = int(
                (points / max_value) * 100
            )
        else:
            width = 0

        if points >= 20:
            color = "#e53935"
        elif points > 0:
            color = "#fb8c00"
        else:
            color = "#43a047"

        html = (
            '<div style="margin:12px 0;">'
            '<div style="display:flex;'
            'justify-content:space-between;">'
            f'<span><b>{name}</b></span>'
            f'<span><b>+{points}</b></span>'
            '</div>'
            '<div style="background:#eeeeee;'
            'border-radius:8px;height:14px;">'
            f'<div style="width:{width}%;'
            f'background:{color};height:14px;'
            'border-radius:8px;"></div>'
            '</div>'
            '</div>'
        )

        st.markdown(
            html,
            unsafe_allow_html=True
        )


def show_result(score, factors, lang):

    t = TEXT[lang]

    st.divider()

    st.subheader(
        "🧠 " + t["result"]
    )

    if score >= 70:

        st.error(
            f"🔴 {t['critical']} — {score}/100"
        )

        st.warning(
            t["hold"]
        )

    elif score >= 40:

        st.warning(
            f"🟠 {t['suspicious']} — {score}/100"
        )

        st.info(
            t["verify"]
        )

    else:

        st.success(
            f"🟢 {t['safe']} — {score}/100"
        )

        st.info(
            t["allow"]
        )

    st.progress(
        score / 100
    )

    show_chart(
        factors,
        t["contribution"]
    )

    st.subheader(
        "🔎 " + t["why"]
    )

    positive = [
        (name, points)
        for name, points in factors
        if points > 0
    ]

    if positive:

        for name, points in positive:

            st.write(
                f"• **{name}** — +{points} points"
            )

    else:

        st.write(
            t["no_risk"]
        )

    st.subheader(
        "🛡️ " + t["action"]
    )

    if score >= 70:

        st.error(
            t["hold"]
        )

    elif score >= 40:

        st.warning(
            t["verify"]
        )

    else:

        st.success(
            t["allow"]
        )


st.sidebar.title(
    "🛡️ ScamShield"
)

language = st.sidebar.selectbox(
    "Language / மொழி",
    [
        "English",
        "Tamil"
    ]
)

t = TEXT[language]

st.sidebar.info(
    t["about"]
)

st.title(
    t["title"]
)

st.caption(
    t["subtitle"]
)

mode = st.radio(
    t["mode"],
    [
        t["transaction"],
        t["message"],
        t["call"]
    ],
    horizontal=True
)


if mode == t["transaction"]:

    st.subheader(
        "💳 " + t["transaction"]
    )

    amount = st.number_input(
        t["amount"],
        min_value=0.0,
        value=1000.0,
        step=500.0
    )

    col1, col2 = st.columns(2)

    with col1:

        new_beneficiary = st.checkbox(
            t["new_beneficiary"]
        )

        unusual_time = st.checkbox(
            t["night"]
        )

    with col2:

        failed_attempts = st.number_input(
            t["failed"],
            min_value=0,
            max_value=10,
            value=0,
            step=1
        )

        suspicious_link = st.checkbox(
            t["link"]
        )

    if st.button(
        t["analyze"],
        type="primary",
        use_container_width=True
    ):

        score, factors = analyze_transaction(
            amount,
            new_beneficiary,
            failed_attempts,
            unusual_time,
            suspicious_link,
            language
        )

        show_result(
            score,
            factors,
            language
        )


elif mode == t["message"]:

    st.subheader(
        "💬 " + t["message"]
    )

    message = st.text_area(
        t["message_input"],
        height=180
    )

    if st.button(
        t["analyze"],
        type="primary",
        use_container_width=True
    ):

        if not message.strip():

            st.warning(
                t["empty"]
            )

        else:

            score, factors = analyze_text(
                message,
                language
            )

            show_result(
                score,
                factors,
                language
            )


else:

    st.subheader(
        "📞 " + t["call"]
    )

    st.info(
        t["call_info"]
    )

    call_text = st.text_area(
        t["call_input"],
        height=220
    )

    if st.button(
        t["analyze"],
        type="primary",
        use_container_width=True
    ):

        if not call_text.strip():

            st.warning(
                t["empty"]
            )

        else:

            score, factors = analyze_text(
                call_text,
                language
            )

            show_result(
                score,
                factors,
                language
            )


st.divider()

st.caption(
    t["footer"]
)
