import streamlit as st
import pandas as pd

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="ScamShield XAI",
    page_icon="🛡️",
    layout="wide"
)

# =========================================================
# LANGUAGE DATA
# =========================================================

LANGUAGES = {
    "English": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "Explainable AI Scam Detection System",

        "mode": "Detection Mode",
        "transaction": "💳 Transaction",
        "message": "💬 Message",
        "call": "📞 Call",

        "amount": "Transaction Amount",
        "new": "New Beneficiary",
        "failed": "Previous Failed Attempts",
        "unusual": "Unusual Transaction Time",
        "link": "Suspicious Link",

        "analyze": "🔍 Analyze",
        "reset": "🔄 Reset",

        "risk": "Risk Score",
        "factors": "Number of Risk Factors",
        "chart": "📊 Risk Contribution Chart",

        "ai": "🤖 Explainable AI",
        "why": "🔎 Why Was This Transaction Flagged?",
        "action": "🛡️ Recommended Action",
        "pipeline": "🧠 Explainable AI Pipeline",

        "safe": "SAFE",
        "suspicious": "SUSPICIOUS",
        "high": "HIGH RISK",

        "safe_action": "The transaction appears relatively safe. Continue to stay alert.",
        "suspicious_action": "Verify the beneficiary and transaction details before proceeding.",
        "high_action": "Do not proceed until the transaction is verified through an official channel.",

        "message_input": "Paste the message here",
        "call_input": "Paste the call transcript here",

        "empty": "Please enter some information first.",

        "amount_high": "High transaction amount",
        "amount_medium": "Higher-than-normal transaction amount",
        "new_factor": "New beneficiary",
        "failed_factor": "Previous failed attempts",
        "unusual_factor": "Unusual transaction time",
        "link_factor": "Suspicious link",

        "otp_factor": "OTP / verification code request",
        "urgent_factor": "Urgent or threatening language",
        "remote_factor": "Remote access request",
        "bank_factor": "Possible bank impersonation",
        "prize_factor": "Prize / reward claim",
        "external_factor": "External link detected",

        "footer": "Hackathon prototype — Explainable AI based scam detection."
    },

    "Tamil": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "விளக்கக்கூடிய AI மோசடி கண்டறிதல் அமைப்பு",

        "mode": "கண்டறிதல் வகை",
        "transaction": "💳 பரிவர்த்தனை",
        "message": "💬 குறுஞ்செய்தி",
        "call": "📞 அழைப்பு",

        "amount": "பரிவர்த்தனை தொகை",
        "new": "புதிய பயனாளி",
        "failed": "முந்தைய தோல்வியடைந்த முயற்சிகள்",
        "unusual": "வழக்கத்திற்கு மாறான நேரம்",
        "link": "சந்தேகமான இணைப்பு",

        "analyze": "🔍 ஆய்வு செய்",
        "reset": "🔄 மீட்டமை",

        "risk": "ஆபத்து மதிப்பெண்",
        "factors": "ஆபத்து காரணிகளின் எண்ணிக்கை",
        "chart": "📊 ஆபத்து காரணிகளின் பங்களிப்பு",

        "ai": "🤖 விளக்கக்கூடிய AI",
        "why": "🔎 இந்த பரிவர்த்தனை ஏன் Flag செய்யப்பட்டது?",
        "action": "🛡️ பரிந்துரைக்கப்படும் நடவடிக்கை",
        "pipeline": "🧠 விளக்கக்கூடிய AI செயல்முறை",

        "safe": "பாதுகாப்பானது",
        "suspicious": "சந்தேகத்திற்கிடமானது",
        "high": "அதிக ஆபத்து",

        "safe_action": "இந்த பரிவர்த்தனை ஒப்பீட்டளவில் பாதுகாப்பாக உள்ளது. இருப்பினும் கவனமாக இருங்கள்.",
        "suspicious_action": "தொடர்வதற்கு முன் பயனாளி மற்றும் பரிவர்த்தனை விவரங்களைச் சரிபார்க்கவும்.",
        "high_action": "அதிகாரப்பூர்வ வழியில் சரிபார்க்கும் வரை பரிவர்த்தனையைத் தொடர வேண்டாம்.",

        "message_input": "குறுஞ்செய்தியை இங்கே உள்ளிடவும்",
        "call_input": "அழைப்பு உரையை இங்கே உள்ளிடவும்",

        "empty": "முதலில் தகவலை உள்ளிடவும்.",

        "amount_high": "அதிக பரிவர்த்தனை தொகை",
        "amount_medium": "வழக்கத்தை விட அதிகமான தொகை",
        "new_factor": "புதிய பயனாளி",
        "failed_factor": "முந்தைய தோல்வியடைந்த முயற்சிகள்",
        "unusual_factor": "வழக்கத்திற்கு மாறான பரிவர்த்தனை நேரம்",
        "link_factor": "சந்தேகமான இணைப்பு",

        "otp_factor": "OTP / சரிபார்ப்பு குறியீடு கேட்கப்பட்டது",
        "urgent_factor": "அவசரப்படுத்தும் அல்லது மிரட்டும் மொழி",
        "remote_factor": "தொலைநிலை அணுகல் கேட்கப்பட்டது",
        "bank_factor": "வங்கி போல ஆள்மாறாட்டம் இருக்கலாம்",
        "prize_factor": "பரிசு / வெகுமதி மோசடி இருக்கலாம்",
        "external_factor": "வெளிப்புற இணைப்பு கண்டறியப்பட்டது",

        "footer": "ஹேக்கத்தான் முன்மாதிரி — விளக்கக்கூடிய AI அடிப்படையிலான மோசடி கண்டறிதல்."
    },

    "Hindi": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "व्याख्यात्मक AI घोटाला पहचान प्रणाली",

        "mode": "पहचान मोड",
        "transaction": "💳 लेनदेन",
        "message": "💬 संदेश",
        "call": "📞 कॉल",

        "amount": "लेनदेन राशि",
        "new": "नया लाभार्थी",
        "failed": "पिछले असफल प्रयास",
        "unusual": "असामान्य लेनदेन समय",
        "link": "संदिग्ध लिंक",

        "analyze": "🔍 विश्लेषण करें",
        "reset": "🔄 रीसेट",

        "risk": "जोखिम स्कोर",
        "factors": "जोखिम कारकों की संख्या",
        "chart": "📊 जोखिम योगदान चार्ट",

        "ai": "🤖 व्याख्यात्मक AI",
        "why": "🔎 इस लेनदेन को क्यों Flag किया गया?",
        "action": "🛡️ अनुशंसित कार्रवाई",
        "pipeline": "🧠 व्याख्यात्मक AI प्रक्रिया",

        "safe": "सुरक्षित",
        "suspicious": "संदिग्ध",
        "high": "उच्च जोखिम",

        "safe_action": "लेनदेन अपेक्षाकृत सुरक्षित दिखाई देता है। फिर भी सावधान रहें।",
        "suspicious_action": "आगे बढ़ने से पहले लाभार्थी और लेनदेन की जानकारी सत्यापित करें।",
        "high_action": "आधिकारिक माध्यम से सत्यापन होने तक आगे न बढ़ें।",

        "message_input": "संदेश यहां दर्ज करें",
        "call_input": "कॉल का टेक्स्ट यहां दर्ज करें",

        "empty": "कृपया पहले जानकारी दर्ज करें।",

        "amount_high": "बहुत अधिक लेनदेन राशि",
        "amount_medium": "सामान्य से अधिक लेनदेन राशि",
        "new_factor": "नया लाभार्थी",
        "failed_factor": "पिछले असफल प्रयास",
        "unusual_factor": "असामान्य लेनदेन समय",
        "link_factor": "संदिग्ध लिंक",

        "otp_factor": "OTP / सत्यापन कोड का अनुरोध",
        "urgent_factor": "तत्काल या धमकी भरी भाषा",
        "remote_factor": "रिमोट एक्सेस का अनुरोध",
        "bank_factor": "संभावित बैंक प्रतिरूपण",
        "prize_factor": "इनाम / पुरस्कार का दावा",
        "external_factor": "बाहरी लिंक मिला",

        "footer": "हैकथॉन प्रोटोटाइप — व्याख्यात्मक AI आधारित घोटाला पहचान।"
    },

    "Telugu": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "వివరణాత్మక AI మోసం గుర్తింపు వ్యవస్థ",

        "mode": "గుర్తింపు విధానం",
        "transaction": "💳 లావాదేవీ",
        "message": "💬 సందేశం",
        "call": "📞 కాల్",

        "amount": "లావాదేవీ మొత్తం",
        "new": "కొత్త లబ్ధిదారు",
        "failed": "మునుపటి విఫల ప్రయత్నాలు",
        "unusual": "అసాధారణ లావాదేవీ సమయం",
        "link": "అనుమానాస్పద లింక్",

        "analyze": "🔍 విశ్లేషించండి",
        "reset": "🔄 రీసెట్",

        "risk": "ప్రమాద స్కోర్",
        "factors": "ప్రమాద కారకాల సంఖ్య",
        "chart": "📊 ప్రమాద సహకార చార్ట్",

        "ai": "🤖 వివరణాత్మక AI",
        "why": "🔎 ఈ లావాదేవీని ఎందుకు Flag చేశారు?",
        "action": "🛡️ సిఫార్సు చేసిన చర్య",
        "pipeline": "🧠 వివరణాత్మక AI ప్రక్రియ",

        "safe": "సురక్షితం",
        "suspicious": "అనుమానాస్పదం",
        "high": "అధిక ప్రమాదం",

        "safe_action": "లావాదేవీ సాపేక్షంగా సురక్షితంగా కనిపిస్తోంది. అయినా జాగ్రత్తగా ఉండండి.",
        "suspicious_action": "కొనసాగించే ముందు లబ్ధిదారు మరియు వివరాలను ధృవీకరించండి.",
        "high_action": "అధికారికంగా ధృవీకరించే వరకు కొనసాగవద్దు.",

        "message_input": "సందేశాన్ని ఇక్కడ నమోదు చేయండి",
        "call_input": "కాల్ టెక్స్ట్‌ను ఇక్కడ నమోదు చేయండి",

        "empty": "దయచేసి ముందుగా సమాచారాన్ని నమోదు చేయండి.",

        "amount_high": "అధిక లావాదేవీ మొత్తం",
        "amount_medium": "సాధారణం కంటే ఎక్కువ మొత్తం",
        "new_factor": "కొత్త లబ్ధిదారు",
        "failed_factor": "మునుపటి విఫల ప్రయత్నాలు",
        "unusual_factor": "అసాధారణ లావాదేవీ సమయం",
        "link_factor": "అనుమానాస్పద లింక్",

        "otp_factor": "OTP / ధృవీకరణ కోడ్ అభ్యర్థన",
        "urgent_factor": "అత్యవసర లేదా బెదిరింపు భాష",
        "remote_factor": "రిమోట్ యాక్సెస్ అభ్యర్థన",
        "bank_factor": "బ్యాంక్ వలె నటించే అవకాశం",
        "prize_factor": "బహుమతి / రివార్డ్ క్లెయిమ్",
        "external_factor": "బాహ్య లింక్ కనుగొనబడింది",

        "footer": "హ్యాకథాన్ ప్రోటోటైప్ — వివరణాత్మక AI ఆధారిత మోసం గుర్తింపు."
    },

    "Malayalam": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "Explainable AI തട്ടിപ്പ് കണ്ടെത്തൽ സംവിധാനം",

        "mode": "കണ്ടെത്തൽ മോഡ്",
        "transaction": "💳 ഇടപാട്",
        "message": "💬 സന്ദേശം",
        "call": "📞 കോൾ",

        "amount": "ഇടപാട് തുക",
        "new": "പുതിയ ഗുണഭോക്താവ്",
        "failed": "മുമ്പത്തെ പരാജയപ്പെട്ട ശ്രമങ്ങൾ",
        "unusual": "അസാധാരണ ഇടപാട് സമയം",
        "link": "സംശയാസ്പദമായ ലിങ്ക്",

        "analyze": "🔍 പരിശോധിക്കുക",
        "reset": "🔄 റീസെറ്റ്",

        "risk": "റിസ്ക് സ്കോർ",
        "factors": "റിസ്ക് ഘടകങ്ങളുടെ എണ്ണം",
        "chart": "📊 റിസ്ക് കോൺട്രിബ്യൂഷൻ ചാർട്ട്",

        "ai": "🤖 Explainable AI",
        "why": "🔎 ഈ ഇടപാട് Flag ചെയ്തത് എന്തുകൊണ്ട്?",
        "action": "🛡️ ശുപാർശ ചെയ്യുന്ന നടപടി",
        "pipeline": "🧠 Explainable AI പ്രക്രിയ",

        "safe": "സുരക്ഷിതം",
        "suspicious": "സംശയാസ്പദം",
        "high": "ഉയർന്ന റിസ്ക്",

        "safe_action": "ഇടപാട് താരതമ്യേന സുരക്ഷിതമാണ്. എന്നിരുന്നാലും ജാഗ്രത പാലിക്കുക.",
        "suspicious_action": "തുടരുന്നതിന് മുമ്പ് ഗുണഭോക്താവിനെയും വിവരങ്ങളെയും പരിശോധിക്കുക.",
        "high_action": "ഔദ്യോഗികമായി പരിശോധിക്കുന്നതുവരെ തുടരരുത്.",

        "message_input": "സന്ദേശം ഇവിടെ നൽകുക",
        "call_input": "കോൾ ടെക്സ്റ്റ് ഇവിടെ നൽകുക",

        "empty": "ദയവായി ആദ്യം വിവരങ്ങൾ നൽകുക.",

        "amount_high": "വളരെ ഉയർന്ന ഇടപാട് തുക",
        "amount_medium": "സാധാരണയേക്കാൾ ഉയർന്ന തുക",
        "new_factor": "പുതിയ ഗുണഭോക്താവ്",
        "failed_factor": "മുമ്പത്തെ പരാജയപ്പെട്ട ശ്രമങ്ങൾ",
        "unusual_factor": "അസാധാരണ ഇടപാട് സമയം",
        "link_factor": "സംശയാസ്പദമായ ലിങ്ക്",

        "otp_factor": "OTP / verification code ആവശ്യപ്പെട്ടു",
        "urgent_factor": "അടിയന്തരമായ അല്ലെങ്കിൽ ഭീഷണിപ്പെടുത്തുന്ന ഭാഷ",
        "remote_factor": "Remote access ആവശ്യപ്പെട്ടു",
        "bank_factor": "ബാങ്ക് ആയി നടിക്കുന്നതായി തോന്നുന്നു",
        "prize_factor": "സമ്മാനം / റിവാർഡ് അവകാശവാദം",
        "external_factor": "External link കണ്ടെത്തി",

        "footer": "Hackathon prototype — Explainable AI അടിസ്ഥാനമാക്കിയുള്ള തട്ടിപ്പ് കണ്ടെത്തൽ."
    },

    "Kannada": {
        "title": "🛡️ ScamShield XAI",
        "subtitle": "ವಿವರಣಾತ್ಮಕ AI ಮೋಸ ಪತ್ತೆ ವ್ಯವಸ್ಥೆ",

        "mode": "ಪತ್ತೆ ಮೋಡ್",
        "transaction": "💳 ವಹಿವಾಟು",
        "message": "💬 ಸಂದೇಶ",
        "call": "📞 ಕರೆ",

        "amount": "ವಹಿವಾಟಿನ ಮೊತ್ತ",
        "new": "ಹೊಸ ಫಲಾನುಭವಿ",
        "failed": "ಹಿಂದಿನ ವಿಫಲ ಪ್ರಯತ್ನಗಳು",
        "unusual": "ಅಸಾಮಾನ್ಯ ವಹಿವಾಟು ಸಮಯ",
        "link": "ಅನುಮಾನಾಸ್ಪದ ಲಿಂಕ್",

        "analyze": "🔍 ವಿಶ್ಲೇಷಿಸಿ",
        "reset": "🔄 ಮರುಹೊಂದಿಸಿ",

        "risk": "ಅಪಾಯ ಸ್ಕೋರ್",
        "factors": "ಅಪಾಯದ ಅಂಶಗಳ ಸಂಖ್ಯೆ",
        "chart": "📊 ಅಪಾಯ ಕೊಡುಗೆ ಚಾರ್ಟ್",

        "ai": "🤖 Explainable AI",
        "why": "🔎 ಈ ವಹಿವಾಟನ್ನು Flag ಮಾಡಿದ್ದು ಏಕೆ?",
        "action": "🛡️ ಶಿಫಾರಸು ಮಾಡಿದ ಕ್ರಮ",
        "pipeline": "🧠 Explainable AI ಪ್ರಕ್ರಿಯೆ",

        "safe": "ಸುರಕ್ಷಿತ",
        "suspicious": "ಅನುಮಾನಾಸ್ಪದ",
        "high": "ಹೆಚ್ಚಿನ ಅಪಾಯ",

        "safe_action": "ವಹಿವಾಟು ತುಲನಾತ್ಮಕವಾಗಿ ಸುರಕ್ಷಿತವಾಗಿದೆ. ಆದರೂ ಜಾಗರೂಕರಾಗಿರಿ.",
        "suspicious_action": "ಮುಂದುವರಿಯುವ ಮೊದಲು ಫಲಾನುಭವಿ ಮತ್ತು ವಿವರಗಳನ್ನು ಪರಿಶೀಲಿಸಿ.",
        "high_action": "ಅಧಿಕೃತವಾಗಿ ಪರಿಶೀಲಿಸುವವರೆಗೆ ಮುಂದುವರಿಯಬೇಡಿ.",

        "message_input": "ಸಂದೇಶವನ್ನು ಇಲ್ಲಿ ನಮೂದಿಸಿ",
        "call_input": "ಕರೆ ಪಠ್ಯವನ್ನು ಇಲ್ಲಿ ನಮೂದಿಸಿ",

        "empty": "ದಯವಿಟ್ಟು ಮೊದಲು ಮಾಹಿತಿಯನ್ನು ನಮೂದಿಸಿ.",

        "amount_high": "ಹೆಚ್ಚಿನ ವಹಿವಾಟಿನ ಮೊತ್ತ",
        "amount_medium": "ಸಾಮಾನ್ಯಕ್ಕಿಂತ ಹೆಚ್ಚಿನ ಮೊತ್ತ",
        "new_factor": "ಹೊಸ ಫಲಾನುಭವಿ",
        "failed_factor": "ಹಿಂದಿನ ವಿಫಲ ಪ್ರಯತ್ನಗಳು",
        "unusual_factor": "ಅಸಾಮಾನ್ಯ ವಹಿವಾಟು ಸಮಯ",
        "link_factor": "ಅನುಮಾನಾಸ್ಪದ ಲಿಂಕ್",

        "otp_factor": "OTP / ಪರಿಶೀಲನಾ ಕೋಡ್ ವಿನಂತಿ",
        "urgent_factor": "ತುರ್ತು ಅಥವಾ ಬೆದರಿಕೆಯ ಭಾಷೆ",
        "remote_factor": "ರಿಮೋಟ್ ಪ್ರವೇಶ ವಿನಂತಿ",
        "bank_factor": "ಬ್ಯಾಂಕ್‌ನಂತೆ ನಟಿಸುವ ಸಾಧ್ಯತೆ",
        "prize_factor": "ಬಹುಮಾನ / ರಿವಾರ್ಡ್ ಹೇಳಿಕೆ",
        "external_factor": "ಬಾಹ್ಯ ಲಿಂಕ್ ಕಂಡುಬಂದಿದೆ",

        "footer": "Hackathon prototype — Explainable AI ಆಧಾರಿತ ಮೋಸ ಪತ್ತೆ."
    }
}

