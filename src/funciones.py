

def limpieza_tipo(df):

    df.Tipo = df.Tipo.str.replace(r'(€+)', '', regex=True)
    df.Tipo = df.Tipo.str.replace('Asiática','')
    df.Tipo = df.Tipo.str.replace(r'.*Ita.*', 'Italiana', regex=True)
    df.Tipo = df.Tipo.str.replace(r'Japonesa, [A-Za-z]+', 'Japonesa', regex=True)
    df.Tipo = df.Tipo.str.replace(r'China, [A-Za-z]+', 'China', regex=True)
    df.Tipo = df.Tipo.str.replace(r'Mexicana, [A-Za-z]+', 'Mexicana', regex=True)
    df.Tipo = df.Tipo.str.replace(r'Americana, [A-Za-z]+', 'Americana', regex=True)
    df.Tipo = df.Tipo.str.replace(r'Shushi [A-Za-z]+', 'Japonesa', regex=True)
    df.Tipo  =df.Tipo.str.replace('Italianaánea','Italiana')
    df.Tipo  =df.Tipo.str.replace('Americanaña','Americana')
    df.Tipo  =df.Tipo.str.replace('Japonesaé','Japonesa')
    df.Tipo  =df.Tipo.str.replace('Mexicanaña','Mexicana')
    df.Tipo  =df.Tipo.str.replace('Chinaé','China')
    df.Tipo  =df.Tipo.str.replace(', ','')
    df.Tipo = df.Tipo.str.replace('InternacionalSushi','Sushi')
    df.Tipo = df.Tipo.str.replace('IndiaInternacional', 'India')
    