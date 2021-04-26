source = ["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

write_file = open('kimetsu.txt', 'w')
for i in source:
    write_file.write(i+'\n')
write_file.close()

read_file = open('kimetsu.txt')
raw_data = read_file.read()
read_file.close()
point_data = raw_data.splitlines()
source = []
for i in point_data:
    source.append(i)
print('書き込み後のファイルから読み込んだメンバーズは{}です。'.format(source))

def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    if word in source:
        print("{}が見つかりました。".format(word))
    else:
        print("{}は登場人物ではありませんが、特別に追加します。".format(word))
        source.append(word)

        append_file = open('kimetsu.txt', 'a')
        append_file.write('\n'+word)
        append_file.close()

        print('追加後の新メンバーズは{}です。'.format(source))

if __name__ == "__main__":
    search()

read_file = open('kimetsu.txt')
raw_data = read_file.read()
read_file.close()
point_data = raw_data.splitlines()

print(raw_data)

source = []
for i in point_data:
    source.append(i)
print('追加後のファイルから読み込んだ新メンバーズは{}です。追加後の名前の前に、空の名前が一つ挿入されてしまう問題が発生しています。解決方法を教えていただけないでしょうか。よろしくお願い致します。'.format(source))