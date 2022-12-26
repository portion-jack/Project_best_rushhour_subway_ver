import pandas as pd
import requests
from private._private_ import app_key

namer=pd.read_csv('data/StationCode_mapper.csv',index_col=0)


def get_congest(station_name,station_line):
    """
    stationcode => (station_congest, station congest sectional)
    using 35 api cnts
    """
    station_code = namer[(namer['stationName']==station_name) & (namer['subwayLine']==station_line)]['stationCode'].values[0]
    for sc in [station_code]:
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
            
        df_2_cleaned['subwayLine'] = cur_line
        df_2_cleaned['stationName'] = cur_name

        df_2_cleaned.to_csv(f'data/final_data/{cur_name}_{cur_line}congest_section.csv')
        return df_1_cleaned, df_2_cleaned