def Companyanalysis():
    import pandas as pd
    import numpy as np
    # from matplotlib import pyplot as plt
    import time
    from datetime import datetime

    # Original.csv読み込み
    df = pd.read_csv('df_original.csv', encoding='utf-8', dtype={'レンタル区分': str, '展覧会名': str, '委託商品区分': str})

    # カラム抽出
    df = df[['営業名', '得意先', '出荷日', '伝票№', '素材名', '製品名', '受注金額', '重量']].copy()

    # カラムリネーム
    df = df.rename(columns={'得意先': '得意先名', '受注金額': '売上金額'})

    # カラム「営業名」を変換
    df["営業名"] = df["営業名"].apply(lambda x: x.split(" / ")[0])

    # カラム「出荷日」を日付フォーマットに変換
    time = df["出荷日"]
    time2 = pd.to_datetime(time, format='%Y%m%d')
    time3 = time2.dt.year
    df["year"] = time3

    # 不要金額削除
    df = df[df['伝票№'] != 2101624]
    df = df[df['伝票№'] != 2101621]

    # 生産地分類追加
    # 最新生産地データ読み込み
    produce = pd.read_csv('./map_csv/' + 'produce.csv', encoding='utf-8')

    # 最新生産地分類を辞書型に変換
    produce_f = dict(zip(produce['0'], produce['1']))

    # 新型式分類
    df['生産地'] = df['製品名'].map(produce_f)

    # 営業所分類追加
    # 最新営業所データ読み込み
    branch = pd.read_csv('./map_csv/' + 'branch.csv', encoding='utf-8')

    # 最新営業所分類を辞書型に変換
    branch_f = dict(zip(branch['担当営業'], branch['営業所']))

    # 新営業所分類
    df['営業所'] = df.営業名.map(branch_f)

    # 最新素材データ読み込み
    sozai = pd.read_csv('./map_csv/' + 'sozai.csv', encoding='utf-8')

    # 最新素材分類を辞書型に変換
    sozai_f = dict(zip(sozai['素材名'], sozai['材料']))

    # 新型式分類
    df['材料'] = df.素材名.map(sozai_f)

    # df_PowerBI.csvを書き出し
    df.to_csv('df_PowerBI.csv', encoding='utf-8', index=None)


Companyanalysis()