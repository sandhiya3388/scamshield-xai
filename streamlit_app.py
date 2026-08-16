import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="ScamShield XAI",
    page_icon="🛡️",
    layout="wide"
)

LANG = {
    "English": {
        "title": "ScamShield XAI",
        "sub": "Explainable AI Scam Detector",
        "about": "About ScamShield",
        "about_text": "ScamShield checks transaction, message, or call information for common scam indicators and explains the result.",
        "language": "Language",
        "type": "Detection type",
        "transaction": "Transaction",
        "message": "Message / SMS",
        "call": "Call",
        "amount": "Transaction amount",
        "beneficiary": "Is this a new beneficiary?",
        "link": "Does the message contain a suspicious link?",
        "unusual_time": "Is the transaction at an unusual time?",
        "failed": "Previous failed attempts",
        "text": "Paste the message or call transcript",
        "urgent": "Does it contain urgent or threatening language?",
        "unknown": "Is the caller unknown to you?",
        "analyze": "Analyze",
        "result": "Risk assessment",
        "safe": "SAFE",
        "suspicious": "SUSPICIOUS",
        "high": "HIGH RISK",
        "score": "Risk score",
        "explain": "Explainable AI",
        "why": "Why was this flagged?",
        "action": "Recommended action",
        "safe_action": "The indicators are low. Still verify important payments before proceeding.",
        "susp_action": "Verify the sender, beneficiary, and details before proceeding.",
        "high_action": "Do not proceed until the sender, beneficiary, and transaction details are independently verified.",
        "indicators": "Risk contributions",
        "none": "No strong suspicious indicators were detected.",
        "amount_reason": "The transaction amount is unusually high.",
        "beneficiary_reason": "The beneficiary is new.",
        "link_reason": "A suspicious link indicator was selected.",
        "time_reason": "The transaction is at an unusual time.",
        "failed_reason": "There were previous failed attempts.",
        "urgent_reason": "The text contains urgent or threatening language.",
        "unknown_reason": "The caller is unknown to you.",
        "chart": "Risk contribution chart",
        "report": "Download analysis report",
        "disclaimer": "Prototype for hackathon demonstration. This is not a bank or law-enforcement decision system.",
        "call_note": "For calls, paste the call transcript or describe what the caller asked you to do. This prototype does not automatically listen to phone calls.",
        "clear": "Clear / reset"
    },

    "Tamil": {
        "title": "ScamShield XAI",
        "sub": "விளக்கக்கூடிய செயற்கை நுண்ணறிவு மோசடி கண்டறிதல்",
        "about": "ScamShield பற்றி",
        "about_text": "பரிவர்த்தனை, குறுஞ்செய்தி அல்லது அழைப்பு விவரங்களில் உள்ள பொதுவான மோசடி அறிகுறிகளை கண்டறிந்து, முடிவுக்கான காரணங்களை ScamShield விளக்குகிறது.",
        "language": "மொழி",
        "type": "கண்டறிதல் வகை",
        "transaction": "பரிவர்த்தனை",
        "message": "செய்தி / குறுஞ்செய்தி",
        "call": "அழைப்பு",
        "amount": "பரிவர்த்தனை தொகை",
        "beneficiary": "இது புதிய பெறுநரா?",
        "link": "செய்தியில் சந்தேகமான இணைப்பு உள்ளதா?",
        "unusual_time": "வழக்கத்திற்கு மாறான நேரத்தில் பரிவர்த்தனை நடந்ததா?",
        "failed": "முந்தைய தோல்வியடைந்த முயற்சிகள்",
        "text": "செய்தி அல்லது அழைப்பு உரையை இங்கே ஒட்டவும்",
        "urgent": "அவசரப்படுத்தும் அல்லது மிரட்டும் சொற்கள் உள்ளனவா?",
        "unknown": "அழைப்பவர் உங்களுக்கு தெரியாதவரா?",
        "analyze": "பகுப்பாய்வு செய்",
        "result": "ஆபத்து மதிப்பீடு",
        "safe": "பாதுகாப்பானது",
        "suspicious": "சந்தேகமானது",
        "high": "அதிக ஆபத்து",
        "score": "ஆபத்து மதிப்பெண்",
        "explain": "விளக்கக்கூடிய செயற்கை நுண்ணறிவு",
        "why": "இது ஏன் எச்சரிக்கப்பட்டது?",
        "action": "பரிந்துரைக்கப்படும் நடவடிக்கை",
        "safe_action": "வலுவான சந்தேக அறிகுறிகள் குறைவாக உள்ளன. முக்கியமான பணப்பரிவர்த்தனைகளை உறுதி செய்த பிறகே தொடரவும்.",
        "susp_action": "அனுப்புநர், பெறுநர் மற்றும் விவரங்களை உறுதி செய்த பிறகே தொடரவும்.",
        "high_action": "அனுப்புநர், பெறுநர் மற்றும் பரிவர்த்தனை விவரங்களை தனியாக உறுதி செய்யும் வரை தொடர வேண்டாம்.",
        "indicators": "ஆபத்து காரணிகள்",
        "none": "வலுவான சந்தேக அறிகுறிகள் எதுவும் கண்டறியப்படவில்லை.",
        "amount_reason": "பரிவர்த்தனை தொகை வழக்கத்தை விட அதிகமாக உள்ளது.",
        "beneficiary_reason": "பெறுநர் புதியவர்.",
        "link_reason": "சந்தேகமான இணைப்பு இருப்பதாக தேர்ந்தெடுக்கப்பட்டுள்ளது.",
        "time_reason": "பரிவர்த்தனை வழக்கத்திற்கு மாறான நேரத்தில் உள்ளது.",
        "failed_reason": "முந்தைய தோல்வியடைந்த முயற்சிகள் உள்ளன.",
        "urgent_reason": "செய்தியில் அவசரப்படுத்தும் அல்லது மிரட்டும் சொற்கள் உள்ளன.",
        "unknown_reason": "அழைப்பவர் உங்களுக்கு தெரியாதவர்.",
        "chart": "ஆபத்து காரணிகளின் வரைபடம்",
        "report": "பகுப்பாய்வு அறிக்கையை பதிவிறக்கு",
        "disclaimer": "ஹேக்கத்தான் செயல்விளக்கத்திற்கான முன்மாதிரி. இது வங்கி அல்லது சட்ட அமலாக்க முடிவு அமைப்பு அல்ல.",
        "call_note": "அழைப்புகளுக்கு, அழைப்பில் பேசப்பட்ட உரையை இங்கே ஒட்டவும் அல்லது அழைப்பவர் கேட்டதை எழுதவும். இந்த முன்மாதிரி தொலைபேசி அழைப்புகளை தானாக கேட்காது.",
        "clear": "மீட்டமை"
    },

    "Hindi": {
        "title": "ScamShield XAI",
        "sub": "व्याख्यात्मक AI घोटाला पहचान प्रणाली",
        "about": "ScamShield के बारे में",
        "about_text": "ScamShield लेनदेन, संदेश या कॉल की जानकारी में सामान्य घोटाला संकेतों की जांच करता है और परिणाम का कारण बताता है।",
        "language": "भाषा",
        "type": "जांच का प्रकार",
        "transaction": "लेनदेन",
        "message": "संदेश / SMS",
        "call": "कॉल",
        "amount": "लेनदेन राशि",
        "beneficiary": "क्या यह नया प्राप्तकर्ता है?",
        "link": "क्या संदेश में संदिग्ध लिंक है?",
        "unusual_time": "क्या लेनदेन असामान्य समय पर हुआ?",
        "failed": "पिछले असफल प्रयास",
        "text": "संदेश या कॉल का विवरण यहां लिखें",
        "urgent": "क्या इसमें जल्दबाजी या धमकी वाली भाषा है?",
        "unknown": "क्या कॉल करने वाला व्यक्ति आपके लिए अनजान है?",
        "analyze": "विश्लेषण करें",
        "result": "जोखिम मूल्यांकन",
        "safe": "सुरक्षित",
        "suspicious": "संदिग्ध",
        "high": "उच्च जोखिम",
        "score": "जोखिम स्कोर",
        "explain": "व्याख्यात्मक AI",
        "why": "इसे संदिग्ध क्यों माना गया?",
        "action": "अनुशंसित कार्रवाई",
        "safe_action": "मजबूत संदिग्ध संकेत कम हैं। फिर भी महत्वपूर्ण भुगतान से पहले विवरण की पुष्टि करें।",
        "susp_action": "आगे बढ़ने से पहले भेजने वाले, प्राप्तकर्ता और विवरण की पुष्टि करें।",
        "high_action": "स्वतंत्र रूप से पुष्टि किए बिना आगे न बढ़ें।",
        "indicators": "जोखिम के कारण",
        "none": "कोई मजबूत संदिग्ध संकेत नहीं मिला।",
        "amount_reason": "लेनदेन राशि सामान्य से अधिक है।",
        "beneficiary_reason": "प्राप्तकर्ता नया है।",
        "link_reason": "संदिग्ध लिंक का संकेत चुना गया है।",
        "time_reason": "लेनदेन असामान्य समय पर है।",
        "failed_reason": "पिछले असफल प्रयास हुए हैं।",
        "urgent_reason": "संदेश में जल्दबाजी या धमकी वाली भाषा है।",
        "unknown_reason": "कॉल करने वाला व्यक्ति अनजान है।",
        "chart": "जोखिम योगदान चार्ट",
        "report": "विश्लेषण रिपोर्ट डाउनलोड करें",
        "disclaimer": "हैकथॉन प्रदर्शन के लिए प्रोटोटाइप। यह बैंक या कानून प्रवर्तन निर्णय प्रणाली नहीं है।",
        "call_note": "कॉल के लिए, बातचीत का विवरण यहां लिखें। यह प्रोटोटाइप फोन कॉल को अपने आप नहीं सुनता।",
        "clear": "रीसेट"
    }
}


