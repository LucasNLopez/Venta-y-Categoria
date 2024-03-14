import pandas as pd
import sys

def categorias(df):
    #print("Asegúrese de que el archivo que intenta utilizar se encuentre en la misma dirección que el Script.")
    #name = input("Ingrese el nombre del archivo Excel:\n")
    #name += ".xlsx"
    #try:
    #    df = pd.read_excel(name)
    #except FileNotFoundError:
    #    print(f"Error: El archivo {name} no se encuentra en la ruta especificada. Por favor, verifique la ruta y el nombre del archivo.")
    #    sys.exit()
    #except pd.errors.EmptyDataError:
    #    print(f"Error: El archivo {name} está vacío o no tiene el formato correcto.")
    #    sys.exit()
    #try:
        valores_90vl = ["CUARTO TRASERO INCOMPLETO (CAJA)", "CUARTO DELANTERO INCOMPLETO (CAJA)"]
        df_filtrado_90 = pd.DataFrame()
        for vl in valores_90vl:
            filtro90 = df["Producto Desc"] == vl
            df_filtrado_90 = pd.concat([df_filtrado_90, df[filtro90]], ignore_index=True)
        df_90vl = df_filtrado_90[["Nro Serie"]]
        df90_final = pd.DataFrame({
            "Nro Etiqueta": df_90vl["Nro Serie"],
            "Venta": "",
            "Categoria": "Inc. 90 VL",
        })
        valores_rueda = ["BOLA DE LOMO (CAJA)", "CUADRADA (CAJA)", "NALGA DE ADENTRO C/T (CAJA)", "PECETO (CAJA)",
                        "NALGA DE ADENTRO S/T (CAJA)"]
        df_rueda = pd.DataFrame()
        for rueda in valores_rueda:
            filtro_rueda = df["Producto Desc"] == rueda
            df_rueda = pd.concat([df_rueda, df[filtro_rueda]], ignore_index=True)
        rueda_cupo_final = pd.DataFrame({
            "Nro Etiqueta": df_rueda["Nro Serie"],
            "Venta": "",
            "Categoria": "Rueda",
        })
        valores_gtb=["BRAZUELO (CAJA)","GARRON (CAJA)","TORTUGUITA (CAJA)"]
        df_gtb=pd.DataFrame()
        for gtb in valores_gtb:
            filtro_gtb=df["Producto Desc"]==gtb
            df_gtb=pd.concat([df_gtb,df[filtro_gtb]],ignore_index=True)
        gtb_final=pd.DataFrame({
            "Nro Etiqueta": df_gtb["Nro Serie"],
            "Venta": "",
            "Categoria": "SSHM",
        })
        valores_gf=["BOLA DE LOMO (CAJA)","CUADRADA (CAJA)","PECETO (CAJA)","AGUJA (CAJA)","CHINGOLO (CAJA)",
                "COGOTE (CAJA)","MARUCHA (CAJA)","PECHO (CAJA)","PALETA (CAJA)","NALGA DE ADENTRO S/T (CAJA)"]
        gf_df=pd.DataFrame()
        for gf in valores_gf:
            filtro_gf=df["Producto Desc"]==gf
            gf_df=pd.concat([gf_df,df[filtro_gf]],ignore_index=True)
        filtro=["GRAIN FED"]
        gf_filtro=gf_df[gf_df["Contramarca"].isin(filtro)]
        gf_final=pd.DataFrame({
            "Nro Etiqueta": gf_filtro["Nro Serie"],
            "Venta": "",
            "Categoria": "Mix Cuts GF",
        })
        valores_ffq=["AGUJA (CAJA)","CHINGOLO (CAJA)","COGOTE (CAJA)","MARUCHA (CAJA)","PECHO (CAJA)","PALETA (CAJA)"]
        df_filtrado=pd.DataFrame()
        for c in valores_ffq:
            filtroDE=df["Producto Desc"]==c
            df_filtrado=pd.concat([df_filtrado,df[filtroDE]],ignore_index=True)
        ffq_final=pd.DataFrame({
            "Nro Etiqueta": df_filtrado["Nro Serie"],
            "Venta": "",
            "Categoria": "FFQ",
        })
        valores_asado=["ASADO CON HUESO CON MATAMBRE CON ENTRAÑA A 4 COSTILLAS (CAJA)","ASADO CON HUESO CON MATAMBRE CON ENTRAÑA A 5 COSTILLAS (CAJA)"]
        df_filtrado_asados=pd.DataFrame()
        for v in valores_asado:
                filtro_asados=df["Producto Desc"]==v
                df_filtrado_asados=pd.concat([df_filtrado_asados,df[filtro_asados]],ignore_index=True)
        asados_final=pd.DataFrame({
            "Nro Etiqueta": df_filtrado_asados["Nro Serie"],
            "Venta": "",
            "Categoria": "ASADO C/H",
        })
        df_grasa=df[df["Producto Desc"]=="GRASA"]
        grasa_final=pd.DataFrame({
            "Nro Etiqueta": df_grasa["Nro Serie"],
            "Venta": "",
            "Categoria": "Fat",
        })
        valores_falda=["FALDA C/HUESO (CAJA)"]
        df_filtrado_falda=pd.DataFrame()
        for v in valores_falda:
                filtro_falda=df["Producto Desc"]==v
                df_filtrado_falda=pd.concat([df_filtrado_falda,df[filtro_falda]],ignore_index=True)
        falda_final=pd.DataFrame({
            "Nro Etiqueta": df_filtrado_falda["Nro Serie"],
            "Venta": "",
            "Categoria": "FALDA C/HUESO",
        })
        vacio=df[df["Producto Desc"]=="VACIO (CAJA)"]
        vacio_final=pd.DataFrame({
            "Nro Etiqueta": vacio["Nro Serie"],
            "Venta": "",
            "Categoria": "VACIO",
        })
        valores_a_buscar = ["BIFE ANCHO S/T-+2 kg. (CAJA) ", "BIFE ANCHO S/T-+ 2,5 (CAJA)", "BIFE ANCHO S/T--2 kg. (CAJA)",
                            "BIFE ANGOSTO CON CORDON-+3,5 kg. (CAJA) ","BIFE ANGOSTO CON CORDON-2,5 A 3 (CAJA)",
                            "BIFE ANGOSTO CON CORDON-3 A 3,5 (CAJA)","BIFE ANGOSTO CON CORDON-3 A 3.5 kg. (CAJA) ",
                            "BIFE ANGOSTO CON CORDON--3 kg. (CAJA) ","BIFE ANGOSTO CON CORDON-3,5 A 4 (CAJA)","BIFE ANGOSTO CON CORDON-4 A 5 (CAJA)",
                            "LOMO S/C +5 (CAJA)","LOMO S/C 2 LB (CAJA)","LOMO S/C 2/3 LB (CAJA)",
                            "LOMO S/C 3/4 LB (CAJA)","LOMO S/C 4/5 LB (CAJA)"]
        df_filtrado = pd.DataFrame()  # Crea un DataFrame vacío para almacenar los resultados
        for valor in valores_a_buscar:
            filtro = df["Producto Desc"] == valor
            df_filtrado = pd.concat([df_filtrado, df[filtro]], ignore_index=True)
        ral_final=pd.DataFrame({
            "Nro Etiqueta": df_filtrado["Nro Serie"],
            "Venta": "",
            "Categoria": "R&L",
        })
        #gf_filtro=gf_df[gf_df["Contramarca"].isin(filtro)]
        #ral_filtro_s=["S"]
        #ral_s = df_filtrado[df_filtrado["Contramarca"].isin(ral_filtro_s)]
        #ral_s_final=pd.DataFrame({
        #    "Nro Etiqueta": ral_s["Nro Serie"],
        #    "Venta": "",
        #    "Categoria": "R&L",
        #})
        df_cuadril= df[df["Producto Desc"].str.startswith("CUADRIL (CAJA)")]
        cuadril_final=pd.DataFrame({
            "Nro Etiqueta": df_cuadril["Nro Serie"],
            "Venta": "",
            "Categoria": "RUMP",
        })
        df_huesos=df[df["Producto Desc"].str.startswith("HUESO")]
        huesos_final=pd.DataFrame({
            "Nro Etiqueta": df_huesos["Nro Serie"],
            "Venta": "",
            "Categoria": "Mix Huesos",
        })
        df_grasa_pecho= df[df["Producto Desc"].str.startswith("GRASA DE PECHO (CAJA)")]
        grasa_pecho_final=pd.DataFrame({
            "Nro Etiqueta": df_grasa_pecho["Nro Serie"],
            "Venta": "",
            "Categoria": "Mix Cuts",
        })
        df_70 = df[df["Producto Desc"].str.contains("70 vl", case=False)]
        df70_final=pd.DataFrame({
            "Nro Etiqueta": df_70["Nro Serie"],
            "Venta": "",
            "Categoria": "Trimming 70vl",
        })
        frames = [rueda_cupo_final, df90_final,gtb_final,gf_final,ffq_final,asados_final,grasa_final,falda_final,vacio_final,cuadril_final,
                huesos_final,grasa_pecho_final,df70_final,ral_final]
        result = pd.concat(frames)
        categorias_final = pd.DataFrame({"Nro Etiqueta": result["Nro Etiqueta"], "Venta": "", "Categoria": result["Categoria"]})
        categorias_final.to_excel("final.xlsx", index=False)
        print("Excel creado con exito")
    #except Exception:
    #    print(f"Error: Verifique la estructura del archivo {name}.")
    #    sys.exit()
