import numpy

facts = []


def fact(N):
    print(N)
    if N == 0 or N == 1:
        return 1
    # if facts[N]:
    #     return facts[N]
    result = N * fact(N - 1)
    return result


def C(n, k):
    return fact(n) / fact(k) / fact(n - k)


def combination(index, k, A):

    a = np.zeros(8)
    print(a)

    res = [0]
    n = len(A)
    s = 0
    for t in range(1, k):
        j = res[t - 1] + 1
        while (j < (n - k + t)) and ((s + C(n - j, k - t)) <= index):
            s += C(n - j, k - t)
            j += 1
            print(res)
    res.append(j)

    # res.insert(0, 1)

    return res


print(combination(0, 3, [6, 7, 8, 9]))

# def log():
#     msg = Array.prototype.slice.call(arguments).join(" ")
#     document.getElementById("log").value += "\n" + msg
#     console.log(arguments)

# M = ["A", "B", "C", "D", "E"];
# for i in range(0, C(M.length, 3)):
#     log(i, combination(i, 3, M.slice(0)).join(""))
