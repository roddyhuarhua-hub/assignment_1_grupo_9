# Assignment 3 · Lluvias y declaratorias de emergencia (ene-may 2022)

**Grupo 9** · Diplomado PUCP 2026

**Dashboard:** _(pega aquí el enlace `https://....streamlit.app` después de desplegar)_

## 1. ¿Qué pregunta responde este dashboard?

¿Los departamentos donde más llovió entre enero y mayo de 2022 son los mismos
donde la PCM declaró estado de emergencia por lluvias?

## 2. ¿De dónde vienen los datos y de cuándo son?

Es la `tabla_final.csv` del Assignment 2, una fila por departamento (25 en
total). Cubre del **1 de enero al 31 de mayo de 2022**.

| Variable | Fuente |
|---|---|
| Lluvia acumulada y días de lluvia fuerte | [Open-Meteo](https://open-meteo.com) (reanálisis), medida en la capital de cada departamento |
| Declaratorias y prórrogas de emergencia | Decretos supremos de la PCM publicados en [gob.pe](https://www.gob.pe/pcm) |
| Fronteras departamentales | GeoJSON de la sesión 7 del curso |

## 3. ¿Qué encontraste?

1. **La lluvia sigue la geografía.** Loreto (1,581.8 mm), Ucayali (1,288.8 mm) y
   Áncash (975.3 mm) acumulan lo más alto; la costa sur casi no recibe
   (Tacna 11.5 mm, Moquegua 17.8 mm).
2. **Las declaratorias no coinciden con la lluvia.** Solo hay 3 departamentos
   con declaratoria (Amazonas, Ayacucho y Piura) y ninguno está entre los 3
   más lluviosos. Loreto y Ucayali acumulan más de 1,000 mm y no tienen
   ninguna.
3. **Más lluvia total suele ir con más días de lluvia fuerte**: Loreto (25
   días) y Ucayali (20 días) lideran en ambas.

## 4. ¿Qué limitaciones tiene lo que hiciste?

- **Un solo punto por departamento.** La lluvia se mide en la capital, no en
  todo el territorio. Lima y Callao tienen el mismo valor (39.2 mm) porque
  caen en la misma celda del modelo.
- **Reanálisis, no estaciones.** Open-Meteo estima la lluvia con un modelo; no
  son mediciones de SENAMHI.
- **Solo 3 casos con declaratoria.** Con tan pocos casos no se puede afirmar
  una relación estadística, solo describir lo observado.
- **Una emergencia depende del daño, no solo de la lluvia.** Aquí no tenemos
  variables de vulnerabilidad, viviendas ni infraestructura.
- **Solo ene-may 2022.** No sabemos si otra temporada muestra el mismo patrón.

## Contenido de la carpeta

| Archivo | Qué es |
|---|---|
| `visualizacion.ipynb` | Parte 1: tres gráficos con Plotly Express |
| `mapas.ipynb` | Parte 2: cruce por ubigeo, mapas con Geopandas y Folium |
| `app.py` | Parte 3: dashboard en Streamlit |
| `requirements.txt` | Librerías que necesita la app |
| `datos/` | `dataset.csv`, `departamentos.geojson`, `ubigeos.csv` y el GeoJSON original |

## Correr en local

```bash
cd assignment_3
uv run streamlit run app.py
```
