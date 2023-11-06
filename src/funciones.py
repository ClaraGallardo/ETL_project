import requests
import json
import pandas as pd

with open('API.txt') as file:
    
    key = file.read() #cargo mi contraseña y la guardo en una variable

def limpieza_tipo(df):

    '''
    Función creada para limpiar toda la columna del dataframe de Tripadvisor
    '''

    df.Tipo = df.Tipo.str.replace(r'(€+)', '', regex=True)
    df.Tipo = df.Tipo.str.replace('Asiática','')
    df.Tipo = df.Tipo.str.replace(r'.*Ita.*', 'Italiana', regex=True)
    df.Tipo = df.Tipo.str.replace(r'Japonesa, [A-Za-z]+', 'Japonesa', regex=True)
    df.Tipo = df.Tipo.str.replace(r'China, [A-Za-z]+', 'China', regex=True)
    df.Tipo = df.Tipo.str.replace(r'Mexicana, [A-Za-z]+', 'Mexicana', regex=True)
    df.Tipo = df.Tipo.str.replace(r'Americana, [A-Za-z]+', 'Americana', regex=True)
    df.Tipo = df.Tipo.str.replace(r'Shushi [A-Za-z]+', 'Japonesa', regex=True)
    df.Tipo = df.Tipo.str.replace('Italianaánea','Italiana')
    df.Tipo = df.Tipo.str.replace('Americanaña','Americana')
    df.Tipo = df.Tipo.str.replace('Japonesaé','Japonesa')
    df.Tipo = df.Tipo.str.replace('Mexicanaña','Mexicana')
    df.Tipo = df.Tipo.str.replace('Chinaé','China')
    df.Tipo = df.Tipo.str.replace(', ','')
    df.Tipo = df.Tipo.str.replace('InternacionalSushi','Sushi')
    df.Tipo = df.Tipo.str.replace('IndiaInternacional', 'India')
    df.Tipo = df.Tipo.str.replace('CaribeñaLatina','Caribeña')
    df.Tipo = df.Tipo.str.replace('CaribeñaLatina','Caribeña')
    df.Tipo = df.Tipo.str.replace('PeruanaLatina','Peruana')
    df.Tipo = df.Tipo.str.replace('LatinaVenezolana','Venezolana')
    df.Tipo = df.Tipo.str.replace('FrancesaCaribeña','Caribeña')
    df.Tipo = df.Tipo.str.replace('MediterráneaSaludable','Mediterránea')
    df.Tipo = df.Tipo.str.replace('IndiaSaludable','India')
    df.Tipo = df.Tipo.str.replace('LatinaColombiana','Colombiana')
    df.Tipo = df.Tipo.str.replace('TurcaDe Oriente Medio','Turca')
    df.Tipo = df.Tipo.str.replace('Sushi','Japonesa')
    df.Tipo = df.Tipo.str.replace('Restaurante de carneBarbacoa','Argentino')


def consulta_API(tipo):

    '''
    Realiza una consulta a la API de Google Places para buscar restaurantes cercanos de un tipo específico, devuelve una lista llamada 'results'.

    Args:
        tipo (str): El tipo de restaurante que se desea buscar, por ejemplo, "coreano".

    Returns:
        list: Una lista de diccionarios con información de restaurantes que coinciden con el tipo especificado.
    '''

    API_URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"

    # Parámetros de la consulta
    params= {
    "location": "40.416709,-3.690286",
    "radius": 20000,
    "type": "restaurant",
    "keyword": [tipo],
    "language": "es",
    "key": key
    }

    response = requests.get(API_URL, params=params)

    if response.status_code != 200:

        raise Exception("Error al realizar la consulta: {} {}".format(response.status_code, response.content))

    data = json.loads(response.content)

    results = data["results"]

    # Filtra los resultados por puntuación
    results = [result for result in results if result["rating"] is not None]

    #Añade el tipo de restaurante
    for result in results:
        result["tipo"] = result["types"][0]


    return results

def optim(df):

    '''
    Optimiza los datos de un dataframe.

    Args:
        dataframe(pandas.DataFrame): El DataFrame que optimizas
    '''
    int_columnas = df.select_dtypes(include=['int']).columns
    df[int_columnas] = df[int_columnas].apply(pd.to_numeric, downcast='integer')

    float_columnas = df.select_dtypes(include=['float']).columns
    df[float_columnas] = df[float_columnas].apply(pd.to_numeric, downcast='float')

    object_columnas = df.select_dtypes(include=['object']).columns
    df[object_columnas] = df[object_columnas].astype('category')

    datetime_columnas = df.select_dtypes(include=['datetime']).columns
    df[datetime_columnas] = df[datetime_columnas].apply(pd.to_datetime, errors='coerce')

    return df

def convertir_coordenadas(columna_x, columna_y):
  """Convierte dos columnas de coordenadas a un formato de coordenada.

  Args:
    columna_x: La columna de coordenadas X.
    columna_y: La columna de coordenadas Y.

  Returns:
    Una lista de coordenadas en formato de coordenada.
  """

  # Convertimos las coordenadas a números enteros.

  columna_x = columna_x.astype(int)
  columna_y = columna_y.astype(int)

  # Multiplicamos las coordenadas por el factor de escala.

  factor_escala = 1e-7
  columna_x = columna_x * factor_escala
  columna_y = columna_y * factor_escala

  # Convertimos las coordenadas a formato de coordenada.

  coordenadas = []
  for x, y in zip(columna_x, columna_y):
    coordenadas.append(f"{x},{y}")

  return coordenadas
