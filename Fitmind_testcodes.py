import streamlit as st
import pandas as pd
from datetime import datetime

# Laden des vorhandenen DataFrames oder Erstellen eines neuen, falls keiner vorhanden ist
def load_or_create_df():
    try:
        df = pd.read_csv("data.csv")  # Versuche, den DataFrame aus einer CSV-Datei zu laden
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Datum", "Mood", "Stress"])  # Wenn die Datei nicht gefunden wird, erstelle einen leeren DataFrame
    return df

# Funktion zum Speichern des DataFrames in einer CSV-Datei
def save_df(df):
    df.to_csv("data.csv", index=False)

# Laden des vorhandenen DataFrames oder Erstellen eines neuen
df = load_or_create_df()

# Datum für die aktuelle Zeile
current_date = datetime.now().date()

# Benutzereingabe für Mood und Stress
num_rows = st.number_input("Anzahl der Zeilen zum Hinzufügen", min_value=1, value=1, step=1)
for i in range(num_rows):
    mood = st.number_input(f"Mood für Zeile {i+1}", min_value=1, max_value=10, step=1)
    stress = st.number_input(f"Stress für Zeile {i+1}", min_value=1, max_value=10, step=1)
    df.loc[len(df)] = [current_date, mood, stress]

# Speichern des aktualisierten DataFrames
save_df(df)

# Anzeigen der Tabelle mit den eingegebenen Daten
st.write("Eingegebene Daten:")
st.data
