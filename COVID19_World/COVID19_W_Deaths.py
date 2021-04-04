def c19_w_deaths():

    import pandas as pd
    import numpy as np

    #Recovered基本データセットの読み込み
    c19w_df = pd.read_csv('./Original_Data/'+ "time_series_covid19_deaths_global.csv" , encoding = "utf=8")

    #不要列の削除
    del c19w_df["Province/State"]
    del c19w_df["Lat"]
    del c19w_df["Long"]

    #同じ名前が複数ある国の確認
    Cs = c19w_df["Country/Region"].value_counts().head(10)
    #print(Cs)

    #value_countsのデータから、列Country/Regionに同じ国名が複数ある国の選択
    scl = c19w_df["Country/Region"].value_counts().head(10)
    scl = scl.index[0:7]
    scl

    #列Country/Regionに同じ国名が複数ある国の抽出・csv書き込み・再読み込み
    for sc in scl:
        sc_df = c19w_df.loc[c19w_df["Country/Region"] ==  sc]
        sc_df = sc_df.groupby(["Country/Region"]).sum()
        sc_df.to_csv('./csv/'+""+ sc + "_df.csv", encoding = "utf=8")
        sc_df2 = pd.read_csv('./csv/'+""+ sc + "_df.csv", encoding = "utf=8")

    China_df2 = pd.read_csv('./csv/'+"China_df.csv", encoding = "utf=8")
    Canada_df2 = pd.read_csv('./csv/'+"Canada_df.csv", encoding = "utf=8")
    France_df2 = pd.read_csv('./csv/'+"France_df.csv", encoding = "utf=8")
    UnitedKingdom_df2 = pd.read_csv('./csv/'+"United Kingdom_df.csv", encoding = "utf=8")
    Australia_df2 = pd.read_csv('./csv/'+"Australia_df.csv", encoding = "utf=8")
    Netherlands_df2 = pd.read_csv('./csv/'+"Netherlands_df.csv", encoding = "utf=8")
    Denmark_df2 = pd.read_csv('./csv/'+"Denmark_df.csv", encoding = "utf=8")




    #結合予定7カ国の行をオリジナルデータからの削除
    c19w_df = c19w_df[c19w_df["Country/Region"] != "China"]
    c19w_df = c19w_df[c19w_df["Country/Region"] != "Canada"]
    c19w_df = c19w_df[c19w_df["Country/Region"] !=  "United Kingdom"]
    c19w_df = c19w_df[c19w_df["Country/Region"] !=  "France"]
    c19w_df = c19w_df[c19w_df["Country/Region"] !=  "Australia"]
    c19w_df = c19w_df[c19w_df["Country/Region"] !=  "Netherlands"]
    c19w_df = c19w_df[c19w_df["Country/Region"] !=  "Denmark"]

    c19w_df.info()

    #結合予定7カ国のオリジナルデータからの削除の確認
    c19w_df["Country/Region"].value_counts().head(10)

    #c19w_dfのcsvファイルへの書き出し・再読み込み
    c19w_df.to_csv('./csv/'+ "c19w_df.csv", encoding = "utf=8")
    c19w_df2 = pd.read_csv('./csv/'+ "c19w_df.csv", encoding = "utf=8", index_col=0)

    #合計データとオリジナルデータの結合
    c19w_df3 = pd.concat([China_df2, Canada_df2, UnitedKingdom_df2, France_df2, Australia_df2, Netherlands_df2 , Denmark_df2 , c19w_df2], axis=0)

    #行と列の変換
    c19w_df4 = c19w_df3.T

    #c19w_df4のcsvファイルへの書き出し・再読み込み
    c19w_df4.to_csv('./csv/' + "c19w_df4.csv", encoding = "utf=8", header = None)
    c19w_df5 = pd.read_csv('./csv/' + "c19w_df4.csv", encoding = "utf=8")

    #以下日付変換用追加コード

    # 日付を降順に並び替え
    c19w_df5 = c19w_df5.sort_index(ascending=False)
    c19w_df5 = c19w_df5.reset_index(drop=True).copy()
    #c19w_df5.head()

    c188_df = c19w_df5.copy()
    c188 = c188_df.copy()
    del c188["Country/Region"]

    cc188 = c188.columns

    # 日別数字に変換
    # 各列の数字を格納
    St_d = []
    St_ED = []

    for St in cc188:
        # print(ic)
        for i_cd in c188_df[St]:
            St_d.append(i_cd)
        # print(len(c188_df[St]))

        # 当日数字から前日数字を引いて日別数字を算出
        for i in range(len(St_d)):
            if i + 1 < len(St_d):
                W = St_d[i] - St_d[i + 1]
                St_ED.append(W)


            elif i == len(St_d) - 1:
                W2 = c188_df[St][len(c188_df[St]) - 1]
                St_ED.append(W2)

            else:
                break

        St_day = pd.DataFrame(St_ED)

        Cn = [St]
        St_day.columns = Cn
        # print(St_ed_df.head())
        St_day.to_csv("./csv/csv_day_Deaths/" + St + "_day.csv", encoding="utf-8", index=None)
        #print(St_day)
        St_d.clear()
        St_ED.clear()

    # csvファイルのパスを読み込み
    import glob

    p = "./csv/csv_day_Deaths/"
    csv_list = glob.glob(p + "*.csv")

    # リストに各csvファイルのパスをリストに格納
    df_list = []
    for i in csv_list:
        df = pd.read_csv(i)
        df_list.append(df)

    # csvファイルの結合
    df_country = pd.concat(df_list, sort=False, axis=1)

    # 日付のみの列を作成
    df_date = c19w_df5["Country/Region"]

    # 全ての国のデータを横に結合
    df_country = pd.concat(df_list, sort=False, axis=1)

    # 日付データと国データの結合
    c19w_day = pd.concat([df_date, df_country], axis=1)



    #以下、オリジナルコード

    # 作成したデータフレームを格納する空のリストを作成
    lo_df = []

    # カラムの国名をfor分で回す
    for i in c19w_day.columns[1:]:
        # 日付と該当する国の感染者数の二列のデータを作成
        x = c19w_day[["Country/Region", i]].copy()

        # カラム「Countryを作成し、該当する都道府県名を入力
        x["Country"] = i

        # 二列目の国名iを「状況に変更
        x = x.rename(columns={i: "Deaths"})

        # 1列目のカラムを「Country/Region」から「Date」に変更
        x = x.rename(columns={"Country/Region": "Date"})

        # 変数xをデータフレームlo_dfに格納
        lo_df.append(x)

    #日付変換

    # 年月日を格納する空のリストを作成
    ymd_l = []
    y_l = []
    m_l = []
    d_l = []

    X = lo_df[0]

    for i in range(len(X["Date"])):
        y = X["Date"][i].split('/')[2]
        y = "20" + y
        y_l.append(y)

    for i in range(len(X["Date"])):
        m = X["Date"][i].split('/')[0]
        if len(m) == 1:
            m = "0" + m
            m_l.append(m)
        else:
            m_l.append(m)

    for i in range(len(X["Date"])):
        d = X["Date"][i].split('/')[1]
        if len(d) == 1:
            d = "0" + d
            d_l.append(d)
        else:
            d_l.append(d)

    nums = len(m_l)
    for num in range(nums):
        ymd = y_l[num] + m_l[num] + d_l[num]
        # print(len(ymd))
        # print(ymd)
        ymd_l.append(ymd)

    #バラバラの188国分のデータセットを1つに結合
    c19w_deaths= pd.concat(lo_df , sort=False)

    #データフレームc19w_deathsに新しい列Date_new行を追加
    c19w_deaths["Date_new"] =  pd.DataFrame(ymd_l)

    #不要になった列Dateの削除
    del c19w_deaths["Date"]

    #カラムの並び替え
    c19w_deaths= c19w_deaths[["Date_new","Country","Deaths"]]

    #カラムのリネーム
    c19w_deaths= c19w_deaths.rename(columns={"Date_new" : "Date"})

    #csvファイルへの書き込み
    c19w_deaths.to_csv("./csv/csv_comp/" + "c19w_deaths.csv",index =None , encoding = "utf=8")

    #csvファイルからの読み込み
    c19w_deaths= pd.read_csv("./csv/csv_comp/" + "c19w_deaths.csv" , encoding = "utf=8")

    #c19w_deaths.head()


    #変換確認用コード

    print(c19w_df5["Japan"].head())
    print(c19w_df5["Japan"].tail())

    print(c19w_day["Japan"].sum())
    print()
    print(c19w_day["Japan"].head())
    print(c19w_day["Japan"].tail())

    #--------------------------------
    print()
    print()
    print(c19w_df5["US"].head())
    print(c19w_df5["US"].tail())

    print(c19w_day["US"].sum())
    print()
    print(c19w_day["US"].head())
    print(c19w_day["US"].tail())





