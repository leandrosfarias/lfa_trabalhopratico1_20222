import re


# from .abertura_arquivo import leitura

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


class Automato:
    def __init__(
            self,
            estados: list,
            estado_inicial: list,
            estados_aceitacao: list,
            alfabeto: list,
            transicoes: list
    ):
        self.estados = estados
        self.estado_inicial = estado_inicial
        self.estados_aceitacao = estados_aceitacao
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.matriz_transicoes = []
        self.set_transicoes(self.transicoes)

    def set_transicoes(self, transicoes):
        for t in transicoes:
            self.matriz_transicoes.append(re.split('[:>]', t))

    def tipo(self):
        for transicao in self.matriz_transicoes:
            for transicao_ in self.matriz_transicoes:
                if transicao != transicao_ and transicao[0] == transicao_[0] and \
                        transicao[1] == transicao_[1] and transicao[2] != transicao_[2]:
                    return print("Não Deterministico")
            if '$' in transicao:
                return print("Não Deterministico com Transição Vazia")

        return print("Deterministico")

    def transicao(self, estado_origem, simbolo):
        for transicao in self.matriz_transicoes:
            if estado_origem in transicao[0] and simbolo in transicao[1]:
                return transicao[2]

    def analise_palavra(self, palavra):
        if self.estado_inicial in self.estados_aceitacao and len(palavra) == 0:
            return True
        estado_atual = self.estado_inicial[0]
        for simbolo in palavra:
            estado_atual = self.transicao(estado_atual, simbolo)
        if estado_atual in self.estados_aceitacao:
            return print("Aceita!")
        else:
            return print("Rejeitada!")

    def __str__(self):
        print(f'''
      Estados: {self.estados}
      Estado Inicial: {self.estado_inicial}
      Estados de Aceitação: {self.estados_aceitacao}
      Alfabeto: {self.alfabeto}
      Transições: {self.transicoes}
      Matriz de Transições: {self.matriz_transicoes}
      ''')


conjunto = leitura('./automatos/DFA1.txt')

automato = Automato(conjunto['estados'],
                    conjunto['estado_inicial'],
                    conjunto['estados_aceitacao'],
                    conjunto['alfabeto'],
                    conjunto['transicoes'])
automato.__str__()
automato.analise_palavra('')
