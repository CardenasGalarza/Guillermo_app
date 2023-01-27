import streamlit as st
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
#from soupsieve import select  # pip install pandas openpyxl
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
############################################ OCULTAR INFROMACION NO IMPORTANTE
import base64
#import pyodbc
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
#########################################3333
##########################
from datetime import datetime
import gspread
#import pyautogui
from streamlit_option_menu import option_menu

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
names = ['YERINA GAMARRA', 'MARGOTH GONZALES', 'JHONATAN CORONADO', 'LUISA HUINCHO', 'JOSE SOLARTE', 'PATRICIA ZAPATA', ' ROJAS', 'GIOVANNA CALATAYUD', 'MIRELLA SEBASTIANI', 'SOFIA NOVOA', 'ZOILA CHAVEZ', 'YENY CARRION', 'AUGUSTO CHURATA', 'LUKI TORREJON', 'NAHUM SILVA', 'ARNOLD NAYAP', 'CLAUDIA USCUVILCA', 'FELIX BERNAOLA', 'LIZ ALMONACID', 'DAIVIS JULCARIMA', 'JULINHO HUAIRE', 'MILAGROS OTINIANO', 'WILSON ROJAS', 'ELOISA FLORES', ' NAPAN', 'ALFREDO SOBERON', 'KARINA PONCE', 'ESTHER SANTIBAÑEZ', 'MICHELLE OBREGON', 'ELIZABETH FUENTES', ' ENRIQUEZ', 'ALEXANDRA CARRERA', 'CAROLINA SILVERA', 'CLEER LOPEZ', 'INES LUQUE', 'RICARDO ALVA', 'ENRIQUE LAZO', 'SERGIO FABIAN', 'STUWARD AGUILAR', 'KAREM RIVERA', 'DEL MELENDEZ', 'YOEL YARIHUAMAN', 'ELIZABETH DIAZ', 'FRANCO ARANIBAR', 'ELISON SAJAMI', 'MAVEL OSORIO', 'ZENOVIA ESPINOZA', 'JORDAN AZPUR', ' ROSALES', ' FIGARI', ' CASTRO', 'Giancarlos']
usernames = ['GAMARRA60', 'GONZALES61', 'CORONADO62', 'HUINCHO63', 'SOLARTE64', 'ZAPATA65', 'ROJAS66', 'CALATAYUD67', 'SEBASTIANI68', 'NOVOA69', 'CHAVEZ70', 'CARRION71', 'CHURATA72', 'TORREJON73', 'SILVA74', 'NAYAP75', 'USCUVILCA76', 'BERNAOLA77', 'ALMONACID78', 'JULCARIMA79', 'HUAIRE80', 'OTINIANO81', 'ROJAS82', 'FLORES83', 'NAPAN84', 'SOBERON85', 'PONCE86', 'SANTIBAÑEZ87', 'OBREGON88', 'FUENTES89', 'ENRIQUEZ90', 'CARRERA91', 'SILVERA92', 'LOPEZ93', 'LUQUE94', 'ALVA95', 'LAZO96', 'FABIAN97', 'AGUILAR98', 'RIVERA99', 'MELENDEZ100', 'YARIHUAMAN101', 'DIAZ102', 'ARANIBAR103', 'SAJAMI104', 'OSORIO105', 'ESPINOZA106', 'AZPUR107', 'ROSALES108', 'FIGARI109', 'CASTRO110', 'Cardenas']

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

    # 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu
    EXAMPLE_NO = 1


    def streamlit_menu(example=1):
        if example == 1:
            # 1. as sidebar menu
            with st.sidebar:
                selected = option_menu(
                    menu_title="Main Menu",  # required
                    options=["Contact", "Datacob", "Report"],  # required
                    icons=["house", "book", "envelope"],  # optional
                    menu_icon="cast",  # optional
                    default_index=0,  # optional
                )
            return selected

        if example == 2:
            # 2. horizontal menu w/o custom style
            selected = option_menu(
                menu_title=None,  # required
                options=["Contact", "Datacob", "Report"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                orientation="horizontal",
            )
            return selected

        if example == 3:
            # 2. horizontal menu with custom style
            selected = option_menu(
                menu_title=None,  # required
                options=["Contact", "Datacob", "Report"],  # required
                icons=["house", "book", "envelope"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                orientation="horizontal",
                styles={
                    "container": {"padding": "0!important", "background-color": "#fafafa"},
                    "icon": {"color": "orange", "font-size": "25px"},
                    "nav-link": {
                        "font-size": "25px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "#eee",
                    },
                    "nav-link-selected": {"background-color": "green"},
                },
            )
            return selected

    selected = streamlit_menu(example=EXAMPLE_NO)

    if selected == "Datacob":

        xs = usernames = ['Cardenas']
        #xs = ['Cardenas', 'LLLERENAL', 'Hinostroza', 'Argomedo', 'VIERA']
        bs = (username in xs)

        if bs == True:

            import streamlit as st
            import streamlit as st
            from streamlit_option_menu import option_menu
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

            cnxn = mysql.connector.connect( host="us-cdbr-east-06.cleardb.net",
                                            port="3306",
                                            user="be690637bd68c4",
                                            passwd="88b2781e",
                                            db="heroku_4843d4a20ed7194"
                                            )
            cursor = cnxn.cursor()

            #cnxn =  mysql.connector.connect( host="10.226.120.172",
            #                                port="3306",
            #                                user="slinea",
            #                                passwd="OP81^K@u",
            #                                db="segunda_linea"
            #                                )
            #cursor = cnxn.cursor()



            sql = """
            SELECT * FROM bdtickets ;
            """
            #######
            ## TODO BASE DE DATOS MYSQL
            #######
            df1 = pd.read_sql(sql, cnxn)
            df1["codreq"]=df1["codreq"].astype(str)
            #print(df1)
                #st.title(f"You have selected {selected}")
            st.title("COBRE TICKETS PENDIENTES💻")



            page_names = ['COBRE']
            page = st.sidebar.radio('Selecciona inf. Tecnoligia💻',page_names, index=0)
            #######
            ## TODO CONECTION A LA BASE DE DATOS MYSQL

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

            sql = """
            SELECT GESTOR, codreq,tiptecnologia_x, FEC_CERRAR FROM bdtickets WHERE  ESTADO="PENDIENTE" ;
            """
            pend = pd.read_sql(sql, cnxn)
            pend = pend[pend['tiptecnologia_x'] == page]
            pendca = str(len(pend))
            #print(pendca)
            sql = """
            SELECT GESTOR, codreq, FEC_CERRAR FROM bdtickets WHERE  ESTADO="CERRAR" ;
            """
            df = pd.read_sql(sql, cnxn)
            dfg = df[df['GESTOR'] == name]
            date = datetime.now()
            ##TODO SIEMPRE VER ESTO PARA CONTADOR
            ##FIXME SOLO CAMBIAR ESTO FIRMATO DE FECHA NO LO DE ABAJO
            #tcanti = (date.strftime("%Y-%d-%m"))   ## inicio de semana hasta el dia 12 a alas 12 am de la madrugada para el dia 13
            tcanti = (date.strftime("%Y-%m-%d"))  ## aparttir del dei >12 luego dias despues de se semana
            #print(tcanti)
            ##### cantidad de cerradas
            df = dfg
            df['FEC_CERRAR'] = pd.to_datetime(df['FEC_CERRAR']).dt.date
            #df['FEC_CERRAR'] = pd.to_datetime(df['FEC_CERRAR'], format='%Y-%m-%d')
            df['FEC_CERRAR'] = pd.to_datetime(df['FEC_CERRAR'])
            #print(df)
            canti = str(len(df[df['FEC_CERRAR'] == tcanti]))
            #print(canti)
            st.markdown(f'<p class="big-font"; style="text-align:center;color:Cyan;font-size:24px"><b>👉🏻  {canti} ✔️{pendca}</b></p>', unsafe_allow_html=True)
            #st.sidebar.header("catidad trabajada "+ str(canti))
            ### EXTARER DATOS
            sql = """
            SELECT * FROM bdtickets  WHERE ESTADO = 'PENDIENTE' ORDER BY fec_regist ;
            """
            date = datetime.now()
            tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))

            df = pd.read_sql(sql, cnxn)
            ###############
            ####FIXME TODO PARA CAMBIAR LA CANTODAD MAS SIMPLE ES > 8 CARACTERES
            #df = df[df['codreq'].str.len() > 8]  ###PARA ESTAR COMO ANTES SOLO OCULTAR ESTA LINEA
            ########################################
            ##########################################
            df = df[df['tiptecnologia_x'] == page]
            df = df[df['FEC_PROG'] < tiempo]
            df = df[(df["GESTOR"]==name) | (df["GESTOR"]=="")].head(1)
            #print(df)

            #df = df[df['codofcadm'] == 'GIANCARLOS']
            #df = df.head(1)
            #print(df)

            #dfu =df["codreq"].head(1)
            #dfu = (dfu.to_string(index=False))
            #print(df)
            #df = df[df.year.isin([2008, 2009])]


            ###########
            ### EXTARER DATOS
            sql2 = """
                SELECT *
                FROM bdtickets
                WHERE
                ESTADO = 'PROGRAMADO' ORDER BY FEC_PROG ;
            """

            date = datetime.now()
            tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))

            df2 = pd.read_sql(sql2, cnxn)
            df2 = df2[df2['GESTOR'] == name]
            df2 = df2[df2['FEC_PROG'] < tiempo].head(1)
            #df2 = df2[df2['ESTADO'] == 'PROGRAMADO']
            #df = df[df['codofcadm'] == 'GIANCARLOS']
            #df = df.head(1)
            #print(df2)

            sql2G = """
                select * from bdtickets 
                where  ESTADO  IN ('PROGRAMADO', 'PENDIENTE')
            """
            mdfff =df2["nomcli"].head(1)
            mdfff = (mdfff.to_string(index=False))

            cuadromdf = pd.read_sql(sql2G, cnxn)
            cuadromdf = cuadromdf[cuadromdf['nomcli'] == mdfff]
            cuadromdf = cuadromdf[cuadromdf['desnomctr'] == 'OOCC']
            cuadromdf = cuadromdf.drop_duplicates()
            cuadromdf = cuadromdf.set_index('nomcli')
            cuadromdf = cuadromdf.iloc[:, [0, 2, 3,4,5,6,7,8,10,11] ]
            st.dataframe(cuadromdf)



            col1, col2, col3 = st.columns(3)

            
            with col1:
                if st.button('Click me'):
                    codreq_values = cuadromdf['codreq'].tolist()
                    val = 'En espera'
                    estadf = 'CERRAR'
                    nomdf = name
                    temdf = tiempo
                    actdf = '1'

                    placeholders = ', '.join(['%s']*len(codreq_values))
                    query = f"UPDATE bdtickets SET ESTADO = '{estadf}', GESTOR = '{nomdf}',FEC_PROG = '{temdf}', FEC_CERRAR = '{temdf}', ACCION = '{val}', ACTIVO = '{actdf}' WHERE codreq IN ({placeholders})"
                    cursor.execute(query, codreq_values)
                    cnxn.commit()

                    sql136 = "UPDATE bdtickets SET ESTADO = %s, GESTOR = '',FEC_PROG = '', FEC_CERRAR = '', ACCION = '', ACTIVO = '0' WHERE GESTOR = %s AND ESTADO = 'PROGRAMADO'"
                    #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                    val136 = ('PENDIENTE', nomdf)
                    cursor.execute(sql136, val136)
                    cnxn.commit()

                    st.write('Se cargo los datos para tu gestion, Masivas')




            dfunom =df2["desnomctr"].head(1)
            dfu2 =df2["codreq"].head(1)
            codcli =df2["codcli"].head(1)
            fec_regist =df2["fec_regist"].head(1)
            tiptecnologia_x =df2["tiptecnologia_x"].head(1)
            numtelefvoip =df2["numtelefvoip"].head(1)
            TELEFONO_REFERENCIA_1_CRM =df2["TELEFONO_REFERENCIA_1_CRM"].head(1)
            codnod =df2["codnod"].head(1)
            Categorization_Tier2 =df2["nomcli"].head(1)
            CUSTOMERID_CRM__c =df2["desdtt"].head(1)
            Area_CRM =df2["codofcadm"].head(1)
            desmotv =df2["desmotv"].head(1)
            # ejemplo de texto completo
            desobsordtrab =(df2["desobsordtrab"].unique())

            ##TODO ESTO es para ver cada datos de la tabla filtrada

            dfunom = (dfunom.to_string(index=False))
            dfu2 = (dfu2.to_string(index=False))
            codcli = (codcli.to_string(index=False))
            fec_regist = (fec_regist.to_string(index=False))
            tiptecnologia_x = (tiptecnologia_x.to_string(index=False))
            numtelefvoip = (numtelefvoip.to_string(index=False))
            TELEFONO_REFERENCIA_1_CRM = (TELEFONO_REFERENCIA_1_CRM.to_string(index=False))
            codnod = (codnod.to_string(index=False))
            Categorization_Tier2 = (Categorization_Tier2.to_string(index=False))
            CUSTOMERID_CRM__c = (CUSTOMERID_CRM__c.to_string(index=False))
            Area_CRM = (Area_CRM.to_string(index=False))
            desmotv = (desmotv.to_string(index=False))
            #desobsordtrab = (desobsordtrab.to_string(index=False))
            ## ejemplo de texto completo
            desobsordtrab = (str(desobsordtrab)[2:-2])
            #print(desobsordtrab)
            #df = df[df.year.isin([2008, 2009])]
            # para los botones horizontal
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)


            try:


                genre = st.radio(
                    "Establece tu preferencia de actividad",
                    ('Programar', 'Masivas','Finalizar', 'Analisis', 'Dashboard'))


                if  genre == 'Programar':
                    lencodcli = len(codcli)
                    #print(lencodcli)
                    if lencodcli == 0:

                        my_bar = st.progress(0)
                        ## fecha para programar y cerrar
                        date = datetime.now()
                        tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))
                        #print(tiempo) # DD Month, YYYY HH:MM:SS

                        options = (df2['codreq'].unique())


                        add  = str('CERRAR')
                        nom = str(name)
                        adwe = (str(options)[2:-2])
                        rreeee = (str(options)[2:-2])
                        #print(rreeee)



                        options = (df['codreq'].unique())

                        add  = str('PROGRAMADO')
                        nom = str(name)
                        adwe = (str(options)[2:-2])
                        #print(adwe)
                        #st.info(dfu2)

                        #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                        #st.info(dfu2)
                        ### un ejemplo para texto
                        #st.info(desobsordtrab)
                        #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{canti}</p>', unsafe_allow_html=True)
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{dfunom}</p>', unsafe_allow_html=True)

                        with st.form(key='my_form', clear_on_submit=True):
                        
                            col1, col2, col3 = st.columns(3)



                            with col1:
                                st.markdown("**Numero de tickets**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{dfu2}</p>', unsafe_allow_html=True)

                                #filter_page_or_query = st.markdown("Dimension to filter #1"), st.markdown("<P style='text-align: center; color: BLUE;'>Some title</P>", unsafe_allow_html=True)

                            with col2:
                                #st.markdown("**Codigo de cliente**")
                                lenCodigoclienteinp = st.text_input("**Codigo de cliente**")
                                #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                                #lenCodigocliente = len(codcli)
                                #print(lenArea_CRM)
                                #if lenArea_CRM
                                #if lenCodigocliente > 1:
                                #    st.markdown("**Codigo de cliente**")
                                #    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)
                                #else:
                                #    lenCodigoclienteinp = st.text_input("**Codigo de cliente**")
                                

                            with col3:
                                st.markdown("**Fecha de Ticket**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{fec_regist}</p>', unsafe_allow_html=True)


                            with col1:

                                    Tecno = st.selectbox(
                                        "**Tecnologia**",
                                        (
                                            "GPON",
                                            "HFC",
                                        ),
                                        key="filter_type3",
                                        help="""
                                        Ten encuenta tu accion `Ticket` inf.
                                        """,
                                    )

                            with col2:
                                #st.markdown("**Telefono**")
                                #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">_{numtelefvoip}</p>', unsafe_allow_html=True)
                                lenTelefono = st.text_input("**Telefono**")

                            with col3:
                                #st.markdown("**Telf Ref**")
                                #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{TELEFONO_REFERENCIA_1_CRM}</p>', unsafe_allow_html=True)
                                lenTelfRef = st.text_input("**Telf Ref**")

                            with col1:
                                #st.markdown("**Nodo**")
                                #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codnod}</p>', unsafe_allow_html=True)
                                lenNodo = st.text_input("**Nodo**")

                            with col2:
                                st.markdown("**CategTier 2**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Categorization_Tier2}</p>', unsafe_allow_html=True)

                            with col3:
                                st.markdown("**Observacion**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{desmotv}</p>', unsafe_allow_html=True)

                            with col1:
                                #st.markdown("**Cuestomerid crm**")
                                #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{CUSTOMERID_CRM__c}</p>', unsafe_allow_html=True)
                                lenCuestomerid = st.text_input("**Cuestomerid crm**")

                            with col2:
                                st.markdown("**Ubilic**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Area_CRM}</p>', unsafe_allow_html=True)

                                #lenArea_CRM = len(Area_CRM)
                                ##print(lenArea_CRM)
                                ##if lenArea_CRM
                                #if lenArea_CRM > 1:
                                #    st.markdown("**Area crm**")
                                #    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Area_CRM}</p>', unsafe_allow_html=True)
                                #else:
                                #    lenArea_CRMinp = st.text_input("**Area crm**")


                            #with col3:
                            #    #st.markdown("**Observacion 2**")
                            #    #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:15px;border-radius:2%;">{desobsordtrab}</p>', unsafe_allow_html=True)
                            #    lenObservacion2 = st.text_input("**Observacion 2**")

                            with col1:
                                lencodofcadm = st.text_input("**codofcadm**")

                            with col2:
                                lendesdtt = st.text_input("**desdtt**")

                            with col3:
                                lenservicioAfectado = st.text_input("**servicioAfectado**")

                            lennomcliente = st.text_input("**Nombre_Cliente**")

                            lenObservacion2 = st.text_area("Observación", key="text")

                            col1, col2, col3 , col4, col5 = st.columns(5)

                            with col1:
                                pass
                            with col2:
                                pass
                            with col4:
                                pass
                            with col5:
                                pass
                            with col3 :
                                submitted = st.form_submit_button("✍🏻Enviar")

                            if submitted == True:
                                dt1 = len(lenCodigoclienteinp)
                                dt2 = len(lenTelefono)
                                dt3 = len(lenTelfRef)
                                dt4 = len(lenNodo)
                                dt5 = len(lenCuestomerid)
                                dt6 = len(lenObservacion2)
                                dt7 = len(lencodofcadm)
                                dt8 = len(lendesdtt)
                                dt9 = len(lenservicioAfectado)

                                #https://stackoverflow.com/questions/16522111/python-syntax-for-if-a-or-b-or-c-but-not-all-of-them
                                #if (dt1 and dt2 and dto) > 0:
                                if dt1 > 0 and dt2 > 0 and  dt3 > 0 and  dt4 > 0 and  dt5 > 0 and  dt6 > 0 and  dt7 > 0 and  dt8 > 0 and  dt9 > 0:
                                #if dt1, dt2  > 0:
                                    if Tecno != page:
                                        sql = "UPDATE bdtickets SET codcli = %s, tiptecnologia_x = %s, numtelefvoip = %s, TELEFONO_REFERENCIA_1_CRM = %s, codnod = %s, CUSTOMERID_CRM__c = %s, desobsordtrab = %s, codofcadm = %s, desdtt = %s, servicioAfectado = %s, nomcli = %s, ESTADO='PENDIENTE', GESTOR='', FEC_PROG='' ,FEC_CERRAR='' ,ACCION='' ,OBS='' ,ACTIVO='0'  WHERE codreq = %s"
                                        val = (lenCodigoclienteinp, Tecno, lenTelefono, lenTelfRef, lenNodo, lenCuestomerid, lenObservacion2, lencodofcadm, lendesdtt, lenservicioAfectado, lennomcliente, rreeee)
                                        #print(lenCodigoclienteinp)
                                        #print(rreeee)
                                        cursor.execute(sql, val)
                                        cnxn.commit()
                                        st.experimental_rerun()
                                    else:
                                        sql = "UPDATE bdtickets SET codcli = %s, tiptecnologia_x = %s, numtelefvoip = %s, TELEFONO_REFERENCIA_1_CRM = %s, codnod = %s, CUSTOMERID_CRM__c = %s, desobsordtrab = %s, codofcadm = %s, desdtt = %s, servicioAfectado = %s, nomcli = %s  WHERE codreq = %s"
                                        val = (lenCodigoclienteinp, Tecno, lenTelefono, lenTelfRef, lenNodo, lenCuestomerid, lenObservacion2, lencodofcadm, lendesdtt, lenservicioAfectado, lennomcliente, rreeee)
                                        #print(lenCodigoclienteinp)
                                        #print(rreeee)
                                        cursor.execute(sql, val)
                                        cnxn.commit()
                                        st.experimental_rerun()

                                else:
                                    #st.error('👀 TIENES QUE ESCRIBIR EN TODOS LOS INPUT👀 ')
                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,MistyRose, MistyRose);color:BLACK;font-size:18px;border-radius:2%;"><b>😡👀 TE FALTA INGRESAR LOS DATOS REQUERIDOS 👀😡</b></p>', unsafe_allow_html=True)

                            #PONER COLOR A LOS INPUT TRABAJA CON CSS
                            def local_css(file_name):
                                with open(file_name) as f:
                                    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

                            def remote_css(url):
                                st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

                            def icon(icon_name):
                                st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

                            local_css("style.css")

                            # st.experimental_rerun()
                        ## fondo total
                        def add_bg_from_url():
                            st.markdown(
                                f"""
                                <style>
                                .stApp {{
                                    background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_960_720.jpg 1x, https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_1280.jpg");
                                    background-attachment: fixed;
                                    background-size: cover
                                }}
                                </style>
                                """,
                                unsafe_allow_html=True
                            )
                        add_bg_from_url() 

                            #remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
                    else:
                        #TODO SIVERVPARA BARRA AZUL
                        my_bar = st.progress(0)
                        ## fecha para programar y cerrar
                        date = datetime.now()
                        tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))
                        #print(tiempo) # DD Month, YYYY HH:MM:SS

                        options = (df2['codreq'].unique())

                        add  = str('CERRAR')
                        nom = str(name)
                        adwe = (str(options)[2:-2])
                        #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                        sql = "UPDATE bdtickets SET ESTADO = %s, GESTOR = %s WHERE codreq = %s AND ESTADO='PROGRAMADO'"
                        val = (add, nom, adwe)
                        cursor.execute(sql, val)


                        options = (df['codreq'].unique())

                        add  = str('PROGRAMADO')
                        nom = str(name)
                        adwe = (str(options)[2:-2])
                        #st.info(dfu2)

                        #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                        #st.info(dfu2)
                        ### un ejemplo para texto
                        #st.info(desobsordtrab)
                        #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{canti}</p>', unsafe_allow_html=True)
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{dfunom}</p>', unsafe_allow_html=True)


                        
                        col1, col2, col3 = st.columns(3)



                        with col1:
                            st.markdown("**Numero de tickets**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{dfu2}</p>', unsafe_allow_html=True)

                            #filter_page_or_query = st.markdown("Dimension to filter #1"), st.markdown("<P style='text-align: center; color: BLUE;'>Some title</P>", unsafe_allow_html=True)

                        with col2:
                            st.markdown("**Codigo de cliente**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                            

                        with col3:
                            st.markdown("**Fecha de Ticket**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{fec_regist}</p>', unsafe_allow_html=True)


                        with col1:
                            st.markdown("**Data**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tiptecnologia_x}</p>', unsafe_allow_html=True)


                        with col2:
                            st.markdown("**Origen**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">_{numtelefvoip}</p>', unsafe_allow_html=True)


                        with col3:
                            st.markdown("**Terminal**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{TELEFONO_REFERENCIA_1_CRM}</p>', unsafe_allow_html=True)


                        with col1:
                            st.markdown("**Ciudad**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codnod}</p>', unsafe_allow_html=True)

                        with col2:
                            st.markdown("**MDF**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Categorization_Tier2}</p>', unsafe_allow_html=True)

                        with col3:
                            st.markdown("**Cabec.**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{desmotv}</p>', unsafe_allow_html=True)

                        with col1:
                            st.markdown("**Circuito**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{CUSTOMERID_CRM__c}</p>', unsafe_allow_html=True)

                        with col2:
                            st.markdown("**Ubilic**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Area_CRM}</p>', unsafe_allow_html=True)
                        
                        with col3:
                            st.markdown("**Zonal**")
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:15px;border-radius:2%;">{desobsordtrab}</p>', unsafe_allow_html=True)
                        
                        with col1:
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            st.write("")
                            textogestion = "Realizar Actividades💻"
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:Black;font-size:22px;border-radius:2%;">{textogestion}</p>', unsafe_allow_html=True)
                        with col1:
                            filter_type3 = st.selectbox(
                                "Accion",
                                (
                                    "71_REVERIFICA SIN DEFECTO",
                                    "7B_SOLUCION EN LINEA",
                                    "7C_TEMA COMERCIALES",
                                    "7D_GENERA NUEVO REQ",
                                    #"7E_NO SE UBICA CLITE",
                                    "7F_REQ MAL GENERADO",
                                    "Requiere Visita Tecnica",
                                    "En espera",
                                ),
                                key="filter_type3",
                                help="""
                                Ten encuenta tu accion `Ticket` inf.
                                """,
                            )



                        st.write("")
                        #title = st.text_input("INGRESA TU GESTION")
                        raw_text = st.text_area("Observación", key="text")
                        #form = st.form(key='text')
                        #print(input)
                        def clear_text():
                            st.session_state["text"] = ""
                            
                        st.button("🗑️Limpiar ", on_click=clear_text)
                            
                        #st.button("clear text input", on_click=clear_text)

                        #st.button("Inicio")
                        col1, col2, col3 , col4, col5 = st.columns(5)

                        with col1:
                            pass
                        with col2:
                            pass
                        with col4:
                            pass
                        with col5:
                            pass
                        with col3 :

                            sql = """
                            SELECT * FROM bdtickets  WHERE ACCION = 'En espera'
                            """
                            esperadt = pd.read_sql(sql, cnxn)
                            esperadt2 = esperadt[esperadt['GESTOR'] == name]
                            #espera = esperadt2['codreq']
                            estoesp = int(len(esperadt2))
                            
                            #print(estoesp)


                                
                            if st.button("✔️Cerrar"):
                                #def __init__(self):
                                #    st.experimental_rerun()

                                sql1 = "UPDATE bdtickets SET ACCION = %s, OBS = %s, FEC_CERRAR = %s WHERE codreq = %s AND ACTIVO = '1' "
                                #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                                val1 = (filter_type3,raw_text,tiempo ,dfu2)
                                cursor.execute(sql1, val1)
                                #time.sleep(1)

                                #caching.clear_cache()
                                #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                                #st.info(dfu)
                                sql = "UPDATE bdtickets SET ESTADO = %s, GESTOR = %s, FEC_PROG = %s, ACTIVO = '1' WHERE codreq = %s AND ACTIVO = '0' "
                                val = (add, nom, tiempo, adwe)
                                cursor.execute(sql, val)
                                cnxn.commit()
                                #cursor.close()
                                #cnxn.close()
                                    ###TODO IMPORTANTE ES PARA REFRESCAR LA PAGINA
                                    #st.experimental_rerun()
                                    #st.legacy_caching.clear_cache()
                                    #st.legacy_caching.clear_cache()
                                #import pyautogui
                                #pyautogui.hotkey("ctrl","F5")
                                #st.experimental_singleton.clear()
                                st.balloons()
                                time.sleep(0.75)
                                st.experimental_rerun()

                                #

                            # st.experimental_rerun()
                            ## fondo total
                            def add_bg_from_url():
                                st.markdown(
                                    f"""
                                    <style>
                                    .stApp {{
                                        background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_960_720.jpg 1x, https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_1280.jpg");
                                        background-attachment: fixed;
                                        background-size: cover
                                    }}
                                    </style>
                                    """,
                                    unsafe_allow_html=True
                                )
                            add_bg_from_url() 




                if  genre == 'Finalizar':

                    #TODO SIVERVPARA BARRA AZUL
                    my_bar = st.progress(0)
                    ## fecha para programar y cerrar
                    date = datetime.now()
                    tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))
                    #print(tiempo) # DD Month, YYYY HH:MM:SS

                    options = (df2['codreq'].unique())

                    add  = str('CERRAR')
                    nom = str(name)
                    adwe = (str(options)[2:-2])
                    #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                    sql = "UPDATE bdtickets SET ESTADO = %s, GESTOR = %s WHERE codreq = %s AND ESTADO='PROGRAMADO'"
                    val = (add, nom, adwe)
                    cursor.execute(sql, val)


                    options = (df['codreq'].unique())

                    add  = str('PROGRAMADO')
                    nom = str(name)
                    adwe = (str(options)[2:-2])
                    #st.info(dfu2)

                    #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                    #st.info(dfu2)
                    ### un ejemplo para texto
                    #st.info(desobsordtrab)
                    #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{canti}</p>', unsafe_allow_html=True)
                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{dfunom}</p>', unsafe_allow_html=True)


                    
                    col1, col2, col3 = st.columns(3)



                    with col1:
                        st.markdown("**Numero de tickets**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{dfu2}</p>', unsafe_allow_html=True)

                        #filter_page_or_query = st.markdown("Dimension to filter #1"), st.markdown("<P style='text-align: center; color: BLUE;'>Some title</P>", unsafe_allow_html=True)

                    with col2:
                        st.markdown("**Codigo de cliente**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                        

                    with col3:
                        st.markdown("**Fecha de Ticket**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{fec_regist}</p>', unsafe_allow_html=True)


                    with col1:
                        st.markdown("**Tecnologia**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tiptecnologia_x}</p>', unsafe_allow_html=True)


                    with col2:
                        st.markdown("**Telefono**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">_{numtelefvoip}</p>', unsafe_allow_html=True)


                    with col3:
                        st.markdown("**Telf Ref**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{TELEFONO_REFERENCIA_1_CRM}</p>', unsafe_allow_html=True)


                    with col1:
                        st.markdown("**Nodo**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codnod}</p>', unsafe_allow_html=True)

                    with col2:
                        st.markdown("**CategTier 2**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Categorization_Tier2}</p>', unsafe_allow_html=True)

                    with col3:
                        st.markdown("**Observacion**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{desmotv}</p>', unsafe_allow_html=True)

                    with col1:
                        st.markdown("**Cuestomerid crm**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{CUSTOMERID_CRM__c}</p>', unsafe_allow_html=True)

                    with col2:
                        st.markdown("**Area crm**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Area_CRM}</p>', unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown("**Observacion 2**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:15px;border-radius:2%;">{desobsordtrab}</p>', unsafe_allow_html=True)
                    
                    with col1:
                        st.write("")
                        st.write("")
                        st.write("")
                        st.write("")
                        st.write("")
                        textogestion = "Realizar Actividades💻"
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:Black;font-size:22px;border-radius:2%;">{textogestion}</p>', unsafe_allow_html=True)
                    with col1:
                        filter_type3 = st.selectbox(
                            "Accion",
                            (
                                "71_REVERIFICA SIN DEFECTO",
                                "7B_SOLUCION EN LINEA",
                                "7C_TEMA COMERCIALES",
                                "7D_GENERA NUEVO REQ",
                                "7E_NO SE UBICA CLITE",
                                "7F_REQ MAL GENERADO",
                                "Requiere Visita Tecnica",
                            ),
                            key="filter_type3",
                            help="""
                            Ten encuenta tu accion `Ticket` inf.
                            """,
                        )


                    st.write("")
                    #title = st.text_input("INGRESA TU GESTION")
                    raw_text = st.text_area("Observación", key="text")
                    #form = st.form(key='text')
                    #print(input)
                    def clear_text():
                        st.session_state["text"] = ""
                        
                    st.button("🗑️Limpiar ", on_click=clear_text)
                        
                    #st.button("clear text input", on_click=clear_text)

                    #st.button("Inicio")
                    col1, col2, col3 , col4, col5 = st.columns(5)

                    with col1:
                        pass
                    with col2:
                        pass
                    with col4:
                        pass
                    with col5:
                        pass
                    with col3 :
                        
                        if st.button("😮‍💨Fin"):
                            #def __init__(self):
                            #    st.experimental_rerun()

                            sql1 = "UPDATE bdtickets SET ACCION = %s, OBS = %s, FEC_CERRAR = %s WHERE codreq = %s AND ACTIVO = '1' "
                            #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                            val1 = (filter_type3,raw_text,tiempo ,dfu2)
                            cursor.execute(sql1, val1)
                            cnxn.commit()

                            sql1 = "UPDATE bdtickets SET ESTADO = %s,GESTOR = '', FEC_PROG = '',ACTIVO = '0', LLAMADA = '0',ACCION ='' WHERE GESTOR = %s AND ACCION = '7E_NO SE UBICA CLITE'"
                            #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                            val1 = ('PENDIENTE', name)
                            cursor.execute(sql1, val1)
                            cnxn.commit()

                            #cursor.close()
                            #cnxn.close()
                                ###TODO IMPORTANTE ES PARA REFRESCAR LA PAGINA
                                #st.experimental_rerun()
                                #st.legacy_caching.clear_cache()
                                #st.legacy_caching.clear_cache()
                            #import pyautogui
                            #pyautogui.hotkey("ctrl","F5")
                            #st.experimental_singleton.clear()
                            st.experimental_rerun()



                if  genre == 'Dashboard':
                    #if  'Cardenas' == username:      #
                        st.markdown("""
                            <iframe title="Gastion19" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=0c6caef7-27cf-4548-849c-1970f2d9b0bf&autoAuth=true&ctid=9744600e-3e04-492e-baa1-25ec245c6f10" frameborder="0" allowFullScreen="true"></iframe>
                        """, unsafe_allow_html=True)

                        # st.experimental_rerun()
                        ## fondo total
                        def add_bg_from_url():
                            st.markdown(
                                f"""
                                <style>
                                .stApp {{
                                    background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_960_720.jpg 1x, https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_1280.jpg");
                                    background-attachment: fixed;
                                    background-size: cover
                                }}
                                </style>
                                """,
                                unsafe_allow_html=True
                            )
                        add_bg_from_url()



                if  genre == 'Analisis':
                    st.text("Cuadro de gestion individual!!!") 

                    st.success("Total tickets cerradas: " + " " + canti) 
                    ### programado
                    sql = """
                    SELECT GESTOR, codreq, FEC_PROG FROM bdtickets WHERE  ESTADO="PROGRAMADO" ;
                    """
                    df = pd.read_sql(sql, cnxn)
                    dfg = df[df['GESTOR'] == name]
                    #print(dfg)
                    #date = datetime.now()
                    #tcanti = (date.strftime("%Y-%m-%d"))
                ##### cantidad de programadas
                    #dfp = dfg
                    #dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG']).dt.date
                    #dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG'], format='%Y-%m-%d')
                    cantipro = str(len(dfg))
                    #print(cantipro)
                    st.info("Toltal tickets programado: " + " " + cantipro) 
                ##3 tranferir
                    sql = """
                    SELECT GESTOR, codreq, FEC_PROG FROM bdtickets WHERE  ACCION="7E_NO SE UBICA CLITE" ;
                    """
                    df = pd.read_sql(sql, cnxn)
                    dfg = df[df['GESTOR'] == name]
                    #print(dfg)
                    #date = datetime.now()
                    #tcanti = (date.strftime("%Y-%m-%d"))
                ##### cantidad de tranferir
                    #dfp = dfg
                    #dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG']).dt.date
                    #dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG'], format='%Y-%m-%d')
                    cantipro = str(len(dfg))
                    #print(cantipro)
                    #print("Tranferir" + " " + cantipro)
                    st.warning("Total tickest por llamar: " + " " + cantipro)

                    sql = """
                    SELECT * FROM bdtickets  WHERE ACCION = 'En espera' ;
                    """
                    df = pd.read_sql(sql, cnxn)
                    dfg = df[df['GESTOR'] == name]
                    #print(dfg)
                    #date = datetime.now()
                    #tcanti = (date.strftime("%Y-%m-%d"))
                ##### cantidad de tranferir
                    #dfp = dfg
                    #dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG']).dt.date
                    #dfp['FEC_PROG'] = pd.to_datetime(dfp['FEC_PROG'], format='%Y-%m-%d')
                    cantipro = str(len(dfg))
                    #print(cantipro)
                    #print("Tranferir" + " " + cantipro)
                    st.error("Total tickest En espera: " + " " + cantipro)

                if  genre == 'Masivas':

                    sql = """
                    SELECT * FROM bdtickets  WHERE ACCION = 'En espera'
                    """
                    esperadt = pd.read_sql(sql, cnxn)
                    esperadt2 = esperadt[esperadt['GESTOR'] == name]
                    espera = esperadt2['codreq']
                    
                    #print(espera)

                    filtro = st.selectbox(
                        "Tickets",
                        (espera
                        ),
                        key="filter_type3",
                        help="""
                        Ten encuenta tu accion `Ticket` inf.
                        """,
                    )

                    dtes = esperadt2[esperadt2['codreq'] == filtro]

                    nomcli = dtes['desnomctr']
                    nomcli = (nomcli.to_string(index=False))


                    tk = dtes['codreq']
                    tk = (tk.to_string(index=False))
                    codcli = dtes['codcli']
                    codcli = (codcli.to_string(index=False))
                    fec_regist = dtes['fec_regist']
                    fec_regist = (fec_regist.to_string(index=False))
                    tiptecnologia_x = dtes['tiptecnologia_x']
                    tiptecnologia_x = (tiptecnologia_x.to_string(index=False))
                    numtelefvoip = dtes['numtelefvoip']
                    numtelefvoip = (numtelefvoip.to_string(index=False))
                    TELEFONO_REFERENCIA_1_CRM = dtes['TELEFONO_REFERENCIA_1_CRM']
                    TELEFONO_REFERENCIA_1_CRM = (TELEFONO_REFERENCIA_1_CRM.to_string(index=False))
                    codnod = dtes['codnod']
                    codnod = (codnod.to_string(index=False))
                    Categorization_Tier2 = dtes['nomcli']
                    Categorization_Tier2 = (Categorization_Tier2.to_string(index=False))
                    desmotv = dtes['desmotv']
                    desmotv = (desmotv.to_string(index=False))
                    CUSTOMERID_CRM__c = dtes['desdtt']
                    CUSTOMERID_CRM__c = (CUSTOMERID_CRM__c.to_string(index=False))
                    Area_CRM = dtes['codofcadm']
                    Area_CRM = (Area_CRM.to_string(index=False))
                    desobsordtrab = dtes['desobsordtrab']
                    desobsordtrab = (desobsordtrab.to_string(index=False))


                    #TODO SIVERVPARA BARRA AZUL
                    my_bar = st.progress(0)
                    ## fecha para programar y cerrar
                    date = datetime.now()
                    tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))
                    #print(tiempo) # DD Month, YYYY HH:MM:SS


                    #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                    #st.info(dfu2)
                    ### un ejemplo para texto
                    #st.info(desobsordtrab)
                    #st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{canti}</p>', unsafe_allow_html=True)
                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">{nomcli}</p>', unsafe_allow_html=True)


                    
                    col1, col2, col3 = st.columns(3)



                    with col1:
                        st.markdown("**Numero de tickets**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tk}</p>', unsafe_allow_html=True)

                        #filter_page_or_query = st.markdown("Dimension to filter #1"), st.markdown("<P style='text-align: center; color: BLUE;'>Some title</P>", unsafe_allow_html=True)

                    with col2:
                        st.markdown("**Codigo de cliente**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                        

                    with col3:
                        st.markdown("**Fecha de Ticket**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{fec_regist}</p>', unsafe_allow_html=True)


                    with col1:
                        st.markdown("**Data**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tiptecnologia_x}</p>', unsafe_allow_html=True)


                    with col2:
                        st.markdown("**Origen**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">_{numtelefvoip}</p>', unsafe_allow_html=True)


                    with col3:
                        st.markdown("**Terminal**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{TELEFONO_REFERENCIA_1_CRM}</p>', unsafe_allow_html=True)


                    with col1:
                        st.markdown("**Ciudad**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codnod}</p>', unsafe_allow_html=True)

                    with col2:
                        st.markdown("**MDF**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Categorization_Tier2}</p>', unsafe_allow_html=True)

                    with col3:
                        st.markdown("**Cabec.**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{desmotv}</p>', unsafe_allow_html=True)

                    with col1:
                        st.markdown("**Circuito**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{CUSTOMERID_CRM__c}</p>', unsafe_allow_html=True)

                    with col2:
                        st.markdown("**Ubilic**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{Area_CRM}</p>', unsafe_allow_html=True)
                    
                    with col3:
                        st.markdown("**Zonal**")
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:15px;border-radius:2%;">{desobsordtrab}</p>', unsafe_allow_html=True)
                    
                    with col1:
                        st.write("")
                        st.write("")
                        st.write("")
                        st.write("")
                        st.write("")
                        textogestion = "Realizar Actividades💻"
                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:Black;font-size:22px;border-radius:2%;">{textogestion}</p>', unsafe_allow_html=True)
                    with col1:

                        filter_type3 = st.selectbox(
                            "Accion",
                            (
                                "71_REVERIFICA SIN DEFECTO",
                                "7B_SOLUCION EN LINEA",
                                "7C_TEMA COMERCIALES",
                                "7D_GENERA NUEVO REQ",
                                #"7E_NO SE UBICA CLITE",
                                "7F_REQ MAL GENERADO",
                                "Requiere Visita Tecnica",
                            ),
                            help="""
                            Ten encuenta tu accion `Ticket` inf.
                            """,
                        )


                    st.write("")
                    #title = st.text_input("INGRESA TU GESTION")
                    raw_text = st.text_area("Observación", key="text")
                    #form = st.form(key='text')
                    #print(input)
                    def clear_text():
                        st.session_state["text"] = ""
                        
                    st.button("🗑️Limpiar ", on_click=clear_text)
                        
                    #st.button("clear text input", on_click=clear_text)

                    #st.button("Inicio")
                    col1, col2, col3 , col4, col5 = st.columns(5)

                    with col1:
                        pass
                    with col2:
                        pass
                    with col4:
                        pass
                    with col5:
                        pass
                    with col3 :


                        if st.button("😮‍💨Fin"):
                            #def __init__(self):
                            #    st.experimental_rerun()

                            sql1 = "UPDATE bdtickets SET ACCION = %s, OBS = %s, FEC_CERRAR = %s WHERE codreq = %s AND ACTIVO = '1' "
                            #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                            val1 = (filter_type3,raw_text,tiempo ,tk)
                            cursor.execute(sql1, val1)
                            cnxn.commit()
                            #cursor.close()
                            #cnxn.close()
                                ###TODO IMPORTANTE ES PARA REFRESCAR LA PAGINA
                                #st.experimental_rerun()
                                #st.legacy_caching.clear_cache()
                                #st.legacy_caching.clear_cache()
                            #import pyautogui
                            #pyautogui.hotkey("ctrl","F5")
                            #st.experimental_singleton.clear()
                            st.experimental_rerun()


            except Error as e:
                print('디비 관련 에러 발생', e)

            finally : 
                # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
                #    커서와 커넥션을 모두 닫아준다.
                cursor.close()
                cnxn.close()
                #print('MYSQL 커넥션 종료')

            # para los botones horizontal
            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
            ## fondo total
            def add_bg_from_url():
                st.markdown(
                    f"""
                    <style>
                    .stApp {{
                        background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_960_720.jpg 1x, https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_1280.jpg");
                        background-attachment: fixed;
                        background-size: cover
                    }}
                    </style>
                    """,
                    unsafe_allow_html=True
                )
            add_bg_from_url() 
            try:

                ## botones en general
                primaryColor = st.get_option("theme.primaryColor")
                s = f"""
                <style>
                @import url('https://fonts.googleapis.com/css2?family=Atma:wght@600&display=swap');
                div.stButton > button:first-child {{ border: 5px solid {primaryColor}; border-radius:20px 20px 20px 20px; }}
                <style>
                """
                st.markdown(s, unsafe_allow_html=True)

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
                            background-image: url("https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_960_720.jpg 1x, https://cdn.pixabay.com/photo/2015/04/23/21/59/hot-air-balloon-736879_1280.jpg");
                            background-attachment: fixed;
                            background-size: cover
                        }}
                        </style>
                        """,
                        unsafe_allow_html=True
                    )
                add_bg_from_url() 
                ### para la barra
                for percent_complete in range(100):
                    time.sleep(0.01)
                    my_bar.progress(percent_complete + 1)
            except Exception as e:
                pass

            ## borrar nombres de la pagina
            hide_streamlit_style = """
                        <style>
                        #MainMenu {visibility: hidden;}
                        footer {visibility: hidden;}
                        header {visibility: hidden;}
                        </style>
                        """
            st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

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

            st.markdown(
                f"""
                <header class="css-1595djx e8zbici2">
                    <p class="logo-text">App Alarmas 👨🏻‍💻Giancarlos .C</p>
                </header>
                """,
                unsafe_allow_html=True
            )
            ###
            ####
            ####
            ####
            ######
            ######






    if selected == "Contact":

        xs = usernames = ['GAMARRA60', 'GONZALES61', 'CORONADO62', 'HUINCHO63', 'SOLARTE64', 'ZAPATA65', 'ROJAS66', 'CALATAYUD67', 'SEBASTIANI68', 'NOVOA69', 'CHAVEZ70', 'CARRION71', 'CHURATA72', 'TORREJON73', 'SILVA74', 'NAYAP75', 'USCUVILCA76', 'BERNAOLA77', 'ALMONACID78', 'JULCARIMA79', 'HUAIRE80', 'OTINIANO81', 'ROJAS82', 'FLORES83', 'NAPAN84', 'SOBERON85', 'PONCE86', 'SANTIBAÑEZ87', 'OBREGON88', 'FUENTES89', 'ENRIQUEZ90', 'CARRERA91', 'SILVERA92', 'LOPEZ93', 'LUQUE94', 'ALVA95', 'LAZO96', 'FABIAN97', 'AGUILAR98', 'RIVERA99', 'MELENDEZ100', 'YARIHUAMAN101', 'DIAZ102', 'ARANIBAR103', 'SAJAMI104', 'OSORIO105', 'ESPINOZA106', 'AZPUR107', 'ROSALES108', 'FIGARI109', 'CASTRO110']
        #xs = ['Cardenas', 'LLLERENAL', 'Hinostroza', 'Argomedo', 'VIERA']
        bs = (username in xs)

        if bs == True:

            #st.title(f"You have selected {selected}")
            #st.title(f"Hola {name} estamos en proceso de esta opcion...😮‍💨👨🏻‍💻")

            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,white, white);color:navy;font-size:24px;border-radius:2%;"><b>ENVIAR MENSAJE GESTION</b></p>', unsafe_allow_html=True)


            with st.form(key='my_form', clear_on_submit=True):

                    import streamlit as st
                    import streamlit as st
                    from streamlit_option_menu import option_menu
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


                    col1, col2, col3, col4 = st.columns(4)

                    with col1:
                        ticket = st.text_input('Ticket')
                    with col2:
                        celu = st.text_input('N° Cel')
                    with col3:
                        suscriptortelefono = st.text_input('codigo de serv')
                    with col4:
                        #servi = st.text_input('servicio')
                        motivo2desc = st.selectbox(
                            "servicio",
                            (
                            '',
                            'cableTv',
                            'telef fijo',
                            'internet',
                            ),
                            key="filter_type89",
                            help="""
                            Ten encuenta tu accion `servicio` inf.
                            """,
                        )

                        

                    mensaje = st.selectbox(
                        "Mensaje",
                        (
                        '',
                        'Cierra el caso con motivo: Cobertura WiFi',
                        'Cierra el caso con motivo: Configurac WiFi pss y ssid',
                        'Servicio operativo (parámetros OK)',
                        'Sin contacto (parámetros OK)',
                        'Cierra caso y genera avería',
                        'Refuerzo educativo TODOS'

                        ),
                        key="filter_type8",
                        help="""
                        Ten encuenta tu accion `Ticket` inf.
                        """,
                    )


                    #TODO SIVERVPARA BARRA AZUL
                    #celu = '925266696'
                    #print(celu)

                    st.balloons()
                # Every form must have a submit button.
                    submitted = st.form_submit_button("✉️Enviar")

                    if submitted == True:

                        dt1 = len(ticket)
                        dt2 = len(celu)
                        dt3 = len(suscriptortelefono)
                        dt4 = len(motivo2desc)

                        if dt1 > 0 and dt2 == 9 and  dt3 > 0 and  dt4 > 0:

                            with st.spinner('Enviado mensaje...'):

                                date = datetime.now()
                                tiempo = (date.strftime("%d-%m-%Y %H:%M:%S"))

                                cnxn = mysql.connector.connect( host="us-cdbr-east-06.cleardb.net",
                                                                port="3306",
                                                                user="be690637bd68c4",
                                                                passwd="88b2781e",
                                                                db="heroku_4843d4a20ed7194"
                                                                )
                                cursor = cnxn.cursor()

                                sql = "INSERT INTO bdmensaje (codreq, FECHA_ENV, SMS, CEL_num) VALUES (%s, %s, %s, %s)"
                                val = (ticket, tiempo, mensaje, celu)
                                cursor.execute(sql, val)
                                #cnxn.commit()

                                cnxn.commit()
                                cursor.close()
                                cnxn.close()
                                #print(dfunom)

                                import streamlit as st
                                import glob
                                import os
                                import time

                                import streamlit as st
                                from selenium import webdriver
                                from selenium.webdriver.chrome.options import Options
                                from selenium.webdriver.support.wait import WebDriverWait
                                from selenium.webdriver.common.by import By

                                options = Options()
                                options.add_argument("--headless")
                                options.add_argument("--no-sandbox")
                                options.add_argument("--disable-dev-shm-usage")
                                options.add_argument("--disable-gpu")
                                options.add_argument("--disable-features=NetworkService")
                                options.add_argument("--window-size=1920x1080")
                                options.add_argument("--disable-features=VizDisplayCompositor")

                                

                                #def delete_selenium_log():
                                #    if os.path.exists('selenium.log'):
                                #        os.remove('selenium.log')


                                #def show_selenium_log():
                                #    if os.path.exists('selenium.log'):
                                #        with open('selenium.log') as f:
                                #            content = f.read()
                                #            st.code(content)


                                # not required anymore:
                                # def get_chromedriver_path():
                                #     results = glob.glob('/**/chromedriver', recursive=True)  # workaround on streamlit sharing
                                #     return results[0]
                                #st.button("Inicio")

                                st.balloons()

                                

                                driver = webdriver.Chrome(options=options, service_log_path='selenium.log')

                                username = 'caramburu_TDP'
                                passwordd = 'WebSys29*T*'
                                driver.get("https://auth.movistaradvertising.com/login?logout")
                                time.sleep(1)

                                #pyautogui.hotkey("ctrl","F5")

                                

                                xpath = driver.find_element("xpath", '//INPUT[@id="username"]')
                                xpath.send_keys(username)
                                time.sleep(2)

                                xpath = driver.find_element("xpath", '//INPUT[@id="password"]')
                                xpath.send_keys(passwordd)
                                time.sleep(2)


                                xpath = driver.find_element("xpath", '//BUTTON[@type="submit"][text()="Ingresar"]')
                                xpath.click()
                                time.sleep(4)


                                xpath = driver.find_element("xpath", '//*[@id="dropdown-user-menu"]/div/button[2]')
                                xpath.click()
                                time.sleep(6)

                                xpath = driver.find_element("xpath", '//SPAN[@_ngcontent-c1=""][text()="SMSi"]')
                                xpath.click()
                                time.sleep(4)

                                #celu = '925266696'
                                #mensaje = 'Listoooossdddssss'

                                xpath = driver.find_element("xpath", '//INPUT[@id="inputGsmList"]')
                                xpath.send_keys(celu)
                                time.sleep(6)

                                if 'Cierra el caso con motivo: Cobertura WiFi' == mensaje:

                                    xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                                    xpath.send_keys(f"Hola, detectamos que la intermitencia del servicio {suscriptortelefono} se debe al alcance Wifi, recomendamos comprar un repetidor. Mas info al 080011800, Movistar.")
                                    time.sleep(6)


                                    xpath = driver.find_element("xpath", '//BUTTON[@id="buttonProcess"]')
                                    xpath.click()
                                    time.sleep(6)

                                    xpath = driver.find_element("xpath", '//*[@id="buttonSend"]')
                                    xpath.click()
                                    time.sleep(5)

                                    driver.quit()

                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">Mensaje enviado</p>', unsafe_allow_html=True)
                                    #st.success('Mensaje enviado')
                                    st.balloons()
                                    #st.experimental_rerun()

                                    col1, col2, col3 = st.columns(3)

                                    with col1:
                                        st.markdown("**Numero de tickets**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{ticket}</p>', unsafe_allow_html=True)

                                

                                    with col2:
                                        st.markdown("**Numero de codcli**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{suscriptortelefono}</p>', unsafe_allow_html=True)

                                

                                    with col3:
                                        st.markdown("**Servi**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{motivo2desc}</p>', unsafe_allow_html=True)

                                
                                if 'Cierra el caso con motivo: Configurac WiFi pss y ssid' == mensaje:


                                    xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                                    xpath.send_keys(f"Hola, se realizó la configuración de tu red WiFi del servicio {suscriptortelefono}. Sigue disfrutando de tu navegación, Movistar.")
                                    time.sleep(6)


                                    xpath = driver.find_element("xpath", '//BUTTON[@id="buttonProcess"]')
                                    xpath.click()
                                    time.sleep(6)

                                    xpath = driver.find_element("xpath", '//*[@id="buttonSend"]')
                                    xpath.click()
                                    time.sleep(5)

                                    driver.quit()

                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">Mensaje enviado</p>', unsafe_allow_html=True)

                                    #st.success('Mensaje enviado')
                                    st.balloons()
                                    #st.experimental_rerun()
                                    col1, col2, col3 = st.columns(3)

                                    with col1:
                                        st.markdown("**Numero de tickets**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{ticket}</p>', unsafe_allow_html=True)

                                

                                    with col2:
                                        st.markdown("**Numero de codcli**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{suscriptortelefono}</p>', unsafe_allow_html=True)

                                

                                    with col3:
                                        st.markdown("**Servi**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{motivo2desc}</p>', unsafe_allow_html=True)

                                if 'Servicio operativo (parámetros OK)' == mensaje:


                                    xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                                    xpath.send_keys(f"Hola, intentamos contactarte para validar que tu servicio de {motivo2desc} {suscriptortelefono} ya se encuentra operativo, por favor realizar las validaciones, Movistar.")
                                    time.sleep(6)


                                    xpath = driver.find_element("xpath", '//BUTTON[@id="buttonProcess"]')
                                    xpath.click()
                                    time.sleep(6)

                                    xpath = driver.find_element("xpath", '//*[@id="buttonSend"]')
                                    xpath.click()
                                    time.sleep(5)

                                    driver.quit()

                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">Mensaje enviado</p>', unsafe_allow_html=True)

                                    #st.success('Mensaje enviado')
                                    st.balloons()
                                    #st.experimental_rerun()
                                    col1, col2, col3 = st.columns(3)

                                    with col1:
                                        st.markdown("**Numero de tickets**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{ticket}</p>', unsafe_allow_html=True)

                                

                                    with col2:
                                        st.markdown("**Numero de codcli**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{suscriptortelefono}</p>', unsafe_allow_html=True)

                                

                                    with col3:
                                        st.markdown("**Servi**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{motivo2desc}</p>', unsafe_allow_html=True)

                                if 'Sin contacto (parámetros OK)' == mensaje:


                                    xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                                    xpath.send_keys(f"Hola, intentamos contactarte para validar que tu servicio de {motivo2desc} {suscriptortelefono} ya se encuentra operativo, intentaremos llamarte nuevamente, Movistar.")
                                    time.sleep(6)


                                    xpath = driver.find_element("xpath", '//BUTTON[@id="buttonProcess"]')
                                    xpath.click()
                                    time.sleep(6)

                                    xpath = driver.find_element("xpath", '//*[@id="buttonSend"]')
                                    xpath.click()
                                    time.sleep(5)

                                    driver.quit()

                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">Mensaje enviado</p>', unsafe_allow_html=True)

                                    #st.success('Mensaje enviado')
                                    st.balloons()
                                    #st.experimental_rerun()
                                    col1, col2, col3 = st.columns(3)

                                    with col1:
                                        st.markdown("**Numero de tickets**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{ticket}</p>', unsafe_allow_html=True)

                                

                                    with col2:
                                        st.markdown("**Numero de codcli**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{suscriptortelefono}</p>', unsafe_allow_html=True)

                                

                                    with col3:
                                        st.markdown("**Servi**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{motivo2desc}</p>', unsafe_allow_html=True)

                                if 'Cierra caso y genera avería' == mensaje:


                                    xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                                    xpath.send_keys(f"Hola, te contactamos por tu servicio de {motivo2desc}  {suscriptortelefono}, se generó la avería {ticket}, en las próximas horas un técnico te visitará, Movistar.")
                                    time.sleep(6)


                                    xpath = driver.find_element("xpath", '//BUTTON[@id="buttonProcess"]')
                                    xpath.click()
                                    time.sleep(6)

                                    xpath = driver.find_element("xpath", '//*[@id="buttonSend"]')
                                    xpath.click()
                                    time.sleep(5)

                                    driver.quit()

                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">Mensaje enviado</p>', unsafe_allow_html=True)

                                    #st.success('Mensaje enviado')
                                    st.balloons()
                                    #st.experimental_rerun()
                                    col1, col2, col3 = st.columns(3)

                                    with col1:
                                        st.markdown("**Numero de tickets**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{ticket}</p>', unsafe_allow_html=True)

                                

                                    with col2:
                                        st.markdown("**Numero de codcli**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{suscriptortelefono}</p>', unsafe_allow_html=True)

                                

                                    with col3:
                                        st.markdown("**Servi**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{motivo2desc}</p>', unsafe_allow_html=True)

                                if 'Refuerzo educativo TODOS' == mensaje:


                                    xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                                    xpath.send_keys(f"Hola, nos alegra haberte ayudado, tu {motivo2desc} {suscriptortelefono} se encuentra operativo. Disfruta tu navegación con estos tips http://smvst.com/tipsInt, Movistar.")
                                    time.sleep(6)


                                    xpath = driver.find_element("xpath", '//BUTTON[@id="buttonProcess"]')
                                    xpath.click()
                                    time.sleep(6)

                                    xpath = driver.find_element("xpath", '//*[@id="buttonSend"]')
                                    xpath.click()
                                    time.sleep(5)

                                    driver.quit()

                                    st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,Cyan, Cyan);color:BLACK;font-size:16px;border-radius:2%;">Mensaje enviado</p>', unsafe_allow_html=True)

                                    #st.success('Mensaje enviado')
                                    st.balloons()
                                    #st.experimental_rerun()
                                    col1, col2, col3 = st.columns(3)

                                    with col1:
                                        st.markdown("**Numero de tickets**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{ticket}</p>', unsafe_allow_html=True)

                                

                                    with col2:
                                        st.markdown("**Numero de codcli**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{suscriptortelefono}</p>', unsafe_allow_html=True)

                                

                                    with col3:
                                        st.markdown("**Servi**")
                                        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{motivo2desc}</p>', unsafe_allow_html=True)

                        else:
                            #st.error('👀 TIENES QUE ESCRIBIR EN TODOS LOS INPUT👀 ')
                            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,#e30052, #e30052);color:white;font-size:18px;border-radius:2%;"><b>😡👀 TE FALTA INGRESAR LOS DATOS REQUERIDOS 👀😡</b></p>', unsafe_allow_html=True)

            df = pd.DataFrame()
            df['CASO'] = [ 
                    'Cierra el caso con motivo: Cobertura WiFi',
                    'Cierra el caso con motivo: Configurac WiFi pss y ssid',
                    'Servicio operativo (parámetros OK)',
                    'Sin contacto (parámetros OK)',
                    'Cierra caso y genera avería',
                    'Refuerzo educativo TODOS']
                                
            df['SMS'] = [
                    'Hola, detectamos que la intermitencia del servicio {suscriptortelefono} se debe al alcance Wifi, recomendamos comprar un repetidor. Mas info al 080011800, Movistar.',
                    'Hola, se realizó la configuración de tu red WiFi del servicio {suscriptortelefono}. Sigue disfrutando de tu navegación, Movistar.',
                    'Hola, intentamos contactarte para validar que tu servicio de {motivo2desc} {suscriptortelefono} ya se encuentra operativo, por favor realizar las validaciones, Movistar.',
                    'Hola, intentamos contactarte para validar que tu servicio de {motivo2desc} {suscriptortelefono} ya se encuentra operativo, intentaremos llamarte nuevamente, Movistar.',
                    'Hola, te contactamos por tu servicio de {motivo2desc}  {suscriptortelefono}, se generó la avería {ticket}, en las próximas horas un técnico te visitará, Movistar.',
                    'Hola, nos alegra haberte ayudado, tu {motivo2desc} (suscriptortelefono) se encuentra operativo. Disfruta tu navegación con estos tips http://smvst.com/tipsInt, Movistar.']
            st.dataframe(df)

    if selected == "Report":

        xs = usernames = ['GUILLERMOAPP']
        #xs = ['Cardenas', 'LLLERENAL', 'Hinostroza', 'Argomedo', 'VIERA']
        bs = (username in xs)

        if bs == True:
            st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,white, white);color:navy;font-size:24px;border-radius:2%;"><b>sistematizar procesos de data GESTION</b></p>', unsafe_allow_html=True)

            st.sidebar.subheader("Cargar datos de acuerdo a lo requerido")

                    # Setup file upload
            uploaded_file = st.sidebar.file_uploader(
                                    label="Solo cargar data TT y CMR. (200MB max)",
                                    type=['csv', 'xlsx', 'XLS'])

            #global df
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

                        if columdf == 72:

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

                        #else:
                        #    st.error('DATA NO CORRESPONDE LOS PARAMETROS👋🏻')


                    except Exception as e:
                        st.error('DATA NO CORRESPONDE 👋🏻')

                    finally :
                        # 5. 모든 데이터베이스 실행 명령을 전부 끝냈으면,
                        #    커서와 커넥션을 모두 닫아준다.
                        cursor.close()
                        cnxn.close()

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
