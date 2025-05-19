from zipfile import ZipFile

def get_lines_from_zip(path):
    archive = ZipFile(path, 'r')
    files = archive.namelist()
    all_lines = []
    filenames = []

    for file in files:
        with archive.open(file) as file_content:
            content = file_content.read().decode('utf-8')
            lines = content.splitlines()
            all_lines.append(lines)
            filenames.append(file)
    return all_lines, filenames

def find_matching_lines(lines1, lines2):
    matching = []
    for i, line1 in enumerate(lines1):
        for j, line2 in enumerate(lines2):
            if line1.strip() == line2.strip() and line1.strip() != "":
                matching.append((i + 1, j + 1))  # líneas coincidentes
    return matching

def to_html_with_highlight(lines, highlight_indices, title):
    html_lines = []
    for i, line in enumerate(lines):
        if (i + 1) in highlight_indices:
            html_lines.append(f'<span style="background-color: yellow;">{i+1:03d}: {line}</span>')
        else:
            html_lines.append(f'<span>{i+1:03d}: {line}</span>')
    return f'<h2>{title}</h2><pre style="background-color: #f0f0f0; padding: 10px;">' + '\n'.join(html_lines) + '</pre>'
