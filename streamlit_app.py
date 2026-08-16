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
# LANGUAGES
# =========================================================

languages = {
    "English 🇬🇧": "en",
    "தமிழ் 🇮🇳": "ta",
    "हिन्दी 🇮🇳": "hi",
    "తెలుగు 🇮🇳": "te",
    "മലയാളം 🇮🇳": "ml"
}

selected_language = st.sidebar.selectbox(
    "🌐 Language",
    list(languages.keys())
)

lang = languages[selected_language]

# =========================================================
# TRANSLATIONS
# =========================================================

T = {

"en": {
"title":"🛡️ ScamShield AI",
"subtitle":"Explainable AI Scam Detection",
"intro":"Detect suspicious calls, messages and financial transactions — and understand WHY they are suspicious.",
"home":"🏠 Home",
"call":"📞 Call Detection",
"message":"💬 Message Detection",
"transaction":"💳 Transaction Detection",
"phone":"Phone Number",
"call_text":"What did the caller say?",
"otp":"Did the caller ask for OTP/PIN/password?",
"urgency":"Did the caller create urgency or threaten you?",
"unknown":"Is the caller unknown to you?",
"message_text":"Paste the message here",
"link":"Does the message contain a link?",
"money":"Does it ask for money/payment?",
"personal":"Does it ask for personal or banking information?",
"amount":"Transaction Amount (₹)",
"usual":"Usual Transaction Amount (₹)",
"beneficiary":"Is this a new beneficiary?",
"time":"Transaction Time",
"failed":"Previous failed attempts",
"yes":"Yes",
"no":"No",
"analyze_call":"🔍 ANALYZE CALL",
"analyze_message":"🔍 ANALYZE MESSAGE",
"analyze_transaction":"🔍 ANALYZE TRANSACTION",
"risk":"🚨 Risk Assessment",
"score":"Risk Score",
"reasons":"🤖 Why is this suspicious?",
"contribution":"📊 Risk Contribution",
"action":"🛡️ Recommended Action",
"history":"🕘 Recent Analysis",
"download":"📥 Download Report",
"safe":"🟢 LOW RISK",
"suspicious":"🟠 SUSPICIOUS",
"high":"🔴 HIGH RISK",
"hold":"Do not proceed until verified.",
"verify":"Verify the caller/message through an official source.",
"proceed":"No major suspicious indicators detected.",
"no_reason":"No major suspicious indicators were detected.",
"factor":"Factor",
"points":"Risk Points",
"welcome":"Select a detection method from the sidebar."
},

"ta": {
"title":"🛡️ ScamShield AI",
"subtitle":"விளக்கக்கூடிய AI மோசடி கண்டறிதல்",
"intro":"சந்தேகத்திற்குரிய அழைப்புகள், குறுஞ்செய்திகள் மற்றும் பணப் பரிவர்த்தனைகளைக் கண்டறிந்து, அவை ஏன் சந்தேகத்திற்குரியவை என்பதை விளக்குகிறது.",
"home":"🏠 முகப்பு",
"call":"📞 அழைப்பு கண்டறிதல்",
"message":"💬 குறுஞ்செய்தி கண்டறிதல்",
"transaction":"💳 பணப் பரிவர்த்தனை கண்டறிதல்",
"phone":"தொலைபேசி எண்",
"call_text":"அழைப்பாளர் என்ன கூறினார்?",
"otp":"OTP / PIN / கடவுச்சொல் கேட்டாரா?",
"urgency":"அவசரப்படுத்தினாரா அல்லது அச்சுறுத்தினாரா?",
"unknown":"அழைப்பாளர் உங்களுக்கு தெரியாதவரா?",
"message_text":"குறுஞ்செய்தியை இங்கே உள்ளிடவும்",
"link":"குறுஞ்செய்தியில் இணைப்பு உள்ளதா?",
"money":"பணம் செலுத்துமாறு கேட்கிறதா?",
"personal":"தனிப்பட்ட அல்லது வங்கி தகவல்களை கேட்கிறதா?",
"amount":"பரிவர்த்தனைத் தொகை (₹)",
"usual":"வழக்கமான பரிவர்த்தனைத் தொகை (₹)",
"beneficiary":"புதிய பணம் பெறுபவரா?",
"time":"பரிவர்த்தனை நேரம்",
"failed":"முந்தைய தோல்வியடைந்த முயற்சிகள்",
"yes":"ஆம்",
"no":"இல்லை",
"analyze_call":"🔍 அழைப்பை ஆய்வு செய்க",
"analyze_message":"🔍 குறுஞ்செய்தியை ஆய்வு செய்க",
"analyze_transaction":"🔍 பரிவர்த்தனையை ஆய்வு செய்க",
"risk":"🚨 ஆபத்து மதிப்பீடு",
"score":"ஆபத்து மதிப்பெண்",
"reasons":"🤖 இது ஏன் சந்தேகத்திற்குரியது?",
"contribution":"📊 ஆபத்திற்கான பங்களிப்பு",
"action":"🛡️ பரிந்துரைக்கப்படும் நடவடிக்கை",
"history":"🕘 சமீபத்திய ஆய்வுகள்",
"download":"📥 அறிக்கையைப் பதிவிறக்குக",
"safe":"🟢 குறைந்த ஆபத்து",
"suspicious":"🟠 சந்தேகத்திற்குரியது",
"high":"🔴 அதிக ஆபத்து",
"hold":"சரிபார்க்கும் வரை தொடர வேண்டாம்.",
"verify":"அதிகாரப்பூர்வ வழியின் மூலம் சரிபார்க்கவும்.",
"proceed":"முக்கியமான சந்தேகக் காரணிகள் எதுவும் கண்டறியப்படவில்லை.",
"no_reason":"முக்கியமான சந்தேகக் காரணிகள் எதுவும் கண்டறியப்படவில்லை.",
"factor":"காரணி",
"points":"ஆபத்து புள்ளிகள்",
"welcome":"இடது பக்கத்தில் இருந்து ஒரு கண்டறிதல் முறையைத் தேர்ந்தெடுக்கவும்."
},

"hi": {
"title":"🛡️ ScamShield AI",
"subtitle":"Explainable AI Scam Detection",
"intro":"संदिग्ध कॉल, संदेश और वित्तीय लेनदेन का पता लगाएं और समझें कि वे संदिग्ध क्यों हैं।",
"home":"🏠 होम",
"call":"📞 कॉल डिटेक्शन",
"message":"💬 संदेश डिटेक्शन",
"transaction":"💳 लेनदेन डिटेक्शन",
"phone":"फोन नंबर",
"call_text":"कॉलर ने क्या कहा?",
"otp":"क्या कॉलर ने OTP / PIN / पासवर्ड मांगा?",
"urgency":"क्या कॉलर ने जल्दी करने या धमकी देने की कोशिश की?",
"unknown":"क्या कॉलर आपके लिए अज्ञात है?",
"message_text":"संदेश यहां डालें",
"link":"क्या संदेश में कोई लिंक है?",
"money":"क्या संदेश पैसे मांगता है?",
"personal":"क्या व्यक्तिगत या बैंकिंग जानकारी मांगी गई है?",
"amount":"लेनदेन राशि (₹)",
"usual":"सामान्य लेनदेन राशि (₹)",
"beneficiary":"क्या यह नया लाभार्थी है?",
"time":"लेनदेन का समय",
"failed":"पिछले असफल प्रयास",
"yes":"हाँ",
"no":"नहीं",
"analyze_call":"🔍 कॉल ANALYZE करें",
"analyze_message":"🔍 संदेश ANALYZE करें",
"analyze_transaction":"🔍 लेनदेन ANALYZE करें",
"risk":"🚨 Risk Assessment",
"score":"Risk Score",
"reasons":"🤖 यह संदिग्ध क्यों है?",
"contribution":"📊 Risk Contribution",
"action":"🛡️ Recommended Action",
"history":"🕘 Recent Analysis",
"download":"📥
