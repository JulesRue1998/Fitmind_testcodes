import streamlit as st
import pandas as pd
from datetime import datetime

# Funktion zur Erstellung einer neuen Zeile in der DataFrame-Tabelle
def add_row(data):
    new_row = {}
    # Aktuelles Datum für den Zeilenindex
    current_date = datetime.now().date()
    # Wert für die Stimmung
    mood_value = st.number_input("Wert für Stimmung (1-10)", min_value=1, max_value=10, key="new_row_mood")
    # Wert für den Stress
    stress_value = st.number_input("Wert für Stress (1-10)", min_value=1, max_value=10, key="new_row_stress")
    # Neue Zeile zum DataFrame hinzufügen
    new_row[current_date] = [mood_value, stress_value]
    data = data.append(pd.DataFrame(new_row, index=['Stimmung', 'Stress']).T)
    return data

# Titel und Anweisungen
st.subheader("Benutzerdefinierte Daten eingeben")

# Eingabe der Werte für die ersten beiden Zeilen durch den Benutzer
moos_value = st.number_input("Wert für Stimmung (1-10)", min_value=1, max_value=10, value=5, key="mood")
stress_value = st.number_input("Wert für Stress (1-10)", min_value=1, max_value=10, value=5, key="stress")

# Festlegen der ersten beiden Zeilen mit den ausgewählten Werten
data = pd.DataFrame({'Stimmung': [moos_value], 'Stress': [stress_value]})

# Schaltfläche zum Hinzufügen einer neuen Zeile
if st.button("Neue Zeile hinzufügen"):
    data = add_row(data)

# Anzeigen des erstellten DataFrames
st.subheader("Erstellter DataFrame")
st.write(data)
