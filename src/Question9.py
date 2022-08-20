import pandas as pd
POP_data = pd.read_excel("DDW-0000C-08.xlsx",skiprows = 7,header = None)
langdata = pd.read_excel("DDW-C19-0000.xlsx",skiprows = 6,header = None)

POP_data = POP_data[(POP_data[4]=="Total") & (POP_data[5]=="All ages")]

langdata = langdata[langdata[3]=="Total"]
langdata = langdata[[0,4,6,7,9,10]]
langdata = langdata.dropna()
langdata[0] = langdata[0].astype(int)

loc_list= list(set(langdata[0]))
loc_list.sort()

literacygroup_m = {'Illiterate':[10],'Literate but below primary':[19],'Primary but below middle':[22],'Middle but below matric/secondary':[25]\
                 ,'Matric/Secondary but below graduate':[28,31,34,37],'Graduate and above':[40]}

out = []
for code in loc_list:
    temp_pop = POP_data[POP_data[1]==code]
    temp_lang = langdata[langdata[0]==code]
    
    best_group_male = ""
    best_group_female = ""
    
    max_ratio_male = 0
    max_ratio_female = 0
    
    for group in literacygroup_m:
        
        males_speaking = temp_lang[temp_lang[4]==group].iloc[0,4]
        females_speaking = temp_lang[temp_lang[4]==group].iloc[0,5]
        
        total_males = 0
        total_females = 0
        
        for i in literacygroup_m[group]:
            total_males += temp_pop.iloc[0,i]
            total_females += temp_pop.iloc[0,i+1]
        
        male_ratio = males_speaking/total_males
        female_ratio = females_speaking/total_females
        
        if male_ratio > max_ratio_male:
            max_ratio_male = male_ratio
            best_group_male = group
            
        if female_ratio > max_ratio_female:
            max_ratio_female = female_ratio
            best_group_female = group
            
    if code<10:
        code = "0"+str(code)
    else:
        code = str(code)
    
    out.append([code,best_group_male,max_ratio_male,best_group_female,max_ratio_female])
        
out1 = []
for code in loc_list:
    temp_pop = POP_data[POP_data[1]==code]
    temp_lang = langdata[langdata[0]==code]
    
    best_group_male = ""
    best_group_female = ""
    
    max_ratio_male = 0
    max_ratio_female = 0
    
    for group in literacygroup_m:
        
        males_speaking = temp_lang[temp_lang[4]==group].iloc[0,2]-temp_lang[temp_lang[4]==group].iloc[0,4]
        females_speaking = temp_lang[temp_lang[4]==group].iloc[0,3]-temp_lang[temp_lang[4]==group].iloc[0,5]
        
        total_males = 0
        total_females = 0
        
        for i in literacygroup_m[group]:
            total_males += temp_pop.iloc[0,i]
            total_females += temp_pop.iloc[0,i+1]
        
        male_ratio = males_speaking/total_males
        female_ratio = females_speaking/total_females
        
        if male_ratio > max_ratio_male:
            max_ratio_male = male_ratio
            best_group_male = group
            
        if female_ratio > max_ratio_female:
            max_ratio_female = female_ratio
            best_group_female = group
            
    if code<10:
        code = "0"+str(code)
    else:
        code = str(code)
    
    out1.append([code,best_group_male,max_ratio_male,best_group_female,max_ratio_female])
        
out2 = []
for code in loc_list:
    temp_pop = POP_data[POP_data[1]==code]
    temp_lang = langdata[langdata[0]==code]
    
    best_group_male = ""
    best_group_female = ""
    
    max_ratio_male = 0
    max_ratio_female = 0
    
    for group in literacygroup_m:
        
        total_males = 0
        total_females = 0
        
        for i in literacygroup_m[group]:
            total_males += temp_pop.iloc[0,i]
            total_females += temp_pop.iloc[0,i+1]
            
        males_speaking = total_males - temp_lang[temp_lang[4]==group].iloc[0,2]
        females_speaking = total_females - temp_lang[temp_lang[4]==group].iloc[0,3]  
        
        
        male_ratio = males_speaking/total_males
        female_ratio = females_speaking/total_females
        
        if male_ratio > max_ratio_male:
            max_ratio_male = male_ratio
            best_group_male = group
            
        if female_ratio > max_ratio_female:
            max_ratio_female = female_ratio
            best_group_female = group
            
    if code<10:
        code = "0"+str(code)
    else:
        code = str(code)
    
    out2.append([code,best_group_male,max_ratio_male,best_group_female,max_ratio_female])

df = pd.DataFrame(out,columns = ["state/ut","literacy-group-males","ratio-males","literacy-group-females","ratio-females"])
df.to_csv('literacy-gender-a.csv', index=False)
df = pd.DataFrame(out1,columns = ["state/ut","literacy-group-males","ratio-males","literacy-group-females","ratio-females"])
df.to_csv('literacy-gender-b.csv', index=False)
df = pd.DataFrame(out2,columns = ["state/ut","literacy-group-males","ratio-males","literacy-group-females","ratio-females"])
df.to_csv('literacy-gender-c.csv', index=False)