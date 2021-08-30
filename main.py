from datetime import datetime
import pandas as pd
import openpyxl


def write_str(t_id, c_id):
    dfp = df.loc[df['tid'].isin(t_id)]
    for i in dfp.index:
        string = str(c_id) + ';0;0;1;' + str(dfp['card'][i]) + ';' + str(dfp['type_id'][i]) + ';' + str(
            df['priсe'][i]) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
        print(string)


fsell = 'C:/worker/sell.csv'
fpart = 'C:/worker/part.xlsx'
df = pd.read_csv(fsell, delimiter=',', header=0, dtype={'price': int})
dfpart = pd.read_excel(fpart, header=0, engine='openpyxl')
amountnow = 0
write_str([49, 45, 173, 47], 112)
write_str([174, 44, 46, 48], 113)
dfp = df.loc[df['tid'].isin([34, 28, 50, 33])]

