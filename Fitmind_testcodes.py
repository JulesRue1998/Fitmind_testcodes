import streamlit as st
import pandas as pd
from datetime import datetime

# Benutzereingabe für die Anzahl der Zeilen im DataFrame
num_rows = st.number_input("Anzahl der Zeilen", min_value=1, value=10, step=1)

# Erstellung eines leeren DataFrames mit den Spalten "Stimmung" und "Stress"
df = pd.DataFrame(columns=["Stimmung", "Stress"])

# Aktuelles Datum für den Zeilenindex
current_date = datetime.now().date()

# Anzeigen des erstellten DataFrames
st.dataframe(df)
