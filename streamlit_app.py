import re
import math
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# -----------------------------------------------------------------------
# PAGE CONFIG
# -----------------------------------------------------------------------
st.set_page_config(
    page_title="Scam & Fraud Detection Dashboard",
    page_icon="🛡️",
    layout="wide",
)

# -----------------------------------------------------------------------
# GLOBAL STYLES
# -----------------------------------------------------------------------
st.markdown(
    """
    <style>
    .big-risk-high {
        background-color:#ffe3e3; color:#b30000; padding:16px;
        border-radius:12px; font-size:24px; font-weight:800; text-align:center;
        border:2px solid #ff4d4d;
    }
    .big-risk-medium {
        background-color:#fff6da; color:#8a6100; padding:16px;
        border-radius:12px; font-size:24px; font-weight:800; text-align:center;
        border:2px solid #ffcc00;
    }
    .big-risk-low {
        background-color:#e2fbe6; color:#0a6b1e; padding:16px;
        border-radius:12px; font-size:24px; font-weight:800; text-align:center;
        border:2px solid #2ecc71;
    }
    .factor-card {
        background-color:#f7f8fa; border-radius:10px; padding:10px 14px;
        margin-bottom:8px; border-left:5px solid #ff6b6b;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------------------
# HELPER: risk banner + gauge
# -----------------------------------------------------------------------
def risk_band(score: float):
    if score >= 70:
        return "HIGH RISK", "big-risk-high", "🚨"
    elif score >= 35:
        return "MEDIUM RISK", "big-risk-medium", "⚠️"
    else:
        return "LOW RISK", "big-risk-low", "✅"


def render_header(score: float):
    label, css_class, emoji = risk_band(score)
    st.markdown(
        f'<div class="{css_class}">{emoji} {label} &nbsp;|&nbsp; Risk Score: {score:.0f} / 100</div>',
        unsafe_allow_html=True,
    )


def render_gauge(score: float):
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            number={"suffix": " /100"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "#2c3e50"},
                "steps": [
                    {"range": [0, 35], "color": "#d4f7dc"},
                    {"range": [35, 70], "color": "#fff3cd"},
                    {"range": [70, 100], "color": "#ffd6d6"},
                ],
                "threshold": {
                    "line": {"color": "red", "width": 4},
                    "thickness": 0.8,
                    "value": score,
                },
            },
        )
    )
    fig.update_layout(height=260, margin=dict(l=10, r=10, t=10, b=10))
    st.plotly_chart(fig, use_container_width=True)


def render_contribution_chart(contributions: dict):
    df = pd.DataFrame(
        {"Factor": list(contributions.keys()), "Contribution": list(contributions.values())}
    )
    df = df[df["Contribution"] > 0].sort_values("Contribution", ascending=True)
    if df.empty:
        st.info("No significant risk factors contributed to this score.")
        return
    fig = px.bar(
        df,
        x="Contribution",
        y="Factor",
        orientation="h",
        color="Contribution",
        color_continuous_scale=["#f1c40f", "#e67e22", "#e74c3c"],
        text="Contribution",
    )
    fig.update_traces(texttemplate="%{text:.1f}", textposition="outside")
    fig.update_layout(height=380, showlegend=False, margin=dict(l=10, r=10, t=30, b=10))
    st.plotly_chart(fig, use_container_width=True)


def render_factor_explanations(explanations: dict):
    for factor, text in explanations.items():
        st.markdown(
            f'<div class="factor-card"><b>{factor}</b><br>{text}</div>',
            unsafe_allow_html=True,
        )


def render_recommendation(score: float, domain: str):
    label, _, _ = risk_band(score)
    actions = {
        "HIGH RISK": {
            "SMS": "🚫 Do NOT click any link. Block sender and report as spam. Never share OTP/PIN.",
            "Email": "🚫 Do NOT click links or download attachments. Verify sender via official channel. Report as phishing.",
            "Call": "🚫 Hang up immediately. Do not share OTP, PIN, or bank details. Block and report the number.",
            "Transaction": "🚫 Hold/decline transaction. Trigger manual review and step-up authentication (OTP/biometric).",
        },
        "MEDIUM RISK": {
            "SMS": "⚠️ Verify sender identity independently before acting. Avoid clicking embedded links.",
            "Email": "⚠️ Confirm with sender via a separate channel before responding or clicking anything.",
            "Call": "⚠️ Ask caller to verify identity via official callback number before sharing any info.",
            "Transaction": "⚠️ Flag for secondary verification (SMS/email OTP) before approval.",
        },
        "LOW RISK": {
            "SMS": "✅ Appears safe. Standard monitoring is sufficient.",
            "Email": "✅ Appears safe. No action needed beyond routine spam filtering.",
            "Call": "✅ Appears safe. No unusual pattern detected.",
            "Transaction": "✅ Appears safe. Proceed with normal processing.",
        },
    }
    st.success(actions[label][domain]) if label == "LOW RISK" else st.error(actions[label][domain]) if label == "HIGH RISK" else st.warning(actions[label][domain])


def render_pipeline():
    with st.expander("🧠 Explainable AI Pipeline — how the score is built"):
        st.markdown(
            """
1. **Input capture** — Raw message / call metadata / transaction fields are collected from the form.
2. **Feature extraction** — Rule-based & pattern features are derived (keywords, links, urgency phrases, numeric anomalies, geo/velocity signals).
3. **Weighted scoring engine** — Each feature has a transparent weight (learned heuristically / from a trained model), producing a partial risk contribution.
4. **Aggregation** — Contributions are summed and squashed (sigmoid-style) into a 0–100 Risk Score.
5. **Explainability layer** — Each contributing factor is surfaced with its share of the score (SHAP-style local explanation) and a plain-language reason.
6. **Decision layer** — Score is mapped to LOW / MEDIUM / HIGH bands, each tied to a recommended action.
            """
        )


def summary_reason(top_factors: list, domain_word: str):
    if not top_factors:
        st.info(f"No strong red flags were found in this {domain_word}.")
        return
    bullets = "\n".join([f"- **{f}**" for f in top_factors])
    st.markdown(f"This {domain_word} was flagged mainly because of:\n\n{bullets}")


# -----------------------------------------------------------------------
# SCORING HELPERS (shared)
# -----------------------------------------------------------------------
def squash(raw_sum: float, scale: float = 18.0) -> float:
    """Convert an additive weighted sum into a 0-100 score with a sigmoid squash."""
    return 100 / (1 + math.exp(-raw_sum / scale + 3))


# =========================================================================
# MODULE 1: SMS / MESSAGE TEXT SCAM DETECTION
# =========================================================================
SMS_KEYWORDS = {
    "urgent action required": 12, "verify your account": 10, "click here": 9,
    "won a prize": 14, "lottery": 14, "otp": 11, "suspended": 10,
    "limited time": 8, "free gift": 9, "act now": 9, "bank account": 8,
    "kyc": 9, "refund": 7, "congratulations": 7, "claim now": 10,
    "password": 8, "update your details": 9, "loan approved": 10,
}

def analyze_sms(text: str, sender_unknown: bool, contains_link: bool, asks_for_otp: bool):
    text_l = text.lower()
    contributions, explanations = {}, {}

    kw_hits = [kw for kw in SMS_KEYWORDS if kw in text_l]
    if kw_hits:
        contrib = sum(SMS_KEYWORDS[k] for k in kw_hits)
        contributions["Suspicious keywords"] = contrib
        explanations["Suspicious keywords"] = f"Found {len(kw_hits)} scam-associated phrase(s): {', '.join(kw_hits)}."

    caps_ratio = sum(1 for c in text if c.isupper()) / max(len(text), 1)
    if caps_ratio > 0.3:
        contributions["Excessive capitalization"] = 8
        explanations["Excessive capitalization"] = f"{caps_ratio*100:.0f}% of characters are uppercase — common urgency tactic."

    link_count = len(re.findall(r"(https?://|www\.)\S+", text))
    if contains_link or link_count > 0:
        contributions["Contains link(s)"] = 12 + 4 * min(link_count, 2)
        explanations["Contains link(s)"] = "Message contains embedded URL(s), often used for phishing redirection."

    if sender_unknown:
        contributions["Unknown / unsaved sender"] = 10
        explanations["Unknown / unsaved sender"] = "Sender number is not in contacts and has no prior history."

    if asks_for_otp:
        contributions["Requests OTP/PIN"] = 20
        explanations["Requests OTP/PIN"] = "Legitimate institutions never ask you to share OTP or PIN via SMS."

    phone_count = len(re.findall(r"\b\d{10}\b", text))
    if phone_count:
        contributions["Embedded phone number"] = 6
        explanations["Embedded phone number"] = "Message asks you to call an embedded number directly — common vishing pattern."

    raw_sum = sum(contributions.values())
    score = min(squash(raw_sum, scale=20), 100)
    return score, contributions, explanations


# =========================================================================
# MODULE 2: EMAIL PHISHING DETECTION
# =========================================================================
EMAIL_KEYWORDS = {
    "verify your account": 11, "unusual activity": 10, "click the link below": 12,
    "update payment": 10, "your account will be suspended": 13, "invoice attached": 6,
    "wire transfer": 12, "gift card": 13, "urgent": 8, "password expires": 9,
    "confirm your identity": 10, "security alert": 8,
}

def analyze_email(subject: str, body: str, sender_domain: str, expected_domain: str,
                   has_attachment: bool, mismatched_display_name: bool):
    text_l = (subject + " " + body).lower()
    contributions, explanations = {}, {}

    kw_hits = [kw for kw in EMAIL_KEYWORDS if kw in text_l]
    if kw_hits:
        contrib = sum(EMAIL_KEYWORDS[k] for k in kw_hits)
        contributions["Suspicious phrasing"] = contrib
        explanations["Suspicious phrasing"] = f"Detected phishing-style phrase(s): {', '.join(kw_hits)}."

    if expected_domain and sender_domain and expected_domain.lower() not in sender_domain.lower():
        contributions["Domain mismatch"] = 22
        explanations["Domain mismatch"] = f"Sender domain '{sender_domain}' does not match the expected organization domain '{expected_domain}'."

    if mismatched_display_name:
        contributions["Spoofed display name"] = 14
        explanations["Spoofed display name"] = "Display name looks legitimate but the underlying email address doesn't match."

    link_count = len(re.findall(r"(https?://|www\.)\S+", body))
    if link_count:
        contributions["Embedded links"] = 10 + 3 * min(link_count, 3)
        explanations["Embedded links"] = f"{link_count} link(s) found in the email body — verify destination before clicking."

    if has_attachment:
        contributions["Unexpected attachment"] = 9
        explanations["Unexpected attachment"] = "Attachments can carry malware/macros — confirm relevance with sender first."

    raw_sum = sum(contributions.values())
    score = min(squash(raw_sum, scale=22), 100)
    return score, contributions, explanations


# =========================================================================
# MODULE 3: CALL / PHONE NUMBER SCAM DETECTION
# =========================================================================
def analyze_call(phone_number: str, country_mismatch: bool, robocall_pattern: bool,
                  asked_for_otp: bool, asked_for_money: bool, call_duration_sec: int,
                  reported_count: int):
    contributions, explanations = {}, {}

    if country_mismatch:
        contributions["Unexpected international code"] = 14
        explanations["Unexpected international code"] = "Call originates from a country code unusual for this account/context."

    if robocall_pattern:
        contributions["Robocall / auto-dialer pattern"] = 12
        explanations["Robocall / auto-dialer pattern"] = "Call behavior matches known robocall/auto-dialer signatures (silence gap, scripted tone)."

    if asked_for_otp:
        contributions["Requested OTP/PIN"] = 25
        explanations["Requested OTP/PIN"] = "Caller asked for a one-time password or PIN — a strong scam indicator."

    if asked_for_money:
        contributions["Requested payment/gift cards"] = 20
        explanations["Requested payment/gift cards"] = "Caller pressured for immediate payment, wire transfer, or gift cards."

    if call_duration_sec < 15:
        contributions["Very short call"] = 5
        explanations["Very short call"] = "Extremely short duration is typical of scam probing/robocalls."

    if reported_count > 0:
        contributions["Community-reported number"] = min(10 + reported_count * 2, 30)
        explanations["Community-reported number"] = f"This number has been reported {reported_count} time(s) by other users."

    raw_sum = sum(contributions.values())
    score = min(squash(raw_sum, scale=22), 100)
    return score, contributions, explanations


# =========================================================================
# MODULE 4: TRANSACTION FRAUD DETECTION
# =========================================================================
def analyze_transaction(amount: float, avg_amount: float, distance_from_home_km: float,
                         distance_from_last_txn_km: float, is_online: bool, is_foreign: bool,
                         hour_of_day: int, new_device: bool):
    contributions, explanations = {}, {}

    ratio = amount / max(avg_amount, 1)
    if ratio > 3:
        contributions["Amount far above average"] = min(10 * ratio, 30)
        explanations["Amount far above average"] = f"Transaction amount is {ratio:.1f}x the account's average purchase."

    if distance_from_home_km > 100:
        contributions["Unusual location (far from home)"] = min(distance_from_home_km / 20, 20)
        explanations["Unusual location (far from home)"] = f"Transaction occurred {distance_from_home_km:.0f} km from the account's home location."

    if distance_from_last_txn_km > 300:
        contributions["Impossible travel velocity"] = 20
        explanations["Impossible travel velocity"] = f"{distance_from_last_txn_km:.0f} km from the previous transaction in a short time window — physically implausible."

    if is_online:
        contributions["Card-not-present (online)"] = 6
        explanations["Card-not-present (online)"] = "Online transactions carry higher fraud risk than in-person chip/PIN."

    if is_foreign:
        contributions["Foreign transaction"] = 9
        explanations["Foreign transaction"] = "Transaction originates from a country different from the cardholder's registered country."

    if hour_of_day < 5 or hour_of_day > 23:
        contributions["Odd transaction hour"] = 7
        explanations["Odd transaction hour"] = f"Transaction occurred at {hour_of_day}:00, outside typical spending hours."

    if new_device:
        contributions["New/unrecognized device"] = 11
        explanations["New/unrecognized device"] = "Transaction initiated from a device not previously linked to this account."

    raw_sum = sum(contributions.values())
    score = min(squash(raw_sum, scale=20), 100)
    return score, contributions, explanations


# -----------------------------------------------------------------------
# SIDEBAR
# -----------------------------------------------------------------------
st.sidebar.title("🛡️ Scam & Fraud Detector")
st.sidebar.caption("Explainable AI risk engine — SMS, Email, Call & Transaction")
render_pipeline_sidebar = st.sidebar.container()

# -----------------------------------------------------------------------
# MAIN TITLE
# -----------------------------------------------------------------------
st.title("🛡️ Universal Scam & Fraud Detection Dashboard")
st.caption("Enter details below and get an instant explainable risk assessment.")

tab_sms, tab_email, tab_call, tab_txn = st.tabs(
    ["📱 SMS / Message", "📧 Email", "📞 Call / Phone", "💳 Transaction"]
)

# ---------------- TAB: SMS ----------------
with tab_sms:
    st.subheader("📱 SMS / Message Scam Check")
    col1, col2 = st.columns([2, 1])
    with col1:
        sms_text = st.text_area(
            "Paste the message text",
            "Dear customer, your account will be SUSPENDED. Click here to verify your account and claim now your refund. Share OTP to confirm.",
            height=120,
        )
    with col2:
        sender_unknown = st.checkbox("Sender is unknown/unsaved", value=True)
        contains_link = st.checkbox("Message contains a link", value=True)
        asks_otp = st.checkbox("Message asks for OTP/PIN", value=True)

    if st.button("🔍 Analyze Message", key="sms_btn"):
        score, contrib, expl = analyze_sms(sms_text, sender_unknown, contains_link, asks_otp)
        render_header(score)
        c1, c2 = st.columns(2)
        with c1:
            render_gauge(score)
        with c2:
            st.metric("Number of Risk Factors", len(contrib))
        st.subheader("📊 Risk Contribution Chart")
        render_contribution_chart(contrib)
        st.subheader("🤖 Explainable AI — Factor Breakdown")
        render_factor_explanations(expl)
        st.subheader("🔎 Why Was This Flagged?")
        summary_reason(sorted(contrib, key=contrib.get, reverse=True)[:3], "message")
        st.subheader("🛡️ Recommended Action")
        render_recommendation(score, "SMS")

# ---------------- TAB: EMAIL ----------------
with tab_email:
    st.subheader("📧 Email Phishing Check")
    subject = st.text_input("Email subject", "Urgent: Verify your account now")
    body = st.text_area(
        "Email body",
        "We noticed unusual activity. Click the link below to confirm your identity and update payment details immediately, or your account will be suspended.",
        height=120,
    )
    c1, c2, c3 = st.columns(3)
    with c1:
        sender_domain = st.text_input("Sender domain", "secure-bank-alerts.com")
    with c2:
        expected_domain = st.text_input("Expected official domain", "bank.com")
    with c3:
        has_attachment = st.checkbox("Has attachment", value=False)
    mismatched_name = st.checkbox("Display name looks official but address doesn't match", value=True)

    if st.button("🔍 Analyze Email", key="email_btn"):
        score, contrib, expl = analyze_email(subject, body, sender_domain, expected_domain, has_attachment, mismatched_name)
        render_header(score)
        c1, c2 = st.columns(2)
        with c1:
            render_gauge(score)
        with c2:
            st.metric("Number of Risk Factors", len(contrib))
        st.subheader("📊 Risk Contribution Chart")
        render_contribution_chart(contrib)
        st.subheader("🤖 Explainable AI — Factor Breakdown")
        render_factor_explanations(expl)
        st.subheader("🔎 Why Was This Flagged?")
        summary_reason(sorted(contrib, key=contrib.get, reverse=True)[:3], "email")
        st.subheader("🛡️ Recommended Action")
        render_recommendation(score, "Email")

# ---------------- TAB: CALL ----------------
