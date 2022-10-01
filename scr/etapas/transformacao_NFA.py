from scr.modelo.Automato import Automato


def tabela_transicao(automato, novos_estados, tabela, conjunto):

    if "".join(conjunto) not in novos_estados:
        novos_estados.append("".join(conjunto))

        for simbolo in automato.alfabeto:
            tabela[(tuple(conjunto), simbolo)] = ["vazio"]
            for estado in conjunto:
                for transicao in automato.matriz_transicoes:
                    if estado in transicao[0] and simbolo in transicao[1]:
                        if transicao[2] not in tabela[(tuple(conjunto), simbolo)]:
                            if "vazio" in tabela[(tuple(conjunto), simbolo)]:
                                tabela[(tuple(conjunto), simbolo)].remove("vazio")
                                tabela[(tuple(conjunto), simbolo)].append(transicao[2])
                            else:
                                tabela[(tuple(conjunto), simbolo)].append(transicao[2])

    for conjunto_ in tabela.values():
        if "".join(conjunto_) not in novos_estados:
            return tabela_transicao(automato, novos_estados, tabela, conjunto_)

    else:
        return tabela


def transformacao_NFA(automato, novos_estados, tabela):
    transicoes = []
    estados_aceitacao = []

    # Pegando as transições
    for k, v in tabela.items():
        transicoes.append(f'{"".join(k[0])}:{k[1]}>{"".join(v)}')

    # Pegando os estados de aceite
    for conjunto in tabela.values():
        for estado in conjunto:
            if estado in automato.estados_aceitacao and "".join(conjunto) not in estados_aceitacao:
                estados_aceitacao.append("".join(conjunto))

    afd = Automato(
        estados=novos_estados,
        estado_inicial=automato.estado_inicial,
        estados_aceitacao=estados_aceitacao,
        alfabeto=automato.alfabeto,
        transicoes=transicoes,
    )

    return afd
