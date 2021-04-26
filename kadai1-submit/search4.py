source = ["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

write_file = open('member.txt', 'w')
for i in source:
    write_file.write(i+'\n')
write_file.close()
