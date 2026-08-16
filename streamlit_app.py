import streamlit as st
import pandas as pd
import re

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="ScamShield XAI",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------------------------------------
# LANGUAGE DATA
# ---------------------------------------------------------

LANG = {
    "English": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "Explainable AI Scam Detection System",
        "about": "About ScamShield",
        "about_text": "ScamShield analyzes calls and messages to identify suspicious scam indicators and clearly explains why something is risky.",
        "language": "Language",
        "call_tab": "📞 Call Detection",
        "message_tab": "💬 Message Detection",
        "caller": "Caller phone number",
        "call_text": "Enter the call conversation or what the caller said",
        "message_text": "Paste the suspicious message here",
        "analyze_call": "🔍 Analyze Call",
        "analyze_message": "🔍 Analyze Message",
        "risk": "Risk Assessment",
        "explanation": "Explainable AI",
        "why": "Why was this flagged?",
        "action": "Recommended Action",
        "safe_action": "The content appears low risk. Still verify important requests independently.",
        "suspicious_action": "Be careful. Verify the sender, caller and request before taking action.",
        "high_action": "Do not proceed. Verify the request through an official channel.",
        "safe": "SAFE",
        "suspicious": "SUSPICIOUS",
        "high": "HIGH RISK",
        "contribution": "Risk Contribution",
        "points": "points",
        "no_indicators": "No strong scam indicators were detected.",
        "enter_call": "Please enter call details before analysis.",
        "enter_message": "Please enter a message before analysis.",
        "phone": "Phone Number",
        "score": "Risk Score",
        "reason": "Reason",
        "download": "Download Analysis",
        "prototype": "Prototype for hackathon demonstration",
        "warning": "This is a demonstration system and should not replace official fraud investigation.",
        "urgent": "Urgency or pressure",
        "otp": "OTP / verification request",
        "money": "Money or payment request",
        "bank": "Banking information request",
        "link": "Suspicious link",
        "reward": "Prize / reward claim",
        "impersonation": "Impersonation",
        "remote": "Remote access request",
        "new_number": "Unknown or unusual number",
        "call_reason": "The caller used suspicious language or requested sensitive information.",
        "message_reason": "The message contains patterns commonly associated with scams."
    },

    "தமிழ்": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "விளக்கக்கூடிய செயற்கை நுண்ணறிவு மோசடி கண்டறிதல் அமைப்பு",
        "about": "ScamShield பற்றி",
        "about_text": "ScamShield அழைப்புகள் மற்றும் குறுஞ்செய்திகளில் உள்ள சந்தேகத்திற்கிடமான அறிகுறிகளை கண்டறிந்து, அவை ஏன் ஆபத்தானவை என்பதை விளக்குகிறது.",
        "language": "மொழி",
        "call_tab": "📞 அழைப்பு கண்டறிதல்",
        "message_tab": "💬 செய்தி கண்டறிதல்",
        "caller": "அழைத்த தொலைபேசி எண்",
        "call_text": "அழைப்பில் பேசிய தகவலை இங்கே உள்ளிடவும்",
        "message_text": "சந்தேகத்திற்கிடமான செய்தியை இங்கே ஒட்டவும்",
        "analyze_call": "🔍 அழைப்பை பகுப்பாய்வு செய்",
        "analyze_message": "🔍 செய்தியை பகுப்பாய்வு செய்",
        "risk": "ஆபத்து மதிப்பீடு",
        "explanation": "விளக்கக்கூடிய செயற்கை நுண்ணறிவு",
        "why": "இந்த தகவல் ஏன் எச்சரிக்கப்பட்டது?",
        "action": "பரிந்துரைக்கப்படும் நடவடிக்கை",
        "safe_action": "இந்த தகவலில் குறைந்த அளவிலான ஆபத்து மட்டுமே காணப்படுகிறது. முக்கியமான கோரிக்கைகளை தனியாக சரிபார்க்கவும்.",
        "suspicious_action": "கவனமாக இருங்கள். நடவடிக்கை எடுப்பதற்கு முன் அனுப்புநர் அல்லது அழைப்பாளரை சரிபார்க்கவும்.",
        "high_action": "தொடர வேண்டாம். அதிகாரப்பூர்வ வழியின் மூலம் கோரிக்கையை சரிபார்க்கவும்.",
        "safe": "பாதுகாப்பானது",
        "suspicious": "சந்தேகத்திற்கிடமானது",
        "high": "அதிக ஆபத்து",
        "contribution": "ஆபத்து காரணிகளின் பங்களிப்பு",
        "points": "புள்ளிகள்",
        "no_indicators": "வலுவான மோசடி அறிகுறிகள் எதுவும் கண்டறியப்படவில்லை.",
        "enter_call": "பகுப்பாய்வு செய்வதற்கு முன் அழைப்பு தகவலை உள்ளிடவும்.",
        "enter_message": "பகுப்பாய்வு செய்வதற்கு முன் செய்தியை உள்ளிடவும்.",
        "phone": "தொலைபேசி எண்",
        "score": "ஆபத்து மதிப்பெண்",
        "reason": "காரணம்",
        "download": "பகுப்பாய்வை பதிவிறக்கு",
        "prototype": "ஹேக்கத்தான் விளக்கத்திற்கான மாதிரி அமைப்பு",
        "warning": "இது ஒரு மாதிரி அமைப்பு. அதிகாரப்பூர்வ மோசடி விசாரணைக்கு மாற்றாக இதைப் பயன்படுத்த வேண்டாம்.",
        "urgent": "அவசரம் அல்லது அழுத்தம்",
        "otp": "OTP / சரிபார்ப்பு கோரிக்கை",
        "money": "பணம் அல்லது பணம் செலுத்தும் கோரிக்கை",
        "bank": "வங்கி தகவல் கோரிக்கை",
        "link": "சந்தேகத்திற்கிடமான இணைப்பு",
        "reward": "பரிசு / வெகுமதி கோரிக்கை",
        "impersonation": "ஆள்மாறாட்டம்",
        "remote": "தொலைநிலை அணுகல் கோரிக்கை",
        "new_number": "அறிமுகமில்லாத அல்லது வழக்கத்திற்கு மாறான எண்",
        "call_reason": "அழைப்பாளர் சந்தேகத்திற்கிடமான வார்த்தைகளை பயன்படுத்தியிருக்கலாம் அல்லது முக்கியமான தகவலை கேட்டிருக்கலாம்.",
        "message_reason": "இந்த செய்தியில் பொதுவாக மோசடிகளில் காணப்படும் சில அறிகுறிகள் உள்ளன."
    },

    "Hindi": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "व्याख्यात्मक AI घोटाला पहचान प्रणाली",
        "about": "ScamShield के बारे में",
        "about_text": "ScamShield कॉल और संदेशों में संदिग्ध संकेतों की पहचान करता है और बताता है कि वे जोखिमपूर्ण क्यों हैं।",
        "language": "भाषा",
        "call_tab": "📞 कॉल पहचान",
        "message_tab": "💬 संदेश पहचान",
        "caller": "कॉलर का फोन नंबर",
        "call_text": "कॉल में कही गई बात यहां लिखें",
        "message_text": "संदिग्ध संदेश यहां पेस्ट करें",
        "analyze_call": "🔍 कॉल का विश्लेषण करें",
        "analyze_message": "🔍 संदेश का विश्लेषण करें",
        "risk": "जोखिम मूल्यांकन",
        "explanation": "व्याख्यात्मक AI",
        "why": "इसे क्यों चिन्हित किया गया?",
        "action": "सुझाई गई कार्रवाई",
        "safe_action": "जोखिम कम दिखाई देता है। फिर भी महत्वपूर्ण अनुरोधों को स्वतंत्र रूप से सत्यापित करें।",
        "suspicious_action": "सावधान रहें। कार्रवाई करने से पहले प्रेषक या कॉलर को सत्यापित करें।",
        "high_action": "आगे न बढ़ें। आधिकारिक माध्यम से अनुरोध सत्यापित करें।",
        "safe": "सुरक्षित",
        "suspicious": "संदिग्ध",
        "high": "उच्च जोखिम",
        "contribution": "जोखिम योगदान",
        "points": "अंक",
        "no_indicators": "कोई मजबूत घोटाला संकेत नहीं मिला।",
        "enter_call": "विश्लेषण से पहले कॉल की जानकारी दर्ज करें।",
        "enter_message": "विश्लेषण से पहले संदेश दर्ज करें।",
        "phone": "फोन नंबर",
        "score": "जोखिम स्कोर",
        "reason": "कारण",
        "download": "विश्लेषण डाउनलोड करें",
        "prototype": "हैकाथॉन प्रदर्शन के लिए प्रोटोटाइप",
        "warning": "यह एक प्रदर्शन प्रणाली है और आधिकारिक धोखाधड़ी जांच का विकल्प नहीं है।",
        "urgent": "जल्दबाजी या दबाव",
        "otp": "OTP / सत्यापन अनुरोध",
        "money": "पैसे या भुगतान का अनुरोध",
        "bank": "बैंक जानकारी का अनुरोध",
        "link": "संदिग्ध लिंक",
        "reward": "इनाम / पुरस्कार का दावा",
        "impersonation": "किसी और की पहचान का उपयोग",
        "remote": "रिमोट एक्सेस का अनुरोध",
        "new_number": "अज्ञात या असामान्य नंबर",
        "call_reason": "कॉलर ने संदिग्ध भाषा का उपयोग किया या संवेदनशील जानकारी मांगी।",
        "message_reason": "संदेश में आम घोटाला पैटर्न दिखाई देते हैं।"
    }
}

