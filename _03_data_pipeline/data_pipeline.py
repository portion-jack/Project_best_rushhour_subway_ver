# imports
import json
import pandas as pd
from glob import glob
from _01_get_api.get_api_save_json import get_data_1, get_data_2, get_data_3
from _02_preprocessing.preprocessing import data_1_json2df, data_2_json2df, data_3_json2df
mapper=pd.read_csv('raw_data/StationCode_mapper.csv',index_col=0)


def check_data(stationname,subwayline,dow,hh):
    station_code=mapper[(mapper['subwayLine']==subwayline) & (mapper['stationName']==stationname)]['stationCode'].values[0]

    if len(glob(f'raw_data/*{station_code}_{dow}_{hh}.json'))==0:
        print('--'*30)
        print(f'{stationname} : {dow} : {hh} 아직 존재하지 않는 데이터 입니다.')
        
        
    elif len(glob(f'raw_data/*{station_code}_{dow}_{hh}.json'))==3:
        print('--'*30)
        print(f'{stationname} : {dow} : {hh} 현재 존재하는 데이터입니다.')
        with open(f'raw_data/01_{station_code}_{dow}_{hh}.json','r') as infile:
            data_1=json.load(infile)
        st=data_1['contents']['statStartDate']
        et=data_1['contents']['statEndDate']
        print(f'현재 데이터 시작일 : {st} / 종료일 : {et}')
    return None

def get_data(stationname,subwayline,dow,hh):
    station_code=mapper[(mapper['subwayLine']==subwayline) & (mapper['stationName']==stationname)]['stationCode'].values[0]
    
    get_data_1(station_code,dow,hh)
    get_data_2(station_code,dow,hh)
    get_data_3(station_code,dow,hh)
    
    df_1 = data_1_json2df(station_code,dow,hh)
    df_2 = data_2_json2df(station_code,dow,hh)
    df_3 = data_3_json2df(station_code,dow,hh)

    df_1.to_csv(f'preprocessed_data/01_{dow}_{hh}_{subwayline}_{stationname}.csv')
    df_2.to_csv(f'preprocessed_data/02_{dow}_{hh}_{subwayline}_{stationname}.csv')
    df_3.to_csv(f'preprocessed_data/03_{dow}_{hh}_{subwayline}_{stationname}.csv')
    print('추출 완료')
    return None