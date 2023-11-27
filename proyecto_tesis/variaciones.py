import re
from difflib import SequenceMatcher

def normalizar_palabra_clave(palabra_clave):
    # Agrega aquí más variaciones según sea necesario
    variaciones = [
        palabra_clave, re.sub(r'[^\w\s]', '', palabra_clave), 
        re.sub(r'[^\w\s]', ' ', palabra_clave), 
        re.sub(r'\s', '', palabra_clave), 
        re.sub(r'\s', ' ', palabra_clave),
        re.sub(r'(\w)\.(\w)', r'\1 \2', palabra_clave),  # Reemplaza puntos con espacio entre letras
        palabra_clave.replace("/", " "),  # Reemplaza "/" con espacio
        palabra_clave.replace("ESP", ""),  # Elimina "ESP"
        palabra_clave.replace("C ", "C")  # Elimina espacio después de "C"
    ]
    return variaciones

def encontrar_variaciones(texto, palabra_clave):
    # Normaliza la palabra clave y genera patrones
    variaciones = normalizar_palabra_clave(palabra_clave)
    
    # Crea una expresión regular para buscar variaciones
    patrones = '|'.join(re.escape(variacion) for variacion in variaciones)

    # Encuentra todas las coincidencias en el texto
    coincidencias = re.findall(patrones, texto, flags=re.IGNORECASE)
    
    # También utiliza SequenceMatcher para encontrar variaciones basadas en similitud
    for variacion in normalizar_palabra_clave(palabra_clave):
        ratio = SequenceMatcher(None, variacion.lower(), texto.lower()).ratio()
        if ratio > 0.6:  # Ajusta el umbral según sea necesario
            coincidencias.append(variacion)

    return coincidencias

# Ejemplo de uso
texto_etiqueta = "C.E., C/E, C ESP"
palabra_clave_estandar = "CE"

resultados = encontrar_variaciones(texto_etiqueta, palabra_clave_estandar)
print("Palabra clave estándar:", palabra_clave_estandar)
print("Variaciones encontradas:", resultados)
