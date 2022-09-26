def tabela_transicao(automato, tabela, conjunto):
    if len(tabela) == 0:

        for s in automato.alfabeto:
            tabela[(tuple(conjunto), s)] = []
            for t in automato.matriz_transicoes:
                for estado in range(len(tuple(conjunto))):
                    if tuple(conjunto)[estado] in t[0] and s in t[1]:
                        if tuple(conjunto) not in tabela[(tuple(conjunto), s)]:
                            tabela[(tuple(conjunto), s)].append(t[-1])

        for conjunto_ in tabela.values():
            if "".join(conjunto_) not in automato.estados:
                return tabela_transicao(automato, tabela, conjunto_)

    else:
        if "".join(conjunto) not in automato.estados:
            automato.estados.append("".join(conjunto))

            for s in automato.alfabeto:
                tabela[(tuple(conjunto), s)] = []
                for t in automato.matriz_transicoes:
                    for estado in range(len(tuple(conjunto))):
                        if tuple(conjunto)[estado] in t[0] and s in t[1]:
                            if tuple(conjunto) not in tabela[(tuple(conjunto), s)]:
                                tabela[(tuple(conjunto), s)].append(t[-1])

        for conjunto_ in tabela.values():
            if "".join(conjunto_) not in automato.estados:
                return tabela_transicao(automato, tabela, conjunto_)

        else:
            return tabela



def transformacao_NFA():
    pass
