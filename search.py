import pandas as pd

def search():
    # 検索対象
    df=pd.read_csv("./source.csv")
    source=list(df["name"])

    while True:
        # ユーザー入力
        word=input("鬼滅の登場人物を入力　＞＞　")
    
        #検索
        if word in source:
            print("{}が見つかりました".format(word))
        else:
            print("{}が見つかりませんでした".format(word))
            # 追加
            add_flg=input("追加登録しますか？(0:しない,1:する')　＞＞　")
            if add_flg == "1":
                source.append(word)

        df=pd.DataFrame(source,columns=["name"])
        df.to_csv("./source.csv,encoding=utf_8-sig")
        print(source)

if __name__ == "__main__":
    search()



# # 課題
# １．入力したキーワードで、キャラクターリスト(source)を検索して、存在すれば存在する旨を、存在しなければ存在しない旨をPrint文で表示してみましょう<br>

# ２．１に追加して結果が存在しなかった場合に、キャラクターリスト(source)に追加できるようにしてみましょう<br>

# ３．２に追加してキャラクターリスト(source)をCSVから読み込んで登録できるようにしてみましょう<br>

# ４．３に追加してキャラクターリスト(source)をCSVに書き込めるようにしてみましょう