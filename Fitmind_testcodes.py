import streamlit as st
import pandas as pd

# Titel und Anweisungen
st.subheader("Benutzerdefinierte Daten eingeben")

# Eingabe der Werte für die ersten beiden Zeilen durch den Benutzer
moos_value = st.number_input("Wert für Stimmung (1-10)", min_value=1, max_value=10, value=5)
stress_value = st.number_input("Wert für Stress (1-10)", min_value=1, max_value=10, value=5)

# Festlegen der ersten beiden Zeilen mit den ausgewählten Werten
data = pd.DataFrame({'Stimmung': [moos_value], 'Stress': [stress_value]})

# Eingabe der Anzahl der zusätzlichen Zeilen durch den Benutzer
num_rows = st.number_input("Anzahl der zusätzlichen Zeilen", min_value=0, value=0)

# Eingabe der Daten für jede zusätzliche Zeile
for i in range(num_rows):
    # Datum für den Zeilenindex
    row_date = st.date_input(f"Datum für Zeile {i+3}", key=f"row_date_{i}")
    # Wert für die Stimmung
    mood_value = st.number_input(f"Wert für Stimmung in Zeile {i+3} (1-10)", min_value=1, max_value=10, key=f"mood_{i}")
    # Wert für den Stress
    stress_value = st.number_input(f"Wert für Stress in Zeile {i+3} (1-10)", min_value=1, max_value=10, key=f"stress_{i}")
    # Neue Zeile zum DataFrame hinzufügen
    data.loc[row_date] = [mood_value, stress_value]

# Anzeigen des erstellten DataFrames
st.subheader("Erstellter DataFrame")
st.write(data)
