def leitura(path):
    automato = {}

    with open(path) as arquivo:

        linhas = arquivo.readlines()

        conteudos = []
        for cabecalho in range(len(linhas)):
            if '#' in linhas[cabecalho]:
                indice_cabecalho = cabecalho
                conteudo = []
                for indice_conteudo in range(indice_cabecalho + 1, len(linhas)):
                    if '#' not in linhas[indice_conteudo]:
                        conteudo.append(linhas[indice_conteudo].strip())
                    else:
                        break
                conteudos.append(conteudo.copy())
                conteudo.clear()

    automato['estados'], automato['estado_inicial'], automato['estados_aceitacao'], automato['alfabeto'], automato[
        'transicoes'] = conteudos

    return automato