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
        print("{}が見つからなかったので追加します".format(word))
        source.append(word)
        print('新メンバーズは{}です'.format(source))



if __name__ == "__main__":
    search()
