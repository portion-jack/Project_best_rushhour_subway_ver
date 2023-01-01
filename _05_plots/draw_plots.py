import matplotlib.pyplot as plt
plt.rc('font',family='AppleGothic')
import seaborn as sns

def plot_congest_station(df):
    plt.figure(figsize=(12,8))
    df.groupby('time')['congestionTrain'].mean().plot(c='k',lw=5)
    df.groupby('time')['congestionTrain'].mean().plot(kind='bar',color='r')
    plt.xticks(rotation=30,ticks=range(0,len(df.time.unique()),6))
    plt.title(df['station_name'].unique()[0],fontsize=14)
    plt.show()
    return None

def plot_congest_sectional(df):
    plt.figure(figsize=(10,9))
    sns.heatmap(
        data=df.groupby('time')[[i for i in df.columns if i.startswith('혼잡도')]].mean().iloc[3:-7,:],
        annot=True,
        fmt='.1f',
        linewidths=1,
        cmap='rocket_r',
        vmin=0,
        vmax=100
        )
    plt.yticks(rotation=0)
    plt.title(df['station_name'].unique()[0],fontsize=14)
    plt.show()
    return None

def plot_getoff_sectional(df):
    plt.figure(figsize=(10,9))
    sns.heatmap(
        data=df.groupby('time')[[i for i in df.columns if i.startswith('하차수')]].mean().iloc[3:-7,:],
        annot=True,
        fmt='.1f',
        linewidths=1,
        cmap='rocket_r',
        vmin=0,
        vmax=100
        )
    plt.yticks(rotation=0)
    plt.title(df['station_name'].unique()[0],fontsize=14)
    plt.show()
    return None
