def teste_leitura1(path): # OBJETIVO -> VERIFICAR LEIRUTA CORRRETA DO ARQUIVO CHECANDO CABEÇALHOS
    base = open(path, 'r')
    for linha in base:
        if "states" in linha:
            print("States entrou")
        if "initial" in linha:
            print("Initial entrou")
        if "accepting" in linha:
            print("Accepting entrou")
        if "alphabet" in linha:
            print("Alphabet entrou")
        if "transitions" in linha:
            print("Transitions entrou")
    print(base.readlines())
    base.close()


#teste_leitura1('.\\automatos\\DFA1.txt') #FUNCIONANDO



def teste_leitura2(path): # OBJETIVO -> OBTER TODAS AS LINHAS SEM O CABEÇALHO PARA FUTURA MANIPULAÇÃO

    linhas_sem_cabecalho = []

    with open(path, 'r') as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas:
            if "#" not in linha:
                linhas_sem_cabecalho.append(linha.strip())

    arquivo.close()
    return print(linhas_sem_cabecalho)


teste_leitura2('.\\automatos\\DFA1.txt') #FUNCIONANDO



