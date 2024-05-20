import streamlit as st
import pandas as pd
from datetime import datetime

# Funktion zum Hinzufügen von Spalten
def add_columns(df, num_columns):
    current_date = datetime.now().date()
    for i in range(num_columns):
        mood = st.number_input(f"Stimmung (Spalte {len(df.columns)+i+1})", min_value=1, max_value=10, step=1)
        stress = st.number_input(f"Stress (Spalte {len(df.columns)+i+1})", min_value=1, max_value=10, step=1)
        df[current_date] = [mood, stress]
    return df

# Laden des vorhandenen DataFrames (falls vorhanden)
@st.cache(allow_output_mutation=True)
def load_df():
    return pd.DataFrame(columns=["Datum"])

# Benutzereingabe für die Anzahl der zusätzlichen Spalten
num_additional_columns = st.number_input("Anzahl der zusätzlichen Spalten", min_value=1, value=1, step=1)

# Laden des DataFrames
df = load_df()

# Hinzufügen von zusätzlichen Spalten
if num_additional_columns > 0:
    df = add_columns(df, num_additional_columns)

# Anzeigen des DataFrames
st.dataframe(df)
