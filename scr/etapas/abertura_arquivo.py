import re


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


        transicoes_formatadas = []
        for transicao in conteudos[-1]:
            if len(re.split('[:>]', transicao.strip())[1]) > 1 and \
                    len(re.split('[:>]', transicao.strip())[-1]) > 2:
                for caracter in re.split('[:>]', transicao.strip())[1]:
                    for estado in re.split('[,]', re.split('[:>]', transicao.strip())[-1]):
                        if caracter != ',':
                            transicoes_formatadas.append(transicao.strip()[0:2] + ':' + caracter + '>' + estado)

            elif len(re.split('[:>]', transicao.strip())[1]) > 1:
                for caracter in re.split('[:>]', transicao.strip())[1]:
                    if caracter != ',':
                        transicoes_formatadas.append(transicao.strip()[0:2] + ':' + caracter + '>' + transicao.strip()[-2:])

            elif len(re.split('[:>]', transicao.strip())[-1]) > 2:
                for estado in re.split('[,]', re.split('[:>]', transicao.strip())[-1]):
                    if estado != ',':
                        transicoes_formatadas.append(transicao.strip()[0:2] + ':' + transicao[3] + '>' + estado)
            else:
                transicoes_formatadas.append(transicao.strip())

    conteudos[-1] = transicoes_formatadas

    automato['estados'], \
    automato['estado_inicial'], \
    automato['estados_aceitacao'], \
    automato['alfabeto'], \
    automato['transicoes'] = conteudos

    return automato