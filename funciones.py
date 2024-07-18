# funcionas.py

import pandas as pd
import sys

def procesar_data(df):
    categorias_final = pd.DataFrame(columns=["Nro Etiqueta", "Venta", "Categoria"])
    
    categorias = {
        "Inc. 90 VL": ["CUARTO TRASERO INCOMPLETO (CAJA)", "CUARTO DELANTERO INCOMPLETO (CAJA)"],
        "Rueda": ["BOLA DE LOMO (CAJA)", "CUADRADA (CAJA)", "NALGA DE ADENTRO C/T (CAJA)", "PECETO (CAJA)", "NALGA DE ADENTRO S/T (CAJA)"],
        "SSHM": ["BRAZUELO (CAJA)", "GARRON (CAJA)", "TORTUGUITA (CAJA)"],
        "Mix Cuts GF": ["BOLA DE LOMO (CAJA)", "CUADRADA (CAJA)", "PECETO (CAJA)", "AGUJA (CAJA)", "CHINGOLO (CAJA)",
                        "COGOTE (CAJA)", "MARUCHA (CAJA)", "PECHO (CAJA)", "PALETA (CAJA)", "NALGA DE ADENTRO S/T (CAJA)"],
        "FFQ": ["AGUJA (CAJA)", "CHINGOLO (CAJA)", "COGOTE (CAJA)", "MARUCHA (CAJA)", "PECHO (CAJA)", "PALETA (CAJA)"],
        "ASADO S/H": ["ASADO SIN HUESO (CAJA)"],
        "ASADO C/H": ["ASADO CON HUESO (CAJA)", "ASADO CON HUESO CON MATAMBRE CON ENTRAÑA A 4 COSTILLAS (CAJA)", "ASADO CON HUESO CON MATAMBRE CON ENTRAÑA A 5 COSTILLAS (CAJA)"],
        "Fat": ["GRASA"],
        "FALDA C/HUESO": ["FALDA C/HUESO (CAJA)"],
        "VACIO": ["VACIO (CAJA)"],
        "R&L": ["BIFE ANCHO S/T-+2 kg. (CAJA)", "BIFE ANCHO S/T-+ 2,5 (CAJA)", "BIFE ANCHO S/T--2 kg. (CAJA)",
                "BIFE ANGOSTO CON CORDON-+3,5 kg. (CAJA)", "BIFE ANGOSTO CON CORDON-2,5 A 3 (CAJA)",
                "BIFE ANGOSTO CON CORDON-3 A 3,5 (CAJA)", "BIFE ANGOSTO CON CORDON-3 A 3.5 kg. (CAJA)",
                "BIFE ANGOSTO CON CORDON--3 kg. (CAJA)", "BIFE ANGOSTO CON CORDON-3,5 A 4 (CAJA)",
                "BIFE ANGOSTO CON CORDON-4 A 5 (CAJA)", "LOMO S/C +5 (CAJA)", "LOMO S/C 2 LB (CAJA)",
                "LOMO S/C 2/3 LB (CAJA)", "LOMO S/C 3/4 LB (CAJA)", "LOMO S/C 4/5 LB (CAJA)"],
        "RUMP": ["CUADRIL (CAJA)"],
        "Mix Huesos": ["HUESO"],
        "Trimming 70vl": ["70 vl"],
        "6 Cortes D/E": ["CUARTO TRASERO INCOMPLETO (CAJA)", "CUARTO DELANTERO INCOMPLETO (CAJA)", "BRAZUELO (CAJA)",
                        "GARRON (CAJA)", "TORTUGUITA (CAJA)", "ASADO SIN HUESO (CAJA)"]
    }
    
    for categoria, productos in categorias.items():
        filtro = df["Producto Desc"].isin(productos)
        df_filtrado = df[filtro]
        df_final = pd.DataFrame({
            "Nro Etiqueta": df_filtrado["Nro Serie"],
            "Venta": "",
            "Categoria": categoria,
        })
        categorias_final = pd.concat([categorias_final, df_final], ignore_index=True)
    
    return categorias_final

def categorias(df):
    categorias_final = procesar_data(df)
    categorias_final.to_excel("final.xlsx", index=False)
    print("Excel creado con éxito")

def nv(df):
    try:
        nota = input("Ingrese la nota de venta a asignar: \n")
        categoria = input("Ingrese la categoria a asignar: \n")
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
