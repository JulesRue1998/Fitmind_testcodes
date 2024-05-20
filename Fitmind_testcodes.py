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
mood = st.number_input("Mood", min_value=1, max_value=10, step=1, key="mood")
stress = st.number_input("Stress", min_value=1, max_value=10, step=1, key="stress")

# Anzeigen der eingegebenen Daten
st.write("Datum:", current_date)
st.write("Mood:", mood)
st.write("Stress:", stress)
