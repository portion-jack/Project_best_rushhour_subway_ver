import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["date.autoformatter.minute"] = "%H:%M"
plt.rcParams['font.family']='AppleGothic'


def read_congest_section(subwayline):
    congest_path=glob.glob(f'data/final_data/*{subwayline}congest_section.csv')

    tmp_li = list()
    for congest in congest_path:
        tmp_li.append(pd.read_csv(congest,index_col=0))
    df_congest = pd.concat(tmp_li)

    df_congest['time']=df_congest['hh'].apply(lambda x: str(x).zfill(2)) + df_congest['mm'].apply(lambda x: str(x).zfill(2))
    df_congest['time']=pd.to_datetime(df_congest['time'],format='%H%M')
    return df_congest

def read_congest():
    congest_path=glob.glob('data/final_data/*congest.csv')

    tmp_li = list()
    for congest in congest_path:
        tmp_li.append(pd.read_csv(congest,index_col=0))
    df_congest = pd.concat(tmp_li)

    df_congest['time']=df_congest['hh'].apply(lambda x: str(x).zfill(2)) + df_congest['mm'].apply(lambda x: str(x).zfill(2))
    df_congest['time']=pd.to_datetime(df_congest['time'],format='%H%M')
    return df_congest
