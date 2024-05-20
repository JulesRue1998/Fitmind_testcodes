import streamlit as st
import pandas as pd
from datetime import datetime

# Festlegung der Anzahl der Zeilen im DataFrame
num_rows = 1

# Erstellung eines leeren DataFrames mit den Spalten "Stimmung" und "Stress"
df = pd.DataFrame(columns=["Stimmung", "Stress"])

# Heutiges Datum
current_date = datetime.now().date()

# Schleife zur Eingabe der Daten für jede Zeile
for i in range(num_rows):
    # Benutzereingabe für Stimmung und Stress für jede Zeile
    mood = st.number_input(f"Stimmung", min_value=1, max_value=10, step=1)
    stress = st.number_input(f"Stress", min_value=1, max_value=10, step=1)
    # Hinzufügen der eingegebenen Daten als Zeile zum DataFrame
    df.loc[current_date] = [mood, stress]

import streamlit as st
import pandas as pd
from datetime import datetime

# Funktion zum Hinzufügen von Zeilen
def add_rows(df, num_rows):
    current_date = datetime.now().date()
    for i in range(num_rows):
        mood = st.number_input(f"Stimmung (Zeile {len(df)+i+1})", min_value=1, max_value=10, step=1)
        stress = st.number_input(f"Stress (Zeile {len(df)+i+1})", min_value=1, max_value=10, step=1)
        df.loc[len(df)] = [current_date, mood, stress]
    return df

# Laden des vorhandenen DataFrames (falls vorhanden)
st.cache(allow_output_mutation=True)
def load_df():
    return pd.DataFrame(columns=["Datum", "Stimmung", "Stress"])

# Benutzereingabe für die Anzahl der zusätzlichen Zeilen
num_additional_rows = st.number_input("Anzahl der zusätzlichen Zeilen", min_value=1, value=1, step=1)

# Laden des DataFrames
df = load_df()

# Hinzufügen von zusätzlichen Zeilen
if num_additional_rows > 0:
    df = add_rows(df, num_additional_rows)

# Anzeigen des DataFrames
st.dataframe(df)
