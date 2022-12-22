import gspread
import numpy as np
from pkg_resources import working_set
import pandas as pd
from datetime import datetime

df = pd.read_excel('DATA/averias_down (3).xlsx', usecols = 'A:AU')
df = df.dropna(subset=["CODREQ"])
df = df.fillna('')
print(df)

gc = gspread.service_account(filename='datacargar-947843f340e2.json')
sh = gc.open("guille_app")

#  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
worksheet = sh.get_worksheet(4)

#borrar datos total y dejar encabezado
worksheet.resize(rows=1)
worksheet.resize(rows=30)
#cargar datos df
worksheet.update([df.columns.values.tolist()] + df.values.tolist())
