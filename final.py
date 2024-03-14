import pandas as pd
import sys
from notaventa import nv
from categorias import categorias


def asignacion():
    print("Asegúrese de que el archivo que intenta utilizar se encuentre en la misma dirección que el Script.")
    name = input("Ingrese el nombre del archivo Excel:\n")
    name += ".xlsx"
    try:
        df = pd.read_excel(name)
    except FileNotFoundError:
        print(f"Error: El archivo {name} no se encuentra en la ruta especificada. Por favor, verifique la ruta y el nombre del archivo.")
        sys.exit()
    except pd.errors.EmptyDataError:
        print(f"Error: El archivo {name} está vacío o no tiene el formato correcto.")
        sys.exit()
    print("""
    -Opcion 1: Asignar Nota de Venta.
    -Opcion 2: Categorizar.
    """)
    opcion = int(input("Elija una opcion: "))
    if opcion==1:
        nv(df)
    elif opcion==2:
        categorias(df)
    else:
        print("Error")
        sys.exit()
if __name__ == "__main__":
    asignacion()