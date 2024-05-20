import pandas as pd
import streamlit as st
from datetime import datetime

st.subheader("Mood & Stress Tracker")

# Aktuelles Datum
current_date = datetime.now().date()

# DataFrame mit dem aktuellen Datum erstellen
data_df = pd.DataFrame(
    {
        "Datum": ["Stress", "Mood"],
        "Verlauf der letzten 30 Tage": [None, None]
    }
)

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
