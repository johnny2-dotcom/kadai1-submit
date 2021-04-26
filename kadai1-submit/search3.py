read_file = open('source.txt')
raw_data = read_file.read()
read_file.close()
point_data = raw_data.splitlines()


print(raw_data)

source = []
for i in raw_data:
    source.append(i)
print(source)


source = []
for i in point_data:
    source.append(i)
print(source)
    
