import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dummy DataFrame for demonstration
data = {
    'Date': [],
    'Mood': [],
    'Stress Level': []
}

# Title and instructions
st.subheader("Mental Health")
st.write("Wie geht es dir heute?")
mood = st.slider("Stimmung", 0, 10, 5)
st.write("Wie gestresst warst du heute?")
stress_level = st.slider("Stresslevel", 0, 10, 5)

# Append data to DataFrame only if it's not empty
if data['Date']:
    data['Date'].append(pd.Timestamp.now().date())
    data['Mood'].append(mood)
    data['Stress Level'].append(stress_level)
else:
    data['Date'] = [pd.Timestamp.now().date()]
    data['Mood'] = [mood]
    data['Stress Level'] = [stress_level]

# Convert data to DataFrame
df = pd.DataFrame(data)

# Line chart
st.subheader("Stress Level and Mood Over Time")
plt.figure(figsize=(10, 6))

# Plot stress level
plt.plot(df['Date'], df['Stress Level'], marker='o', label='Stress Level')

# Plot mood
plt.plot(df['Date'], df['Mood'], marker='o', label='Mood')

plt.xlabel('Date')
plt.ylabel('Level')
plt.title('Stress Level and Mood Over Time')
plt.xticks(rotation=45)
plt.legend()
st.pyplot(plt)

