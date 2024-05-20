import streamlit as st
import pandas as pd

# Titel und Anweisungen
st.subheader("Benutzerdefinierte Daten eingeben")

# Eingabe der Werte für die ersten beiden Zeilen durch den Benutzer
moos_value = st.number_input("Wert für Moos (1-10)", min_value=1, max_value=10, value=5)
stress_value = st.number_input("Wert für Stress (1-10)", min_value=1, max_value=10, value=5)

# Festlegen der ersten beiden Zeilen mit den ausgewählten Werten
data = pd.DataFrame({'Datum': ['Moos', 'Stress'], 'Spalte 2': [moos_value, stress_value]})

# Eingabe der Anzahl der zusätzlichen Spalten durch den Benutzer
num_cols = st.number_input("Anzahl der zusätzlichen Spalten", min_value=0, value=0)

# Eingabe der Daten für jede zusätzliche Spalte
for i in range(num_cols):
    # Datum für den Spaltennamen
    col_date = st.date_input(f"Datum für Spalte {i+3}", key=f"col_date_{i}")
    # Wert für die Spalte
    col_value = st.number_input(f"Wert für Spalte {i+3} (1-10)", min_value=1, max_value=10, key=f"col_value_{i}")
    # Spalte zum DataFrame hinzufügen
    data[col_date] = col_value

# Anzeigen des erstellten DataFrames
st.subheader("Erstellter DataFrame")
st.write(data)
