"""Dashboard: lluvias y declaratorias de emergencia en el Perú, ene-may 2022.

Correr en local, desde la carpeta assignment_3/:
    uv run streamlit run app.py
"""

import json
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# ---------------------------------------------------------------- configuracion
st.set_page_config(page_title="Lluvias y emergencias", page_icon="🌧️", layout="wide")

# Los datos se buscan junto a este archivo y no "donde se lanzó la app":
# en tu computadora corre desde esta carpeta, pero Streamlit Cloud la corre
# desde la raíz del repositorio y una ruta suelta no existe ahí.
CARPETA = Path(__file__).parent
FUENTE = "Fuente: Open-Meteo (reanálisis) y PCM en gob.pe, enero-mayo 2022"


# ------------------------------------------------------------------ carga datos
# @st.cache_data guarda el resultado: sin esto, los archivos se leen otra vez
# cada vez que alguien mueve un filtro.
@st.cache_data
def cargar():
    # dtype=str: el ubigeo "01" no puede perder su cero.
    datos = pd.read_csv(CARPETA / "datos" / "dataset.csv", dtype={"ubigeo": str})
    with open(CARPETA / "datos" / "departamentos.geojson", encoding="utf-8") as archivo:
        formas = json.load(archivo)
    return datos, formas


datos, formas = cargar()

# Una columna de texto es más legible en gráficos y en la tabla que un 0 o un 1.
datos["emergencia"] = "Sin declaratoria"
datos.loc[datos["declaratorias"] > 0, "emergencia"] = "Con declaratoria"

# ----------------------------------------------------------------------- filtros
st.sidebar.header("Filtros")

departamentos = sorted(datos["departamento"].unique())
elegidos = st.sidebar.multiselect(
    "Departamento", departamentos, default=departamentos
)

lluvia_minima = st.sidebar.slider(
    "Lluvia mínima (mm)", 0, int(datos["lluvia_total_mm"].max()), 0, step=50
)

estado = st.sidebar.selectbox(
    "Declaratoria de emergencia", ["Todos", "Con declaratoria", "Sin declaratoria"]
)

filtrado = datos[
    datos["departamento"].isin(elegidos) & (datos["lluvia_total_mm"] >= lluvia_minima)
]
if estado != "Todos":
    filtrado = filtrado[filtrado["emergencia"] == estado]

# ------------------------------------------------------------------------ titulo
st.title("🌧️ ¿Dónde llovió y dónde se declaró emergencia?")
st.caption(FUENTE)

if filtrado.empty:
    st.warning("Ningún departamento cumple los filtros. Ajusta la selección.")
    st.stop()

# ---------------------------------------------------------------------- metricas
c1, c2, c3, c4 = st.columns(4)
c1.metric("Departamentos", f"{len(filtrado)}")
c2.metric("Lluvia promedio (mm)", f"{filtrado['lluvia_total_mm'].mean():,.1f}")
c3.metric("Días de lluvia fuerte", f"{int(filtrado['dias_lluvia_fuerte'].sum())}")
c4.metric("Declaratorias", f"{int(filtrado['declaratorias'].sum())}")

st.divider()

# ---------------------------------------------------------------------- graficos
izq, der = st.columns(2)

with izq:
    por_lluvia = filtrado.sort_values("lluvia_total_mm", ascending=False)
    mas_lluvioso = por_lluvia.iloc[0]["departamento"]

    fig = px.bar(
        por_lluvia,
        x="lluvia_total_mm",
        y="departamento",
        orientation="h",
        title=f"{mas_lluvioso} es el departamento con más lluvia entre los elegidos",
        labels={"lluvia_total_mm": "Lluvia acumulada (mm)", "departamento": ""},
    )
    fig.update_yaxes(autorange="reversed")
    fig.update_layout(template="plotly_white", height=500)
    st.plotly_chart(fig, width="stretch")
    st.caption(FUENTE)

with der:
    fig = px.scatter(
        filtrado,
        x="lluvia_total_mm",
        y="dias_lluvia_fuerte",
        color="emergencia",
        hover_name="departamento",
        title="Más lluvia acumulada suele traer más días de lluvia fuerte",
        labels={
            "lluvia_total_mm": "Lluvia acumulada (mm)",
            "dias_lluvia_fuerte": "Días de lluvia fuerte",
            "emergencia": "",
        },
    )
    fig.update_layout(template="plotly_white", height=500)
    st.plotly_chart(fig, width="stretch")
    st.caption(FUENTE)

fig = px.box(
    filtrado,
    x="emergencia",
    y="lluvia_total_mm",
    points="all",
    hover_name="departamento",
    title="La lluvia de los departamentos con y sin declaratoria",
    labels={"emergencia": "", "lluvia_total_mm": "Lluvia acumulada (mm)"},
)
fig.update_layout(template="plotly_white", height=400)
st.plotly_chart(fig, width="stretch")
st.caption(FUENTE)

# -------------------------------------------------------------------------- mapa
st.subheader("Mapa de lluvia acumulada")

fig = px.choropleth_map(
    filtrado,
    geojson=formas,
    locations="ubigeo",
    featureidkey="properties.ubigeo",
    color="lluvia_total_mm",
    color_continuous_scale="Blues",
    map_style="open-street-map",
    zoom=4.2,
    center={"lat": -9.2, "lon": -75.0},
    opacity=0.7,
    hover_name="departamento",
    hover_data={
        "ubigeo": False,
        "lluvia_total_mm": True,
        "dias_lluvia_fuerte": True,
        "declaratorias": True,
    },
    labels={"lluvia_total_mm": "Lluvia (mm)"},
    height=550,
)
fig.update_layout(margin=dict(l=0, r=0, t=0, b=0))
st.plotly_chart(fig, width="stretch")
st.caption("Los departamentos sin datos filtrados no se pintan.")

# ------------------------------------------------------------------------- tabla
st.subheader("Datos filtrados")

tabla = filtrado[
    ["ubigeo", "departamento", "capital", "lluvia_total_mm",
     "dias_lluvia_fuerte", "declaratorias", "prorrogas"]
].sort_values("lluvia_total_mm", ascending=False)

st.dataframe(tabla, width="stretch", hide_index=True)

st.download_button(
    "Descargar datos filtrados (CSV)",
    tabla.to_csv(index=False).encode("utf-8"),
    "lluvias_filtrado.csv",
    "text/csv",
)
