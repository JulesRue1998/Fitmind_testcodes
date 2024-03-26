import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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



