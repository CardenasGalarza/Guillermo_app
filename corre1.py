import pandas as pd
import gspread
from datetime import datetime
import numpy as np
import re

#df1 = pd.read_excel('dic_20_Copia de PasaParametros.xlsx', sheet_name = 'priorizado')
##print(df1)
#df1 = df1.fillna('')
#df1 = df1.astype(str)

gc = gspread.service_account(filename='datacargar-947843f340e2.json')
sh = gc.open("guille_app")

#  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
worksheet = sh.get_worksheet(2)

#borrar datos total y dejar encabezado
#worksheet.resize(rows=1)
#worksheet.resize(rows=30)
##cargar datos df
#worksheet.update([df1.columns.values.tolist()] + df1.values.tolist())
df1 = pd.DataFrame(worksheet.get_all_records())
#print(df1)


df2 = pd.read_excel('DATA/Copia de Colas_Pais_New_20Diciembre2022.xlsx', engine="openpyxl")
######3######################
df2 = df2[["CUSTOMERID_CRM__c"]]

df2['ESTADO'] = '1'



df1["CUSTOMERID_CRM__c"]=df1["CUSTOMERID_CRM__c"].astype(str)
df2["CUSTOMERID_CRM__c"]=df2["CUSTOMERID_CRM__c"].astype(str)
#######
## TODO UNIR BASE DE DATOS MYSQL Y GOOGLE
#######
union = pd.concat([df1, df2])

union['CUSTOMERID_CRM__c'] = pd.to_numeric(union['CUSTOMERID_CRM__c'], errors='coerce').fillna(0).astype(int)
#print(len(union))
union = union.drop_duplicates(subset=['CUSTOMERID_CRM__c'])

alx = union.astype({'CUSTOMERID_CRM__c': 'str'})
union = alx[alx['CUSTOMERID_CRM__c'].str.len() > 1 ]

worksheet = sh.get_worksheet(2)

#borrar datos total y dejar encabezado
worksheet.resize(rows=1)
worksheet.resize(rows=30)
#cargar datos df
worksheet.update([union.columns.values.tolist()] + union.values.tolist())

print(union)