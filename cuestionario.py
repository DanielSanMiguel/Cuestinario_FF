# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 21:12:20 2023

@author: Daniel
"""

import streamlit as st
import requests
import json
from PIL import Image
#import os
#from dotenv import load_dotenv
#load_dotenv('C:\\Users\\Daniel\\Desktop\\Python\\.env')
#api_key = os.environ.get('Token_flyfut')
api_key = st.secrets['at_token']
base_id = 'appFezarrh9fv6WrS'
table_name = 'cuestionario'
headers = {"Authorization" : f"Bearer {api_key}",  "Content-Type" : 'application/json' }
image = Image.open('logo.png')
clients = ['analista_1', 'analista_2']
pilots = ['piloto_1', 'piloto_2']

user = st.text_input('Introduzca su nombre completo:')
if user in clients:
    st.image(image)
    contenedor = st.container()
    contenedor.write(user)
    incidencias = contenedor.text_input('Incidencias')
    calidad = contenedor.text_input('Calidad del Servicio')
    calificacion = contenedor.select_slider('Calificacion: de 1 (muy mal) a 5 (excelente)',options=[1,2,3,4,5])
    
    b_1 = st.button('ENVIAR')
    if b_1:
        data = {
      "records": [
        {
          "fields": {
            "Name": user,
            "Calidad Servicio": calidad,
            "Incidencias": incidencias,
            "Calificacion": calificacion
          }
        }]}
        requests.post(r'https://api.airtable.com/v0/appFezarrh9fv6WrS/cuestionario', json.dumps(data),headers=headers)
elif user in pilots:
    contenedor_2 = st.container()
    incidencias = contenedor_2.text_input('Incidencias')
    calificacion = contenedor_2.select_slider('Calificacion: de 1 (muy mal) a 5 (excelente)',options=[1,2,3,4,5])
    
    b_1 = st.button('ENVIAR')
    if b_1:
        data = {
      "records": [
        {
          "fields": {
            "Name": user,
            "Incidencias": incidencias,
            "Calificacion": calificacion
          }
        }]}
        requests.post(r'https://api.airtable.com/v0/appFezarrh9fv6WrS/cuestionario', json.dumps(data),headers=headers)
else:
    st.write('Nombre incorrecto, vuleva a intentarlo.')
