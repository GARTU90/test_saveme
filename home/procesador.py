# Arreglo en memoria donde se guardan las respuestas
respuestas_guardadas = []

# Diccionario de keywords médicas
palabras_clave = {
    'dolor': 'síntoma general',
    'dolor de cabeza': 'neurológico',
    'mareo': 'neurológico',
    'dolor abdominal': 'digestivo',
    'resequedad': 'dermatológico',
    'nauseas': 'digestivo',
    'fiebre': 'infeccioso',
    'tos': 'respiratorio',
    'diarrea': 'digestivo',
    'vómito': 'digestivo'
}

def procesar_respuesta(seguro, problema):
    entrada = {
        'seguro': seguro,
        'problema': problema,
    }

    respuestas_guardadas.append(entrada)

    texto = problema.lower()
    encontrados = []

    for palabra, categoria in palabras_clave.items():
        if palabra in texto:
            encontrados.append((palabra, categoria))

    return encontrados
