import pandas as pd
import streamlit as st
from datetime import datetime

st.subheader("Mood & Stress Tracker")

# Aktuelles Datum
current_date = datetime.now().date()

# DataFrame mit dem aktuellen Datum erstellen
data_df = pd.DataFrame(
    {
        "Datum": ["Stress", "Mood"],
        "Verlauf der letzten 30 Tage": [None, None]
    }
)

# Benutzereingabe für Stress (Wert zwischen 1 und 10)
stress = st.slider("Stress (1-10)", min_value=1, max_value=10, step=1)
data_df["Stress"] = stress


# Benutzereingabe für die Spalten außer "Verlauf der letzten 30 Tage"
for column in data_df.columns:
    if column not in ["Datum", "Mood", "Stress", "Verlauf der letzten 30 Tage"]:
        data_df[column] = st.text_input(f"{column} (beliebiger Wert)")

# Benutzereingabe für den Spaltennamen
new_column_name = st.text_input("Neues Datum", "")

# Wenn ein neuer Spaltenname eingegeben wurde
if new_column_name:
    # Generiere die Werte für die neue Spalte (zum Beispiel Nullen für jeden Tag)
    new_column_values = [0] * 30  # Dummy-Werte, die ersetzt werden müssen
    # Füge die neue Spalte zum DataFrame hinzu
    data_df[new_column_name] = new_column_values
# Benutzereingabe für Mood (Wert zwischen 1 und 10)
mood = st.slider("Mood (1-10)", min_value=1, max_value=10, step=1)
data_df["Mood"] = mood




# Anzeigen des DataFrames
st.write(data_df)
