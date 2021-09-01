from datetime import datetime
import pandas as pd
import openpyxl

fsell = 'C:/worker/sell_orel.csv'
fpart = 'C:/worker/part.xlsx'

dfpart = pd.read_excel(fpart, header=0, engine='openpyxl', dtype={'company_id': str, 'type': str})
regname = 'RegisterSubscriptionSales_00057_00046_1000000001_' + str(datetime.today().strftime("%Y%m%d")) + '.csv'
df = pd.read_csv(fsell, delimiter=',', header=0, dtype={'price': int})
amount = 0
comp_id = 243
part = 0
tid = 145

# def write_str(t_id, c_id):
#     dfp = df.loc[df['type_id'].isin(t_id)]
#     for i in dfp.index:
#         dfreg = pd.read_csv('c:/worker/' + regname, header=0, dtype={'amount': int})
#         dfcomp = dfreg['organizationID'].isin(comp_id)['ticket_id'].isin(t_id)
#         cur_sum = dfcomp['amount'].sum() + df['priсe'][i]
#         if cur_sum <= amount:
#             if part != 0:
#                 string = str(c_id) + ';0;0;1;' + str(dfp['card'][i]) + ';' + str(dfp['type_id'][i]) + ';' + str(
#                     part) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
#             else:
#                 string = str(c_id) + ';0;0;1;' + str(dfp['card'][i]) + ';' + str(dfp['type_id'][i]) + ';' + str(
#                     df['priсe'][i]) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
#             with open('c:/worker/' + regname, 'a') as f_in:
#                 f_in.write(string + "\n")
#             part = 0
#         elif cur_sum > amount:
#             part = cur_sum - amount
#             string = str(c_id) + ';0;0;1;' + str(dfp['card'][i]) + ';' + str(dfp['type_id'][i]) + ';' + str(
#                 df['priсe'][i] - part) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
#             with open('c:/worker/' + regname, 'a') as f_in:
#                 f_in.write(string + "\n")

with open('c:/worker/' + regname, 'a') as f_in:
    f_in.write("OrganizationID;INN;BIC;MifareUID;TransportCardID;TicketID;Amount;Datetime\n")
for i in df.index:
    for t in dfpart.index:
        print(str(dfpart['type'][t]))
        t_id = str(dfpart['type'][t])
        c_id = str(dfpart['company_id'][t])
        dfp = df.loc[df['type_id'].isin([145])]
        for l in dfp.index:
            dfreg = pd.read_csv('c:/worker/' + regname, header=0, dtype={'amount': int}, delimiter=';')
            if dfreg.empty:
                cur_sum = 0

            else:
                dfcomp = dfreg.loc[dfreg['OrganizationID'].isin([c_id])]
                print(dfcomp)
                cur_sum = dfcomp['Amount'].sum()
            print(dfpart['amount'][t])
            amount = dfpart['amount'][t]
            cur_sum = cur_sum + df['priсe'][i]
            if cur_sum <= amount:
                if part != 0:
                    string = str(c_id) + ';0;0;1;' + str(dfp['card'][l]) + ';' + str(dfp['type_id'][l]) + ';' + str(
                        part) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
                else:
                    string = str(c_id) + ';0;0;1;' + str(dfp['card'][l]) + ';' + str(dfp['type_id'][l]) + ';' + str(
                        df['priсe'][i]) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
                with open('c:/worker/' + regname, 'a') as f_in:
                    f_in.write(string + "\n")
                part = 0
            elif cur_sum > amount:
                part = cur_sum - amount
                string = str(c_id) + ';0;0;1;' + str(dfp['card'][l]) + ';' + str(dfp['type_id'][l]) + ';' + str(
                    df['priсe'][i] - part) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
                with open('c:/worker/' + regname, 'a') as f_in:
                    f_in.write(string + "\n")
                t=t+1

