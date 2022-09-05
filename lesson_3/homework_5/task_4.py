# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def RLE_compression(str_data):
    data_compressed = [[], []]
    i = 0
    k = 1
    print(data_compressed)

    while i < len(str_data):
        while i < len(str_data) - 1 and str_data[i] == str_data[i + 1]:
            i += 1
            k += 1
        data_compressed[0].append(str_data[i])
        data_compressed[1].append(k)
        i += 1
        print(data_compressed)
        k = 1

    return data_compressed


print(RLE_compression('377771010'))
print(RLE_compression('22233__A7  866666'))


def RLE_recovery(data_compressed):
    str_data = ''
    for el in range(len(data_compressed[0])):
        str_data += data_compressed[0][el] * data_compressed[1][el]
    return str_data


print(RLE_recovery(
    [['2', '3', '_', 'A', '7', ' ', '8', '6'], [3, 2, 2, 1, 1, 2, 1, 5]]))
print(RLE_recovery([['3', '7', '10'], [1, 4, 2]]))
