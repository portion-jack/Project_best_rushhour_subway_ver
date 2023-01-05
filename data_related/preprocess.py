import json
import pandas as pd

def json2df(json_path):
    with open(f'{json_path}','r') as f:
        tmp=json.load(f)
        
    tmp_df_1=pd.DataFrame(tmp['contents']).drop(columns={'stat'})
    tmp_df_2=pd.DataFrame(tmp['contents']['stat'])
    tmp_df=pd.concat([tmp_df_1,tmp_df_2],axis=1)
    tmp_df=tmp_df.explode('data')
    _df_=pd.concat([tmp_df.drop(columns=['data']),tmp_df['data'].apply(pd.Series)],axis=1)
    return _df_

def json2df_congest(st_code,dow,hh):
    with open(f'raw_data/01_{st_code}_{dow}_{hh}.json','r') as f:
        tmp=json.load(f)
        
    tmp_df_1=pd.DataFrame(tmp['contents']).drop(columns={'stat'})
    tmp_df_2=pd.DataFrame(tmp['contents']['stat'])
    tmp_df=pd.concat([tmp_df_1,tmp_df_2],axis=1)
    tmp_df=tmp_df.explode('data')
    _df_=pd.concat([tmp_df.drop(columns=['data']),tmp_df['data'].apply(pd.Series)],axis=1)
    return _df_

def json2df_congest_sectional(st_code,dow,hh):
    with open(f'raw_data/02_{st_code}_{dow}_{hh}.json','r') as f:
        tmp=json.load(f)
        
    tmp_df_1=pd.DataFrame(tmp['contents']).drop(columns={'stat'})
    tmp_df_2=pd.DataFrame(tmp['contents']['stat'])
    tmp_df=pd.concat([tmp_df_1,tmp_df_2],axis=1)
    tmp_df=tmp_df.explode('data')
    _df_=pd.concat([tmp_df.drop(columns=['data']),tmp_df['data'].apply(pd.Series)],axis=1)
    return _df_


def json2df_dropoff(st_code,dow,hh):
    with open(f'raw_data/03_{st_code}_{dow}_{hh}.json','r') as f:
        tmp=json.load(f)
        
    tmp_df_1=pd.DataFrame(tmp['contents']).drop(columns={'stat'})
    tmp_df_2=pd.DataFrame(tmp['contents']['stat'])
    tmp_df=pd.concat([tmp_df_1,tmp_df_2],axis=1)
    tmp_df=tmp_df.explode('data')
    _df_=pd.concat([tmp_df.drop(columns=['data']),tmp_df['data'].apply(pd.Series)],axis=1)
    return _df_