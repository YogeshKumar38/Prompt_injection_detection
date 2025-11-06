import streamlit as st
import json
import os
import re
from transformers import pipeline

# ---------- Config ----------
KEYWORDS_JSON = "keywords.json"

# Load semantic model (for intent/context analysis)
@st.cache_resource
def load_semantic_model():
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

semantic_model = load_semantic_model()

# Risk thresholds
def risk_level_from_score(score: int) -> (str, str):
    if score <= 2:
        return "Safe (0–2)", "safe"
    elif 3 <= score <= 5:
        return "Suspicious (3–5)", "suspicious"
    else:
        return "High Risk (6+)", "high"

# Category messages
CATEGORY_MESSAGES = {
    "Security Bypass": {
        "title": "⚠ Security Alert: Security Bypass Attempt Detected",
        "body": "Your input contained phrases associated with attempts to bypass or manipulate system instructions. Please rephrase your request."
    },
    "Malware/Hacking": {
        "title": "🚨 Security Protocol Activated: Malicious Content Request",
        "body": "The system identified content related to hacking or malware creation. Such prompts are not allowed."
    },
    "Violence/Illegal Content": {
        "title": "🚨 Critical Policy Violation: Illegal Content Detected",
        "body": "Your request includes references to violence or illegal acts. Please modify it to stay within safe limits."
    }
}

# ---------- Helpers ----------
def load_keywords(json_path: str):
    if not os.path.exists(json_path):
        st.error(f"Missing {json_path}. Please add your keywords JSON.")
        return {}
    with open(json_path, "r", encoding="utf8") as f:
        return json.load(f)

def analyze_text(text: str, keywords_map: dict):
    text_lower = text.lower()
    total_score = 0
    matched = []
    categories = set()

    for kw, info in keywords_map.items():
        weight = int(info.get("weight", 1))
        category = info.get("category", "Unknown")

        if " " in kw:
            if kw in text_lower:
                matched.append((kw, category, weight))
                categories.add(category)
                total_score += weight
        else:
            pattern = r"\b" + re.escape(kw) + r"\b"
            if re.search(pattern, text_lower):
                matched.append((kw, category, weight))
                categories.add(category)
                total_score += weight

    return matched, categories, total_score

# ---------- Semantic Context Analyzer ----------
def analyze_context(prompt: str):
    candidate_labels = ["educational", "malicious", "neutral", "research", "instructional"]
    result = semantic_model(prompt, candidate_labels)
    top_label = result["labels"][0]
    score = result["scores"][0]

    # Simplify to main intent type
    if top_label in ["educational", "research", "neutral"]:
        intent = "Safe / Informational"
    elif top_label == "malicious":
        intent = "Potentially Harmful"
    else:
        intent = "Uncertain"

    return intent, top_label, round(score * 100, 2)

# ---------- Streamlit UI ----------
st.set_page_config(page_title="Prompt Injection Detector (Smart)", layout="centered")

st.title("🧠 Prompt Injection Detector (Smart Version)")
st.caption("Now detects intent and context to reduce false positives")

keywords_map = load_keywords(KEYWORDS_JSON)

st.subheader("Input Prompt")
prompt_text = st.text_area("Enter prompt to analyze", height=160)

if st.button("Analyze"):
    if not prompt_text.strip():
        st.warning("Please enter a prompt to analyze.")
    else:
        matched, categories, total_score = analyze_text(prompt_text, keywords_map)
        level_text, level_key = risk_level_from_score(total_score)

        # Context check
        intent, top_label, confidence = analyze_context(prompt_text)

        # Adjust risk if context is safe
        if intent == "Safe / Informational" and total_score > 0:
            total_score = max(0, total_score - 3)
            level_text, level_key = risk_level_from_score(total_score)

        style_map = {
            "safe": "color: #1f8a3d; font-weight:700;",
            "suspicious": "color: #b36b00; font-weight:700;",
            "high": "color: #b00000; font-weight:700; background-color:#00000010; padding:4px; border-radius:4px;"
        }

        # Display results
        st.markdown(f"<div style='{style_map[level_key]}'>Risk Score: {total_score} — {level_text}</div>", unsafe_allow_html=True)
        st.markdown(f"<div style='font-weight:600; margin-top:8px;'>Intent Detected: <span style='color:#333;'>{intent}</span> (Confidence: {confidence}%)</div>", unsafe_allow_html=True)

        if not categories:
            st.markdown("<div style='color:#000000; font-weight:700;'>Result: Safe Prompt — no violations detected.</div>", unsafe_allow_html=True)
        else:
            for cat in sorted(categories):
                msg = CATEGORY_MESSAGES.get(cat)
                if msg:
                    st.markdown(
                        f"<div style='margin-top:12px; padding:12px;'>"
                        f"<div style='color:#b00000; font-weight:800; font-size:16px;'>{msg['title']}</div>"
                        f"<div style='color:#000000; margin-top:6px;'>{msg['body']}</div>"
                        f"</div>",
                        unsafe_allow_html=True
                    )

        if matched:
            rows = "".join(
                f"<tr><td style='padding:6px;border-bottom:1px solid #eee;'>{kw}</td><td style='padding:6px;border-bottom:1px solid #eee;'>{cat}</td><td style='padding:6px;border-bottom:1px solid #eee;text-align:center;'>{w}</td></tr>"
                for kw, cat, w in matched
            )
            st.markdown(
                "<div style='margin-top:12px;'>"
                "<div style='font-weight:700;margin-bottom:6px;'>Matched keywords</div>"
                "<table style='width:100%; border-collapse:collapse;'>"
                "<thead><tr><th style='text-align:left;padding:6px;border-bottom:2px solid #ddd;'>Keyword</th>"
                "<th style='text-align:left;padding:6px;border-bottom:2px solid #ddd;'>Category</th>"
                "<th style='text-align:center;padding:6px;border-bottom:2px solid #ddd;'>Weight</th></tr></thead>"
                f"<tbody>{rows}</tbody></table></div>",
                unsafe_allow_html=True
            )

with st.expander("Preview keywords.json (editable outside the app)"):
    st.code(json.dumps(keywords_map, indent=2), language="json")

st.caption("Now includes context-based filtering to reduce false flags. Run with: streamlit run app.py")
