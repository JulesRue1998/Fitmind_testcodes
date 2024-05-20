import pandas as pd
import streamlit as st
from datetime import datetime

st.subheader("Mood & Stress Tracker")

# Aktuelles Datum
current_date = datetime.now().date()

# DataFrame mit dem aktuellen Datum erstellen
data_df = pd.DataFrame(
    {
        "Datum": ["Stress"],
        "current_date": ["Mood"],
        "current_date": [None],
        "Verlauf der letzten 30 Tage": [None]
    }
)



st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.TextColumn(
            "Widgets",
            help="Streamlit **widget** commands 🎈",
            default="st.",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        )
    },
    hide_index=True,
)
