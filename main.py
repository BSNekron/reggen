from datetime import datetime
import pandas as pd
import openpyxl
fsell = 'C:/worker/sell.csv'
fpart = 'C:/worker/part.xlsx'
df = pd.read_csv(fsell, delimiter=',', header=0, dtype={'price': int})
dfp = df.loc[df['tid'].isin([49, 45, 173, 47])]
dfpart = pd.read_excel(fpart, header=0, engine='openpyxl')
print(dfp.index)
amountnow =0
for i in dfp.index:
         string = '112;0;0;1;' + str(dfp['card'][i]) + ';' + str(dfp['type_id'][i]) + ';' + str(
            df['priсe'][i]) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
         print(string)