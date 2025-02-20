

import streamlit as st
import numpy as np

"""
np.random.randn(3) generates a 1-dimensional array with 3 elements.
np.random.randn(10, 20) generates a 2-dimensional array with 10 rows and 20 columns.

"""

dataframe = np.random.randn(10, 20,)
st.dataframe(dataframe)

