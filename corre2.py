import pandas as pd
import gspread
from datetime import datetime
import numpy as np

#df1 = pd.read_excel('dic_20_Copia de PasaParametros.xlsx', sheet_name = 'priorizado')
##print(df1)
#df1 = df1.fillna('')
#df1 = df1.astype(str)

gc = gspread.service_account(filename='datacargar-947843f340e2.json')
sh = gc.open("guille_app")

#  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
worksheet = sh.get_worksheet(3)

#borrar datos total y dejar encabezado
#worksheet.resize(rows=1)
#worksheet.resize(rows=30)
##cargar datos df
#worksheet.update([df1.columns.values.tolist()] + df1.values.tolist())
df1 = pd.DataFrame(worksheet.get_all_records())
print(df1)


df2 = pd.read_excel('DATA/averias_preferentes_toa (013).xlsx', sheet_name = 'Hoja1')
######3######################
df2=df2[["customernumber"]]
df2 = df2.dropna()
df2["customernumber"]=df2["customernumber"].astype(int)
now = datetime.today().strftime('%Y-%m-%d')

df2['fecha'] = np.nan
df2['fecha'] = df2['fecha'].fillna(now)



df1["customernumber"]=df1["customernumber"].astype(str)
df2["customernumber"]=df2["customernumber"].astype(str)
#######
## TODO UNIR BASE DE DATOS MYSQL Y GOOGLE
#######
union = pd.concat([df1, df2])
#print(len(union))
union = union.drop_duplicates(subset=['customernumber'])


alx = union.astype({'customernumber': 'str'})

union = alx[alx['customernumber'].str.len() > 1 ]


worksheet = sh.get_worksheet(3)

#borrar datos total y dejar encabezado
worksheet.resize(rows=1)
worksheet.resize(rows=30)
#cargar datos df
worksheet.update([union.columns.values.tolist()] + union.values.tolist())

print(union)