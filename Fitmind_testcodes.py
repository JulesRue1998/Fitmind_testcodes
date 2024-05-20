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
st.write("Trage deine Stimmung und Stresslevel ein:")

# Input Widgets für manuelle Eingabe
mood = st.number_input("Stimmung", min_value=1, max_value=10, value=5)
stress_level = st.number_input("Stresslevel", min_value=1, max_value=10, value=5)

# Daten an die Session-Variable anhängen
if st.button("Daten speichern"):
    new_entry = {'Date': pd.Timestamp.now().date(), 'Mood': mood, 'Stress Level': stress_level}
    st.session_state.data = st.session_state.data.append(new_entry, ignore_index=True)

# Erfolgsmeldung anzeigen
if 'new_entry' in locals():
    st.success("Daten erfolgreich gespeichert!")
