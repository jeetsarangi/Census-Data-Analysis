import pandas as pd
import numpy as np

langdata = pd.read_excel("DDW-C18-0000.xlsx")
POP_data = pd.read_excel("DDW-0000C-14.xls")

POP_data = POP_data.rename(columns = {'C-14 POPULATION IN FIVE YEAR AGE-GROUP BY RESIDENCE AND SEX ':"Unnamed:4"})
POP_data = POP_data[['Unnamed: 1','Unnamed:4','Unnamed: 5']]

agegroups = {'5-9':['5-9'],'10-14':['10-14'],'15-19':['15-19'],'20-24':['20-24'],'25-29':['25-29'],'30-49':['30-34','35-39','40-44','45-49'],'50-69':['50-54','55-59','60-64','65-69'],'70+':['70-74','75-79','80+']}

fil_lang_data = langdata[(langdata["Unnamed: 3"] == "Total")]
loc_list = list(set(fil_lang_data["C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX"]))

out = []
for code in loc_list:
    
    temp1 = fil_lang_data[(fil_lang_data['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX']==code)]
    max_percentage = 0
    bestgroup = '5-9'
    for age in agegroups:
        speaking = temp1[temp1['Unnamed: 4']==age].iloc[0,8]
        group1 = agegroups[age]
        tot = 0
        for i in group1:
            tot += int(POP_data[(POP_data['Unnamed: 1']==code) & (POP_data['Unnamed:4']==i)].iloc[0,2])
        curr_percentage = speaking/tot
        if max_percentage < curr_percentage:
            bestgroup = age
            max_percentage = curr_percentage
    out.append((code,temp1.iloc[0,2],bestgroup,max_percentage*100))

temp1[temp1['Unnamed: 4']==age]
out.sort()

dic = {"State-Code":[row[0] for row in out],"state/ut":[row[1] for row in out],"age-group":[row[2] for row in out],"percentage":[row[3] for row in out]}
df = pd.DataFrame(dic)
df.to_csv('age-india.csv', index=False)

