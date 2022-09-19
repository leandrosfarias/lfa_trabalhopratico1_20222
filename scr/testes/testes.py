def teste_leitura1(path):  # OBJETIVO -> VERIFICAR LEITURA CORRRETA DO ARQUIVO CHECANDO CABEÇALHOS
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


#teste_leitura1('.\\automatos\\DFA1.txt')  FUNCIONANDO


def teste_leitura2(path):  # OBJETIVO -> OBTER TODAS AS LINHAS SEM O CABEÇALHO PARA FUTURA MANIPULAÇÃO

    linhas_sem_cabecalho = []

    with open(path, 'r') as arquivo:

        linhas = arquivo.readlines()

        for linha in linhas:
            if "#" not in linha:
                linhas_sem_cabecalho.append(linha.strip())

    arquivo.close()
    return print(linhas_sem_cabecalho)


# teste_leitura2('.\\automatos\\DFA1.txt')  FUNCIONANDO


def teste_leitura3(path): # OBJETIVO -> SEPARAÇÃO DOS CONJUNTOS:
    automato = []
    with open(path, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            automato.append(linha.strip('\n'))
        arquivo.close()
        automato = ','.join(automato).strip().split('#')
        estados = []
        estado_inicial = []
        estados_aceitacao = []
        alfabeto = []
        transicoes = []
        for i in range(len(automato)):
            if 'states' in automato[i]:
                estados = automato[i].split(',')
                estados.remove('states')
                if '' in estados:
                    estados.remove('')
            if 'initial' in automato[i]:
                estado_inicial = automato[i].split(',')
                estado_inicial.remove('initial')
                if '' in estados:
                    estados.remove('')
            if 'accepting' in automato[i]:
                estados_aceitacao = automato[i].split(',')
                estados_aceitacao.remove('accepting')
                if '' in estados:
                    estados.remove('')
            if 'alphabet' in automato[i]:
                alfabeto = automato[i].split(',')
                alfabeto.remove('alphabet')
                if '' in estados:
                    estados.remove('')
            if 'transitions' in automato[i]:
                transicoes = automato[i].split(',')
                transicoes.remove('transitions')
                if '' in estados:
                    estados.remove('')
        print(f'Estados: {estados}')
        print(f'Estado inicial: {estado_inicial}')
        print(f'Estados de aceitação: {estados_aceitacao}')
        print(f'Alfabeto: {alfabeto}')
        print(f'Transições: {transicoes}')
        # return automato


# teste
#teste_leitura3('automatos/DFA1.txt') FUNCIONANDO