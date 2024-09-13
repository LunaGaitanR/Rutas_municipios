import networkx as nx
import pandas as pd
import plotly.graph_objects as go
from algorithm import neighbors

def draw():
    df=neighbors.getData()
    G=nx.Graph()
    G.add_nodes_from(neighbors.getGraph())
    
    for city, neighbors_dict in neighbors.getGraph().items():
        G.add_node(city)
        for neighbor, distance in neighbors_dict.items():
            G.add_edge(city, neighbor, weight=distance)
            
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