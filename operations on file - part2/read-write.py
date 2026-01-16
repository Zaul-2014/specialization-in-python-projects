file = open('Data.txt', 'w+')

file.write('hello world')
file.seek(0)

Data = file.read()

print(Data)

file.close()
#file quit line