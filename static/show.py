import networkx as nx
import pandas as pd
import requests
import plotly.graph_objects as go

# Suponiendo que tienes un DataFrame df con las columnas 'municipio', 'latitud', 'longitud'
# y un grafo G creado con NetworkX

# Crear un mapa base

def request():

    # URL de tu endpoint en Postman
    url = "http://127.0.0.1:8000/api/location/?place="

    # Hacer la solicitud HTTP
    response = requests.get(url)

    # Convertir la respuesta JSON a un diccionario de Python
    data = response.json()

    # Crear un DataFrame a partir del diccionario
    df = pd.DataFrame(data)

    # Ejemplo de cómo podría verse el DataFrame si la respuesta JSON es una lista de diccionarios
    # [{'municipio': 'Bogotá', 'latitud': 4.6097, 'longitud': -74.0817}, ...]
    print(df.head())
def draw():
    fig = go.Figure(go.Scattermapbox(
        lat=df['latitud'],
        lon=df['longitud'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=10,
            color='blue'
        )
    ))

    # Agregar las aristas (ejemplo simplificado)
    for edge in G.edges():
        x0, y0 = df.loc[df['municipio'] == edge[0], ['longitud', 'latitud']].values[0]
        x1, y1 = df.loc[df['municipio'] == edge[1], ['longitud', 'latitud']].values[0]
        fig.add_trace(go.Scattermapbox(
            mode="lines",
            lon=[x0, x1],
            lat=[y0, y1],
            marker=go.scattermapbox.Marker(size=10),
            line=dict(width=2, color='red')
        ))

    # Personalizar el mapa
    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_zoom=6,
        mapbox_center = {"lat": 4.6097, "lon": -74.0817} # Centro de Colombia
    )

    fig.show()