# Assignment 1 – Fundamentos de Python

**Diplomado en Ciencia de Datos – PUCP | Grupo 9**

Tarea 1 del curso: práctica de listas, tuplas, diccionarios y NumPy, junto con
el flujo de trabajo colaborativo en GitHub (issues, commits y push).

## Integrantes

| Nombre | Usuario de GitHub |
| --- | --- |
| Victor Eduardo Roman Lazarte | [@victorroman1998](https://github.com/victorroman1998) |
| Amanda Valery Gomez Flores | [@av-gomez](https://github.com/av-gomez) |
| Roddy Edison Huarhua Rojas | [@roddyhuarhua-hub](https://github.com/roddyhuarhua-hub) |
| Jhanela Luz Carhuaz Fuster | [@Jhane080](https://github.com/Jhane080) |

## Estructura del repositorio

```
assignment_1_grupo_9/
│
├── README.md
└── assignment_1/
    ├── lists.ipynb          # Parte 1 – Listas
    ├── tuples.ipynb         # Parte 2 – Tuplas
    ├── dictionaries.ipynb   # Parte 3 – Diccionarios
    └── numpy.ipynb          # Parte 4 – NumPy
```

## Contenido de cada notebook

| Notebook | Tema | Operaciones principales |
| --- | --- | --- |
| `lists.ipynb` | Listas | `append()`, `sort()`, `max()`, `min()`, `len()` |
| `tuples.ipynb` | Tuplas | indexación, `max()`, `min()`, `len()`, inmutabilidad |
| `dictionaries.ipynb` | Diccionarios | `keys()`, `get()`, asignación, `pop()` |
| `numpy.ipynb` | NumPy | `arange()`, `zeros()`, `ones()`, `array()`, `.shape` |

## Organización del trabajo

El trabajo es **responsabilidad compartida de los cuatro integrantes**. Cada
parte tiene un issue que se usa como espacio de coordinación: ahí se avisa
quién está trabajando en qué, se resuelven dudas y se deja constancia de las
revisiones. Todos revisamos todas las partes antes de cerrar su issue.

| Issue | Parte | Notebook |
| --- | --- | --- |
| #1 | Lists | `lists.ipynb` |
| #2 | Tuples | `tuples.ipynb` |
| #3 | Dictionaries | `dictionaries.ipynb` |
| #4 | NumPy | `numpy.ipynb` |

### Criterios acordados

- Cada notebook abre identificando al Grupo 9.
- **Debajo de cada bloque de código va una celda de texto** que explica qué hace
  y por qué se eligió ese camino. Es requisito del curso: bloque sin explicación,
  o explicación que no corresponde al código, vale cero.
- Para mostrar un único valor se escribe la expresión suelta; `print()` solo
  cuando hay varios valores en la misma celda.
- Antes de cerrar un issue, el notebook debe ejecutarse de principio a fin sin
  errores y con las salidas guardadas.

## Cómo ejecutar los notebooks

Se requiere Python 3 y las siguientes librerías:

```bash
pip install numpy jupyter
```

Luego, desde la carpeta `assignment_1/`:

```bash
jupyter notebook
```

También pueden abrirse directamente en VS Code con la extensión de Jupyter.
