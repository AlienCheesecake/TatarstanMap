import xlrd
f = xlrd.open_workbook('Towns.xls')
sh = f.sheet_by_index(0)
Tablica = [[float(sh.cell_value(n, m)) for m in range(1, 16)] for n in range(1, 16)]
Goroda = [sh.cell_value(n, 0) for n in range(1, 16)]
print('Пункты: ', ' '.join(Goroda))
start = Goroda.index(input('Место отправления: '))
finish = Goroda.index(input('Место прибытия: '))
def dijkstra(Tablica, start):
    n = len(Tablica)
    Q = [(0, start)]
    d = [float('inf') for i in range(n)]
    d[start] = 0
    while len(Q) != 0:
        (cost, u) = Q.pop(0)
        for v in range(n):
            if d[v] > d[u] + Tablica[u][v]:
                d[v] = d[u] + Tablica[u][v]
                Q.append((d[v], v))
    return d
def getPath(finish):
    global d
    n = len(Tablica)
    path = [finish]
    while finish != start:
        for v in range(n):
            if d[v] == d[finish] - Tablica[finish][v]:
                path.append(v)
                finish = v
    return path[::-1]
d = dijkstra(Tablica, start)
p = getPath(finish)
path = [Goroda[i] for i in p]
print('Кратчайшее расстояние:', d[finish])
print('Путь:', ' '.join(path))
