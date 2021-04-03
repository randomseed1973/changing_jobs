def c19j():

    import pandas as pd
    import numpy as np

    #c19_j1 = pd.read_csv("SIGNATE_COVID19.csv" , encoding = "utf=8")
    c19_j1 = pd.read_csv("SIGNATE COVID-19 Case Dataset - 罹患者統計.csv", encoding="utf=8")

    #1行目を削除
    c19_j1 = c19_j1[1:]

    #2列目・3列目の削除
    del c19_j1["日本国内\n累計罹患者数"]
    del c19_j1["日本国内\n新規罹患者数"]

    c19_j1.head()

    #欠損値の確認
    c19_j1.isnull().sum()

    #欠損値の削除
    c19_j1 = c19_j1.dropna()
    #欠損値の再確認
    c19_j1.isnull().sum()

    # 作成したデータフレームを格納する空のリストを作成
    lo_df = []

    # カラムの都道府県をfor分で回す
    for i in c19_j1.columns[1:]:
        # 日付と該当する都道府県の感染者数の二列のデータを作成
        x = c19_j1[["日付", i]].copy()

        # カラム「Location」を作成し、該当する都道府県名を入力
        x["Location"] = i

        # 2列目のカラムを都道府県名から「Confirmed」に変更
        x = x.rename(columns={i: "Confirmed"})

        # 1列目のカラムを日付から「Date」に変更
        x = x.rename(columns={"日付": "Date"})

        # 変数xをデータフレームlo_dfに格納
        lo_df.append(x)

    # リストに格納されたデータフレームの確認
    lo_df[0]

    lo_df[0].tail()

    lo_df[46].head()

    lo_df[46].tail()

    #データの結合
    c19j1_df = pd.concat(lo_df , sort=False, ignore_index=True)
    c19j1_df.head()
    c19j1_df.tail()

    #データ数の確認
    len(c19j1_df)

    #欠損値の確認
    c19j1_df.isnull().sum()

    #Confirmedをキャスト
    c19j1_df["Confirmed"] = c19j1_df["Confirmed"].astype(np.int64)
    c19j1_df.info()

    c19j1_df.head()
    c19j1_df.tail()

    #csvファイルに書き込み
    #c19j1_df.to_csv("c19j1_df_20200830.csv", index = False, encoding="utf-8")
    c19j1_df.to_csv("COVID19_Japan_1.csv", index=False, encoding="utf-8")


c19j()
