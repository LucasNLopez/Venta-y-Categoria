# funciones.py

import pandas as pd
import sys

# Definición de los diccionarios de productos padre por categoría
categorias_china = {
    "Inc. 90 VL": ["Trasero Inc.", "Delantero Inc."],
    "Rueda": ["Bola de Lomo", "Cuadrada", "Nalga S/T", "Peceto"],
    "SSHM": ["Brazuelo", "Garrón", "Tortuguita"],
    #"Mix Cuts GF": ["Bola de Lomo", "Cuadrada", "Peceto", "Aguja", "Chingolo",
    #                "Cogote", "Marucha", "Pecho", "Paleta", "Nalga S/T"], - cuando la contramarca de estos productos es GF
    "FFQ": ["Aguja", "Chingolo", "Cogote", "Marucha", "Pecho", "Paleta"],
    #"ASADO S/H": ["Asado S/Hueso"],
    "ASADO C/H": ["Asado C/Hueso"],
    "Fat": ["Grasa Caja"],
    "FALDA C/HUESO": ["Falda"],
    "VACIO": ["Vacio"],
    "R&L": ["Bife Ancho","Bife Angosto","Lomo","Tapita de Cuadril"],
    "RUMP": ["Cuadril"],
    "Mix Huesos": ["H. Upper Bone", "H. Neck Bone", "H. Lumbar Bone", "H. Lower Bone", "H. Knee Bone",
                    "H. Feather Bone", "H. Chuck Bone", "H. Brisket Bone", "H. Humerus Bone", "H. Radius Bone", "H. Tibia Bone"],
    "Trimming 70vl": ["Trimming 70 VL"],
    #"6 Cortes D/E": ["Trasero Inc.", "Delantero Inc.", "Brazuelo", "Garrón", "Tortuguita", "Asado S/Hueso"] - cuando la contramarca de estos productos es  95VL
}

categorias_hilton = {
    "R&L": ["Bife Ancho", "Bife Angosto", "Lomo","Cuadril"],
    "Picanha": ["Tapita de Cuadril"],
    "Rueda": ["Bola de Lomo", "Cuadrada", "Nalga S/T", "Peceto"]
}
categorias_no_hilton = {
    "R&L": ["Bife Ancho", "Bife Angosto", "Lomo","Cuadril"],
    "Picanha": ["Tapita de Cuadril"],
    "Rueda": ["Bola de Lomo", "Cuadrada", "Nalga S/T", "Peceto"]
}

categorias_estados_unidos = {
    "RUMP": ["Cuadril"],
    "Mix Cuts": ["Entraña","Vacio","Tapita de Cuadril","Bife Ancho", "Bife Angosto", "Lomo"],
    "Colita de Cuadril": ["Colita de Cuadril"],
    "Incompleto 85CL": ["Trasero Inc.", "Delantero Inc."]
}

categorias_3ros_paises = {
    "R&L": ["Bife Ancho", "Bife Angosto", "Lomo","Cuadril"],
    "Picanha": ["Tapita de Cuadril"]
}

categorias_canada = {
    "Incompleto 85CL": ["Trasero Inc.", "Delantero Inc."]
}

categorias_mexico = {
    "Rueda": ["Bola de Lomo", "Nalga C/T", "Nalga Afuera"],
}
categorias_sudafrica = {
    "Fat": ["Grasa Caja"]
}
categorias_israel = {
    "Kosher": ["Aguja","Asado S/Hueso","Bife Ancho","Brazuelo","Chingolo","Cogote","Grasa Caja","Intercostales",
            "Marucha","Menudencias","Paleta","Pecho","Seso","Tapa Bife","Tapa de Aguja","Trimming 70 VL"
            ]
}
categorias_481 ={
    "FULL SET": ["Nalga S/T","Paleta","Bola de Lomo","Cuadrada","Colita de Cuadril","Cuadril",
                "Lomo","Peceto","Aguja","Chingolo","Marucha","Tapita de Cuadril","Bife Ancho","Bife Angosto","Pecho","Vacio",]
}
# Definición de los destinos comerciales
destinos = {
    "China": ["China"],
    "Hilton": ["Hilton"],
    "No Hilton": ["No Hilton"],
    "Estados Unidos": ["Estados Unidos"],
    "3ros Paises": ["3ros Paises"],
    "Mexico": ["Mexico"],
    "Canada": ["Canada"],
    "Sudafrica": ["Sudafrica"],
    "Israel": ["Israel"],
    "481": ["481"]
}
def filtro_6cortes(df):
    filtro_6cortes = ["Trasero Inc.", "Delantero Inc.", "Brazuelo", "Garrón", "Tortuguita", "Asado S/Hueso"]
    categorias_final = pd.DataFrame(columns=["Nro Etiqueta", "Venta", "Categoria"])

    for vl in filtro_6cortes:
        filtro_producto = df["Producto Padre"] == vl
        filtro_contramarca = df["Contramarca"] == "95VL"
        df_filtrado = df[filtro_producto & filtro_contramarca]

        if not df_filtrado.empty:
            df_temp = pd.DataFrame({
                "Nro Etiqueta": df_filtrado["Nro Serie"],
                "Venta": "",
                "Categoria": "6 Cortes D/E"
            })
            categorias_final = pd.concat([categorias_final, df_temp], ignore_index=True)

    return categorias_final
def procesar_data(df):
    categorias_final = pd.DataFrame(columns=["Nro Etiqueta", "Venta", "Categoria", "Destino"])

    for destino, destinos_comerciales in destinos.items():
        nombre_variable = f'categorias_{destino.lower().replace(" ", "_")}'
        if nombre_variable in globals():
            diccionario = globals()[nombre_variable]
            for categoria, productos in diccionario.items():
                filtro_producto = df["Producto Padre"].isin(productos)
                
                # Convertir destinos_comerciales a una lista de strings
                destinos_comerciales = list(map(str, destinos_comerciales))
                
                filtro_destino = df["Destino Comercial"].astype(str).isin(destinos_comerciales)
                filtro_final = filtro_producto & filtro_destino
                df_filtrado = df[filtro_final]
                df_final = pd.DataFrame({
                    "Nro Etiqueta": df_filtrado["Nro Serie"],
                    "Venta": "",
                    "Categoria": categoria,
                    "Destino": destino
                })
                categorias_final = pd.concat([categorias_final, df_final], ignore_index=True)
        else:
            print(f"Error: No se encontró el diccionario para {destino}")

    return categorias_final


def categorias(df):
    # Filtrar para obtener datos de 6CortesD/E.xlsx
    df_6cortes_final = filtro_6cortes(df)

    if not df_6cortes_final.empty:
        df_6cortes_final.to_excel("Cortes95VL.xlsx", index=False)
        print("Excel 6Cortes creado con éxito.\n")
    else:
        print("No se encontraron datos del 6Cortes D/E para crear el Excel.")

    # Procesar el resto de categorías como antes
    categorias_final = procesar_data(df)
    categorias_final.to_excel("final.xlsx", index=False)
    print("Excel Final creado con éxito.")
def nv(df):
    try:
        nota = input("Ingrese la nota de venta a asignar: \n")
        categoria = input("Ingrese la categoría a asignar: \n")
        df_resto = df[["Nro Serie"]]
        resto_final = pd.DataFrame({
            "Nro Etiqueta": df_resto["Nro Serie"],
            "Venta": nota,
            "Categoria": categoria,
        })
        resto_final.to_excel("final.xlsx", index=False)
        print("Excel creado con éxito")
    except KeyError:
        print("Error: Columna 'Destino Comercial' no encontrada en el DataFrame.")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit()