def get_level(score):
    if score >= 70:
        return "high"
    if score >= 35:
        return "suspicious"
    return "safe"


def make_bar(label, points, max_points):
    width = int((points / max_points) * 100)

    if width < 5:
        width = 5

    if points >= 25:
        fill = "#d32f2f"
    elif points >= 10:
        fill = "#f9a825"
    else:
        fill = "#2e7d32"

    st.markdown(
        f'<div style="margin:8px 0;">'
        f'<div style="display:flex;justify-content:space-between;">'
        f'<span>{label}</span><b>{points} points</b></div>'
        f'<div style="background:#e8e8e8;border-radius:8px;height:14px;">'
        f'<div style="background:{fill};width:{width}%;height:14px;border-radius:8px;"></div>'
        f'</div></div>',
        unsafe_allow_html=True
    )


with st.sidebar:
    st.header("ScamShield")

    language = st.selectbox(
        "Language / மொழி / भाषा",
        list(LANG.keys())
    )

    t = LANG[language]

    st.markdown("---")
    st.subheader(t["about"])
    st.write(t["about_text"])


t = LANG[language]

st.title("🛡️ " + t["title"])
st.subheader(t["sub"])


detection_type = st.radio(
    t["type"],
    [
        t["transaction"],
        t["message"],
        t["call"]
    ],
    horizontal=True
)


