# imports
import pandas as pd
from glob import glob

def read_data(station_line, station_name):
    paths=glob(f'preprocessed_data/01_???_??_[{station_line}]*{station_name}.csv')
    result_li = list()
    for path in paths:
        result_li.append(pd.read_csv(path,index_col=0))
    df_1=pd.concat(result_li)
    df_1['time_line'] = df_1['hh'].apply(lambda x: str(x).zfill(2) + ":") + df_1['mm'].apply(lambda x: str(x).zfill(2))
    df_1['weekday']=df_1['dow'].apply(lambda x: 'weekend' if x in ['SAT','SUN'] else 'weekday')

    paths=glob(f'preprocessed_data/02_???_??_[{station_line}]*{station_name}.csv')
    result_li = list()
    for path in paths:
        result_li.append(pd.read_csv(path,index_col=0))
    df_2=pd.concat(result_li)
    df_2['time_line'] = df_2['hh'].apply(lambda x: str(x).zfill(2) + ":") + df_2['mm'].apply(lambda x: str(x).zfill(2))
    df_2['weekday']=df_2['dow'].apply(lambda x: 'weekend' if x in ['SAT','SUN'] else 'weekday')

    paths=glob(f'preprocessed_data/03_???_??_[{station_line}]*{station_name}.csv')
    result_li = list()
    for path in paths:
        result_li.append(pd.read_csv(path,index_col=0))
    df_3=pd.concat(result_li)
    df_3['time_line'] = df_3['hh'].apply(lambda x: str(x).zfill(2) + ":") + df_3['mm'].apply(lambda x: str(x).zfill(2))
    df_3['weekday']=df_3['dow'].apply(lambda x: 'weekend' if x in ['SAT','SUN'] else 'weekday')
    return df_1, df_2, df_3

time_line_mapper={
    '출근시간':[i for i in range(6,10)],
    '퇴근시간':[i for i in range(16,20)]
}
def slice_time(df,time_type):
    time_range = time_line_mapper[time_type]
    df_using=df[df['hh'].isin(time_range)]
    return df_using