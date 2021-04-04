Randomseed1973_changing_jobs

プログラミング言語pythonを使ったデータ分析の取り組みとして以下を提示いたします。

1：SalesAnalysisフォルダ  
    ・現在所属する企業で、週一度のペースで、提出している売上分析資料です  
    ・内容はダミーデータに変更してあります  
    ・下記に詳細有  
  
2：COVID19_Japan_1フォルダ  
    ・個人で取り組んでいるCOVID-19分析用資料。  
    ・日本全国と都道府県別の感染者数。  
    ・元データは日本のAI開発コンペティションサイトSIGNATEからダウンロード・使用。  
    ・下記に詳細有
  
3：COVID19_Japan_2フォルダ  
    ・個人で取り組んでいるCOVID-19の分析用資料。  
    ・日本全国の感染者数・死亡者数・回復者数・PCR検査数。  
    ・元データは厚生労働省オープンデータからダウンロード・使用。  
    ・下記に詳細有
  
4：COVID19_Worldフォルダ  
    ・個人で取り組んでいるCOVID-19の分析用資料。  
    ・全国世界のの感染者数・死亡者数。  
    ・元データはジョンズホプキンズ大学のGitHubからダウンロード・使用。  
    ・下記に詳細有  


詳細

1：SalesAnalysisフォルダ  
    ・現在所属する企業で、週一度のペースで、提出している売上分析資料です(内容はダミーデータに変更してあります)。  
    ・会社システムからダウンロードしたcsvデータを、プログラミング言語pythonを使って処理してビジネスインテリジェンスツール用に変換、Microsoft Power BIにて視覚化・分析資料を作成。  
    ・個人的な取り組みとして昨年3月から所属する営業所で提供を開始し、昨年9月からは会社から依頼があり週一度のペースで営業所のリーダーに提出し現在も継続中。  

    ファイル内データ説明  
    1：df_original.csv(システムからのダウンロードしたcsvデータ。行・列の数はそのままですが、内容は変更してあります)  
    2：Original_to_PowerBI_conversion.py(1のデータをPower BIに用に変換する為のpythonプログラム)  
    3：df_PowerBI.csv(2によって変換された、ビジネスインテリジェンスツール用csvデータ)  
    4：PowerBI.pbix(3のデータを読み込み、作成した、Microsoft Power BIデータ)  

    付記
        1：map_csvフォルダとその中のデータは2のプログラムを動かす為の補助データ。
        2：Original_to_PowerBI_conversion.ipynb、は2と同様ですが、こちらはWebブラウザ上で動作する実行環境Jupyter Notebook上で動作します。



2：COVID19_Japan_1フォルダ
    個人で取り組んでいるCOVID-19_日本版(1)の分析資料。
    日本全国と都道府県別の感染者数。
    日本のAI開発コンペティションサイト『SIGNATE』から日本の都道府県別COVID19データをダウンロード、プログラミング言語pythonを使って処理してビジネスインテリジェンスツール用に変換、Microsoft Power BIにて視覚化までを行っています。
    視覚化したデータ・分析は    
    Googleデータポータル：https://datastudio.google.com/u/2/reporting/bc62963e-afca-47df-9411-6048679673ad/page/bcURB  
    Blog:http://randomseed1973.turtlewalktraveler.com/category/covid-19/japan1/  
    にて公開しております。  
    

    ファイル内データ説明
    1：SIGNATE COVID-19 Case Dataset - 罹患者統計.csv(SIGNATEからダウンロードした日本の都道府県別COVID19のcsvデータ)
    2：COVID19_Japan_1.py(1のデータをビジネスインテリジェンスツール用に変換する為のpythonプログラム)
    3：COVID19_Japan_1.csv(2によって変換された、ビジネスインテリジェンスツール用csvデータ)



3：COVID19_Japan_2フォルダ  
    個人で取り組んでいるCOVID-19_日本版(2)の分析資料。  
    日本全国の感染者数・死亡者数・回復者数・PCR検査数。  
    厚生労働省オープンデータから感染者数・死亡者数・回復者数・PCR検査数のデータをダウンロード、プログラミング言語pythonを使って処理してビジネスインテリジェンスツール用に変換、Googleデータポータルにて視覚化までを行っています。  
    視覚化したデータ・分析は  
    Googleデータポータル：https://datastudio.google.com/u/2/reporting/75618372-9899-4dd3-bd5b-1a686b99e627/page/W7iYB     
    Blog:http://randomseed1973.turtlewalktraveler.com/category/covid-19/japan2/  
    にて公開しております。
    
    ファイル内データ説明
    1：SIGNATE COVID-19 Case Dataset - 罹患者統計.csv(SIGNATEからダウンロードした日本の都道府県別COVID19のcsvデータ)
    2：COVID19_Japan_1.py(1のデータをビジネスインテリジェンスツール用に変換する為のpythonプログラム)
    3：COVID19_Japan_1.csv(2によって変換された、ビジネスインテリジェンスツール用csvデータ)
    


4：COVID19_Worldフォルダ  
    個人で取り組んでいるCOVID-19_世界版の分析資料。  
    全国世界のの感染者数・死亡者数。  
    ジョンズホプキンズ大学のGitHubからデータをダウンロード、プログラミング言語pythonを使って処理してビジネスインテリジェンスツール用に変換、Googleデータポータルにて視覚化までを行っています。  
    視覚化したデータ・分析は   
    Googleデータポータル：https://datastudio.google.com/u/2/reporting/d4b5e00c-501e-4d61-94d2-2cc0cbf11570/page/hWDbB    
    Googleデータポータル2：https://datastudio.google.com/u/2/reporting/c79eae40-99ca-44ab-8544-ee9f8315037d/page/6Sl0B      
    Blog:http://randomseed1973.turtlewalktraveler.com/category/covid-19/world/  
    にて公開しております。  
    
    ファイル内データ説明
    1：Original_Dataフォルダ(ジョンズホプキンズ大学のGitHubからダウンロードした全世界のCOVID-19のcsvデータ)
    2：COVID19_World.py(1のデータをビジネスインテリジェンスツール用に変換する為のpythonプログラム)
    3：COVID19_World.csv(2によって変換された、ビジネスインテリジェンスツール用csvデータ)

    付記
        1：COVID19_W_Comfermed.py・COVID19_W_Deaths.py・COVID19_W_Recovered.pyはCOVID19_World.pyでライブラリーとして使用する関数を記述したファイル。
        2：csvフォルダはCOVID19_World.pyを動作させる際に必要な補助データ等が入っています。