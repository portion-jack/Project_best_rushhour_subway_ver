import json
import pandas as pd

def set_time(df):
    df['time'] = df['hh']+df['mm']
    df['time']=pd.to_datetime(df['time'],format='%H%M')
    return df

# 1_json2df
def data_1_json2df(sc,dow,hh):
    with open(f'raw_data/01_{sc}_{dow}_{hh}.json','r') as infile:
        data_1=json.load(infile)

    for _ in range(len(data_1['contents']['stat'])):
        [i.update({'updn':data_1['contents']['stat'][_]['updnLine']}) for i in data_1['contents']['stat'][_]['data']]
        [i.update({'rapid':data_1['contents']['stat'][_]['directAt']}) for i in data_1['contents']['stat'][_]['data']]
    df_data_1=pd.DataFrame(sum([data_1['contents']['stat'][i]['data'] for i in range(len(data_1['contents']['stat']))],[]))

    df_data_1['station_line'] = data_1['contents']['subwayLine']
    df_data_1['station_name'] = data_1['contents']['stationName']
    df_data_1['station_code'] = data_1['contents']['stationCode']
    df_data_1['start_day'] = data_1['contents']['statStartDate']
    df_data_1['end_day'] = data_1['contents']['statEndDate']
    df_data_1['congestionTrain']=df_data_1['congestionTrain'].apply(lambda x: x if x!=0 else None)
    df_data_1.dropna(inplace=True)
    df_data_1=set_time(df_data_1)
    return df_data_1

# 2_json2df
def data_2_json2df(sc,dow,hh):
    with open(f'raw_data/02_{sc}_{dow}_{hh}.json','r') as infile:
        data_2=json.load(infile)

    for _ in range(len(data_2['contents']['stat'])):
        [i.update({'updn':data_2['contents']['stat'][_]['updnLine']}) for i in data_2['contents']['stat'][_]['data']]
        [i.update({'rapid':data_2['contents']['stat'][_]['directAt']}) for i in data_2['contents']['stat'][_]['data']]

    df_data_2=pd.DataFrame(sum([data_2['contents']['stat'][i]['data'] for i in range(len(data_2['contents']['stat']))],[]))

    df_data_2['station_line'] = data_2['contents']['subwayLine']
    df_data_2['station_name'] = data_2['contents']['stationName']
    df_data_2['station_code'] = data_2['contents']['stationCode']
    df_data_2['start_day'] = data_2['contents']['statStartDate']
    df_data_2['end_day'] = data_2['contents']['statEndDate']
    for i in range(len(df_data_2['congestionCar'][0])):
        df_data_2[f'혼잡도_{i+1}번칸'] = df_data_2['congestionCar'].apply(lambda x : x[i])
    df_data_2['congestionCar']=df_data_2['congestionCar'].apply(lambda x: sum(x) if sum(x) !=0 else None)
    df_data_2.dropna(inplace=True)
    df_data_2=set_time(df_data_2)
    return df_data_2

# 3_json2df
def data_3_json2df(sc,dow,hh):
    with open(f'raw_data/03_{sc}_{dow}_{hh}.json','r') as infile:
        data_3=json.load(infile)

    for _ in range(len(data_3['contents']['stat'])):
        [i.update({'updn':data_3['contents']['stat'][_]['updnLine']}) for i in data_3['contents']['stat'][_]['data']]
        [i.update({'rapid':data_3['contents']['stat'][_]['directAt']}) for i in data_3['contents']['stat'][_]['data']]
    df_data_3=pd.DataFrame(sum([data_3['contents']['stat'][i]['data'] for i in range(len(data_3['contents']['stat']))],[]))

    df_data_3['station_line'] = data_3['contents']['subwayLine']
    df_data_3['station_name'] = data_3['contents']['stationName']
    df_data_3['station_code'] = data_3['contents']['stationCode']
    df_data_3['start_day'] = data_3['contents']['statStartDate']
    df_data_3['end_day'] = data_3['contents']['statEndDate']
    for i in range(len(df_data_3['getOffCarRate'][0])):
        df_data_3[f'하차수_{i+1}번칸'] = df_data_3['getOffCarRate'].apply(lambda x : x[i])
    df_data_3['getOffCarRate']=df_data_3['getOffCarRate'].apply(lambda x: sum(x) if sum(x) !=0 else None)
    df_data_3.dropna(inplace=True)
    df_data_3=set_time(df_data_3)
    return df_data_3
