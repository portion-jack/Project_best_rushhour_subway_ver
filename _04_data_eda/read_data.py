# imports
import json
import pandas as pd
import seaborn as sns
from glob import glob

from _01_get_api.get_api_save_json import get_data_1, get_data_2, get_data_3
from _02_preprocessing.preprocessing import data_1_json2df, data_2_json2df, data_3_json2df
from _03_data_pipeline.data_pipeline import check_data, get_data

def read_data(station_line):
    paths=glob(f'preprocessed_data/01*[{station_line}]*.csv')
    result_li = list()
    for path in paths:
        result_li.append(pd.read_csv(path,index_col=0))
    df_1=pd.concat(result_li)
    df_1['time_line'] = df_1['hh'].apply(lambda x: str(x).zfill(2) + ":") + df_1['mm'].apply(lambda x: str(x).zfill(2))
    df_1['weekday']=df_1['dow'].apply(lambda x: 'weekend' if x in ['SAT','SUN'] else 'weekday')

    paths=glob(f'preprocessed_data/02*[{station_line}]*.csv')
    result_li = list()
    for path in paths:
        result_li.append(pd.read_csv(path,index_col=0))
    df_2=pd.concat(result_li)
    df_2['time_line'] = df_2['hh'].apply(lambda x: str(x).zfill(2) + ":") + df_2['mm'].apply(lambda x: str(x).zfill(2))
    df_2['weekday']=df_2['dow'].apply(lambda x: 'weekend' if x in ['SAT','SUN'] else 'weekday')

    paths=glob(f'preprocessed_data/03*[{station_line}]*.csv')
    result_li = list()
    for path in paths:
        result_li.append(pd.read_csv(path,index_col=0))
    df_3=pd.concat(result_li)
    df_3['time_line'] = df_3['hh'].apply(lambda x: str(x).zfill(2) + ":") + df_3['mm'].apply(lambda x: str(x).zfill(2))
    df_3['weekday']=df_3['dow'].apply(lambda x: 'weekend' if x in ['SAT','SUN'] else 'weekday')
    return df_1, df_2, df_3
