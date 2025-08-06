import pandas as pd
import numpy as np
import pickle
import os
from tensorflow import keras
from django.shortcuts import render
from .forms import PrediccionForm

from django.conf import settings
from django.shortcuts import render



def predecir_precio(request):
    resultado = None
    barrio = None

    if request.method == 'POST':
        form = PrediccionForm(request.POST)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            habitaciones = form.cleaned_data['habitaciones']
            baños = form.cleaned_data['baños']
            area = form.cleaned_data['area']
            barrio = form.cleaned_data['barrio']
            upz = form.cleaned_data['upz']


            # Cargar scaler, modelo y columnas
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            modelo_path = os.path.join(BASE_DIR, 'modelos', 'model.h5')
            scaler_path = os.path.join(BASE_DIR, 'modelos', 'scaler.pkl')
            columnas_path = os.path.join(BASE_DIR, 'modelos', 'columnas.pkl')

            model = keras.models.load_model(modelo_path)
            with open(scaler_path, 'rb') as f:
                scaler = pickle.load(f)
            with open(columnas_path, 'rb') as f:
                columnas = pickle.load(f)

            # Crear dataframe con una sola fila
            df_nuevo = pd.DataFrame([{
                'Tipo': tipo,
                'Habitaciones': habitaciones,
                'Baños': baños,
                'Área': area,
                'Barrio': barrio,
                'UPZ': upz

            }])


            # Hacer get_dummies para Tipo, Barrio y UPZ
            df_nuevo_encoded = pd.get_dummies(df_nuevo, columns=['Tipo', 'UPZ','Barrio'])

            # Añadir columnas que falten y reordenar
            for col in columnas:
                if col not in df_nuevo_encoded.columns:
                    df_nuevo_encoded[col] = 0
            df_nuevo_encoded = df_nuevo_encoded[columnas]

            # Escalar
            X_nuevo_scaled = scaler.transform(df_nuevo_encoded)

            # Predecir
            prediccion = model.predict(X_nuevo_scaled)
            resultado = round(prediccion[0][0], 2)
    else:
        form = PrediccionForm()

    return render(request, 'prediccion_form.html', {'form': form, 'resultado': resultado, 'barrio': barrio , "API_KEY": settings.GOOGLE_MAPS_API_KEY})
# predictor/views.py



