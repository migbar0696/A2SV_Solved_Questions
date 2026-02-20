t = int(input())

for i in range(t):
    n = int(input())
    
    lista = list(map(int, input().split()))
    listb = list(map(int, input().split()))
    
    indexab = []
    indexa = []
    indexb = []
    
    # print(lista)
    # print(listb)
    
    for i in range(n):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                indexa.append(j + 1)
                
    for i in range(n):
        for j in range(n - 1 - i):
            if listb[j] > listb[j + 1]:
                listb[j], listb[j + 1] = listb[j + 1], listb[j]
                indexb.append(j + 1)
    
    for i in range(n):
        if lista[i] > listb[i]:
            lista[i], listb[i] = listb[i], lista[i]
            indexab.append(i + 1)
            
    na = len(indexa )
    nb = len(indexb)
    nab = len( indexab)
    print( na+ nb +nab )
    
    for i in range(na):
        print(1, indexa[i])
    
    for j in range(nb):
        print(2, indexb[j])
    for k in range(nab):
        print(3, indexab[k])
      
