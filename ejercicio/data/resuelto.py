# Acceder al archivo CSV
archivo = open('Listado-Instituciones-Educativas-distribuidas-por-zona-distrito-y-circuito.csv', "r")

# Obtener las líneas del archivo
lineas = archivo.readlines()

# Cerrar el archivo CSV
archivo.close()

# Obtener los encabezados
encabezados = lineas[0].strip().split("|")

# Iterar sobre las líneas del archivo (excepto el encabezado)
for linea in lineas[1:]:
    # Separar los campos de la línea
    campos = linea.strip().split("|")

    # Construir el contenido HTML
    contenido_html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Información de la Institución Educativa</title>
        <style>
            /* Estilos CSS aquí */
            body {
                font-family: Arial, sans-serif;
            }
            .container {
                margin: 20px;
            }
            .campo {
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Información de la Institución Educativa</h1>
            <p class="campo">%s:</p> <p>%s</p>
            <p class="campo">%s:</p> <p>%s</p>
            <p class="campo">%s:</p> <p>%s</p>
            <p class="campo">%s:</p> <p>%s</p>
            <p class="campo">%s:</p> <p>%s</p>
            <p class="campo">%s:</p> <p>%s</p>
            <p class="campo">%s:</p> <p>%s</p>
            <p class="campo">%s:</p> <p>%s</p>
            <p class="campo">%s:</p> <p>%s</p>
            <p class="campo">%s:</p> <p>%s</p>
            <p class="campo">%s:</p> <p>%s</p>
            
        </div>
    </body>
    </html>
    """ % (encabezados[0], campos[0],encabezados[1], campos[1], encabezados[2], campos[2],encabezados[3], campos[3],encabezados[4], campos[4],encabezados[5], campos[5],encabezados[6], campos[6],
        encabezados[7], campos[7],encabezados[13], campos[13],encabezados[14], campos[14],encabezados[15], campos[15])

    # Obtener el nombre del archivo HTML (usando el primer campo como nombre)
    nombre_archivo = "resultados/%s.html" % campos[0]

    # Escribir el contenido HTML en el archivo
    with open(nombre_archivo, "w") as archivo_html:
        archivo_html.write(contenido_html)

    print(f"Archivo HTML generado: {nombre_archivo}")
