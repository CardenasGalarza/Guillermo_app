import os
import sys
import streamlit.web.cli as stcli
import warnings
import streamlit as st
import pickle
from pathlib import Path
import pandas as pd
import numpy as np
#from soupsieve import select  # pip install pandas openpyxl
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
############################################ OCULTAR INFROMACION NO IMPORTANTE
import base64
import streamlit as st
############################################ OCULTAR INFROMACION NO IMPORTANTE
import warnings
warnings.filterwarnings('ignore')
#########################################3333
##########################
from datetime import datetime
import gspread
#import pyautogui
from pkg_resources import working_set
warnings.filterwarnings('ignore')
#####3333
##########################
import time
from datetime import datetime
import mysql.connector


if __name__ == '__main__':

    launchdir = os.path.dirname(sys.argv[0])

    #if launchdir == '':
    #    launchdir = '.'

    print(launchdir)
    #sys.argv = ["streamlit", "run", f"{launchdir}/app.py", "--server.port=10000", "--server.headless=true", "--global.developmentMode=false"]
    sys.argv = ["streamlit", "run", "https://raw.githubusercontent.com/CardenasGalarza/railway_Gestion_19/main/app.py", "--server.port=10000", "--server.headless=true", "--global.developmentMode=false"]
    #sys.argv = ["streamlit", "run", f"{launchdir}/app.py", "--global.developmentMode=false"]
    sys.exit(stcli.main())