# =========================================================
# SCAM ANALYSIS
# =========================================================

def analyze_transaction(amount, new_beneficiary, failed, unusual, link, t):

    factors = []

    if amount >= 50000:
        factors.append((t["amount_high"], 30))

    elif amount >= 20000:
        factors.append((t["amount_medium"], 20))

    if new_beneficiary:
        factors.append((t["new_factor"], 25))

    if failed >= 2:
        factors.append((t["failed_factor"], 15))

    elif failed == 1:
        factors.append((t["failed_factor"], 5))

    if unusual:
        factors.append((t["unusual_factor"], 10))

    if link:
        factors.append((t["link_factor"], 30))

    return factors


def analyze_text(text, t):

    text = text.lower()
    factors = []

    otp_words = [
        "otp",
        "pin",
        "password",
        "verification code",
        "சரிபார்ப்பு குறியீடு"
    ]

    urgent_words = [
        "urgent",
        "immediately",
        "now",
        "blocked",
        "arrest",
        "police",
        "உடனே",
        "இப்போதே",
        "மிரட்டல்"
    ]

    remote_words = [
        "anydesk",
        "teamviewer",
        "remote access",
        "screen share"
    ]

    bank_words = [
        "bank",
        "kyc",
        "account blocked",
        "வங்கி",
        "கணக்கு"
    ]

    prize_words = [
        "winner",
        "prize",
        "reward",
        "lottery",
        "பரிசு",
        "வெற்றி"
    ]

    if any(word in text for word in otp_words):
        factors.append((t["otp_factor"], 25))

    if any(word in text for word in urgent_words):
        factors.append((t["urgent_factor"], 20))

    if any(word in text for word in remote_words):
        factors.append((t["remote_factor"], 30))

    if any(word in text for word in bank_words):
        factors.append((t["bank_factor"], 15))

    if any(word in text for word in prize_words):
        factors.append((t["prize_factor"], 20))

    if (
        "http://" in text
        or "https://" in text
        or "bit.ly" in text
        or "tinyurl" in text
    ):
        factors.append((t["external_factor"], 30))

    return factors


# =========================================================
# RESULT DISPLAY
# =========================================================

def display_result(factors, t):

    if not factors:
        factors = [("No major risk factor detected", 0)]
