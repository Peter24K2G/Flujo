# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 15:11:35 2023

@author: Peter
"""

import streamlit as st
from PIL import Image
import Soluciones as sol
# import matplotlib.pyplot as plt
# import numpy as np

# st.sidebar.markdown("# Interfaz Grafica")
st.sidebar.markdown("## Parametros solucion analitica")
infty_slider = st.sidebar.slider("Numero de calculos en la longitud del medio",0, 10,9,key="oo")
delta_slider = st.sidebar.slider("Tiempo a evaluar [dias]",0,365,30,key="t")
delta_slider = st.sidebar.slider("dt",1,365,1,step=1,key="dt",label_visibility='collapsed')
st.sidebar.write("Mostrar solucion cada",st.session_state.dt,"dias")
st.sidebar.markdown("\n --- \n ## Parametros solucion numerica")
m_slider = st.sidebar.slider("n",0,10,9,key="n",label_visibility='collapsed')
st.sidebar.write("Discretizar la longitd del medio en",st.session_state.n,"elementos")
n_slider = st.sidebar.slider("m",0,365,30,key="m",label_visibility='collapsed')
st.sidebar.write("Realizar ",st.session_state.m,"calculos en la dimension temporal del medio")
delta_slider = st.sidebar.slider("DT",1,365,1,step=1,key="Dt",label_visibility='collapsed')
st.sidebar.write("Mostrar solucion cada",st.session_state.Dt,"espacios en la dimension temporal")


st.markdown("# Interfaz para la solucion de la Ecuacion de Flujo no Estacionario \n --- \n ## Problema planteado")

image = Image.open('Planteamiento.png')
st.image(image,caption='Planteamiento del Problema')

'Agregue los parametros del medio y las condiciones de contorno, segun la grafica'

col1, col2 = st.columns(2)
with col1:
    st.number_input("Almacenamiento [*10-2]",value=0.01,step=0.01, key="s")
    st.number_input("Transmisividad [m^2/d]",value=0.125, key="Tr")
    
with col2:
    st.number_input("Longitud del medio [m]",value=30, key="L")
    st.number_input("Cantidad inicial del nivel de agua [m]",value=10, key="hi")

st.markdown("--- \n ")

def callback(oo,n,m,s,Tr,L,t,hi,dt,Dt):
    fig1 = sol.analitic(oo,s,Tr,L,t,hi,dt)
    fig2 = sol.numeric(n,m,Tr,s,L,hi,Dt)
    del oo,n,m,s,Tr,L,t,hi,dt,Dt
    
    st.markdown("## Solucion Analitica")
    st.pyplot(fig1)
    
    st.markdown("## Solucion Numerica")
    st.pyplot(fig2)


st.button("Solucionar", on_click=callback, args=(
    st.session_state.oo, st.session_state.n, st.session_state.m,
    st.session_state.s,st.session_state.Tr, st.session_state.L,
    st.session_state.t, st.session_state.hi,st.session_state.dt,
    st.session_state.Dt))