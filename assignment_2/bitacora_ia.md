# Bitácora de uso de IA – Assignment 2 (Grupo 9)

Herramienta usada: Claude (asistente de IA). Todo el código sugerido se ejecutó y verificó en nuestros notebooks antes de aceptarlo.

## Entrada 1 – Parte 1: selector de Selenium
- **Qué pedí:** código para extraer el número, el título y el link de cada decreto en los resultados de búsqueda de gob.pe.
- **Qué respondió la IA:** buscar el título con el selector CSS `h3 a` dentro de cada `article`.
- **Qué estaba mal y cómo lo noté:** al ejecutar salió `NoSuchElementException`. La página no tiene un `h3` con link dentro del artículo.
- **Cómo lo corregí:** inspeccionamos el texto del `article`. El número está en la línea antes de "Publicado" y el título en la línea siguiente. El link es el primer `<a>` cuyo `href` contiene `/normas-legales/`. Verificamos que la cantidad extraída coincidiera con la de la web en cada mes (enero 8/8, febrero 5/5, marzo 5/5, abril 4/4, mayo 7/7).

## Entrada 2 – Parte 1: departamentos mal detectados (Ica)
- **Qué pedí:** detectar qué departamentos menciona el título de cada decreto.
- **Qué respondió la IA:** primero, buscar cada nombre con `if d in titulo`.
- **Qué estaba mal y cómo lo noté:** con un título de prueba sobre Huancavelica, la búsqueda devolvía `['Huancavelica', 'Ica']`, porque "Ica" está dentro de "Huancavelica".
- **Cómo lo corregí:** usamos una expresión regular con límites de palabra, `re.search(r"\b" + d + r"\b", titulo)`. Con el mismo ejemplo ahora devuelve solo `['Huancavelica']`.

## Entrada 3 – Parte 2: capitales de Wikipedia
- **Qué pedí:** obtener la lista de departamentos y sus capitales desde Wikipedia con `pd.read_html`.
- **Qué respondió la IA:** tomar la tabla de departamentos y usar la columna de capital tal cual.
- **Qué estaba mal y cómo lo noté:** la tabla tenía 24 filas y faltaba el Callao. Además, algunas capitales venían con notas como `[1]` o "(de facto)"; para Lima aparecía "Huacho (de facto)".
- **Cómo lo corregí:** agregamos el Callao desde otra tabla de la página y limpiamos los corchetes y paréntesis. Para Lima usamos la ciudad de Lima, porque el ubigeo 15 incluye a Lima Metropolitana. Luego comprobamos que la geocodificación devolviera el departamento correcto en los 25 casos (0 discrepancias).

## Entrada 4 – Instalación de librerías
- **Qué pedí:** instalar las librerías dentro del notebook.
- **Qué respondió la IA:** usar `%pip install selenium requests beautifulsoup4 pandas`.
- **Qué estaba mal y cómo lo noté:** apareció "No module named pip". El entorno virtual (.venv) no tenía pip instalado.
- **Cómo lo corregí:** ejecutamos primero `!"{sys.executable}" -m ensurepip --upgrade` y después el `%pip install` funcionó.

## Entrada 5 – Parte 1: NameError por un import perdido
- **Qué pedí:** reemplazar un bloque de código del bucle por meses.
- **Qué respondió la IA:** un bloque nuevo sin la línea `import pandas as pd`.
- **Qué estaba mal y cómo lo noté:** al ejecutar salió `NameError: name 'pd' is not defined`.
- **Cómo lo corregí:** agregamos `import pandas as pd` al inicio de la celda. Aprendimos a revisar los imports cada vez que se reemplaza código.