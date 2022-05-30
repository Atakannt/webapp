import streamlit as st
import pandas as pd
import numpy as np


df = pd.DataFrame(np.zeros((10,20)))

st.dataframe(df)