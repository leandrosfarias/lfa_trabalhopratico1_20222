import re

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
        cont_vazio = 0
        cont_ndeterminismo = 0
        for transicao in self.matriz_transicoes:
            if '$' in transicao:
                cont_vazio+=1
            for transicao_ in self.matriz_transicoes:
                if transicao != transicao_ and transicao[0] == transicao_[0] and \
                        transicao[1] == transicao_[1] and transicao[2] != transicao_[2]:
                    cont_ndeterminismo+=1
        if cont_vazio > 1:
            return "Não Deterministico com Transições Vazias"
        elif cont_ndeterminismo > 1 :
            return "Não Deterministico"
        else:
            return "Deterministico"

    def transicao(self, estado_origem, simbolo):
        for transicao in self.matriz_transicoes:
            if estado_origem in transicao[0] and simbolo in transicao[1]:
                return transicao[2]

    def analise_palavra(self, palavra):
        if self.estado_inicial in self.estados_aceitacao and len(palavra) == 0:
            return print("A palavra processada pelo automato foi: Aceita!")
        estado_atual = self.estado_inicial[0]
        for simbolo in palavra:
            estado_atual = self.transicao(estado_atual, simbolo)
        if estado_atual in self.estados_aceitacao:
            return print("A palavra processada pelo automato foi: Aceita!")
        else:
            return print("A palavra processada pelo automato foi: Rejeitada!")

    def estrutura(self):
        print(f'''
      Estados: {self.estados}
      Estado Inicial: {self.estado_inicial}
      Estados de Aceitação: {self.estados_aceitacao}
      Alfabeto: {self.alfabeto}
      Transições: {self.transicoes}
      Matriz de Transições: {self.matriz_transicoes}
      ''')
