import pandas as pd
import streamlit as st
from datetime import datetime, timedelta

st.subheader("Mood & Stress Tracker")

# Benutzereingabe für die Anzahl der Tage
num_days = st.number_input("Anzahl der Tage", min_value=1, max_value=365, value=1, step=1)

# DataFrame mit den Spalten "Datum", "Mood" und "Stress"
data_df = pd.DataFrame(columns=["Datum", "Mood", "Stress"])

# Schleife für die Erstellung der Einträge für jeden Tag
for i in range(num_days):
    # Aktuelles Datum für den Eintrag
    current_date = (datetime.now() - timedelta(days=i)).date()
    
    # Benutzereingabe für Mood (beliebige Zahl)
    mood = st.text_input(f"Mood für {current_date}", key=f"mood_{i}")
    try:
        mood = float(mood)  # Umwandlung des Benutzereingabewerts in eine Gleitkommazahl
    except ValueError:
        mood = None  # Wenn die Eingabe keine gültige Zahl ist, wird None verwendet
    
    # Benutzereingabe für Stress (beliebige Zahl)
    stress = st.text_input(f"Stress für {current_date}", key=f"stress_{i}")
    try:
        stress = float(stress)  # Umwandlung des Benutzereingabewerts in eine Gleitkommazahl
    except ValueError:
        stress = None  # Wenn die Eingabe keine gültige Zahl ist, wird None verwendet
    
    # Daten für den aktuellen Tag hinzufügen
    data_df = data_df.append({"Datum": current_date, "Mood": mood, "Stress": stress}, ignore_index=True)

# Anzeigen des DataFrames
st.write(data_df)
