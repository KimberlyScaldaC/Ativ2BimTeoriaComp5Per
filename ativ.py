# Nome do arquivo
Nome_Arquivo = 'TEESTE.txt'

Palavras_Separadas = []
valoresRegist = []

Total_Linhas = 0


def print_lista(linha, lista):
    elementos = ', '.join(map(str, lista))
    print(f"{linha}: ({elementos})")


def verificar_operacoes(operacao, Palavras_Separadas, linha, valoresRegist):
    if "ADD" in operacao:
        proxLinha, valoresRegist = ADD(Palavras_Separadas, linha,
                                       valoresRegist)
        return proxLinha, valoresRegist

    if "SUB" in operacao:
        proxLinha, valoresRegist = SUB(Palavras_Separadas, linha,
                                       valoresRegist)
        return proxLinha, valoresRegist

    if "ZER" in operacao:
        proxLinha = ZER(Palavras_Separadas, linha, valoresRegist)
        return proxLinha, valoresRegist


def verificar_registrador(registrador):
    if "A" in registrador:
        #print("'A'")
        return 0

    if "B" in registrador:
        #print("'B'")
        return 1

    if "C" in registrador:
        #print("'C'")
        return 2

    if "D" in registrador:
        #print("'D'")
        return 3

    if "E" in registrador:
        #print("'E'")
        return 4

    if "F" in registrador:
        #print("'F'")
        return 5

    if "G" in registrador:
        #print("'G'")
        return 6

    if "H" in registrador:
        #print("'H'")
        return 7


def ADD(Palavras_Separadas, linha, valoresRegist):
    #print("ENTROU 'ADD'")
    registrador = verificar_registrador(Palavras_Separadas[linha][2])
    valorRegistrador = int(valoresRegist[registrador])
    valorRegistrador += 1
    valoresRegist[registrador] = str(valorRegistrador)
    proxLinha = int(Palavras_Separadas[linha][3])
    return proxLinha, valoresRegist


def SUB(Palavras_Separadas, linha, valoresRegist):
    #print("ENTROU 'SUB'")
    registrador = verificar_registrador(Palavras_Separadas[linha][2])
    if valoresRegist[registrador] == '0':
        valoresRegist[registrador] = '0'
    else:
        valorRegistrador = int(valoresRegist[registrador])
        valorRegistrador -= 1
        valoresRegist[registrador] = str(valorRegistrador)
    proxLinha = int(Palavras_Separadas[linha][3])
    return proxLinha, valoresRegist


def ZER(Palavras_Separadas, linha, valoresRegist):
    #print("ENTROU 'ZER'")
    registrador = verificar_registrador(Palavras_Separadas[linha][2])
    if valoresRegist[registrador] == '0':
        proxLinha = int(Palavras_Separadas[linha][3])
    else:
        proxLinha = int(Palavras_Separadas[linha][4])
    return proxLinha


# ----------------------- MAIN ----------------------------

A = input("Digite o valor para A: ")
B = input("Digite o valor para B: ")
C = '0'
D = '0'
E = '0'
F = '0'
G = '0'
H = '0'

valoresRegist.append(A)
valoresRegist.append(B)
valoresRegist.append(C)
valoresRegist.append(D)
valoresRegist.append(E)
valoresRegist.append(F)
valoresRegist.append(G)
valoresRegist.append(H)

print(valoresRegist)

print("ENTROU 1 WHILE")
with open(Nome_Arquivo, 'r') as arquivo:
    for linha in arquivo:
        Total_Linhas += 1
        linha = linha.strip()
        palavras = linha.split()
        Palavras_Separadas.append(palavras)

proxLinha = 1
while True:
    print_lista(proxLinha, valoresRegist)
    if proxLinha == 0 or proxLinha == 100:
        break
    proxLinha, valoresRegist = verificar_operacoes(
        Palavras_Separadas[proxLinha - 1][1], Palavras_Separadas,
        proxLinha - 1, valoresRegist)
    print("\n")
