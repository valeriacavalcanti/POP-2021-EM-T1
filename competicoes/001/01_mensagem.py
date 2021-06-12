'''
    IFPB - CAMPUS JOÃO PESSOA
    PROJETO OLÍMPICO DE PROGRAMAÇÃO
    ENSINO MÉDIO
    TURMA: 2021 T1

    CONTEST: 001
    DATA: 11/06/2021

    QUESTÃO: 01 (MENSAGEM)
'''

# quantidade de outdoors
qtde = int(input())

# para cada outdoor
for i in range(qtde):
    # mensagem codificada
    codigo = input()
    mensagem = ''
    # para cada grupo de 3 dígitos
    for j in range(0, len(codigo), 3):
        simbolo = chr(int(codigo[j:j+3]))
        # símbolo é uma letra ou espaço em branco
        if (simbolo.isalpha() or simbolo == ' '):
            mensagem += simbolo
    # mensagem decodificada
    print(mensagem)
