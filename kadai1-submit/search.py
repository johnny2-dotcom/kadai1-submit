
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}が見つかりませんでした".format(word))
    # for i in source:
    #     if i == word:
    #         print("{}が見つかりました".format(word))



if __name__ == "__main__":
    search()
