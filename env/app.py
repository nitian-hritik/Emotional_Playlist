import streamlit as st
from sentiment_analysis import analyze_sentiment
from spotify_api import get_playlist_by_mood

st.title("Emotion-Based Playlist Generator")

user_text = st.text_area("How do you feel today?")

if st.button("Generate Playlist"):
    mood = analyze_sentiment(user_text)
    playlists = get_playlist_by_mood(mood)

    st.subheader(f"Recommended Playlists for {mood.capitalize()} Mood")
    for name, link in playlists:
        st.markdown(f"[{name}]({link})")
