# lfa_trabalhopratico1_20222
Trabalho Prático 1 da disciplina Linguagens Formais e Autômatos.

## Integrantes:
* Leandro Silva Farias
* Marcelo Augusto de Souza Cardoso
* João Victor de Almeida Pinto

## Como Testar:

- Ao baixar o projeto acesse o caminho /scr/testes/automatos, nesse diretório armazenamos automatos dos 3 tipos para teste, caso queira adicionar outro automato recomendamos deixar nesse mesmo diretório.

- Para de fato realizar os testes acesse o arquivo main.py, na chamada da função main localizada no entrypoint escreva o nome do arquivo no lugar de "{nome_do_arquivo}" e a palavra que deseja analisar no lugar de "{palavra}", em caso de mudança na localização do arquivo passe o path de acesso no primeiro parâmetro. Por fim execute o entrypoint.

- A saída esperada para DFA's é: tipo, estrutura dos conjuntos e o resultado da análise da palavra enviada.

- Para NFA's e eNFA's a saida esperada será: tipo, tabela de transformação, estrutura do DFA gerado e o resultado da análise da palavra enviada.

# OBSERVAÇÃO:

- Em nossos testes automatos com estados formados apenas com string numéricas apresentaram inconsistências por isso recomendamos o uso do padrão do simulador como por exemplo: "s0, s1, s2" ou qualquer outra letra.
