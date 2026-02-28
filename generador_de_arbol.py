import os
from pathlib import Path

def generar_arbol_ascii(ruta_directorio: Path, prefijo: str = "", lista_ignorar: set = None) -> str:
    """
    Recorre el directorio recursivamente y genera un árbol en formato ASCII.
    """
    if lista_ignorar is None:
        # Carpetas y archivos comunes que no aportan contexto útil a un LLM
        lista_ignorar = {
            '.git', '__pycache__', 'node_modules', 'venv', '.venv', 
            'env', '.idea', '.vscode', '.DS_Store', 'coverage',
            'generador_de_arbol.py', 'mapa_estructura.txt'
        }

    texto_arbol = ""
    
    try:
        # Obtener contenido del directorio
        entradas = list(ruta_directorio.iterdir())
        # Filtrar elementos no deseados
        entradas = [e for e in entradas if e.name not in lista_ignorar]
        # Ordenar: primero las carpetas, luego los archivos, alfabéticamente
        entradas.sort(key=lambda e: (not e.is_dir(), e.name.lower()))
    except PermissionError:
        return texto_arbol

    total = len(entradas)
    for i, entrada in enumerate(entradas):
        es_el_ultimo = (i == total - 1)
        conector = "└── " if es_el_ultimo else "├── "
        
        texto_arbol += f"{prefijo}{conector}{entrada.name}\n"
        
        # Si es un directorio, llamar recursivamente
        if entrada.is_dir():
            extension_prefijo = "    " if es_el_ultimo else "│   "
            texto_arbol += generar_arbol_ascii(
                entrada, 
                prefijo + extension_prefijo, 
                lista_ignorar
            )
            
    return texto_arbol

if __name__ == "__main__":
    # Obtener el directorio donde se ejecuta el script
    directorio_actual = Path.cwd()
    
    # Construir el resultado final
    resultado = f"📦 {directorio_actual.name}/\n"
    resultado += generar_arbol_ascii(directorio_actual)
    
    # Mostrar en la terminal
    print(resultado)
    
    # Guardar en un archivo de texto para copiar fácilmente
    archivo_salida = "mapa_estructura.txt"
    try:
        with open(archivo_salida, "w", encoding="utf-8") as f:
            f.write(resultado)
        print(f"\n✅ Mapa guardado exitosamente en: {archivo_salida}")
    except Exception as e:
        print(f"\n❌ Error al guardar el archivo: {e}")