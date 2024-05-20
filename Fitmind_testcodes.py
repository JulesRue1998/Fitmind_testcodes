import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(1, 5), columns=["Mood", "Stress"])

st.table(df)
