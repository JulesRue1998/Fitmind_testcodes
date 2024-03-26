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
from datetime import datetime
from streamlit_daterange_picker import st_daterange_picker

# Title and instructions
st.title("Diary App")
st.write("Welcome to the Diary App! Select a date range to view or write entries.")

# Date range picker
start_date, end_date = st_daterange_picker(label="Select Date Range", start_date=datetime.now(), end_date=datetime.now())

# Diary entry input
diary_entry = st.text_area("Write your diary entry here:")

# Save button
if st.button("Save Entry"):
    with open("diary_entries.txt", "a") as file:
        file.write(f"Date Range: {start_date} - {end_date}\n")
        file.write(f"Entry: {diary_entry}\n")
        file.write("-" * 50 + "\n")
    st.success("Entry saved successfully!")

# Display existing entries
with open("diary_entries.txt", "r") as file:
    entries = file.readlines()
    st.write("## Existing Entries:")
    for entry in entries:
        st.write(entry.strip())


