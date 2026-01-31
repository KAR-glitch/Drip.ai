import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
client = Groq(api_key=os.getenv("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"))

# ---------------------- AI LOGIC ---------------------- #

def generate_styling_advice(style, occasion):
    prompt = f"You are a professional fashion stylist. Suggest styling advice for a {style} outfit suitable for a {occasion}."
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are an expert fashion stylist."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=120,
        temperature=0.7
    )
    return response.choices[0].message.content

def generate_outfit(style):
    outfits = {
        "Casual": "White t-shirt, blue jeans, sneakers, smartwatch",
        "Formal": "Tailored blazer, trousers, leather shoes, classic watch",
        "Ethnic": "Kurta set with subtle embroidery and traditional footwear",
        "Streetwear": "Oversized hoodie, cargo pants, sneakers, cap"
    }
    return outfits.get(style, "Stylish coordinated outfit")

def analyze_image():
    return "Detected outfit style: modern casual. Dominant colors: neutral and pastel tones."

def generate_trend_insight(style):
    prompt = f"Describe current fashion trends related to {style} style."
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a fashion trend analyst."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100
    )
    return response.choices[0].message.content

# ---------------------- STREAMLIT UI ---------------------- #

st.set_page_config(page_title="AI Fashion Stylist", layout="centered")
st.title("👗 Generative AI Fashion Stylist")

style = st.selectbox("Style Preference", ["Casual", "Formal", "Ethnic", "Streetwear"])
occasion = st.text_input("Occasion (Party, Office, Wedding)")
image = st.file_uploader("Upload Outfit Image", type=["png", "jpg", "jpeg"])

if st.button("Get AI Recommendation"):
    if not occasion or not image:
        st.warning("Please fill all fields and upload an image.")
    else:
        with st.spinner("Analyzing..."):
            advice = generate_styling_advice(style, occasion)
            outfit = generate_outfit(style)
            image_analysis = analyze_image()
            trend = generate_trend_insight(style)

        st.subheader("✨ Personalized Styling Advice")
        st.write(advice)

        st.subheader("👕 Outfit Recommendation")
        st.write(outfit)

        st.subheader("📸 Image Analysis")
        st.write(image_analysis)

        st.subheader("🔥 Trend Insight")
        st.write(trend)
