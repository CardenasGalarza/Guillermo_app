import pandas as pd
import gspread
Trouble = pd.read_excel('DATA/Base Total Trouble Tickets Pendientes - 20 Dec 2022.xlsx', engine="openpyxl", skiprows=3)
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

print(df)
