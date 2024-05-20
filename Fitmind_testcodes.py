import streamlit as st
import pandas as pd

# Titel und Anweisungen
st.subheader("Benutzerdefinierte Daten eingeben")

# Festlegen der ersten beiden Zeilen
data = pd.DataFrame({'Datum': ['Moos', 'Stress'], 'Spalte 2': [None, None]})

# Eingabe der Anzahl der zusätzlichen Spalten durch den Benutzer
num_cols = st.number_input("Anzahl der zusätzlichen Spalten", min_value=0, value=0)

# Eingabe der Spaltennamen durch den Benutzer
for i in range(num_cols):
    col_name = st.text_input(f"Name für Spalte {i+3}", key=f"col_name_{i}")
    data[col_name] = None

# Anzeigen des erstellten DataFrames
st.subheader("Erstellter DataFrame")
st.write(data)

