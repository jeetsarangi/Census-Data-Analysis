import pandas as pd
import numpy as np

langdata = pd.read_excel("DDW-C18-0000.xlsx")
censusdata = pd.read_excel("DDW_PCA0000_2011_Indiastatedist.xlsx")
censusdata.head(10)
censusdata['Name'] = censusdata['Name'].replace(['India'],'INDIA')
censusdata.head()
censusdata = censusdata[["Name","TOT_P","TRU"]]
censusdata = censusdata[censusdata["TRU"]=="Total"]

langdata.head(10)
index = langdata[langdata['C-18 POPULATION BY BILINGUALISM, TRILINGUALISM, AGE AND SEX']=="00"].index
langdata.drop(index,inplace = True)

fil_lang_data = langdata[(langdata["Unnamed: 3"] == "Total") & (langdata["Unnamed: 4"]=="Total")]
loc_list = list(fil_lang_data["Unnamed: 2"])

out = []
for i in loc_list:
    temp1 = fil_lang_data[fil_lang_data["Unnamed: 2"]==i]
    tot_pop = censusdata[(censusdata["Name"]==i)].iloc[0,1]
    out.append((temp1.iloc[0,0],i,temp1.iloc[0,5],temp1.iloc[0,8],tot_pop))

result = []
for row in out:
    deno = row[2]-row[3]
    num = row[3]
    ratio = num/deno
    result.append((row[0],row[1],ratio))

result = sorted(result, key=lambda x: x[2])

result1 = result[-3:][::-1]
for i in result[:3]:
    result1.append(i)

dic = {"State-code":[i[0] for i in result1],"State/Ut":[i[1] for i in result1]}
df = pd.DataFrame(dic)
df.to_csv('3-to-2-ratio.csv', index=False)

