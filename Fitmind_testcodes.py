import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialisierung der Daten nur beim ersten Aufruf der Seite
if 'data' not in st.session_state:
    st.session_state.data = {
        'Date': [],
        'Mood': [],
        'Stress Level': []
    }

# Title und Anweisungen
st.subheader("Mental Health")
st.write("Wie geht es dir heute?")
mood = st.slider("Stimmung", 1, 10, 5)
# Input Widgets
st.write("Wie gestresst warst du heute")
stress_level = st.slider("Stresslevel", 1, 10, 5)

# Daten an die Session-Variable anhängen
if st.button("Daten speichern"):
    st.session_state.data['Date'].append(pd.Timestamp.now().date())
    st.session_state.data['Mood'].append(mood)
    st.session_state.data['Stress Level'].append(stress_level)

# Umwandlung der Daten in DataFrame
df = pd.DataFrame(st.session_state.data)

# Liniendiagramm
st.subheader("Stress Level and Mood Over Time")
plt.figure(figsize=(10, 6))

# Stresslevel plotten
plt.plot(df['Date'], df['Stress Level'], marker='o', label='Stress Level')

# Stimmung plotten
plt.plot(df['Date'], df['Mood'], marker='o', label='Mood')

plt.xlabel('Date')
plt.ylabel('Level')
plt.title('Stress Level and Mood Over Time')
plt.yticks(range(1, 11))  # Festlegen der y-Achse von 1 bis 10

# Festlegen der x-Ticks, um nur das Datum des ersten Eintrags und das aktuelle Datum anzuzeigen
xticks = [df['Date'].iloc[0], pd.Timestamp.now().date()]
plt.xticks(xticks, rotation=45)

plt.legend()
st.pyplot(plt)
