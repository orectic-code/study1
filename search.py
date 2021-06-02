import pandas as pd

def search():
    df = pd.read_csv("./source.csv")  
    source=list(df["name"])

    while True:
        word =input("鬼滅の登場人物の名前を入力 ＞＞ ") 
     
        if word in source:
            print("「{}」が見つかりました".format(word))
        else:
            print("「{}」が見つかりませんでした".format(word))

            add_flg = input("追加登録しますか？(0:しない 1:する)　＞＞　")
            if add_flg == "1":
                source.append(word)

        df=pd.DataFrame(source,columns=["name"])
        df.to_csv("./source.csv",encoding="utf_8-sig")
        print(source)


if __name__ == "__main__":
    search()


