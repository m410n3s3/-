#coding: utf=8

def script0():
    vA = [] # Vetor vazio e de tamanho 0
    vB = [ None ] * 5 # Vetor vazio de tamanho 5
    vC = [1 , 3.4 , "A" , " IFSC " , 3.4 ] #vetor de
        # tamanho 4 e com tipos diferentes
    print ( vA ) # Imprime o vetor vA
    print ( vB ) # Imprime o vetor vB
    print ( vC ) # Imprime o vetor vC
    print("Número de vezes que aparece 3.4: ", vC.count(3.4))

def script1():
    lista1 = ["Rampa", "Descida", 11.34]
    tupla1 = (1, 3.4,"A" , " IFSC "  )
    print(lista1)
    lista1[1]= "Subida"
    print("Lista 1 modificada", end = " ")
    print(lista1)
    print(tupla1)
    tupla1[1] = "2.2"
    print("Tupla 1 modificada", end = " ")
    print(tupla1)

def script2():
    a = 2.4
    b = 3.5
    return [a,b]

def script3():
    frutas = ["maçã","abacate", "açaí", "pêra"]
    print("maçã" in frutas)
    print("cajá" not in frutas)#mesmo que print("cajá" not in frutas)
    fruta_teste = "abacate"
    if fruta_teste not in frutas:
        frutas.append("laranja")
    else:
        print(f"{fruta_teste} adicionado ao vetor")
    print(frutas)

def script4():
    moedas = ["BRL", "USD", "EUR"]
    for i, moeda in enumerate(moedas):
        print(i, moeda)


if __name__=="__main__":
    # saida = script2()
    # print(saida)
    script4()
