import streamlit as st
import pandas as pd

# Titel und Anweisungen
st.subheader("Benutzerdefinierte Daten eingeben")

# Festlegen der ersten beiden Zeilen mit Platzhalterwerten
data = pd.DataFrame({'Datum': ['Moos', 'Stress'], 'Spalte 2': [None, None]})

# Eingabe der Anzahl der zusätzlichen Spalten durch den Benutzer
num_cols = st.number_input("Anzahl der zusätzlichen Spalten", min_value=0, value=0)

# Eingabe der Daten für jede zusätzliche Spalte
for i in range(num_cols):
    # Datum für den Spaltennamen
    col_date = st.date_input(f"Datum für Spalte {i+3}", key=f"col_date_{i}")
    # Wert für die erste Zeile (Moos)
    mood_value = st.slider(f"Wert für Moos in Spalte {i+3}", 1, 10, key=f"mood_{i}")
    # Wert für die zweite Zeile (Stress)
    stress_value = st.slider(f"Wert für Stress in Spalte {i+3}", 1, 10, key=f"stress_{i}")
    # Spalte zum DataFrame hinzufügen
    data[col_date] = [mood_value, stress_value]

# Anzeigen des erstellten DataFrames
st.subheader("Erstellter DataFrame")
st.write(data)
