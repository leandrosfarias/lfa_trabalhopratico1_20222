from etapas import abertura_arquivo, transformacao_NFA
from modelo import Automato

def main(arquivo_automato, palavra):
    conjunto = abertura_arquivo.leitura(arquivo_automato)

    automato = Automato.Automato(conjunto['estados'],
                        conjunto['estado_inicial'],
                        conjunto['estados_aceitacao'],
                        conjunto['alfabeto'],
                        conjunto['transicoes'])


    if automato.tipo() == "Deterministico":
        return automato.analise_palavra(palavra)

    elif automato.tipo() == "Não Deterministico":
        tabela = {}
        transformacao_NFA.tabela_transicao(automato, tabela, [automato.estado_inicial[0]])
        tabela_afd = transformacao_NFA.tabela_transicao(automato, tabela, [automato.estado_inicial[0]])
        afd = transformacao_NFA.transformacao_NFA(automato, tabela)
        afd.estrutura()
        afd.analise_palavra(palavra)

    elif automato.tipo() == "Não Deterministico ":
        pass


if __name__ == '__main__':
    main('./testes/automatos/NFA.txt', '11111001')
