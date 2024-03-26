import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



st.sidebar.title("Menu")

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
