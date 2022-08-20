import pandas as pd
from scipy import stats

langdata = pd.read_excel("DDW-C18-0000.xlsx",skiprows = 6,header = None)
censusdata = pd.read_excel("DDW_PCA0000_2011_Indiastatedist.xlsx")

langdata = langdata[(langdata[3]=="Total")&(langdata[4]=="Total")].reset_index()
langdata = langdata[[0,6,7,9,10]]
langdata.columns = ["statecode","males2","females2","males3","females3"]


censusdata = censusdata[(censusdata["TRU"]=="Total") & ((censusdata["Level"]=="STATE")|(censusdata["Level"]=="India"))]
censusdata = censusdata[["State","TOT_M","TOT_F"]]

loc_list = list(langdata["statecode"])


out = []
for code in loc_list:
    temp_pop = censusdata[censusdata["State"]==code]
    temp_lang = langdata[langdata["statecode"]==code]
    
    malesspeaking1 = temp_pop.iloc[0,1]-temp_lang.iloc[0,1]
    malesspeaking2 = temp_lang.iloc[0,1]-temp_lang.iloc[0,3]
    malesspeaking3 = temp_lang.iloc[0,3]
    
    femalesspeaking1 = temp_pop.iloc[0,2]-temp_lang.iloc[0,2]
    femalesspeaking2 = temp_lang.iloc[0,2]-temp_lang.iloc[0,4]
    femalesspeaking3 = temp_lang.iloc[0,4]
    
    totalmales = temp_pop.iloc[0,1]
    totalfemales = temp_pop.iloc[0,2]
    
    ratio = [malesspeaking1/femalesspeaking1,malesspeaking2/femalesspeaking2,malesspeaking3/femalesspeaking3]
    malefemale = totalmales/totalfemales
    
    _,p_value = stats.ttest_ind(a = ratio,b = [malefemale,malefemale,malefemale],equal_var = False)
    
    if code<10:
        code = "0"+str(code)
    else:
        code = str(code)
    out.append([code,(malesspeaking1/totalmales)*100,(malesspeaking2/totalmales)*100,(malesspeaking3/totalmales)*100,\
                (femalesspeaking1/totalfemales)*100,(femalesspeaking2/totalfemales)*100,(femalesspeaking3/totalfemales)*100,\
                p_value])


dic1 = {"state-code":[row[0] for row in out],"male-percentage":[row[1] for row in out],"female-percentage":[row[4] for row in out],"p-value":[row[7] for row in out]}

dic2 = {"state-code":[row[0] for row in out],"male-percentage":[row[2] for row in out],"female-percentage":[row[5] for row in out],"p-value":[row[7] for row in out]}

dic3 = {"state-code":[row[0] for row in out],"male-percentage":[row[3] for row in out],"female-percentage":[row[6] for row in out],"p-value":[row[7] for row in out]}

df = pd.DataFrame(dic1)
df.to_csv('gender-india-a.csv', index=False)

df = pd.DataFrame(dic2)
df.to_csv('gender-india-b.csv', index=False)

df = pd.DataFrame(dic3)
df.to_csv('gender-india-c.csv', index=False)

