k = { 'a':2, 'k':3, 'o':90, 'g':0}
g = sorted(k.items())
p = sorted(list(k.items()), key=lambda x: x[1], reverse=True)
j = [i for i in p]
print(type(g))