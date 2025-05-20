import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="QuickGo Travel Recommender", page_icon="🌍")
st.title("QuickGo Travel Recommender")

# User input fields
location = st.text_input("🔍 Where are you?", "Cebu")
time_available = st.slider("⏰ Time Available (minutes)", 15, 180, 45)
interests = st.multiselect("🌟 What are your interests?", ["coffee", "nature", "museums", "food", "shopping", "history", "parks"])

if st.button("✨ Get Recommendation"):
    if not openai.api_key:
        st.error("Missing OpenAI API key. Please check your .env file.")
    elif not interests:
        st.warning("Please select at least one interest.")
    else:
        with st.spinner("Sending your preferences to the GPT travel engine..."):
            prompt = f"""
            I'm in {location} and I have {time_available} minutes.
            I enjoy {', '.join(interests)}.
            Can you recommend a place I can quickly visit nearby?
            """

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You're a helpful travel guide who gives local and quick recommendations."},
                        {"role": "user", "content": prompt}
                    ]
                )
                suggestion = response['choices'][0]['message']['content']
                st.success(suggestion)
            except Exception as e:
                st.error(f"Error: {str(e)}")
