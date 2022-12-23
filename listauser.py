import base64
import mysql.connector
from mysql.connector import Error
#import pyodbc
import pandas as pd
import streamlit as st
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')

##########################
import time
from datetime import datetime
from datetime import timedelta
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
 
cnxn = mysql.connector.connect( host="us-cdbr-east-06.cleardb.net",
                                port="3306",
                                user="be690637bd68c4",
                                passwd="88b2781e",
                                db="heroku_4843d4a20ed7194"
                                )
cursor = cnxn.cursor()


#print("listo")
sql = """
SELECT * FROM dbuser
"""
dfuser = pd.read_sql(sql, cnxn)


namesbd = dfuser['names'].tolist()
usernamesbd = dfuser['usernames'].tolist()
passwordsbd = dfuser['passwords'].tolist()



print(usernamesbd)