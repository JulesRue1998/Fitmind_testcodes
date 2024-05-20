import streamlit as st
import pandas as pd
from datetime import datetime

# Laden des vorhandenen DataFrames (falls vorhanden)
existing_df = pd.read_csv("existing_data.csv")  # Beispiel: Annahme, dass bereits ein DataFrame vorhanden ist

# Falls der DataFrame leer ist, erstellen Sie einen neuen mit den Spalten "Stimmung" und "Stress"
if existing_df.empty:
    existing_df = pd.DataFrame(columns=["Stimmung", "Stress"])

# Benutzereingabe für Stimmung und Stress für eine neue Zeile
mood = st.number_input(f"Stimmung", min_value=1, max_value=10, step=1)
stress = st.number_input(f"Stress", min_value=1, max_value=10, step=1)

# Heutiges Datum
current_date = datetime.now().date()

# Hinzufügen der neuen Zeile zum DataFrame
existing_df.loc[current_date] = [mood, stress]

# Anzeigen des aktualisierten DataFrames
st.dataframe(existing_df)

# Speichern Sie den aktualisierten DataFrame für zukünftige Verwendung (optional)
existing_df.to_csv("existing_data.csv", index=False)

