from main_codes.read_data import read_congest_section
import matplotlib.pyplot as plt
import seaborn as sns

def get_sectional_df_morning(stationname,stationline):
    df_congest_sectional=read_congest_section(stationline)
    df_congest_sectional.columns=df_congest_sectional.columns.str.replace('congestion', '혼잡도')

    df_sectional_target=df_congest_sectional[df_congest_sectional['stationName']==stationname]

    # congest sectional main
    congest_cols = [i for i in df_congest_sectional if i.startswith('혼잡도_')]

    for col in congest_cols:
        df_congest_sectional[col] = df_congest_sectional[col].apply(lambda x: x if x !=0 else None)
    df_congest_sectional.dropna(inplace=True)

    df_sectional_mean=df_congest_sectional.groupby('time')[congest_cols].mean()

    df_sectional_mg=df_sectional_mean[(df_sectional_mean.index.hour.isin([7,8,9]))]
    df_sectional_mg['hour']=df_sectional_mg.index.hour
    df_sectional_mg['minutes']=df_sectional_mg.index.minute
    df_sectional_mg['time_line'] = df_sectional_mg['hour'].apply(lambda x: str(x).zfill(2) + ':') + df_sectional_mg['minutes'].apply(lambda x: str(x).zfill(2))


    # congest sectional target
    for col in congest_cols:
        df_sectional_target[col] = df_sectional_target[col].apply(lambda x: x if x !=0 else None)
    df_sectional_target.dropna(inplace=True)

    df_sectional_mean=df_sectional_target.groupby('time')[congest_cols].mean()

    df_sectional_tg=df_sectional_mean[(df_sectional_mean.index.hour.isin([7,8,9]))]
    df_sectional_tg['hour']=df_sectional_tg.index.hour
    df_sectional_tg['minutes']=df_sectional_tg.index.minute
    df_sectional_tg['time_line'] = df_sectional_tg['hour'].apply(lambda x: str(x).zfill(2) + ':') + df_sectional_tg['minutes'].apply(lambda x: str(x).zfill(2))

    return df_sectional_mg, df_sectional_tg, congest_cols


def get_sectional_df_dinner(stationname,stationline):
    df_congest_sectional=read_congest_section(stationline)
    df_congest_sectional.columns=df_congest_sectional.columns.str.replace('congestion', '혼잡도')

    df_sectional_target=df_congest_sectional[df_congest_sectional['stationName']==stationname]

    # congest sectional main
    congest_cols = [i for i in df_congest_sectional if i.startswith('혼잡도_')]

    for col in congest_cols:
        df_congest_sectional[col] = df_congest_sectional[col].apply(lambda x: x if x !=0 else None)
    df_congest_sectional.dropna(inplace=True)

    df_sectional_mean=df_congest_sectional.groupby('time')[congest_cols].mean()

    df_sectional_mg=df_sectional_mean[(df_sectional_mean.index.hour.isin([17,18,19]))]
    df_sectional_mg['hour']=df_sectional_mg.index.hour
    df_sectional_mg['minutes']=df_sectional_mg.index.minute
    df_sectional_mg['time_line'] = df_sectional_mg['hour'].apply(lambda x: str(x).zfill(2) + ':') + df_sectional_mg['minutes'].apply(lambda x: str(x).zfill(2))


    # congest sectional target
    for col in congest_cols:
        df_sectional_target[col] = df_sectional_target[col].apply(lambda x: x if x !=0 else None)
    df_sectional_target.dropna(inplace=True)

    df_sectional_mean=df_sectional_target.groupby('time')[congest_cols].mean()

    df_sectional_tg=df_sectional_mean[(df_sectional_mean.index.hour.isin([17,18,19]))]
    df_sectional_tg['hour']=df_sectional_tg.index.hour
    df_sectional_tg['minutes']=df_sectional_tg.index.minute
    df_sectional_tg['time_line'] = df_sectional_tg['hour'].apply(lambda x: str(x).zfill(2) + ':') + df_sectional_tg['minutes'].apply(lambda x: str(x).zfill(2))

    return df_sectional_mg, df_sectional_tg, congest_cols


def show_sectional_graph(stationname,stationline):
    df_main_morning,df_target_morning,cols = get_sectional_df_morning(stationname,stationline)
    df_main_dinner,df_target_dinner,cols = get_sectional_df_dinner(stationname,stationline)
    plt.figure(figsize=(20,20))

    plt.subplot(2,2,1)
    sns.heatmap(df_main_morning.set_index('time_line')[cols],cmap='rocket_r',
                annot=True,
                fmt='.1f',
                vmin=17,
                vmax=100)
    plt.xticks(rotation=45)
    plt.xlabel('혼잡도')
    plt.ylabel('시간')
    plt.title(f'지하철 칸별 혼잡도 출근시간 평균',fontsize=15)
    

    plt.subplot(2,2,2)
    sns.heatmap(df_target_morning.set_index('time_line')[cols],cmap='rocket_r',
                annot=True,
                fmt='.1f',
                vmin=17,
                vmax=100)
    plt.xticks(rotation=45)
    plt.xlabel('혼잡도')
    plt.ylabel('시간')
    plt.title(f'지하철 칸별 혼잡도 출근시간 {stationname}',fontsize=15)
    

    plt.subplot(2,2,3)
    sns.heatmap(df_main_dinner.set_index('time_line')[cols],cmap='rocket_r',
                annot=True,
                fmt='.1f',
                vmin=17,
                vmax=100)
    plt.xticks(rotation=45)
    plt.xlabel('혼잡도')
    plt.ylabel('시간')
    plt.title(f'지하철 칸별 혼잡도 퇴근시간 평균',fontsize=15)
    

    plt.subplot(2,2,4)
    sns.heatmap(df_target_dinner.set_index('time_line')[cols],cmap='rocket_r',
                annot=True,
                fmt='.1f',
                vmin=17,
                vmax=100)
    plt.xticks(rotation=45)
    plt.xlabel('혼잡도')
    plt.ylabel('시간')
    plt.title(f'지하철 칸별 혼잡도 퇴근시간 {stationname}',fontsize=15)
    plt.tight_layout()
    plt.show()
    return None
