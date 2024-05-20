import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

st.sidebar.header("Categories")

page = st.sidebar.radio("Choose what you need",["FitMind - Introduction", "Fitness", "Mental Health", "Food & Recipes"])

if page == "Fitness":
    st.sidebar.subheader("Fitness Subcategories")
    fitness_subcategories = ["Cardio", "Strength Training", "Flexibility", "Endurance"]
    selected_subcategory = st.sidebar.selectbox("Choose a fitness subcategory", fitness_subcategories)
    
    if selected_subcategory == "Cardio":
        st.write("Content for Cardio category")
    elif selected_subcategory == "Strength Training":
        st.write("Content for Strength Training category")
    elif selected_subcategory == "Flexibility":
        st.write("Content for Flexibility category")
    elif selected_subcategory == "Endurance":
        st.write("Content for Endurance category")
    
    st.sidebar.subheader("Second Subcategory")
    second_subcategory = st.sidebar.selectbox("Choose a second subcategory", ["Option 1", "Option 2", "Option 3"])
    
    if second_subcategory == "Option 1":
        st.write("Content for Option 1")
    elif second_subcategory == "Option 2":
        st.write("Content for Option 2")
    elif second_subcategory == "Option 3":
        st.write("Content for Option 3")
        
elif page == "Food & Recipes":
    st.title("Food & Recipes")
    
    st.sidebar.subheader("Food & Recipes")
    food_subcategories = ["Breakfast", "Lunch", "Dinner", "Snacks"]
    selected_subcategory = st.sidebar.selectbox("Choose a subcategory", food_subcategories)
    
    if selected_subcategory == "Breakfast":
        st.write("Breakfast Recipes")
        
        st.sidebar.subheader("Breakfast Subcategories")
        breakfast_subcategories = ["Eggs", "Toast", "Müsli"]
        selected_breakfast_subcategory = st.sidebar.selectbox("Choose a breakfast", breakfast_subcategories)
        
        if selected_breakfast_subcategory == "Eggs":
            st.write("Egg Recipes")
            # Hier kannst du spezifische Rezepte für Eier anzeigen
            
        elif selected_breakfast_subcategory == "Toast":
            st.write("Oatmeal Recipes")
            # Hier kannst du spezifische Rezepte für Haferflocken anzeigen
            
        elif selected_breakfast_subcategory == "Müsli":
            st.write("Smoothie Recipes")
            # Hier kannst du spezifische Rezepte für Smoothies anzeigen
            
    elif selected_subcategory == "Lunch":
        st.write("Lunch Recipes")
        # Hier kannst du spezifische Rezepte für das Mittagessen anzeigen
        st.sidebar.subheader("Lunch Subcategories")
        Lunch_subcategories = ["Ceasar Salad", "Omurice", "Sandwiches"]
        selected_Lunch_subcategory = st.sidebar.selectbox("Choose a Lunch ", Lunch_subcategories)
        
        if selected_Lunch_subcategory == "Ceasar Salad":
            st.write("Egg Recipes")
            # Hier kannst du spezifische Rezepte für Eier anzeigen
            
        elif selected_Lunch_subcategory == "Omurice":
            st.write("Oatmeal Recipes")
            # Hier kannst du spezifische Rezepte für Haferflocken anzeigen
            
        elif selected_Lunch_subcategory == "Sandwiches":
            st.write("Smoothie Recipes")
            # Hier kannst du spezifische Rezepte für Smoothies anzeigen
        
    elif selected_subcategory == "Dinner":
        st.write("Dinner Recipes")
        # Hier kannst du spezifische Rezepte für das Abendessen anzeigen
        st.sidebar.subheader("Dinner Subcategories")
        Dinner_subcategories = ["Spaghetti", "Salmon", "Feta Pasta"]
        selected_Dinner_subcategory = st.sidebar.selectbox("Choose a Dinner", Dinner_subcategories)
        
        if selected_Dinner_subcategory == "Spaghetti":
            st.write("Egg Recipes")
            # Hier kannst du spezifische Rezepte für Eier anzeigen
            
        elif selected_Dinner_subcategory == "Salmon":
            st.write("Oatmeal Recipes")
            # Hier kannst du spezifische Rezepte für Haferflocken anzeigen
            
        elif selected_Dinner_subcategory == "Feta Pasta":
            st.write("Smoothie Recipes")
            # Hier kannst du spezifische Rezepte für Smoothies anzeigen
        
    elif selected_subcategory == "Snacks":
        st.write("Snack Recipes")
        # Hier kannst du spezifische Rezepte für Snacks anzeigen
        st.sidebar.subheader("Snacks Subcategories")
        Snacks_subcategories = ["Brownies", "Oatmeal", "Smoothies"]
        selected_Snacks_subcategory = st.sidebar.selectbox("Choose a Snack", Snacks_subcategories)
        
        if selected_breakfast_subcategory == "Brownies":
            st.write("Egg Recipes")
            # Hier kannst du spezifische Rezepte für Eier anzeigen
            
        elif selected_breakfast_subcategory == "Oatmeal":
            st.write("Oatmeal Recipes")
            # Hier kannst du spezifische Rezepte für Haferflocken anzeigen
            
        elif selected_breakfast_subcategory == "Smoothies":
            st.write("Smoothie Recipes")
            # Hier kannst du spezifische Rezepte für Smoothies anzeigen

import streamlit as st

# Initialize the water intake counter using session state
if "water_intake" not in st.session_state:
    st.session_state.water_intake = 0

# Display the water emoji
water_emoji = "💧"
st.write(water_emoji)

# Add a button to increment the water intake counter when clicked
if st.button("Drink a glass of water", water_emoji):
    st.session_state.water_intake += 1
    st.write("You drank a glass of water!")
    st.write("Total glasses of water drank today:", st.session_state.water_intake)


import streamlit as st
import pandas as pd

# Load diary data (if it exists)
diary_data = pd.read_csv("diary.csv") if "diary.csv" in st.session_state else pd.DataFrame(columns=["Date", "Entry"])

# Display the diary entry form
st.title("Diary")
entry_date = st.date_input("Date", value=pd.Timestamp.now())
entry_text = st.text_area("Enter your diary entry")

# Save the diary entry when submitted
if st.button("Save Entry"):
    diary_data = diary_data.append({"Date": entry_date, "Entry": entry_text}, ignore_index=True)
    diary_data.to_csv("diary.csv", index=False)
    st.success("Entry saved successfully!")

# Display existing diary entries
if not diary_data.empty:
    st.subheader("Previous Entries")
    st.write(diary_data)
else:
    st.info("No entries yet.")

st.write("Tracker Mood and stress")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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


