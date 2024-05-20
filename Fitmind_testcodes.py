import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialisierung der Daten nur beim ersten Aufruf der Seite
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Date', 'Mood', 'Stress Level'])

# Title und Anweisungen
st.subheader("Mental Health")
st.write("Wie geht es dir heute?")

# Input Widgets
mood = st.slider("Stimmung", 1, 10, 5)
stress_level = st.slider("Stresslevel", 1, 10, 5)

# Daten an die Session-Variable anhängen
if st.button("Daten speichern"):
    new_entry = pd.Series({'Date': pd.Timestamp.now().date(), 'Mood': mood, 'Stress Level': stress_level})
    st.session_state.data = st.session_state.data.append(new_entry, ignore_index=True)

# Liniendiagramm
st.subheader("Stress Level and Mood Over Time")

# Anzeigen der Daten in einer Tabelle
st.write("Gespeicherte Daten:")
st.write(st.session_state.data)

# Plotten des Liniendiagramms
if not st.session_state.data.empty:
    plt.figure(figsize=(10, 6))

    # Stresslevel plotten
    plt.plot(st.session_state.data['Date'], st.session_state.data['Stress Level'], marker='o', label='Stress Level')

    # Stimmung plotten
    plt.plot(st.session_state.data['Date'], st.session_state.data['Mood'], marker='o', label='Mood')

    plt.xlabel('Date')
    plt.ylabel('Level')
    plt.title('Stress Level and Mood Over Time')
    plt.yticks(range(1, 11))  # Festlegen der y-Achse von 1 bis 10
    plt.xticks(rotation=45)
    plt.legend()
    st.pyplot(plt)
else:
    st.write("Keine Daten verfügbar.")
