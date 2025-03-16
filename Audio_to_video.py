import streamlit as st
import google.generativeai as genai
import requests
import os
import time
import base64
import whisper


VOICE_ID = st.secrets["voice"]["VOICE_ID"]
AVATAR_ID = st.secrets["avatar"]["AVATAR_ID"]
HEYGEN_API_KEY = st.secrets["heygen"]["HEYGEN_API_KEY"]
GEMINI_API_KEY = st.secrets["google"]["GEMINI_API_KEY"]
# API Headers
headers = {
    "X-Api-Key": HEYGEN_API_KEY,
    "Content-Type": "application/json"
}

# Function to transcribe audio using Whisper
def transcribe_audio(audio_file):
    try:
        model = whisper.load_model("base")
        audio_path = "temp_audio.wav"

        with open(audio_path, "wb") as f:
            f.write(audio_file.getbuffer())

        result = model.transcribe(audio_path)
        return result["text"]
    except Exception as e:
        st.error(f"Error during transcription: {e}")
        return ""

# Function to generate captions using Gemini
def generate_captions(text):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(f"Generate captions for the following text: {text}")
        return response.text
    except Exception as e:
        st.error(f"Error during caption generation: {e}")
        return ""

# Step 1: Generate the Video
def generate_video(text):
    url = "https://api.heygen.com/v2/video/generate"

    data = {
        "video_inputs": [
            {
                "character": {
                    "type": "avatar",
                    "avatar_id": AVATAR_ID
                },
                "voice": {
                    "type": "text",
                    "voice_id": VOICE_ID,
                    "input_text": text
                }
            }
        ],
        "dimension": {
            "width": 1280,
            "height": 720
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        response_data = response.json()
        if "data" in response_data and "video_id" in response_data["data"]:
            return response_data["data"]["video_id"]
        else:
            st.error("Error: Unable to retrieve video ID.")
            return None
    else:
        st.error(f"Error: {response.status_code}, {response.text}")
        return None

# Step 2: Check Video Status
def check_video_status(video_id):
    status_url = f"https://api.heygen.com/v1/video_status.get?video_id={video_id}"

    while True:
        response = requests.get(status_url, headers=headers)
        if response.status_code == 200:
            status_data = response.json()
            status = status_data["data"]["status"]

            if status == "completed":
                return status_data["data"].get("video_url", "No video URL found.")
            elif status == "failed":
                st.error("Video generation failed!")
                return None
            else:
                st.write(f"Video is still processing... Current status: {status}")
                time.sleep(5)
        else:
            st.error(f"Error retrieving status: {response.status_code}")
            return None

# Streamlit UI
st.title("🎬 Auto Video Creator from Audio")

uploaded_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])

if uploaded_file:
    st.audio(uploaded_file, format='audio/mp3')

    st.write("### Step 1: Transcribing Audio...")
    transcript = transcribe_audio(uploaded_file)
    st.write("Transcription:", transcript)

    if transcript:
        st.write("### Step 2: Generating Captions...")
        captions = generate_captions(transcript)
        st.write("Captions:", captions)

        st.write("### Step 3: Creating Avatar Video...")
        video_id = generate_video(transcript)

        if video_id:
            video_url = check_video_status(video_id)

            if video_url:
                st.video(video_url)
                st.success("✅ Video generated successfully!")
                st.write("[Download Video]", video_url)
            else:
                st.error("❌ Failed to retrieve video URL.")
        else:
            st.error("❌ Failed to generate video. Check API responses.")
