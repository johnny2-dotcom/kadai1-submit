
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く

# 課題１
    if word in source :
        print('{}が見つかりました。'.format(word))
    else:
        print('{}が見つかりません。'.format(word))
# 課題２
        source.append(word)
        print('{}を追加しました。'.format(word))
        print('追加後の登場人物は{}です。'.format(source))

    # print("{}が見つかりました".format(word))

if __name__ == "__main__":
    search()

# 課題３、課題４

with open('source.csv') as file:
    member = file.read()
    name = member.split(',')
    print('source.csvから読み込んだ登場人物は{}です。'.format(name))

def search_write_name():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    if word in name :
        print('{}が見つかりました。output.csvを確認してください。'.format(word))
        with open('output.csv', 'w') as file:
            for person in name:
                file.write(person+',')
    else:
        print('{}が見つかりません。'.format(word))
        name.append(word)
        print('{}を追加しました。output.csvを確認してください。'.format(word))
        with open('output.csv', 'w') as file:
            for person in name:
                file.write(person+',')

if __name__ == "__main__":
    search_write_name() 

