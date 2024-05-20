import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import streamlit as st
import pandas as pd

# Initialisierung der Daten
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Date', 'Mood', 'Stress Level'])

# Tabelle anzeigen
st.subheader("Gespeicherte Daten")
st.write(st.session_state.data)

# Titel und Anweisungen
st.subheader("Mental Health")
st.write("Wie war deine Stimmung heute?")

# Input Widgets für Stimmung und Stressempfinden
mood = st.slider("Stimmung", 1, 10, 5)

st.write("Wie war dein Stressempfinden heute?")
stress_level = st.slider("Stresslevel", 1, 10, 5)

# Daten an die Session-Variable anhängen
if st.button("Daten speichern"):
    new_entry = {'Date': pd.Timestamp.now().date(), 'Mood': mood, 'Stress Level': stress_level}
    st.session_state.data = st.session_state.data.append(new_entry, ignore_index=True)

# Erfolgsmeldung anzeigen
if 'new_entry' in locals():
    st.success("Daten erfolgreich gespeichert!")

