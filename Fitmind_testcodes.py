import streamlit as st
import pandas as pd
import numpy as np

if selected_subcategory == "Stress & Mood Tracker":
    st.subheader("Track your stress ")
    st.write('Enter your stress level for each day.')
    
    # Text elements
    st.write("How is your mood today?")
    mood = st.slider("Mood", 0, 10, 5)

    st.write("How stressed have you been today?")
    stress_level = st.slider("Stress level", 0, 10, 5)

    # Create or load the DataFrame
    if 'mood_data' not in st.session_state:
        st.session_state.mood_data = pd.DataFrame(columns=['Datum', 'Stimmung', 'Stresslevel'])

    # Append new data to the DataFrame
    new_entry = {'Datum': pd.Timestamp.now().date(), 'Stimmung': mood, 'Stresslevel': stress_level}
    st.session_state.mood_data = st.session_state.mood_data.append(new_entry, ignore_index=True)

    # Filter the DataFrame to keep only the last 30 entries
    mood_data_last_30_days = st.session_state.mood_data.tail(30)

    # Chart elements
    st.write("Mood and stress level over the last 30 days:")
    st.line_chart(mood_data_last_30_days.set_index('Datum'))
