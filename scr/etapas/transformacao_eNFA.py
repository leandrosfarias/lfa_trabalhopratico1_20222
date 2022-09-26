from scr.modelo.Automato import Automato


def e_fechamento(automato, estado):
    alcanca = [estado]
    for transicao in automato.matriz_transicoes:
        if estado == transicao[0] and "$" in transicao[1]:
            alcanca.append(transicao[2])
            estado_aux = transicao[2]

            for transicao_ in automato.matriz_transicoes:
                if estado_aux == transicao_[0] and "$" in transicao_[1]:
                    if transicao_[2] not in alcanca:
                        alcanca.append(transicao_[2])
                        estado_aux = transicao_[2]

    return alcanca


def tabela_transicao_e(automato, tabela, conjunto):
    if len(tabela) == 0:

        for s in automato.alfabeto:
            tabela[(tuple(conjunto), s)] = []

            for t in automato.matriz_transicoes:
                for estado in range(len(tuple(conjunto))):

                    for estado_alcancado in e_fechamento(automato, tuple(conjunto)[estado]):
                        if estado_alcancado not in tabela[(tuple(conjunto), s)]:
                            tabela[(tuple(conjunto), s)].append(estado_alcancado)

                            if tuple(conjunto)[estado] in t[0] and s in t[1]:
                                if tuple(conjunto) not in tabela[(tuple(conjunto), s)]:
                                    tabela[(tuple(conjunto), s)].append(t[-1])

        for conjunto_ in tabela.values():
            if "".join(conjunto_) not in automato.estados:
                return tabela_transicao_e(automato, tabela, conjunto_)


    else:
        if "".join(conjunto) not in automato.estados:
            automato.estados.append("".join(conjunto))

            for s in automato.alfabeto:
                tabela[(tuple(conjunto), s)] = []

                for t in automato.matriz_transicoes:
                    for estado in range(len(tuple(conjunto))):

                        for estado_alcancado in e_fechamento(automato, tuple(conjunto)[estado]):
                            if estado_alcancado not in tabela[(tuple(conjunto), s)]:
                                tabela[(tuple(conjunto), s)].append(estado_alcancado)

                                if tuple(conjunto)[estado] in t[0] and s in t[1]:
                                    if tuple(conjunto) not in tabela[(tuple(conjunto), s)]:
                                        tabela[(tuple(conjunto), s)].append(t[-1])

        for conjunto_ in tabela.values():
            if "".join(conjunto_) not in automato.estados:
                return tabela_transicao_e(automato, tabela, conjunto_)

        else:
            return tabela


def transformacao_eNFA(tabela, automato):
    tabela_afd = tabela
    estados_afd = set()
    transicoes = []
    estados_aceitacao = []

    # Pegando os estados
    for linha in list(tabela.keys()):
        if len(linha[0]) > 1:
            estados_afd.add("".join(linha[0]))
        else:
            estados_afd.add(linha[0][0])

    # Pegando as transições
    for k, v in tabela.items():
        transicoes.append(f'{"".join(k[0])}:{k[1]}>{"".join(v)}')

    # Pegando os estados de aceite
    for conjunto in tabela.values():
        for estado in conjunto:
            if estado in automato.estados_aceitacao and "".join(conjunto) not in estados_aceitacao:
                estados_aceitacao.append("".join(conjunto))

    afd = Automato(
        estados=list(estados_afd),
        estado_inicial=automato.estado_inicial,
        estados_aceitacao=estados_aceitacao,
        alfabeto=automato.alfabeto,
        transicoes=transicoes,
    )
    return afd
