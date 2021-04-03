def c19j():

    import pandas as pd
    import numpy as np
    Confirmed = pd.read_csv("./Origina_data/" + "pcr_positive_daily.csv" , encoding = "utf=8")
    Deaths = pd.read_csv("./Origina_data/" + "death_total.csv" , encoding = "utf=8")
    Recovered = pd.read_csv("./Origina_data/" + "recovery_total.csv" , encoding = "utf=8")
    PCR_TEST = pd.read_csv("./Origina_data/" + "pcr_tested_daily.csv" , encoding = "utf=8")

    #カラムのリネーム
    Confirmed = Confirmed.rename(columns = {"日付" : "Date" , "PCR 検査陽性者数(単日)" : "Confirmed"})

    #日付を降順にソート
    Confirmed = Confirmed.sort_index(ascending=False)

    #インデックスのリセット
    Confirmed = Confirmed.reset_index(drop=True).copy()


    Deaths  = Deaths.rename(columns = {"日付" : "Date" , "死亡者数" : "Deaths"})
    Deaths  = Deaths.sort_index(ascending=False)
    Deaths  = Deaths.reset_index(drop=True).copy()

    Recovered  = Recovered.rename(columns = {"日付" : "Date" , "退院、療養解除となった者" : "Recovered"})
    Recovered  = Recovered.sort_index(ascending=False)
    Recovered  = Recovered.reset_index(drop=True).copy()

    PCR_TEST = PCR_TEST.rename(columns = {"日付" : "Date" , "PCR 検査実施件数(単日)" : "PCR_TEST"})
    PCR_TEST  = PCR_TEST.sort_index(ascending=False)
    PCR_TEST  = PCR_TEST.reset_index(drop=True).copy()

    #データのマージ（Confirmed ・ PCR_TEST）
    c19j2_day1 = pd.merge(Confirmed , PCR_TEST , left_on=["Date"],right_on=["Date"], how ="left")
    c19j2_day1["PCR_TEST"] = c19j2_day1["PCR_TEST"].fillna(0).astype(np.int64)
    c19j2_day1.head()

    #データのマージ（Deaths , Recovered）
    c19j2_total = pd.merge(Deaths , Recovered , left_on=["Date"] , right_on=["Date"], how ="right")
    c19j2_total["Deaths"] = c19j2_total["Deaths"].fillna(0).astype(np.int64)
    c19j2_total.head()


    # 各カラムの日付数字への変換
    def oneday(St):
        # 各列の数字を格納
        St_d = []
        for i_cd in c19j2_total[St]:
            St_d.append(i_cd)

        St_ED = []
        # 当日数字から前日数字を引いて日別数字を算出
        for i in range(len(St_d)):
            if i + 1 < len(St_d):
                W = St_d[i] - St_d[i + 1]
                St_ED.append(W)


            elif i == len(St_d) - 1:
                W2 = c19j2_total[St][len(c19j2_total[St]) - 1]
                St_ED.append(W2)

            else:
                break

        St_day = pd.DataFrame(St_ED)
        Cn = [St]
        St_day.columns = Cn
        # print(St_ed_df.head())
        St_day.to_csv("./csv/" + St + "_day.csv", encoding="utf-8", index=None)


    oneday("Recovered")
    oneday("Deaths")

    Recovered_day = pd.read_csv("./csv/" + "Recovered_day.csv", encoding = "utf-8")
    Deaths_day = pd.read_csv("./csv/" + "Deaths_day.csv", encoding = "utf-8")

    #日付のみのデータセットを作成
    c19j2_day2 = c19j2_total.copy()

    #不要列の削除
    del c19j2_day2["Recovered"]
    del c19j2_day2["Deaths"]

    #データの結合(日付・Recovered_day・Deaths_day)
    c19j2_day2 = pd.concat([c19j2_day2 , Recovered_day , Deaths_day], axis=1)

    # 期間累計の確認(Deaths)
    print(c19j2_day2["Deaths"].sum())

    # 期間累計の確認(Recovered)
    print(c19j2_day2["Recovered"].sum())

    #最終結合・データの完成
    c19j2_day = pd.merge(c19j2_day1 , c19j2_day2, left_on=["Date"] , right_on=["Date"], how ="left")
    c19j2_day["Deaths"] = c19j2_day["Deaths"].fillna(0).astype(np.int64)
    c19j2_day["Recovered"] = c19j2_day["Recovered"].fillna(0).astype(np.int64)

    #カラムの並び替え
    c19j2_day =  c19j2_day[["Date" , "Confirmed" , "Deaths" , "Recovered" , "PCR_TEST"]]

    c19j2_day.isnull().sum()
    
    #スタート行の指定が必要な場合
    #c19j2_day = c19j2_day[2:]

    #csvファイルへの書き込み
    c19j2_day.to_csv("COVID19_Japan_2.csv" , encoding = "utf-8", index = None)


c19j()