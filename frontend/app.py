import os
import streamlit as st
import requests

# Fetch API host from environment variable set in docker-compose.yml, defaulting to localhost
API_HOST = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="AI Content Safety Engine", page_icon="🛡️")

st.title("🛡️ Real-Time Content Moderation Engine")
st.caption("CSE Data Science Portfolio Project")

st.subheader("Analyze Text Input")
user_input = st.text_area("Enter text to audit:", "This is a safe sample sentence.")

if st.button("Audit Text"):
    with st.spinner("Analyzing toxicity..."):
        try:
            response = requests.post(
                f"{API_HOST}/v1/moderate-text",
                json={"text": user_input}
            )
            if response.status_code == 200:
                data = response.json()
                if data["flagged"]:
                    st.error(f"⚠️ Flagged Content Detected! (Confidence: {data['confidence_score']*100:.1f}%)")
                else:
                    st.success(f"✅ Content Cleared (Confidence: {(1-data['confidence_score'])*100:.1f}%)")
                st.json(data)
            else:
                st.error("API error occurred.")
        except Exception as e:
            st.error(f"Failed to connect to API backend: {e}")