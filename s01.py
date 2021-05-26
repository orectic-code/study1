import pandas as pd

def search():
    df = pd.read_csv("./source.csv")  
    source=list(df["name"])

    while True:
        # ユーザー入力
        word =input("鬼滅の登場人物の名前を入力 ＞＞ ") #input関数
     
        # 課題１．入力したキーワードで、キャラクターリスト(source)を検索して、存在すれば存在する旨を、存在しなければ存在しない旨をPrint文で表示してみましょう
        if word in source:
            print("「{}」が見つかりました".format(word))
        else:
            print("「{}」が見つかりませんでした".format(word))

            #課題２．１に追加して結果が存在しなかった場合に、キャラクターリスト(source)に追加できるようにしてみましょう
            add_flg = input("追加登録しますか？(0:しない 1:する)　＞＞　")
            if add_flg == "1":
                source.append(word)

        #課題３，４　に追加してキャラクターリスト(source)をCSVに書き込めるようにしてみましょう
        df=pd.DataFrame(source,columns=["name"])
        df.to_csv("./source.csv",encoding="utf_8-sig")
        print(source)


# if __name__ == "__main__" という if文を使うことで、
# 「この hello.py は python hello.py のように実行された
# （== importされたことで動作したのではない）」と判定できます。
if __name__ == "__main__":
    search()

