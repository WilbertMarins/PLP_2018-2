from itertools import combinations

lista=[]
n=int(input())
k=int(input())
soma=0
for j in range(1,n+1):
    lista.append(j)
    soma+=j

for i in (k, len(lista)):
    for comb in combinations(lista, i):

        if sum(comb) != soma:
           print (comb)
