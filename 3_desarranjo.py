list=[]
print("Digite o tamanho da sequencia no vetor: ")
n=int(input())
for j in range(1,n+1):
    list.append(j)

def troca(vetor,i,j):
	aux=0
	aux=vetor[i]
	vetor[i]=vetor[j]
	vetor[j]=aux

def desarranjo(vetor,k,n):
	aux=0
	if(k == len(vetor)):
		for i in range(0,n):
			if(vetor[i] == i + 1):
				aux+=1
		if(aux == 0):
			for w in range(0,n):
				print(vetor[w])
				
			print(" ")
		
	else:
		for l in range (k,len(vetor)):
			troca(vetor,k,l)
			desarranjo(vetor,k+1,n)
			troca(vetor,k,l)
			


def listar_desarranjo(vetor,n):
    desarranjo(vetor,0,n)
	
	
listar_desarranjo(list,n)