# ---------------------------------------------------------
# SCAM INDICATORS
# ---------------------------------------------------------

INDICATORS = {
    "Urgency or pressure": {
        "weight": 20,
        "keywords": [
            "urgent", "immediately", "act now", "hurry",
            "இப்போதே", "அவசரம்", "உடனே",
            "तुरंत", "अभी", "जल्दी"
        ]
    },

    "OTP / verification request": {
        "weight": 25,
        "keywords": [
            "otp", "one time password", "verification code",
            "otp சொல்லுங்கள்", "otp கூறுங்கள்",
            "ओटीपी", "वन टाइम पासवर्ड", "वेरिफिकेशन कोड"
        ]
    },

    "Money or payment request": {
        "weight": 25,
        "keywords": [
            "send money", "transfer money", "pay", "payment",
            "upi", "refund fee", "processing fee",
            "பணம் அனுப்ப", "பணம் செலுத்த", "கட்டணம்",
            "पैसे भेजें", "भुगतान", "फीस"
        ]
    },

    "Banking information request": {
        "weight": 25,
        "keywords": [
            "bank account", "account number", "card number",
            "cvv", "pin", "password",
            "வங்கி கணக்கு", "அட்டை எண்", "ரகசிய எண்",
            "बैंक खाता", "कार्ड नंबर", "पासवर्ड"
        ]
    },

    "Suspicious link": {
        "weight": 25,
        "keywords": [
            "http://", "https://", "www.", ".xyz", ".top",
            ".click", "bit.ly", "tinyurl",
            "இணைப்பை திற", "லிங்கை திற",
            "लिंक खोलें"
        ]
    },

    "Prize / reward claim": {
        "weight": 20,
        "keywords": [
            "winner", "won", "lottery", "prize", "reward",
            "cashback", "gift",
            "வெற்றி", "பரிசு", "லாட்டரி",
            "विजेता", "इनाम", "लॉटरी"
        ]
    },

    "Impersonation": {
        "weight": 25,
        "keywords": [
            "bank officer", "police", "government officer",
            "customer care", "income tax", "rbi",
            "வங்கி அதிகாரி", "போலீஸ்", "அரசு அதிகாரி",
            "बैंक अधिकारी", "पुलिस", "सरकारी अधिकारी"
        ]
    },

    "Remote access request": {
        "weight": 25,
        "keywords": [
            "anydesk", "teamviewer", "remote access",
            "screen share", "install app",
            "ஸ்கிரீன் பகிர", "ஆப் நிறுவ",
            "स्क्रीन शेयर", "ऐप इंस्टॉल"
        ]
    }
}

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>
    .risk-card {
        padding: 18px;
        border-radius: 12px;
        margin-top: 10px;
        margin-bottom: 20px;
        font-size: 22px;
        font-weight: bold;
    }

    .safe-card {
        background-color: #d9f7df;
        border-left: 8px solid #16a34a;
        color: #166534;
    }

    .suspicious-card {
        background-color: #fff1cc;
        border-left: 8px solid #f59e0b;
        color: #92400e;
    }

    .high-card {
        background-color: #ffdede;
        border-left: 8px solid #dc2626;
        color: #991b1b;
    }

    .bar-container {
        width: 100%;
        background-color: #eeeeee;
        border-radius: 8px;
        margin-bottom: 12px;
        overflow: hidden;
    }

    .bar {
        padding: 8px;
        color: white;
        font-weight: bold;
        border-radius: 8px;
    }

    .red-bar {
        background-color: #dc2626;
    }

    .orange-bar {
        background-color: #f59e0b;
    }

    .green-bar {
        background-color: #16a34a;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.sidebar.title("🛡️ ScamShield")
st.sidebar.write("Explainable AI Scam Detection")

language = st.sidebar.selectbox(
    "Language / மொழி / भाषा",
    ["English", "தமிழ்", "Hindi"]
)

T = LANG[language]

st.sidebar.markdown("---")
st.sidebar.subheader(T["about"])
st.sidebar.write(T["about_text"])

st.title(T["title"])
st.subheader(T["subtitle"])

st.info(T["warning"])

# ---------------------------------------------------------
# ANALYSIS FUNCTION
# ---------------------------------------------------------

def analyze_content(text, phone_number=""):
    text_lower = text.lower()

    found = []

    for name, data
