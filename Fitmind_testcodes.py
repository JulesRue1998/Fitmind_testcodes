import streamlit as st
import pandas as pd
from datetime import datetime

# Benutzereingabe für die Anzahl der Zeilen im DataFrame
num_rows = st.number_input("Anzahl der Zeilen", min_value=1, value=10, step=1)

# Erstellung eines leeren DataFrames mit den Spalten "Stimmung" und "Stress"
df = pd.DataFrame(columns=["Stimmung", "Stress"])

# Aktuelles Datum für den Zeilenindex
current_date = datetime.now().date()

# Schleife zur Eingabe der Daten für jede Zeile
for i in range(num_rows):
    # Benutzereingabe für Stimmung und Stress für jede Zeile
    mood = st.number_input(f"Stimmung (Zeile {i+1})", min_value=1, max_value=10, step=1)
    stress = st.number_input(f"Stress (Zeile {i+1})", min_value=1, max_value=10, step=1)
    # Hinzufügen der eingegebenen Daten als Zeile zum DataFrame
    df.loc[current_date] = [mood, stress]

# Anzeigen des erstellten DataFrames
st.dataframe(df)
