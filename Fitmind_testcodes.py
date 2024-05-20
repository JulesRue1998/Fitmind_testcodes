import streamlit as st
import pandas as pd
from datetime import datetime

# Erstellen einer leeren DataFrame
df = pd.DataFrame(columns=["Datum", "Mood", "Stress"])

# Datum für die aktuelle Zeile
current_date = datetime.now().date()

# Benutzereingabe für Mood und Stress
mood = st.number_input("Mood", min_value=1, max_value=10, step=1, key="mood")
stress = st.number_input("Stress", min_value=1, max_value=10, step=1, key="stress")

# Hinzufügen der eingegebenen Daten als Zeile zum DataFrame
df.loc[len(df)] = [current_date, mood, stress]

# Anzeigen der Tabelle mit den eingegebenen Daten
st.write("Eingegebene Daten:")
st.dataframe(df)

# Funktion zum Laden des vorhandenen DataFrames oder zum Erstellen eines neuen, falls keiner vorhanden ist
def load_or_create_df():
    try:
        df = pd.read_csv("data.csv")  # Versuche, den DataFrame aus einer CSV-Datei zu laden
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Datum", "Mood", "Stress"])  # Wenn die Datei nicht gefunden wird, erstelle einen leeren DataFrame
    return df

# Funktion zum Speichern des aktuellen DataFrames in einer CSV-Datei
def save_df(df):
    df.to_csv("data.csv", index=False)

# Laden des vorhandenen DataFrames oder Erstellen eines neuen
df = load_or_create_df()

# Datum für die aktuelle Zeile
current_date = datetime.now().date()

# Benutzereingabe für Mood und Stress
mood = st.number_input("Mood", min_value=1, max_value=10, step=1, key="mood")
stress = st.number_input("Stress", min_value=1, max_value=10, step=1, key="stress")

# Überprüfen, ob der Benutzer eine neue Zeile hinzufügen möchte
if st.button("Neue Zeile hinzufügen"):
    # Hinzufügen der eingegebenen Daten als Zeile zum DataFrame
    df.loc[len(df)] = [current_date, mood, stress]
    # Speichern des aktualisierten DataFrames
    save_df(df)

# Anzeigen der Tabelle mit den eingegebenen Daten
st.write("Eingegebene Daten:")
st.dataframe(df)

# Falls Sie die alten Zeilen unveränderbar machen möchten, können Sie den DataFrame auch einfrieren
# df_frozen = df.copy()  # Erstellen einer Kopie des DataFrames
# df_frozen.set_index("Datum", inplace=True)  # Festlegen des Datums als Index, um die Zeilen unveränderbar zu machen
# st.dataframe(df_frozen)
