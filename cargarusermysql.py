import time
import mysql.connector
import pandas as pd
import numpy as np

df = pd.read_excel('user.xlsx')

df = pd.DataFrame(df).astype(str)

###FIXMEpara pedir la cantidad de datos [1] es la columna
shape = df.shape[1]
text = "%s," ##texto a multiplicar
repeated = text * shape #multiplicar
#repeated = list(repeated)
desobsordtrab = (str(repeated)[:-1]) #quitmanos los []
#print(desobsordtrab)

###FIXME DATOS DE COLUMNAS NOMBRES
df1 = df.columns
matriz_np = np.array(df1)
matriz_np = matriz_np.tolist()
string = (str(matriz_np)[1:-1])
characters = "'!?" ## QUITAMOS LOS ' PARA QUE ESTE SOLO CARACRETES EN LISTA
colum = ''.join( x for x in string if x not in characters)

############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
#########################################3333
#######
## TODO CONECTION A LA BASE DE DATOS MYSQL
#######
cnxn = mysql.connector.connect( host="us-cdbr-east-06.cleardb.net",
                                port="3306",
                                user="be690637bd68c4",
                                passwd="88b2781e",
                                db="heroku_4843d4a20ed7194"
                                )
cursor = cnxn.cursor()
#TODO Cargar data
#######
sql = f"""INSERT INTO dbuser ({colum}) VALUES ({desobsordtrab})"""
for row in df.values.tolist():
    cursor.execute(sql, tuple(row))
cnxn.commit()


cursor.close()
cnxn.close()
print('listo carga datos')


#pyinstaller --onefile --icon=./ave.ico cargar.py