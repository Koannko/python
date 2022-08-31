path = 'file.txt'
f = open(path, 'r')
data = f.read() + ' '
list = [(int(i), int(i)**2)
        for i in data if i != ' ' and int(i) % 2 == 0]
print(list)
f.close()
