Randomseed1973_changing_jobs

プログラミング言語pythonを使ったデータ分析の取り組みとして以下を提示いたします。

1：SalesAnalysisフォルダ
    現在所属する企業で、週一度のペースで、提出している売上分析資料です。
    システムからダウンロードしたデータを、プログラミング言語pythonを使って処理し、ビジネスインテリジェンスツール用に変換、Microsoft Power BIにて分析資料を作成。
    会社非公式ですが、個人的な取り組みとして昨年3月から所属する営業所で提供を開始し、昨年9月からは会社から依頼があり週一度のペースで営業リーダーに提出し現在も継続中。

    ファイル内データ説明
    1：df_original.csv(システムからのダウンロードしたcsvデータ。行・列の数はそのままですが、内容は変更してあります)
    2：Original_to_PowerBI_conversion.py(1のデータをPower BIに用に変換する為のpythonプログラム)
    3：df_PowerBI.csv(1から変換された、ビジネスインテリジェンスツール用csvデータ)
    4：PowerBI.pbix(3のデータを読み込み、作成した、Microsoft Power BIデータ)

    付記
        1：map_csvフォルダとその中のデータは2のプログラムを動かす為の補助データです。
        2：Original_to_PowerBI_conversion.ipynb、は2と同様ですが、こちらはWebブラウザ上で動作する実行環境Jupyter Notebook上で動作します。