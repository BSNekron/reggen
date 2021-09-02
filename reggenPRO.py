from datetime import datetime
import pandas as pd
import openpyxl

fsell = 'C:/worker/sell_orel.csv'
fpart = 'C:/worker/part.xlsx'

dfpart = pd.read_excel(fpart, header=0, engine='openpyxl', dtype={'company_id': str, 'type': str})
regname = 'RegisterSubscriptionSales_00057_00046_1000000001_' + str(datetime.today().strftime("%Y%m%d")) + '.csv'
df = pd.read_csv(fsell, delimiter=',', header=0, dtype={'price': int})
part = 0
start = 0
prev_tid = 0

with open('c:/worker/' + regname, 'a') as f_in:
    f_in.write("OrganizationID;INN;BIC;MifareUID;TransportCardID;TicketID;Amount;Datetime\n")
for t in dfpart.index:
    print(str(dfpart['type'][t] + ' : ' + dfpart['company_id'][t]))
    t_id = str(dfpart['type'][t])
    c_id = str(dfpart['company_id'][t])
    dfp = df.loc[df['type_id'].isin([t_id])]
    dfp = dfp.reset_index()
    if int(t_id) != prev_tid:
        start = 0
        part = 0
    for i in range(start, dfp.index.max(), 1):
        dfreg = pd.read_csv('c:/worker/' + regname, header=0, dtype={'amount': int}, delimiter=';')
        if dfreg.empty:
            cur_sum = 0
        else:
            dfcomp = dfreg.loc[dfreg['OrganizationID'].isin([c_id])]
            dfcomp = dfcomp.loc[dfcomp['TicketID'].isin([t_id])]
            cur_sum = dfcomp['Amount'].sum()
        amount = dfpart['amount'][t]
        cur_sum = cur_sum + dfp['priсe'][i]
        if cur_sum <= amount:
            if part != 0:
                string = str(c_id) + ';0;0;1;' + str(dfp['card'][i]) + ';' + str(dfp['type_id'][i]) + ';' + str(
                    part) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
            else:
                string = str(c_id) + ';0;0;1;' + str(dfp['card'][i]) + ';' + str(dfp['type_id'][i]) + ';' + str(
                    dfp['priсe'][i]) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
            with open('c:/worker/' + regname, 'a') as f_in:
                f_in.write(string + "\n")
            part = 0
        elif cur_sum > amount:
            part = cur_sum - amount
            string = str(c_id) + ';0;0;1;' + str(dfp['card'][i]) + ';' + str(dfp['type_id'][i]) + ';' + str(
                dfp['priсe'][i] - part) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
            with open('c:/worker/' + regname, 'a') as f_in:
                f_in.write(string + "\n")
            start = i
            prev_tid = dfp['type_id'][i]
            dfreg = pd.read_csv('c:/worker/' + regname, header=0, dtype={'amount': int}, delimiter=';')
            dfcomp = dfreg.loc[dfreg['OrganizationID'].isin([c_id])]
            dfcomp = dfcomp.loc[dfcomp['TicketID'].isin([t_id])]
            print(dfcomp['Amount'].sum())
            break
