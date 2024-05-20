

import pandas as pd
import streamlit as st
from datetime import datetime

st.subheader("Mood & Stress Tracker")

# DataFrame mit den Spalten "Datum", "Mood" und "Stress"
data_df = pd.DataFrame(columns=["Datum", "Mood", "Stress"])

# Funktion zum Hinzufügen einer neuen Zeile
def add_row():
    new_row = {"Datum": datetime.now().date(), "Mood": None, "Stress": None}
    data_df.loc[len(data_df)] = new_row

# Schaltfläche zum Hinzufügen einer neuen Zeile
if st.button("Neue Zeile hinzufügen"):
    add_row()

# Benutzereingabe für Mood (beliebige Zahl)
mood = st.text_input("Mood", key="mood")
try:
    mood = float(mood)  # Umwandlung des Benutzereingabewerts in eine Gleitkommazahl
except ValueError:
    mood = None  # Wenn die Eingabe keine gültige Zahl ist, wird None verwendet
data_df["Mood"] = mood

# Benutzereingabe für Stress (beliebige Zahl)
stress = st.text_input("Stress", key="stress")
try:
    stress = float(stress)  # Umwandlung des Benutzereingabewerts in eine Gleitkommazahl
except ValueError:
    stress = None  # Wenn die Eingabe keine gültige Zahl ist, wird None verwendet
data_df["Stress"] = stress

# Anzeigen des DataFrames
st.write(data_df)



