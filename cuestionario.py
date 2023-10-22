# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:12:20 2023

@author: Daniel
"""

import streamlit as st
import requests
import json

api_key = st.secrets['at_token']
base_id = 'appFezarrh9fv6WrS'
table_name = 'cuestionario'
headers = {"Authorization" : f"Bearer {api_key}",  "Content-Type" : 'application/json' }
contenedor = st.container()
name = contenedor.text_input('Nombre')
incidencias = contenedor.text_input('Incidencias')
calidad = contenedor.text_input('Calidad del Servicio')


calificacion = contenedor.select_slider('Calificacion: de 1 (muy mal) a 5 (excelente)',options=[1,2,3,4,5])

b_1 = st.button('ENVIAR')
if b_1:
    data = {
  "records": [
    {
      "fields": {
        "Name": name,
        "Calidad Servicio": calidad,
        "Incidencias": incidencias,
        "Calificacion": calificacion
      }
    }]}
    requests.post(r'https://api.airtable.com/v0/appFezarrh9fv6WrS/cuestionario', json.dumps(data),headers=headers)