import pandas as pd

df_1=pd.read_csv('data/cleaned_공덕_6호선_station_congest.csv',index_col=0)
df_1['data']=df_1['data'].apply(lambda x: eval(x))

df_2=pd.read_csv('data/cleaned_공덕_6호선_station_congest_sectional.csv',index_col=0)
df_2['data']=df_2['data'].apply(lambda x: eval(x))
total_df = list()
for line in [0,1]:
    for date in df_1['time'].unique():
        cc_df=df_1[(df_1['updnLine']==line) & (df_1['time']==date)]
        tmp_list = list()
        for i in range(len(cc_df)):
            tmp_list.append(pd.DataFrame(cc_df['data'].reset_index(drop=True)[i]))
        total_df.append(pd.concat(tmp_list))    
df_1_cleaned=pd.concat(total_df)
df_1_cleaned.reset_index(drop=True,inplace=True)
df_2['time']=df_2['data'].apply(lambda x: f"{x[0]['dow']}_{x[0]['hh']}")
total_df = list()
for line in [0,1]:
    for date in df_2['time'].unique():
        cc_df=df_2[(df_2['updnLine']==line) & (df_2['time']==date)]
        tmp_list = list()
        for i in range(len(cc_df)):
            tmp_list.append(pd.DataFrame(cc_df['data'].reset_index(drop=True)[i]))
        total_df.append(pd.concat(tmp_list))    
df_2_cleaned=pd.concat(total_df)

df_2_cleaned.reset_index(drop=True,inplace=True)
for i in range(len(df_2_cleaned['congestionCar'][0])):
    df_2_cleaned[f'congestion_{i}']=df_2_cleaned['congestionCar'].apply(lambda x: x[i])
