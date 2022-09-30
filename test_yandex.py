with open('input.txt', 'r') as data:
    arr = []
    for line in data:
        arr.append(line)

n = int(arr[0])
tasks = arr[1: n + 1]
exses = []

for task in range(len(tasks)):
    t = tasks[task].split(',')
    exses.append([t[0], int(t[1])])
players = []
count = int(arr[n + 1])
max_pl = 0
info_pl = arr[n + 2:]
for i in range(len(info_pl)):
    p = info_pl[i].split(',')
    players.append([])
    for j in range(len(p)):
        if j >= len(p) - 2:
            players[i].append(int(p[j]))
        else:
            players[i].append(p[j])
count_pls = 0
list_pl = []
final = []
for exs in range(len(exses)):
    max_pl = exses[exs][1]
    for pl in players:
        if exs in pl:
            count_pls += 1
            list_pl.append([players[0], players[:-2], players[:-1]])
    if count_pls > max_pl:
        count_pret = 0
        counts = []
        for i in range(len(players) - 1):
            max_count = players[i][:-2]
            counts.append(players[i][:-2])
            if players[i + 1][:-2] > max_count:
                max_count = players[i + 1][:-2]
        for i in range(len(players)):
            if players[i][:-2] == max_count:
                count_pret += 1
        if count_pret > count_pls:
            falls = []
            for i in range(len(players) - 1):
                falls.append(players[i][:-1])
            min_f = min(falls)
            while count_pls < max_pl:
                for i in range(len(players) - 1):
                    if i == min_f:
                        final.append(players[i][0])
                        falls.extend(i)
                        min_f = min(falls)
        else:
            while count_pls < max_pl:
                for i in range(len(players) - 1):
                    if i == max_count:
                        final.append(players[i][0])
                        counts.extend(i)
                        max_count = max(counts)
    else:
        for i in range(len(players)):
            final.append(players[i][0])
print(final)
