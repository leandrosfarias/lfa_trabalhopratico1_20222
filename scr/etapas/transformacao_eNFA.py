def e_fechamento(automato, estado):
  alcanca = [estado]
  for transicao in automato.matriz_transicoes:
    if estado == transicao[0] and "$" in transicao[1]:
      alcanca.append(transicao[2])
      estado_aux = transicao[2]

      for transicao_ in automato.matriz_transicoes:
        if estado_aux == transicao_[0] and "$" in transicao_[1]:
          if transicao_[2] not in alcanca:
            alcanca.append(transicao_[2])
            estado_aux = transicao_[2]


  return alcanca



def transformacao_eNFA():
    pass
