import streamlit as st
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
#from soupsieve import select  # pip install pandas openpyxl
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
############################################ OCULTAR INFROMACION NO IMPORTANTE
import base64
import mysql.connector
from mysql.connector import Error
#import pyodbc
import streamlit as st
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
#########################################3333
##########################
import time
from datetime import datetime
from datetime import timedelta
import gspread
import re
#import pyautogui
from pkg_resources import working_set

st.set_page_config(page_title='bdtickets-Averias', page_icon="🌀", layout='centered', initial_sidebar_state='auto')

## borrar nombres de la pagina
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

## fondo total
def add_bg_from_url():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://cdn.pixabay.com/photo/2018/11/13/18/06/mail-3813618_960_720.jpg 1x, https://cdn.pixabay.com/photo/2018/11/13/18/06/mail-3813618_1280.jpg");
            background-attachment: fixed;
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_url()
#st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
# --- USER AUTHENTICATION ---
names = ['Giancarlos Cardenas', 'Genesis Medrano', 'Luis Llerena', 'DIANA BERNEDO', 'VIVIAN CERVERA', 'CAROL CHUNGA', 'LAURA VIERA', 'MERCEDES RAYMUNDO', 'MONTES CABANILLAS', 'RENZO RIMARACHIN', 'LORENA BENAVIDES', 'NANCY YEREN', 'GIULIANA BELLIDO', 'CARMEN HUAMANCHUMO', 'GABRIEL SANTA ANA', 'CARMEN POMA REYES', 'JOSE ECHEVARRIA', 'YORMAN MORI', 'ENZO PAULINO', 'GUSTAVO SALCEDO', 'KAREN MAYORCA', 'LESLIE PRUDENCIO', 'BARBARA HUAMANCHUMO', 'Jose Ricardo', 'Eber Hinostroza', 'Bot cardenas']
usernames = ['Cardenas', 'Genesis', 'LLLERENAL', 'BERNEDO', 'CERVERA', 'CHUNGA', 'VIERA', 'RAYMUNDO', 'CABANILLAS', 'RIMARACHIN', 'BENAVIDES', 'YEREN', 'BELLIDO', 'ANDREA', 'SANTA ANA', 'POMA REYES', 'ECHEVARRIA', 'MORI', 'PAULINO', 'SALCEDO', 'MAYORCA', 'PRUDENCIO', 'HUAMANCHUMO', 'Argomedo', 'Hinostroza', 'Bot']

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=30)

name, authentication_status, username = authenticator.login("Login", "main")
#print(username)
#### fondo al costado
def sidebar_bg(side_bg):
   side_bg_ext = 'jpg'
   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
side_bg = 'nooa.jpg'
sidebar_bg(side_bg)


