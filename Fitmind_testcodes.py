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


