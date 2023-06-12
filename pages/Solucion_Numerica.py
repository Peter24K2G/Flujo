# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:12:43 2023

@author: Peter
"""

import streamlit as st

with open('pages/Numeric.md','r') as file:
    text = file.read()
    
st.markdown(text)

st.sidebar.markdown("# Solucion Numerica 🎉")