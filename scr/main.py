from etapas import abertura_arquivo, transformacao_NFA, transformacao_eNFA
from modelo import Automato

def main(arquivo_automato, palavra):

    conjunto = abertura_arquivo.leitura(arquivo_automato)

    automato = Automato.Automato(conjunto['estados'],
                        conjunto['estado_inicial'],
                        conjunto['estados_aceitacao'],
                        conjunto['alfabeto'],
                        conjunto['transicoes'])



    if automato.tipo() == "Deterministico":
        print(f"Esse automato é {automato.tipo()}")
        print()
        print("Estrutura do Automato:")
        automato.estrutura()
        print()
        automato.analise_palavra(palavra)



    elif automato.tipo() == "Não Deterministico":
        print(f"Esse automato é {automato.tipo()}")
        print()
        print("Tabela de Transformação")
        tabela = {}
        novos_estados = []
        tabela_afd = transformacao_NFA.tabela_transicao(automato, novos_estados, tabela, [automato.estado_inicial[0]])
        print(tabela_afd)
        print()
        print("Estrutura do automato transformado")
        afd = transformacao_NFA.transformacao_NFA(automato, novos_estados, tabela)
        print(afd.estrutura())
        print()
        afd.analise_palavra(palavra)



    elif automato.tipo() == "Não Deterministico com Transições Vazias":
        print(f"Esse automato é {automato.tipo()}")
        print()
        print("Tabela de Transformação")
        tabela = {}
        novos_estados = []
        tabela_afd = transformacao_eNFA.tabela_transicao_e(automato, novos_estados, tabela, transformacao_eNFA.e_fechamento(automato, automato.estado_inicial[0]))
        print(tabela_afd)
        print()
        print("Estrutura do automato transformado")
        afd = transformacao_eNFA.transformacao_eNFA(tabela_afd, novos_estados, automato)
        print(afd.estrutura())
        print()
        afd.analise_palavra(palavra)



if __name__ == '__main__':
    main('./testes/automatos/{nome_do_arquivo}.txt', '{palavra}')
