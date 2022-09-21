from etapas import abertura_arquivo


def main():
    automato = abertura_arquivo.leitura('./testes/automatos/DFA1.txt')
    return print(automato)


if __name__ == '__main__':
    main()
