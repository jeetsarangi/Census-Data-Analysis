import pandas as pd
from scipy import stats
langdata = pd.read_excel("DDW-C18-0000.xlsx",skiprows = 6,header = None)
censusdata = pd.read_excel("DDW_PCA0000_2011_Indiastatedist.xlsx")

langdata = langdata[langdata[4]=="Total"]
index = langdata[langdata[3]=="Total"].index
langdata.drop(index,inplace = True)
langdata = langdata[[0,3,5,8]]
langdata.columns = ["statecode","TRU","People2","People3"]

index = censusdata[censusdata["TRU"]=="Total"].index
censusdata.drop(index,inplace = True)
censusdata = censusdata[(censusdata["Level"]=="STATE")|(censusdata["Level"]=="India")]
censusdata = censusdata[["State","TRU","TOT_P"]]

loc_list = list(set(langdata["statecode"]))

out = []
for code in loc_list:
    temp_pop_r = censusdata[(censusdata["State"]==code) &(censusdata["TRU"]=="Rural")]
    temp_lang_r = langdata[(langdata["statecode"]==code) &(langdata["TRU"]=="Rural")]
    temp_pop_u = censusdata[(censusdata["State"]==code) &(censusdata["TRU"]=="Urban")]
    temp_lang_u = langdata[(langdata["statecode"]==code) &(langdata["TRU"]=="Urban")]
    
    
    rural1 = temp_pop_r.iloc[0,2]-temp_lang_r.iloc[0,2]
    rural2 = temp_lang_r.iloc[0,2]-temp_lang_r.iloc[0,3]
    rural3 = temp_lang_r.iloc[0,3]
    
    urban1 = temp_pop_u.iloc[0,2]-temp_lang_u.iloc[0,2]
    urban2 = temp_lang_u.iloc[0,2]-temp_lang_u.iloc[0,3]
    urban3 = temp_lang_u.iloc[0,3]
    
    urban_total = temp_pop_u.iloc[0,2]
    rural_total = temp_pop_r.iloc[0,2]
    
    ratio = [urban1/rural1,urban2/rural2,urban3/rural3]
    urbanrural = urban_total/rural_total
    
    _,p_value = stats.ttest_ind(a = ratio,b = [urbanrural,urbanrural,urbanrural],equal_var = False)
    
    if code<10:
        code = "0"+str(code)
    else:
        code = str(code)
    
    out.append([code,(urban1/urban_total)*100,(urban2/urban_total)*100,(urban3/urban_total)*100,\
                (rural1/rural_total)*100,(rural2/rural_total)*100,(rural3/rural_total)*100,p_value])

dic1 = {"state-code":[row[0] for row in out],"urban-percentage":[row[1] for row in out],"rural-percentage":[row[4] for row in out],"p-value":[row[7] for row in out]}

dic2 = {"state-code":[row[0] for row in out],"urban-percentage":[row[2] for row in out],"rural-percentage":[row[5] for row in out],"p-value":[row[7] for row in out]}

dic3 = {"state-code":[row[0] for row in out],"urban-percentage":[row[3] for row in out],"rural-percentage":[row[6] for row in out],"p-value":[row[7] for row in out]}

df = pd.DataFrame(dic1)
df.to_csv('geography-india-a.csv', index=False)

df = pd.DataFrame(dic2)
df.to_csv('geography-india-b.csv', index=False)

df = pd.DataFrame(dic3)
df.to_csv('geography-india-c.csv', index=False)