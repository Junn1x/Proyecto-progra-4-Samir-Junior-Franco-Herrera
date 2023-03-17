import pandas as pd
from sodapy import Socrata
import numpy as np

def tomarDatos(limiteRegistros, departamento, municipio, cultivo):
    client = Socrata("www.datos.gov.co", None)

    results = client.get("ch4u-f3i5",limit=limiteRegistros,departamento= departamento,municipio = municipio,cultivo = cultivo)

    results_df = pd.DataFrame.from_records(results)

    results_df.drop(columns=["drenaje","riego","estado","tiempo_establecimiento",
                             "fertilizantes_aplicados","materia_org_nica_mo","manganeso_mn_disponible_doble_acido_mg_kg",
                             "zinc_zn_disponible_doble_cido_mg_kg","azufre_s_fosfato_monocalcico_mg_kg",
                             "acidez_al_h_kcl_cmol_kg","aluminio_al_intercambiable_cmol_kg","calcio_ca_intercambiable_cmol_kg",
                             "magnesio_mg_intercambiable_cmol_kg","sodio_na_intercambiable_cmol_kg",
                             "capacidad_de_intercambio_cationico_cice_suma_de_bases_cmol_kg","conductividad_el_ctrica_ce_relacion_2_5_1_0_ds_m",
                             "hierro_fe_disponible_olsen_mg_kg","cobre_cu_disponible_mg_kg","manganeso_mn_disponible_olsen_mg_kg",
                             "zinc_zn_disponible_olsen_mg_kg","boro_b_disponible_mg_kg","hierro_fe_disponible_doble_cido_mg_kg",
                             "cobre_cu_disponible_doble_acido_mg_kg"],inplace=True)
    
    results_df.rename(columns={"ph_agua_suelo_2_5_1_0":"pH","f_sforo_p_bray_ii_mg_kg":"Fosforo","potasio_k_intercambiable_cmol_kg":"Potasio"},inplace=True)
    #results_df[["Potasio","Fosforo","pH"]] = results_df[["Potasio","Fosforo","pH"]]
    results_df.loc[:,"Potasio"]=results_df["Potasio"].str.replace("<","").str.replace(">","").str.replace(",",".")
    results_df.loc[:,"Fosforo"]=results_df["Fosforo"].str.replace("<","").str.replace(">","").str.replace(",",".")
    results_df.loc[:,"pH"]=results_df["pH"].str.replace("<","").str.replace(">","").str.replace(",",".")
    print("Departamento\tMunicipio\tCultivo")
    print(departamento,"\t",municipio,"\t\t",cultivo)
    print("\nMediana de pH", results_df["pH"].median())
    print("Mediana de Fosforo", results_df["Fosforo"].median())
    print("Mediana de Potasio", results_df["Potasio"].median())
    return results_df

