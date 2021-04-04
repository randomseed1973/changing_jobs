def c19_w_merge():

    import pandas as pd
    import numpy as np

    #各データセットの読み込み
    c19w_R= pd.read_csv("./csv/csv_comp/" + "c19w_Recovered.csv",encoding = "utf-8")
    c19w_C= pd.read_csv("./csv/csv_comp/" + "c19w_Confirmed.csv",encoding = "utf-8")
    c19w_D= pd.read_csv("./csv/csv_comp/" + "c19w_Deaths.csv",encoding = "utf-8")

    #ConfirmedとRecoveredの結合
    c19w_f = pd.merge(c19w_C , c19w_R , left_on=["Date","Country"],right_on=["Date","Country"])

    #Confirmed・RecoveredとDeathsの結合
    c19w_f = pd.merge(c19w_f  , c19w_D, left_on=["Date","Country"],right_on=["Date","Country"])


    # 欠損値の削除
    c19w_f = c19w_f.dropna()

    # floatからintにキャスト
    c19w_f["Confirmed"] = c19w_f["Confirmed"].astype(np.int64)
    c19w_f["Recovered"] = c19w_f["Recovered"].astype(np.int64)
    c19w_f["Deaths"] = c19w_f["Deaths"].astype(np.int64)
    print(c19w_f.dtypes)


    #csvファイルへの書き込み
    c19w_f.to_csv("COVID19_World.csv", encoding = "utf-8" , index = None)
    #c19w_df = pd.read_csv("./csv_comp/" + "c19w_df_20200809.csv" , encoding = "utf-8" )

    #完成データセットの内容確認
    #c19w_df.info()
