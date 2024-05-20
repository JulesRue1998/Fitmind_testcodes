import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Laden des vorhandenen DataFrames (falls vorhanden)
@st.experimental_memoize
def load_df():
    return pd.DataFrame(columns=["Datum", "Stimmung", "Stress"])

# Festlegung der Anzahl der Zeilen im DataFrame
num_rows = st.number_input("Anzahl der Zeilen", min_value=1, value=1, step=1)

# Erstellung eines leeren DataFrames, falls nicht vorhanden
df = load_df()

# Heutiges Datum
current_date = datetime.now().date()

# Schleife zur Eingabe der Daten für jede Zeile
for i in range(num_rows):
    # Benutzereingabe für Stimmung und Stress für jede Zeile
    mood = st.number_input(f"Stimmung (Zeile {i+1})", min_value=1, max_value=10, step=1)
    stress = st.number_input(f"Stress (Zeile {i+1})", min_value=1, max_value=10, step=1)
    # Hinzufügen der eingegebenen Daten als Zeile zum DataFrame
    df.loc[len(df)] = [current_date, mood, stress]

# Anzeigen des erstellten DataFrames
st.dataframe(df)

# Neue Zeilen zum DataFrame hinzufügen
if st.button("Neue Zeile hinzufügen"):
    new_mood = st.number_input(f"Stimmung (Zeile {num_rows+1})", min_value=1, max_value=10, step=1)
    new_stress = st.number_input(f"Stress (Zeile {num_rows+1})", min_value=1, max_value=10, step=1)
    df.loc[len(df)] = [current_date, new_mood, new_stress]
    st.experimental_memoize(df)
