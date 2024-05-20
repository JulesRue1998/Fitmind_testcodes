import streamlit as st
import pandas as pd

# Titel und Anweisungen
st.subheader("Mood and Stress Entry")

# Initialisierung der Daten
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Date', 'Mood', 'Stress'])

# Schaltfläche zum Hinzufügen neuer Zeilen
if st.button("Neue Zeile hinzufügen"):
    st.session_state.data.loc[len(st.session_state.data)] = ['Neues Datum', None, None]

# Eingabe für jedes Datum im DataFrame
for i, row in st.session_state.data.iterrows():
    st.write(f"Eintrag {i+1}")
    row['Date'] = st.date_input(f"Datum für Eintrag {i+1}", row['Date'])
    row['Mood'] = st.slider(f"Stimmung für Eintrag {i+1}", 1, 10, row['Mood'] or 5)
    row['Stress'] = st.slider(f"Stress für Eintrag {i+1}", 1, 10, row['Stress'] or 5)

# Anzeigen des erstellten DataFrames
st.subheader("Erstellter DataFrame")
st.write(st.session_state.data)
