
import pandas as pd
import streamlit as st
from datetime import datetime

st.subheader("Mood & Stress Tracker")

# DataFrame mit den Spalten "Datum", "Mood" und "Stress"
data_df = pd.DataFrame(columns=["Datum", "Mood", "Stress"])

# Funktion zum Hinzufügen einer neuen Zeile
def add_row(df):
    # Überprüfen, ob bereits ein Eintrag für das heutige Datum vorhanden ist
    today_entries = df[df["Datum"] == datetime.now().date()]
    if len(today_entries) == 0:  # Wenn kein Eintrag vorhanden ist, eine neue Zeile hinzufügen
        new_row = {"Datum": datetime.now().date(), "Mood": None, "Stress": None}
        df = df.append(new_row, ignore_index=True)  # Neue Zeile hinzufügen
        return df
    else:
        st.warning("Eintrag für heute existiert bereits.")
        return df

# Schaltfläche zum Hinzufügen einer neuen Zeile
if st.button("Neue Zeile hinzufügen"):
    data_df = add_row(data_df)

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

