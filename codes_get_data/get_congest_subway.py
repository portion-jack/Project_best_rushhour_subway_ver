import pandas as pd
import requests
from private._private_ import app_key


namer=pd.read_csv('data/StationCode_mapper.csv',index_col=0)

"""
서울 3대 업무지구인 CBD(종로구·중구 일대), GBD(강남구·서초구 일대), YBD(영등포구 일대)를 비롯해 
서울디지털국가산업단지,마곡&염창지구 등 대규모 업무지구 및 산업단지를 빠르게 이동할 수 있는 지역에 
주거지가 위치하면 출퇴근 시 느끼는 대중교통 혼잡이나 장거리 이동에 대한 부담으로부터 자유로울 수 있다.

출처 : 국토일보(http://www.ikld.kr)
"""

"""
target_1 = ['강남역','역삼역','선릉역']
target_2 = ['시청역','을지로3가역','종각역']
target_3 = ['구로디지털단지역','영등포역','신도림역']
target_4 = ['공덕역']
"""
for sc in [529,626]:

    results = list()
    hours = [7,8,9,17,18,19,20]
    dows = ['MON', 'TUE', 'WED', 'THU', 'FRI']


    cur_name=namer[namer['stationCode']==str(sc)]['stationName'].values[0]
    cur_line=namer[namer['stationCode']==str(sc)]['subwayLine'].values[0]


    # get data 1

    for hour in hours:
        for dow in dows:
            url = f"https://apis.openapi.sk.com/puzzle/congestion-train/stat/stations/{sc}?dow={dow}&hh={str(hour).zfill(2)}"
            headers = {
                "accept": "application/json",
                "appkey": app_key()
            }

            response = requests.get(url, headers=headers)

            res_dict=eval(response.text)
            using_data = list()
            for trains in res_dict['contents']['stat']:
                count = 0
                for train in trains['data']:
                    if train['congestionTrain'] == 0:
                        count += 1
                if count == 0:
                    using_data.append(trains)
                    
            df_main = pd.DataFrame(using_data)
            df_main['subwayLine'] =res_dict['contents']['subwayLine']
            df_main['stationName'] =res_dict['contents']['stationName']
            results.append(df_main)
    df_1=pd.concat(results)

    # get data 2

    results = list()
    for hour in hours:
        for dow in dows:
            url = f"https://apis.openapi.sk.com/puzzle/congestion-car/stat/stations/{sc}?dow={dow}&hh={str(hour).zfill(2)}"
            headers = {
                "accept": "application/json",
                "appkey": app_key()
            }
            response = requests.get(url, headers=headers)
            res_dict=eval(response.text)
            using_data = list()
            for trains in res_dict['contents']['stat']:
                count = 0
                for train in trains['data']:
                    for _ in train['congestionCar']:
                        if _ == 0 :
                            count += 1
                    if count == 0:
                        using_data.append(trains)

            df_main = pd.DataFrame(using_data)
            df_main['subwayLine'] =res_dict['contents']['subwayLine']
            df_main['stationName'] =res_dict['contents']['stationName']
            results.append(df_main)
    df_2=pd.concat(results)

    ## preprocessing_Data_1

    df_1['time'] = df_1['data'].apply(lambda x: f"{x[0]['dow']}_{x[0]['hh']}")
    total_df = list()
    for line in [0,1]:
        for date in df_1['time'].unique():
            cc_df=df_1[(df_1['updnLine']==line) & (df_1['time']==date)]
            tmp_list = list()
            for i in range(len(cc_df)):
                tmp_df=pd.DataFrame(cc_df['data'].reset_index(drop=True)[i])
                tmp_df['up_down'] = line
                tmp_list.append(tmp_df)
            total_df.append(pd.concat(tmp_list))    
    df_1_cleaned=pd.concat(total_df)
    df_1_cleaned['subwayLine'] = cur_line
    df_1_cleaned['stationName'] = cur_name
    df_1_cleaned.reset_index(drop=True,inplace=True)

    cur_name=namer[namer['stationCode']==str(sc)]['stationName'].values[0]

    df_1_cleaned.to_csv(f'data/final_data/{cur_name}_{cur_line}_congest.csv')

    ## preprocessing_Data_2

    df_2['time']=df_2['data'].apply(lambda x: f"{x[0]['dow']}_{x[0]['hh']}")
    total_df = list()
    for line in [0,1]:
        for date in df_2['time'].unique():
            cc_df=df_2[(df_2['updnLine']==line) & (df_2['time']==date)]
            tmp_list = list()
            for i in range(len(cc_df)):
                tmp_df=pd.DataFrame(cc_df['data'].reset_index(drop=True)[i])
                tmp_df['up_down'] = line
                tmp_list.append(tmp_df)
            total_df.append(pd.concat(tmp_list))    
    df_2_cleaned=pd.concat(total_df)

    df_2_cleaned.reset_index(drop=True,inplace=True)
    for i in range(len(df_2_cleaned['congestionCar'][0])):
        df_2_cleaned[f'congestion_{i}']=df_2_cleaned['congestionCar'].apply(lambda x: x[i])
        
    df_1_cleaned['subwayLine'] = cur_line
    df_1_cleaned['stationName'] = cur_name

    df_2_cleaned.to_csv(f'data/final_data/{cur_name}_{cur_line}congest_section.csv')
