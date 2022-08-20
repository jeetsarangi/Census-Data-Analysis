import pandas as pd
import numpy as np

censusdata  = pd.read_excel('DDW-0000C-08.xlsx',header = None,skiprows = 5)
c19 = pd.read_excel('DDW-C19-0000.xlsx',skiprows = 4)
c19 = c19[c19['4']=="Total"]
c19 = c19[["1","3","5","9"]]

censusdata = censusdata[(censusdata[5]=="All ages") & (censusdata[4]=="Total")]
censusdata
censusdata[censusdata[1]==int("00")]

loc_list = list(set(c19["1"]))

literacygroup = {'Illiterate':[9],'Literate but below primary':[18],'Primary but below middle':[21],'Middle but below matric/secondary':[24]\
                 ,'Matric/Secondary but below graduate':[27,30,33,36],'Graduate and above':[39]}


out = []
for code in loc_list:
    state = c19[c19["1"]==code]
    cens = censusdata[censusdata[1]==int(code)]
    max_percent = 0
    bestgrp = ""
    for key in literacygroup:
        speaking = state[state["5"]==key].iloc[0,3]
        total = 0
        for i in literacygroup[key]:
            total += cens.iloc[0,i]
        curr_percentage = (speaking/total)*100
        if curr_percentage > max_percent:
            max_percent = curr_percentage
            bestgrp = key
    out.append((code,state.iloc[0,1],bestgrp,max_percent))
            
        
out.sort()

dic = {"State-Code":[row[0] for row in out],"state/ut":[row[1] for row in out],"literacy-group":[row[2] for row in out],"percentage":[row[3] for row in out]}
df = pd.DataFrame(dic)
df.to_csv('literacy-india.csv', index=False)


