import pandas as pd 
import numpy as np
import os

def add_df(f1,f2):
    f2.columns = ["language","People_count"]
    return f1.append(f2)

Parts_Of_India = ['North','West','Central','East','South','North-East']
out = []
for part in Parts_Of_India:
    state_csv_list = os.listdir("Question7data/"+part)
    Main = pd.DataFrame(columns = ["language","People_count"])
    
    for state in state_csv_list:
        df = pd.read_excel("Question7data/"+part+"/"+state,skiprows = 4)
        df = df.rename(columns = {"4":"language_1","5":"People_count1","9":"language_2","10":"People_count2","14":"language_3","15":"People_count3"})
        df = df.drop(0)
        
        lang1 = df[["language_1","People_count1"]].dropna()
        lang2 = df[["language_2","People_count2"]].dropna()
        lang3 = df[["language_3","People_count3"]].dropna()
        
        Main = add_df(Main,lang1)
        Main = add_df(Main,lang2)
        Main = add_df(Main,lang3)
        
    Main = Main.groupby("language",as_index = False).sum()
    Main = Main.sort_values(by = "People_count",ascending = False)
    
    top_lang = list(Main["language"].iloc[0:3])
    out.append([part]+top_lang)

Parts_Of_India = ['North','West','Central','East','South','North-East']
out1 = []
for part in Parts_Of_India:
    state_csv_list = os.listdir("Question7data/"+part)
    Main = pd.DataFrame(columns = ["language","People_count"])
    
    for state in state_csv_list:
        df = pd.read_excel("Question7data/"+part+"/"+state,skiprows = 4)
        df = df.rename(columns = {"4":"language_1","5":"People_count1","9":"language_2","10":"People_count2","14":"language_3","15":"People_count3"})
        df = df.drop(0)
        
        lang1 = df[["language_1","People_count1"]].dropna()
#         lang2 = df[["language_2","People_count2"]].dropna()
#         lang3 = df[["language_3","People_count3"]].dropna()
        
        Main = add_df(Main,lang1)
#         Main = add_df(Main,lang2)
#         Main = add_df(Main,lang3)
        
    Main = Main.groupby("language",as_index = False).sum()
    Main = Main.sort_values(by = "People_count",ascending = False)
    
    top_lang = list(Main["language"].iloc[0:3])
    out1.append([part]+top_lang)


df = pd.DataFrame(out1,columns = ["region","language-1","language-2","language-3"])
df.to_csv('region-india-a.csv', index=False)
df = pd.DataFrame(out,columns = ["region","language-1","language-2","language-3"])
df.to_csv('region-india-b.csv', index=False)

