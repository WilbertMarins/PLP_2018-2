from itertools import permutations
import re      #uso da bibli de expressões regulares

permutation_list = []
n=int(input())

for w in range(1,n+1):
    permutation_list.append(w)
    
k_terms_total=len(permutation_list)

print()
for i in permutations(permutation_list,k_terms_total): #considera as possibilidades
    i = re.sub(r'\W',"",str(i)) #r'\W' (elimina as ',')
    print(i)
