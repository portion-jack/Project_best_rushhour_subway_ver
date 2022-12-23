import pandas as pd

df_1=pd.read_csv('data/공덕_6호선_station_congest.csv',index_col=0)
df_1['data']=df_1['data'].apply(lambda x: eval(x))
df_1.reset_index(drop=True,inplace=True)
results = list()

for tline in df_1['time'].unique():
    my_list = list()
    
    for i in range(len(df_1[df_1['time']==tline])):
        temp=pd.DataFrame(df_1[df_1['time']==tline]['data'].apply(lambda x: eval(x)).reset_index(drop=True)[i])['congestionTrain']
            
        my_list.append(temp)
    df_=pd.concat(my_list,axis=1)
    df_.index = [0,10,20,30,40,50]
    df_.columns = range(len(df_.columns))

    for col in df_.columns:
        df_[col]=df_[col].apply(lambda x: None if x==0 else x)

    df_.dropna(axis=1,inplace=True)
    df_=df_.mean(axis=1).reset_index().rename(columns={'index':'time'})
    df_['time']=df_['time'].apply(lambda x: f"{tline}_{str(x).zfill(2)}")

    results.append(df_)

df_1_main=pd.concat(results)
