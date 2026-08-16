import streamlit as st
import re

st.set_page_config(
    page_title="ScamShield XAI",
    page_icon="🛡️",
    layout="wide"
)

# -----------------------------
# LANGUAGE TEXT
# -----------------------------
TEXT = {
    "English": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "Explainable AI Scam Detector",
        "about": "ScamShield checks transactions, messages and call transcripts for suspicious patterns.",
        "language": "Language",
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
        "risk": "Risk Score",
        "why": "Why was this flagged?",
        "contribution": "Risk Contributions",
        "action": "Recommended Action",
        "safe": "SAFE",
        "suspicious": "SUSPICIOUS",
        "critical": "CRITICAL",
        "allow": "You can proceed, but stay alert.",
        "verify": "Verify the sender, beneficiary and details before proceeding.",
        "hold": "Do not proceed. Verify the details through an official channel.",
        "no_risk": "No major suspicious indicators were detected.",
        "demo": "Hackathon prototype — not a bank decision system."
    },

    "Tamil": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "விளக்கக்கூடிய செயற்கை நுண்ணறிவு மோசடி கண்டறிதல்",
        "about": "பரிவர்த்தனை, குறுஞ்செய்தி மற்றும் அழைப்பு உரையில் சந்தேகத்திற்கிடமான அறிகுறிகளை ScamShield கண்டறியும்.",
        "language": "மொழி",
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
        "message_input": "குறுஞ்செய்தியை இங்கே ஒட்டவும்",
        "call_input": "அழைப்பு உரையை இங்கே ஒட்டவும்",
        "result": "ஆபத்து மதிப்பீடு",
        "risk": "ஆபத்து மதிப்பெண்",
        "why": "இந்த உள்ளீடு ஏன் சந்தேகமாக உள்ளது?",
        "contribution": "ஆபத்து காரணிகள்",
        "action": "பரிந்துரைக்கப்படும் நடவடிக்கை",
        "safe": "பாதுகாப்பானது",
        "suspicious": "சந்தேகத்திற்கிடமானது",
        "critical": "மிகவும் ஆபத்தானது",
        "allow": "தொடரலாம், ஆனால் கவனமாக இருங்கள்.",
        "verify": "அனுப்புநர் மற்றும் விவரங்களைச் சரிபார்த்த பிறகு தொடரவும்.",
        "hold": "தொடர வேண்டாம். அதிகாரப்பூர்வ வழியில் விவரங்களைச் சரிபார்க்கவும்.",
        "no_risk": "முக்கியமான சந்தேக அறிகுறிகள் எதுவும் கண்டறியப்படவில்லை.",
        "demo": "ஹேக்கத்தான் முன்மாதிரி — வங்கி முடிவு அமைப்பு அல்ல."
    }
}


# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def has_suspicious_link(text):
    pattern = r"(https?://|www\.|bit\.ly|tinyurl|t\.co/)"
    return bool(re.search(pattern, text.lower()))


def analyze_text(text):
    text_lower = text.lower()
    factors = []

    scam_words = [
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

    found_words = [
        word for word in scam_words
        if word in text_lower
    ]

    if found_words:
        factors.append(
            ("Suspicious language / scam keywords", 25)
        )

    if has_suspicious_link(text):
        factors.append(
            ("Suspicious or shortened link", 30)
        )

    if re.search(r"\b\d{4,6}\b", text):
        factors.append(
            ("Possible OTP / verification code request", 20)
        )

    if any(
        x in text_lower
        for x in [
            "http://",
            "https://",
            "bit.ly",
            "tinyurl"
        ]
    ):
        factors.append(
            ("External link detected", 10)
        )

    if any(
        x in text_lower
        for x in [
            "call me",
            "screen share",
            "remote access",
            "anydesk"
        ]
    ):
        factors.append(
            ("Remote access / pressure pattern", 25)
        )

    if not factors:
        factors.append(
            ("No major suspicious text pattern", 0)
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
    suspicious_link
):
    factors = []

    if amount >= 50000:
        factors.append(
            ("Unusually high transaction amount", 30)
        )

    elif amount >= 20000:
        factors.append(
            ("Higher-than-normal transaction amount", 20)
        )

    if new_beneficiary:
        factors.append(
            ("New beneficiary", 25)
        )

    if failed_attempts >= 2:
        factors.append(
            ("Previous failed attempts", 15)
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
            ("No major suspicious transaction indicator", 0)
        )

    score = min(
        sum(points for _, points in factors),
        100
    )

    return score, factors


def risk_label(score, lang):

    t = TEXT[lang]

    if score >= 70:
        return t["critical"], "🔴"

    if score >= 40
