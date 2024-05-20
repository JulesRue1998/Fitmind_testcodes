import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dummy DataFrame for demonstration
data = {
    'Date': pd.date_range(start='2022-01-01', end='2022-01-31'),
    'Stress Level': [3, 4, 2, 5, 6, 3, 4, 5, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 4, 5, 6, 7, 8, 9, 8, 7, 6]
}
df = pd.DataFrame(data)

# Title and instructions
st.title('Stress Tracker')
st.write('Select a date to see the stress level.')

# Date selection
selected_date = st.date_input('Select Date', min_value=df['Date'].min(), max_value=df['Date'].max())

# Filter DataFrame by selected date
selected_data = df[df['Date'] == selected_date]

# Plot stress level for selected date
if not selected_data.empty:
    plt.figure(figsize=(8, 6))
    plt.plot(selected_data['Date'], selected_data['Stress Level'], marker='o')
    plt.title('Stress Level for ' + str(selected_date))
    plt.xlabel('Date')
    plt.ylabel('Stress Level')
    plt.xticks(rotation=45)
    st.pyplot(plt)
else:
    st.write('No data available for selected date.')
