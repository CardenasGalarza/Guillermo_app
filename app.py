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

    xs = ['Cardenas', 'Genesis', 'LLLERENAL', 'BERNEDO', 'CERVERA', 'CHUNGA', 'VIERA', 'RAYMUNDO', 'CABANILLAS', 'RIMARACHIN', 'BENAVIDES', 'YEREN', 'BELLIDO', 'ANDREA', 'SANTA ANA', 'POMA REYES', 'ECHEVARRIA', 'MORI', 'PAULINO', 'SALCEDO', 'MAYORCA', 'PRUDENCIO', 'HUAMANCHUMO', 'Argomedo', 'Hinostroza', 'Bot', 'YERSON', 'Roberto']
    #xs = ['Cardenas', 'LLLERENAL', 'Hinostroza', 'Argomedo', 'VIERA']
    bs = (username in xs)

    if bs == True:

        #st.title(f"You have selected {selected}")
        #st.title(f"Hola {name} estamos en proceso de esta opcion...😮‍💨👨🏻‍💻")

        st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,white, white);color:navy;font-size:24px;border-radius:2%;"><b>ENVIAR MENSAJE GESTION</b></p>', unsafe_allow_html=True)


        with st.form(key='my_form', clear_on_submit=True):

                import streamlit as st
                import streamlit as st
                #from streamlit_option_menu import option_menu
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


                col1, col2, col3 = st.columns(3)

                with col1:
                    tick = st.text_input('Tickets')
                with col2:
                    celu = st.text_input('Numero')

                    

                mensaje = st.selectbox(
                    "Mensaje",
                    (
                    'Cliente no contesta volver a llamar',
                    'Se liquida sin contacto (parámetro ok)',
                    'Cierra el caso con motivo: Cobertura WiFi',
                    'Cierra el caso con motivo: Configurac WiFi pss y ssid',
                    'Servicio operativo (parámetros OK)',
                    'Cierra caso y genera avería',

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

                        #cursor.execute("UPDATE bdtickets SET ESTADO = ?, GESTOR = ? WHERE codreq = ?", add, nom, adwe)
                        sql = """
                        SELECT codreq, CUSTOMERID_CRM__c, servicioAfectado, MENSAJE FROM bdtickets WHERE codreq = %s ;
                        """
                        ##TODO SIEMPRE PONER LA COMA
                        cursor.execute(sql, (tick,))
                        # fetch result
                        record = cursor.fetchall()
                        #print(record)
                        #cursor.close()
                        #cnxn.close()

                        gian = pd.DataFrame(record)
                        gian.columns = ['codreq', 'CUSTOMERID_CRM__c', 'servicioAfectado', 'MENSAJE']
                        #for row in record:
                        #    print("GESTOR = ", row[0], )
                        #    print("codreq = ", row[1])
                        #    print("FEC_CERRAR = ", row[2])
                        #dfg = gian[gian['GESTOR'] == 'Giancarlos Cardenas']

                        tick =gian["codreq"]
                        tick = (tick.to_string(index=False))

                        servi =gian["servicioAfectado"]
                        servi = (servi.to_string(index=False))

                        codcli =gian["CUSTOMERID_CRM__c"]
                        codcli = (codcli.to_string(index=False))

                        numllamada = (gian['MENSAJE'].unique())
                        numllamada = (str(numllamada)[2:-2])
                        #print(numllamada)
                        sumu = int(numllamada) + 1


                        sql = "INSERT INTO bdmensaje (codreq, FECHA_ENV, SMS) VALUES (%s, %s, %s)"
                        val = (tick, tiempo, mensaje)
                        cursor.execute(sql, val)
                        #cnxn.commit()
                        sql1 = "UPDATE bdtickets SET MENSAJE = %s WHERE codreq = %s"
                        #sql1 = "INSERT INTO gestionacc (codreq, ACCION) VALUES (%s, %s)"
                        val1 = (sumu, tick)
                        cursor.execute(sql1, val1)

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

                        if 'Cliente no contesta volver a llamar' == mensaje:

                            xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                            xpath.send_keys(f"Hola, intentamos contactarte para solucionar la avería en tu {servi} {codcli}, estaremos contactandote nuevamente, Movistar.")
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
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tick}</p>', unsafe_allow_html=True)

                        

                            with col2:
                                st.markdown("**Numero de codcli**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                        

                            with col3:
                                st.markdown("**Servi**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{servi}</p>', unsafe_allow_html=True)

                        
                        if 'Se liquida sin contacto (parámetro ok)' == mensaje:


                            xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                            xpath.send_keys(f"Hola, intentamos contactarte para validar que tu {servi} {codcli} , ya se encuentra operativo, por favor realizar las validaciones, Movistar")
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
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tick}</p>', unsafe_allow_html=True)

                        

                            with col2:
                                st.markdown("**Numero de codcli**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                        

                            with col3:
                                st.markdown("**Servi**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{servi}</p>', unsafe_allow_html=True)

                        if 'Cierra el caso con motivo: Cobertura WiFi' == mensaje:


                            xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                            xpath.send_keys(f"Hola, detectamos que la intermitencia del servicio {codcli} se debe al alcance Wifi, recomendamos comprar un repetidor. Más info al 080011800, Movistar.")
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
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tick}</p>', unsafe_allow_html=True)

                        

                            with col2:
                                st.markdown("**Numero de codcli**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                        

                            with col3:
                                st.markdown("**Servi**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{servi}</p>', unsafe_allow_html=True)

                        if 'Cierra el caso con motivo: Configurac WiFi pss y ssid' == mensaje:


                            xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                            xpath.send_keys(f"Hola, se realizó la configuración de tu red WiFi del servicio {codcli}. Sigue pssy ssid disfrutando de tu navegación, Movistar.")
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
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tick}</p>', unsafe_allow_html=True)

                        

                            with col2:
                                st.markdown("**Numero de codcli**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                        

                            with col3:
                                st.markdown("**Servi**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{servi}</p>', unsafe_allow_html=True)

                        if 'Servicio operativo (parámetros OK)' == mensaje:


                            xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                            xpath.send_keys(f"Hola, nos alegra haberte ayudado, tu servicio de {servi} con código de servicio {codcli} se encuentra operativo. Disfruta de tu navegación, Movistar.")
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
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tick}</p>', unsafe_allow_html=True)

                        

                            with col2:
                                st.markdown("**Numero de codcli**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                        

                            with col3:
                                st.markdown("**Servi**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{servi}</p>', unsafe_allow_html=True)

                        if 'Cierra caso y genera avería' == mensaje:


                            xpath = driver.find_element("xpath", '//TEXTAREA[@id="txtMessage"]')
                            xpath.send_keys(f"Hola, te contactamos para indicarte que hemos generado el ticket de avería ticket. Nos pondremos en contacto en las próximas horas, Movistar")
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
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{tick}</p>', unsafe_allow_html=True)

                        

                            with col2:
                                st.markdown("**Numero de codcli**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{codcli}</p>', unsafe_allow_html=True)

                        

                            with col3:
                                st.markdown("**Servi**")
                                st.markdown(f'<p class="big-font"; style="text-align:center;background-image: linear-gradient(to right,LAVENDER, LAVENDER);color:BLACK;font-size:18px;border-radius:2%;">{servi}</p>', unsafe_allow_html=True)

                df = pd.DataFrame()
                df['CASO'] = ['Cliente no contesta volver a llamar',
                                    'Se liquida sin contacto (parámetro ok)',
                                    'Cierra el caso con motivo: Cobertura WiFi',
                                    'Cierra el caso con motivo: Configurac WiFi pss y ssid',
                                    'Servicio operativo (parámetros OK)',
                                    'Cierra caso y genera avería']
                                    
                df['SMS'] = ['Hola, intentamos contactarte para solucionar la avería en tu {servi} {codcli}, estaremos contactandote nuevamente, Movistar.',
                                'Hola, intentamos contactarte para validar que tu {servi} {codcli} , ya se encuentra operativo, por favor realizar las validaciones, Movistar',
                                'Hola, detectamos que la intermitencia del servicio {codcli} se debe al alcance Wifi, recomendamos comprar un repetidor. Mas info al 080011800, Movistar.',
                                'Hola, se realizó la configuración de tu red WiFi del servicio {codcli}. Sigue pssy ssid disfrutando de tu navegación, Movistar.',
                                'Hola, nos alegra haberte ayudado, tu servicio de {servi} con código de servicio {codcli} se encuentra operativo. Disfruta de tu navegación, Movistar.',
                                'Hola, te contactamos para indicarte que hemos generado el ticket de avería ticket. Nos pondremos en contacto en las próximas horas, Movistar']
                st.dataframe(df)

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
