import streamlit as st
import pandas as pd
from datetime import datetime

# Laden des vorhandenen DataFrames (falls vorhanden)
@st.cache(allow_output_mutation=True)
def load_df():
    return pd.DataFrame(columns=["Datum", "Mood", "Stress"])

# Erstellen einer leeren DataFrame
df = load_df()

# Datum für die aktuelle Zeile
current_date = datetime.now().date()

# Benutzereingabe für Mood und Stress
mood = st.number_input("Mood", min_value=1, max_value=10, step=1)
stress = st.number_input("Stress", min_value=1, max_value=10, step=1)

# Hinzufügen der eingegebenen Daten als Zeile zum DataFrame
df.loc[len(df)] = [current_date, mood, stress]

# Anzeigen des DataFrames
st.dataframe(df)
