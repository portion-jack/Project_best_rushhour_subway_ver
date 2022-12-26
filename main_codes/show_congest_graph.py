import glob
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["date.autoformatter.minute"] = "%H:%M"
plt.rcParams['font.family']='AppleGothic'

congest_path=glob.glob('data/final_data/*congest.csv')

tmp_li = list()
for congest in congest_path:
    tmp_li.append(pd.read_csv(congest,index_col=0))

df_congest = pd.concat(tmp_li)

def relative_graph_morning(df_congest,target_name,target_line):
    df_congest['time']=df_congest['hh'].apply(lambda x: str(x).zfill(2)) + df_congest['mm'].apply(lambda x: str(x).zfill(2))
    df_congest['time']=pd.to_datetime(df_congest['time'],format='%H%M')

    df_morning_target=pd.DataFrame(df_congest[(df_congest['stationName']==target_name) & \
                                          (df_congest['subwayLine']==target_line)].groupby(['time','up_down'])['congestionTrain'].mean()).reset_index()
    df_morning_main = pd.DataFrame(df_congest.groupby(['time','up_down'])['congestionTrain'].mean()).reset_index()

    # 혼잡도 평균 그래프
    plt.figure(figsize=(13,8))
    sns.lineplot(
        data=df_morning_main[(df_morning_main['time'].apply(lambda x: x.hour) <= 9) &\
                            (df_morning_main['up_down']==0)],
        x='time',
        y='congestionTrain',
        lw=4,
        alpha=0.5,
        c='k',
        label='출근시간 평균 혼잡도'
    )
    sns.scatterplot(
        data=df_morning_main[(df_morning_main['time'].apply(lambda x: x.hour) <= 9) &\
                            (df_morning_main['up_down']==0)],
        x='time',
        y='congestionTrain',
        s=150,
        alpha=0.5,
        c='k',
    )

    # 혼잡도 타겟 그래프
    sns.lineplot(
        data=df_morning_target[(df_morning_target['time'].apply(lambda x: x.hour) <= 9) &\
                            (df_morning_target['up_down']==0)],
        x='time',
        y='congestionTrain',
        lw=4,
        alpha=0.5,
        c='r',
        label=f'출근시간 {target_name}_{target_line} 혼잡도'
    )
    sns.scatterplot(
        data=df_morning_target[(df_morning_target['time'].apply(lambda x: x.hour) <= 9) &\
                            (df_morning_target['up_down']==0)],
        x='time',
        y='congestionTrain',
        s=150,
        alpha=0.5,
        c='r',
    )
    plt.title(f'출근시간 {target_name}_{target_line} 혼잡도',fontsize=15)
    plt.legend(fontsize=15)
    plt.show()



def relative_graph_dinner(df_congest,target_name,target_line):
    df_congest['time']=df_congest['hh'].apply(lambda x: str(x).zfill(2)) + df_congest['mm'].apply(lambda x: str(x).zfill(2))
    df_congest['time']=pd.to_datetime(df_congest['time'],format='%H%M')

    df_morning_target=pd.DataFrame(df_congest[(df_congest['stationName']==target_name) & \
                                          (df_congest['subwayLine']==target_line)].groupby(['time','up_down'])['congestionTrain'].mean()).reset_index()
    df_morning_main = pd.DataFrame(df_congest.groupby(['time','up_down'])['congestionTrain'].mean()).reset_index()

    # 혼잡도 평균 그래프
    plt.figure(figsize=(13,8))
    sns.lineplot(
        data=df_morning_main[(df_morning_main['time'].apply(lambda x: x.hour) > 9) &\
                            (df_morning_main['up_down']==0)],
        x='time',
        y='congestionTrain',
        lw=4,
        alpha=0.5,
        c='k',
        label='퇴근시간 평균 혼잡도'
    )
    sns.scatterplot(
        data=df_morning_main[(df_morning_main['time'].apply(lambda x: x.hour) > 9) &\
                            (df_morning_main['up_down']==0)],
        x='time',
        y='congestionTrain',
        s=150,
        alpha=0.5,
        c='k',
    )

    # 혼잡도 타겟 그래프
    sns.lineplot(
        data=df_morning_target[(df_morning_target['time'].apply(lambda x: x.hour) > 9) &\
                            (df_morning_target['up_down']==0)],
        x='time',
        y='congestionTrain',
        lw=4,
        alpha=0.5,
        c='r',
        label=f'퇴근시간 {target_name}_{target_line} 혼잡도'
    )
    sns.scatterplot(
        data=df_morning_target[(df_morning_target['time'].apply(lambda x: x.hour) > 9) &\
                            (df_morning_target['up_down']==0)],
        x='time',
        y='congestionTrain',
        s=150,
        alpha=0.5,
        c='r',
    )
    plt.title(f'퇴근시간 {target_name}_{target_line} 혼잡도',fontsize=15)
    plt.legend(fontsize=15)
    plt.show()

