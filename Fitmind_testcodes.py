import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

st.write("Tracker Mood and stress")

# Dummy DataFrame for demonstration
data = {
    'Date': pd.date_range(start='2022-01-01', end='2022-01-31'),
    'Stress Level': [3, 4, 2, 5, 6, 3, 4, 5, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 4, 5, 6, 7, 8, 9, 8, 7, 6],
    'Mood': ['Happy', 'Neutral', 'Sad', 'Happy', 'Neutral', 'Sad', 'Happy', 'Neutral', 'Sad', 'Happy', 'Neutral', 'Sad',
             'Happy', 'Neutral', 'Sad', 'Happy', 'Neutral', 'Sad', 'Happy', 'Neutral', 'Sad', 'Happy', 'Neutral', 'Sad',
             'Happy', 'Neutral', 'Sad', 'Happy', 'Neutral', 'Sad']
}
df = pd.DataFrame(data)

# Title and instructions
st.title('Stress and Mood Tracker')
st.write('Enter your stress level and mood for each day.')

# Input form for stress level and mood
date = st.date_input('Select Date', min_value=df['Date'].min(), max_value=df['Date'].max())
stress_level = st.slider('Stress Level (1-10)', min_value=1, max_value=10, value=5)
mood_options = ['Happy', 'Neutral', 'Sad']
mood = st.selectbox('Mood', mood_options)

# Button to submit data
if st.button('Submit'):
    # Append data to DataFrame
    df = df.append({'Date': date, 'Stress Level': stress_level, 'Mood': mood}, ignore_index=True)
    st.write('Data submitted successfully!')

# Filter DataFrame by selected date
selected_data = df[df['Date'] == date]

# Plot stress level and mood for selected date
if not selected_data.empty:
    fig, ax1 = plt.subplots(figsize=(8, 6))

    # Plot stress level
    ax1.plot(selected_data['Date'], selected_data['Stress Level'], marker='o', color='tab:blue')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Stress Level', color='tab:blue')
    ax1.tick_params('y', colors='tab:blue')

    # Create a second y-axis for mood
    ax2 = ax1.twinx()
    ax2.plot(selected_data['Date'], selected_data['Mood'], marker='o', color='tab:red')
    ax2.set_ylabel('Mood', color='tab:red')
    ax2.tick_params('y', colors='tab:red')

    plt.title('Stress Level and Mood for ' + str(date))
    plt.xticks(rotation=45)
    st.pyplot(plt)
else:
    st.write('No data available for selected date.')


