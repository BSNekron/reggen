from datetime import datetime
import pandas as pd
import openpyxl

fsell = 'C:/worker/sell_orel.csv'
fpart = 'C:/worker/part.xlsx'

dfpart = pd.read_excel(fpart, header=0, engine='openpyxl')
regname = 'RegisterSubscriptionSales_00057_00046_1000000001_' + str(datetime.today().strftime("%Y%m%d")) + '.csv'
df = pd.read_csv(fsell, delimiter=',', header=0, dtype={'price': int})
amount = 0
comp_id = 77
part = 0


def write_str(t_id, c_id):
    dfp = df.loc[df['tid'].isin(t_id)]
    for i in dfp.index:
        dfreg = pd.read_csv('c:/worker/' + regname, header=0, dtype={'amount': int})
        dfcomp = dfreg['organizationID'].isin(comp_id)
        cur_sum = dfcomp['amount'].sum() + df['priсe'][i]
        if cur_sum <= amount:
            if part != 0:
                string = str(c_id) + ';0;0;1;' + str(dfp['card'][i]) + ';' + str(dfp['type_id'][i]) + ';' + str(
                    part) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
            else:
                string = str(c_id) + ';0;0;1;' + str(dfp['card'][i]) + ';' + str(dfp['type_id'][i]) + ';' + str(
                    df['priсe'][i]) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
            with open('c:/worker/' + regname, 'a') as f_in:
                f_in.write(string + "\n")
            part = 0
        elif cur_sum > amount:
            part = cur_sum - amount
            string = str(c_id) + ';0;0;1;' + str(dfp['card'][i]) + ';' + str(dfp['type_id'][i]) + ';' + str(
                df['priсe'][i] - part) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
            with open('c:/worker/' + regname, 'a') as f_in:
                f_in.write(string + "\n")
