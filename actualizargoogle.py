import gspread
import numpy as np
from pkg_resources import working_set
import pandas as pd
from datetime import datetime

df = pd.read_excel('Guillermo_app.xlsx', sheet_name = 'Reporte_Gian', skiprows = 13, usecols = 'D').iloc[:-1]
#https://es.stackoverflow.com/questions/350681/como-extraer-tablas-de-un-excel-para-cruzar-con-otra-base-de-excel-en-python
#df = pd.read_excel('CARGARGILLERMO.xlsx')

now = datetime.today().strftime('%Y-%m-%d')

df['fecha'] = np.nan
df['fecha'] = df['fecha'].fillna(now)

df.columns = ['codliq', 'fecha']

#print(df)

df = df.fillna('')
df["codliq"]=df["codliq"].astype(str)

gc = gspread.service_account(filename='datacargar-947843f340e2.json')
sh = gc.open("guille_app")

#  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
worksheet = sh.get_worksheet(0)

df1 = pd.DataFrame(worksheet.get_all_records())


df1["codliq"]=df1["codliq"].astype(str)
#######
## TODO UNIR BASE DE DATOS MYSQL Y GOOGLE
#######
union = pd.concat([df, df1])
#print(len(union))
union = union.drop_duplicates(subset=['codliq'])

union = union.sort_values(by='fecha')
#borrar datos total y dejar encabezado
worksheet.resize(rows=1)
worksheet.resize(rows=30)
#cargar datos df
worksheet.update([union.columns.values.tolist()] + union.values.tolist())

# ver datos de google sheet
print(union)

#paginas
# drive-886@datacargar.iam.gserviceaccount.com
# https://docs.gspread.org/en/latest/user-guide.html#using-gspread-with-pandas
# https://www.youtube.com/watch?v=A1URtaaA-v0
# https://es.stackoverflow.com/questions/350681/como-extraer-tablas-de-un-excel-para-cruzar-con-otra-base-de-excel-en-python