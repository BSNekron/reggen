from datetime import datetime
import pandas as pd

fsell = 'C:/worker/sell.csv'
fpart = 'C:/worker/part.xlsx'
df = pd.read_csv(fsell, delimiter=',', header=0, dtype={'price': int})
dfpart = pd.read_excel(fpart, header=0, engine='openpyxl')
print(df)
amountnow =0
for i in df.index:
    if df['tid'][i] in [49, 45, 173, 47]:
        string = '112;0;0;1;' + str(df['card'][i]) + ';' + str(df['type_id'][i]) + ';' + str(
            df['priсe'][i]) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))

    elif df['tid'][i] in [174, 44, 46, 48]:
        string = '113;0;0;1;' + str(df['card'][i]) + ';' + str(df['type_id'][i]) + ';' + str(
            df['priсe'][i]) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
    elif df['tid'][i] in [34, 28, 50, 33]:
        sub_df = dfpart[dfpart['company_id'] == 112]
        sumamount = sub_df['amount'][0]
        amountnow = amountnow + df['priсe'][i]
        if amountnow < sumamount :
            string = '113;0;0;1;' + str(df['card'][i]) + ';' + str(df['type_id'][i]) + ';' + str(
                df['priсe'][i]) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))

        elif amountnow > sumamount:
            amountnow = amountnow - sumamount
            string = '113;0;0;1;' + str(df['card'][i]) + ';' + str(df['type_id'][i]) + ';' + str(
                amountnow) + ';' + str(datetime.today().strftime("%d.%m.%Y %H:%M:%S"))
            print(amountnow)
            amountnow = 0