st.markdown(
    """
    <style>

    header .css-1595djx e8zbici2{
    display: flex;
    flex-direction: column;
    align-items: center;
    }

    header .logo-text{
        margin: 0;
        padding: 10px 26px;
        font-weight: bold;
        color: rgb(60, 255, 0);
        font-size: 0.8em;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# para los botones horizontal
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)



if authentication_status == False:
    st.error("Username/password is incorrect")

        ## borrar nombres de la pagina
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

if authentication_status == None:
    st.warning("Please enter your username and password")

        ## borrar nombres de la pagina
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


    st.markdown(
        """
        <style>

        header .css-1595djx e8zbici2{
        display: flex;
        flex-direction: column;
        align-items: center;
        }

        header .logo-text{
            margin: 0;
            padding: 10px 26px;
            font-weight: bold;
            color: rgb(60, 255, 0);
            font-size: 0.8em;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


    # para los botones horizontal
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)



    st.markdown(
        f"""
        <header class="css-1595djx e8zbici2">
            <p class="logo-text">App Alarmas 👨🏻‍💻Giancarlos .C</p>
        </header>
        """,
        unsafe_allow_html=True
    )

    def hide_anchor_link():
        st.markdown("""
            <style>
            .css-15zrgzn {display: none}
            .css-eczf16 {display: none}
            .css-jn99sy {display: none}
            </style>
            """, unsafe_allow_html=True)
    texto  = ('🔒Estamos mejorando la privacidad de la información, si aún no cuentas con tus credenciales, comunicarte con:')
    st.caption( f'<h6 style="color:#FFFFFF;">{texto}</h6>', unsafe_allow_html=True )

    textoo = ('\n\n👨🏻‍💻Luis Llerena. \n\n👨🏻‍💻Giancarlos Cardenas.')
    st.caption( f'<h6 style="color:#FFFFFF;">{textoo}</h6>', unsafe_allow_html=True )
    ###
    ####
    ####
    ####
    ######



if authentication_status:
    # ---- SIDEBAR ----
    authenticator.logout("Logout", "sidebar")
    st.sidebar.title(f"Bienvenid@ {name}")
    #### fondo al costado

    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,white, white);color:navy;font-size:24px;border-radius:2%;"><b>CARGA TUS DATOS</b></p>', unsafe_allow_html=True)

    st.sidebar.subheader("Cargar datos de acuerdo a lo requerido")

            # Setup file upload
    uploaded_file = st.sidebar.file_uploader(
                            label="Solo cargar data TT y CMR. (200MB max)",
                            type=['csv', 'xlsx', 'XLS'])

    global df
    if uploaded_file is not None:
        #print(uploaded_file)
        #print("hello")

        with st.spinner('Procesando los datos...'):

            try:
                #df = pd.read_excel('dic_20_Copia de PasaParametros.xlsx', sheet_name = 'Para Liquidar', skiprows = 15, usecols = 'B').iloc[:-1]
                df = pd.read_excel(uploaded_file)
                #https://es.stackoverflow.com/questions/350681/como-extraer-tablas-de-un-excel-para-cruzar-con-otra-base-de-excel-en-python
                #df = pd.read_excel('CARGARGILLERMO.xlsx')
                columdf = len(df.columns)
                print(columdf)

                if columdf == 2:

                    df = pd.read_excel(uploaded_file, sheet_name = 'Reporte_Gian', skiprows = 13, usecols = 'D').iloc[:-1]

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

                    st.success('cargo con exito data tablas dinamica')


                if columdf == 50:
                    df = pd.read_excel(uploaded_file, usecols = 'A:AU')
                    df = df.dropna(subset=["CODREQ"])
                    df = df.fillna('')
                    #print(df)

                    gc = gspread.service_account(filename='datacargar-947843f340e2.json')
                    sh = gc.open("guille_app")

                    #  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
                    worksheet = sh.get_worksheet(4)

                    #borrar datos total y dejar encabezado
                    worksheet.resize(rows=1)
                    worksheet.resize(rows=30)
                    #cargar datos df
                    worksheet.update([df.columns.values.tolist()] + df.values.tolist())

                    st.success('cargo con exito data DOW')

                if columdf == 172:

                    Trouble = pd.read_excel(uploaded_file, engine="openpyxl", skiprows=3)
                    ######3######################
                    Troubledt=Trouble[["Incident Number",	"CONTRATA_TOA__c",	"Categorization Tier 3", "CUSTOMERID_CRM__c", "OBSERVATIONS_CRM__c", "TELEFONO_REFERENCIA_1_CRM","servicioAfectado"]]
                    Troubledt = Troubledt.fillna('')

                    gc = gspread.service_account(filename='datacargar-947843f340e2.json')
                    sh = gc.open("guille_app")

                    #  el 0 simbol del numero de hoja en este caso es la primera hoja = 0
                    worksheet = sh.get_worksheet(1)

                    #borrar datos total y dejar encabezado
                    worksheet.resize(rows=1)
                    worksheet.resize(rows=30)
                    #cargar datos df
                    worksheet.update([Troubledt.columns.values.tolist()] + Troubledt.values.tolist())
                    df = pd.DataFrame(worksheet.get_all_records())

                    st.success('cargo con exito data TT')

                if columdf == 238:
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


                    df2 = pd.read_excel(uploaded_file, engine="openpyxl")
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

                    st.success('cargo con exito data Colas_Pais_New')

                if columdf == 71:

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


                    df2 = pd.read_excel(uploaded_file, sheet_name = 'Hoja1')
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

                    st.success('cargo con exito data preferentes_toa')

                else:
                    st.error('DATA NO CORRESPONDE LOS PARAMETROS👋🏻')


            except Exception as e:
                st.error('DATA NO CORRESPONDE 👋🏻')

    ## fondo total
    def add_bg_from_url():
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://cdn.pixabay.com/photo/2018/11/13/18/06/mail-3813618_960_720.jpg 1x, https://cdn.pixabay.com/photo/2018/11/13/18/06/mail-3813618_1280.jpg");
                background-attachment: fixed;
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    add_bg_from_url()

    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')
    st.sidebar.markdown('')

    st.sidebar.markdown(
    '<p class="big-font"; style="text-align:center;color:Lime;font-size:16px;border-radius:2%;">©👨🏻‍💻Giancarlos .C</p>', unsafe_allow_html=True
    )
