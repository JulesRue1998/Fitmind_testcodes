import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialisierung der Daten nur beim ersten Aufruf der Seite
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Date', 'Mood', 'Stress Level'])

# Title und Anweisungen
st.subheader("Mental Health")
st.write("Wie geht es dir heute?")

# Input Widgets
mood = st.slider("Stimmung", 1, 10, 5)
stress_level = st.slider("Stresslevel", 1, 10, 5)


