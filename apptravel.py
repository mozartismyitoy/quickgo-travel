import streamlit as st
import requests

st.title("🌏 QuickGo Travel Recommender")

location = st.text_input("📍 Where are you?", "Cebu")
time_available = st.slider("⏱️ Time Available (minutes)", 15, 180, 45)
interests = st.multiselect(
    "🎯 What are your interests?",
    ["coffee", "nature", "museums", "shopping", "beach", "food", "art"],
    default=["coffee", "nature"]
)

if st.button("✨ Get Recommendation"):
    payload = {
        "location": location,
        "time_available": time_available,
        "interests": interests
    }

    st.info("Sending your preferences to the GPT travel engine...")

    try:
        response = requests.post("http://127.0.0.1:8000/recommend", json=payload)
        data = response.json()

        if "suggestions" in data:
            st.success(data["suggestions"])
        else:
            st.error(data.get("error", "Unexpected error."))
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")