if detection_type == t["transaction"]:
    st.info(
        "Enter the transaction details and select any warning signs."
    )

elif detection_type == t["message"]:
    st.info(
        "Paste the message below. The prototype checks common scam indicators."
    )

else:
    st.info(t["call_note"])


amount = 0.0
new_beneficiary = False
suspicious_link = False
unusual_time = False
failed_attempts = 0
urgent_language = False
unknown_caller = False
text = ""


if detection_type == t["transaction"]:

    col1, col2 = st.columns(2)

    with col1:
        amount = st.number_input(
            t["amount"],
            min_value=0.0,
            value=1000.0,
            step=500.0
        )

        new_beneficiary = st.checkbox(
            t["beneficiary"]
        )

        unusual_time = st.checkbox(
            t["unusual_time"]
        )

    with col2:
        failed_attempts = st.number_input(
            t["failed"],
            min_value=0,
            max_value=20,
            value=0,
            step=1
        )

        suspicious_link = st.checkbox(
            t["link"]
        )

        urgent_language = st.checkbox(
            t["urgent"]
        )

else:

    text = st.text_area(
        t["text"],
        height=180
    )

    col1, col2 = st.columns(2)

    with col1:
        suspicious_link = st.checkbox(
            t["link"]
        )

        urgent_language = st.checkbox(
            t["urgent"]
        )

    with col2:

        if detection_type == t["call"]:
            unknown_caller = st.checkbox(
                t["unknown"]
            )

        unusual_time = st.checkbox(
            t["unusual_time"]
        )


analyze = st.button(
    t["analyze"],
    type="primary",
    use_container_width=True
)


if analyze:

    score = 0
    contributions = []

    if amount >= 50000:
        score += 30
        contributions.append(
            (t["amount_reason"], 30)
        )

    elif amount >= 10000:
        score += 15
        contributions.append(
            (t["amount_reason"], 15)
        )

    if new_beneficiary:
        score += 25
        contributions.append(
            (t["beneficiary_reason"], 25)
        )

    if suspicious_link:
        score += 30
        contributions.append(
            (t["link_reason"], 30)
        )

    if unusual_time:
        score += 10
        contributions.append(
            (t["time_reason"], 10)
        )

    if failed_attempts > 0:
        points = min(
            failed_attempts * 5,
            15
        )

        score += points

        contributions.append(
            (t["failed_reason"], points)
        )

    if urgent_language:
        score += 20

        contributions.append(
            (t["urgent_reason"], 20)
        )

    if unknown_caller:
        score += 20

        contributions.append(
            (t["unknown_reason"], 20)
        )


    lower_text = text.lower()

    scam_words = [
        "otp",
        "password",
