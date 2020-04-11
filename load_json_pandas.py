import json as js
from urllib.request import urlopen
import pandas as pd

# 1 read a json file with js.loads(json_url.read()) or the way you want
# 2 view the levels from a file, to see levels json_file.keys()
# 3 Call the function df_name = load_json_df(level='level',load_file_json=json_file) 
def load_json_df(level,load_file_json):
    col = []
    for key in load_file_json[level][0].keys():
        col.append(key)
        
    df_saida = []    
    i = 0
    while i <= len(load_file_json[level])-1:
        v = list((load_file_json[level][i].values()))
        df_saida.append(v)
        i += 1
    df_saida = pd.DataFrame(df_saida) 
    df_saida = df_saida.set_axis(col, axis=1, inplace=False)
    return(df_saida)
