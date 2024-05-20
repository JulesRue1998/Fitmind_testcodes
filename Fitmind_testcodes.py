import streamlit as st
import pandas as pd
from datetime import datetime

# Funktion zum Hinzufügen von Zeilen
def add_rows(df, num_rows):
    for i in range(num_rows):
        current_date = st.date_input(f"Zeile {len(df)+i+1}: Datum", datetime.now().date())
        mood = st.number_input(f"Zeile {len(df)+i+1}: Mood", min_value=1, max_value=10, step=1)
        stress = st.number_input(f"Zeile {len(df)+i+1}: Stress", min_value=1, max_value=10, step=1)
        df.loc[len(df)] = [current_date, mood, stress]
    return df

# Laden des vorhandenen DataFrames (falls vorhanden)
@st.cache(allow_output_mutation=True)
def load_df():
    return pd.DataFrame(columns=["Datum", "Mood", "Stress"])

# Benutzereingabe für die Anzahl der zusätzlichen Zeilen
num_additional_rows = st.number_input("Anzahl der zusätzlichen Zeilen", min_value=1, value=1, step=1)

# Laden des DataFrames
df = load_df()

# Hinzufügen von zusätzlichen Zeilen
if num_additional_rows > 0:
    df = add_rows(df, num_additional_rows)

# Anzeigen des DataFrames
st.dataframe(df)
