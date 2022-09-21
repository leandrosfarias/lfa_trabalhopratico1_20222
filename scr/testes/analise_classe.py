#INCOMPLETO - Código base
#Precisa da análise da palavra
#Juntar a função ler_arquivo

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

automato = Automato(conjunto['estados'], \
                   conjunto['estado_inicial'], \
                   conjunto['estados_aceitacao'], \
                   conjunto['alfabeto'], \
                   conjunto['transicoes'])
