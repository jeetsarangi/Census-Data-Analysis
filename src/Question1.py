import pandas as pd
import numpy as np

langdata = pd.read_excel("DDW-C18-0000.xlsx")
censusdata = pd.read_excel("DDW_PCA0000_2011_Indiastatedist.xlsx")

censusdata.head(10)
censusdata['Name'] = censusdata['Name'].replace(['India'],'INDIA')
censusdata.head()
censusdata = censusdata[["Name","TOT_P","TRU"]]
censusdata = censusdata[censusdata["TRU"]=="Total"]
censusdata
langdata.head(20)

fil_lang_data = langdata[(langdata["Unnamed: 3"] == "Total") & (langdata["Unnamed: 4"]=="Total")]
loc_list = list(fil_lang_data["Unnamed: 2"])
loc_list

out = []
for i in loc_list:
    temp1 = fil_lang_data[fil_lang_data["Unnamed: 2"]==i]
    tot_pop = censusdata[(censusdata["Name"]==i)].iloc[0,1]
    out.append((temp1.iloc[0,0],i,temp1.iloc[0,5],temp1.iloc[0,8],tot_pop))

result = []
for i in out:
    one = i[4]-i[2]
    two = i[2]-i[3]
    three = i[3]
    result.append((i[0],i[1],(one/i[4])*100,(two/i[4])*100,(three/i[4])*100))

dic = {"state-code":[row[0] for row in result],"percent-one":[row[2] for row in result],"percent-two":[row[3] for row in result],"percent-three":[row[4] for row in result]}
df = pd.DataFrame(dic)
df.to_csv('percent-india.csv', index=False)

