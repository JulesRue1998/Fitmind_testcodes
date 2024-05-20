import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Festlegung der Anzahl der Zeilen im DataFrame
num_rows = 1

# Erstellung eines leeren DataFrames mit den Spalten "Stimmung" und "Stress"
df = pd.DataFrame(columns=["Datum", "Stimmung", "Stress"])

# Heutiges Datum
current_date = datetime.now().date()

# Schleife zur Eingabe der Daten für jede Zeile
for i in range(num_rows):
    # Benutzereingabe für Stimmung und Stress für jede Zeile
    mood = st.number_input(f"Stimmung", min_value=1, max_value=10, step=1)
    stress = st.number_input(f"Stress", min_value=1, max_value=10, step=1)
    # Hinzufügen der eingegebenen Daten als Zeile zum DataFrame
    df.loc[current_date] = [current_date, mood, stress]

# Filtern der Daten der letzten 30 Tage
last_30_days = df[df['Datum'] >= current_date - timedelta(days=30)]

# Anzeigen des erstellten DataFrames
st.dataframe(df)

# Line-Chart für die Daten der letzten 30 Tage anzeigen
st.line_chart(last_30_days.set_index('Datum')[['Stimmung', 'Stress']])
