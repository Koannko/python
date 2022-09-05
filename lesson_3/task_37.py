# 37. Дан список чисел. Создать список в который попадают числа, описывающие
# возрастающую последовательность и содержащие максимальное количество элементов.
def subsets(arr, s_len):
    subsets = [[]]
    arr = set(arr)
    for a in arr:
        subsets += [s + [a] for s in subsets if len(s) < s_len]
    return subsets


def find_subset(arr, subset, s_len):
    count = 0
    j = 0
    for i in range(len(arr)):
        if arr[i] == subset[j]:
            count += 1
            j += 1
    return count == s_len


def get_largest_increas_seq(arr):
    s_len = len(arr)
    sets = subsets(arr, s_len)
    while s_len:
        S = list(filter(lambda s: len(s) == s_len, sets))
        for s in S:
            if find_subset(arr, s, s_len):
                return s
        s_len -= 1


# => [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]
print(get_largest_increas_seq([0, 5, 1, 2, 2, 3, 4, 6, 7, 8, 9, 10]))
# => [1, 2, 3, 4, 6, 7]
print(get_largest_increas_seq([1, 5, 2, 3, 4, 6, 1, 7]))
print(get_largest_increas_seq([5, 2, 3, 4, 6, 1, 7]))  # => [2, 3, 4, 6, 7]
print(get_largest_increas_seq([1, 3, 5, 6, 7]))  # => [1, 3, 4, 5, 7]
