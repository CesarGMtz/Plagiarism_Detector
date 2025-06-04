from line_matcher import get_lines_from_zip, find_matching_lines, to_html_with_highlight

# Cargar los códigos desde un ZIP
codes, filenames = get_lines_from_zip('codes/add.zip')

# Asumimos que solo hay 2 archivos
lines1 = codes[0]
lines2 = codes[1]

# Encontrar líneas iguales
matching = find_matching_lines(lines1, lines2)

# Obtener índices de líneas iguales por archivo
matched_lines1 = [i for i, _ in matching]
matched_lines2 = [j for _, j in matching]

# Generar HTML resaltado
html1 = to_html_with_highlight(lines1, matched_lines1, f"Archivo: {filenames[0]}")
html2 = to_html_with_highlight(lines2, matched_lines2, f"Archivo: {filenames[1]}")

# Juntar HTML
full_html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Plagio Detectado</title>
</head>
<body>
    <h1>Resultados de Comparación</h1>
    <p><b>Líneas iguales detectadas:</b> {len(matching)}</p>
    <p><b>Porcentaje de plagio:</b> {round(len(matching) / min(len(lines1), len(lines2)) * 100, 2)}%</p>
    <div style="display: flex; gap: 40px;">
        <div>{html1}</div>
        <div>{html2}</div>
    </div>
</body>
</html>
"""

# Guardar en archivo
with open("res_plagio.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Archivo HTML generado: res_plagio.html")
