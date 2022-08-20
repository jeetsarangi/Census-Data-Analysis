import pandas as pd
POP_data = pd.read_excel("DDW-0000C-14.xls",skiprows = 7,header = None)
langdata = pd.read_excel("DDW-C18-0000.xlsx",skiprows = 6,header = None)

POP_data = POP_data[[1,3,4,6,7]]
POP_data.columns = ["Statecode","State","age-group","Males","Females"]

langdata = langdata[[0,2,4,6,7,9,10]]
langdata.columns = ['State-code','State-name','age-group','Males2','Female2','Males3','Female3']

agegroups = {'5-9':['5-9'],'10-14':['10-14'],'15-19':['15-19'],'20-24':['20-24'],'25-29':['25-29'],'30-49':['30-34','35-39','40-44','45-49'],\
             '50-69':['50-54','55-59','60-64','65-69'],'70+':['70-74','75-79','80+']}

loc_list = list(set(langdata["State-code"]))

out = []
for code in loc_list:
    temp_lang = langdata[langdata["State-code"]==code]
    temp_pop = POP_data[(POP_data["Statecode"]==code)]
    
    best_group_male = ""
    best_group_female = ""
    
    best_ratio_male = 0
    best_ratio_female = 0
    
    for group in agegroups:
        males_speaking = temp_lang[temp_lang["age-group"]==group].iloc[0,5]
        females_speaking = temp_lang[temp_lang["age-group"]==group].iloc[0,6]
        
        total_males = 0
        total_females = 0
        
        for i in agegroups[group]:
            total_males += temp_pop[temp_pop["age-group"]==i].iloc[0,3]
            total_females += temp_pop[temp_pop["age-group"]==i].iloc[0,4]
            
        male_ratio = males_speaking/total_males
        female_ratio = females_speaking/total_females
        
        if best_ratio_male < male_ratio:
            best_ratio_male = male_ratio
            best_group_male = group
            
        if best_ratio_female < female_ratio:
            best_ratio_female = female_ratio
            best_group_female = group
            
    if code<10:
        code = "0"+str(code)
    else:
        code = str(code)
            
    out.append([code,best_group_male,best_ratio_male,best_group_female,best_ratio_female])


out1 = []
for code in loc_list:
    temp_lang = langdata[langdata["State-code"]==code]
    temp_pop = POP_data[(POP_data["Statecode"]==code)]
    
    best_group_male = ""
    best_group_female = ""
    
    best_ratio_male = 0
    best_ratio_female = 0
    
    for group in agegroups:
        males_speaking = temp_lang[temp_lang["age-group"]==group].iloc[0,3]-temp_lang[temp_lang["age-group"]==group].iloc[0,5]
        females_speaking = temp_lang[temp_lang["age-group"]==group].iloc[0,4]-temp_lang[temp_lang["age-group"]==group].iloc[0,6]
        
        total_males = 0
        total_females = 0
        
        for i in agegroups[group]:
            total_males += temp_pop[temp_pop["age-group"]==i].iloc[0,3]
            total_females += temp_pop[temp_pop["age-group"]==i].iloc[0,4]
            
        male_ratio = males_speaking/total_males
        female_ratio = females_speaking/total_females
        
        if best_ratio_male < male_ratio:
            best_ratio_male = male_ratio
            best_group_male = group
            
        if best_ratio_female < female_ratio:
            best_ratio_female = female_ratio
            best_group_female = group
            
    if code<10:
        code = "0"+str(code)
    else:
        code = str(code)
    out1.append([code,best_group_male,best_ratio_male,best_group_female,best_ratio_female])

out2 = []
for code in loc_list:
    temp_lang = langdata[langdata["State-code"]==code]
    temp_pop = POP_data[(POP_data["Statecode"]==code)]
    
    best_group_male = ""
    best_group_female = ""
    
    best_ratio_male = 0
    best_ratio_female = 0
    
    for group in agegroups:
#         males_speaking = temp_lang[temp_lang["age-group"]==group].iloc[0,3]-temp_lang[temp_lang["age-group"]==group].iloc[0,5]
#         females_speaking = temp_lang[temp_lang["age-group"]==group].iloc[0,4]-temp_lang[temp_lang["age-group"]==group].iloc[0,6]
        
        total_males = 0
        total_females = 0
        
        for i in agegroups[group]:
            total_males += temp_pop[temp_pop["age-group"]==i].iloc[0,3]
            total_females += temp_pop[temp_pop["age-group"]==i].iloc[0,4]
            
        males_speaking = total_males - temp_lang[temp_lang["age-group"]==group].iloc[0,3]
        females_speaking = total_females - temp_lang[temp_lang["age-group"]==group].iloc[0,4]
            
        male_ratio = males_speaking/total_males
        female_ratio = females_speaking/total_females
        
        if best_ratio_male < male_ratio:
            best_ratio_male = male_ratio
            best_group_male = group
            
        if best_ratio_female < female_ratio:
            best_ratio_female = female_ratio
            best_group_female = group
            
    if code<10:
        code = "0"+str(code)
    else:
        code = str(code)
    
    out2.append([code,best_group_male,best_ratio_male,best_group_female,best_ratio_female])


df = pd.DataFrame(out,columns = ["state/ut","age-group-males","ratio-males","age-group-females","ratio-females"])
df.to_csv('age-gender-a.csv', index=False)
df = pd.DataFrame(out1,columns = ["state/ut","age-group-males","ratio-males","age-group-females","ratio-females"])
df.to_csv('age-gender-b.csv', index=False)
df = pd.DataFrame(out2,columns = ["state/ut","age-group-males","ratio-males","age-group-females","ratio-females"])
df.to_csv('age-gender-c.csv', index=False)

