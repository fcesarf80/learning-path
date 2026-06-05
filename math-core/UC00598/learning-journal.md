# Learning Journal

## 2026-06-04

### Descoberta importante

Durante o estudo de tabelas verdade percebi que as linhas não são decoradas.

Elas são geradas pela contagem binária.

Exemplo para 3 variáveis:

000
001
010
011
100
101
110
111

A partir dessa percepção ficou mais claro entender:

- por que 3 variáveis geram 8 linhas;
- por que 4 variáveis geram 16 linhas;
- por que a última variável alterna entre 0 e 1 a cada linha;
- a relação entre Sistemas de Numeração e Circuitos Lógicos.

Essa foi a descoberta que começou a destravar meu entendimento sobre tabelas verdade.

## 2026-06-05

### Correção importante

Durante a resolução da expressão:

(A OR B) AND C

cometi um erro ao considerar:

0 AND 0 = 1

Após revisão, reforcei a regra fundamental da porta AND:

A saída só é 1 quando todas as entradas são 1.

Tabela:

0 AND 0 = 0
0 AND 1 = 0
1 AND 0 = 0
1 AND 1 = 1

Percebi que o erro não estava na expressão composta, mas na aplicação da operação AND dentro da resolução.

## 2026-06-06

### Aprendizagem importante

Durante a resolução de tabelas verdade percebi que alguns erros não aconteciam por falta de conhecimento das portas lógicas, mas por tentar resolver expressões diretamente sem criar colunas intermediárias.

Ao utilizar colunas auxiliares para cada etapa da expressão, os resultados tornaram-se muito mais consistentes e fáceis de verificar.

Conclusão:

Quando a expressão lógica possui mais de uma operação, devo resolver uma etapa de cada vez e registrar os resultados intermediários em colunas próprias.

O processo é mais importante do que tentar fazer tudo mentalmente.

# Learning Journal

## 2026-06-06

### Tema

Tabelas Verdade e Expressões Lógicas Compostas

---

### Conhecimentos Consolidados

#### Construção de Tabelas Verdade

Compreendi que as linhas da tabela verdade são geradas pela contagem binária.

Exemplo para três variáveis:

000
001
010
011
100
101
110
111

Quantidade de linhas:

- 2 variáveis → 2² = 4 linhas
- 3 variáveis → 2³ = 8 linhas
- 4 variáveis → 2⁴ = 16 linhas
- 5 variáveis → 2⁵ = 32 linhas

---

#### Portas Lógicas

Reforcei o funcionamento das seguintes portas:

- NOT
- AND
- OR
- NAND
- NOR
- XOR
- XNOR

Observações importantes:

AND → só produz 1 quando todas as entradas são 1.

OR → produz 1 quando existe pelo menos uma entrada igual a 1.

XOR → produz 1 quando as entradas são diferentes.

XNOR → produz 1 quando as entradas são iguais.

---

### Descoberta Importante

Percebi que vários erros não aconteciam por desconhecimento das portas lógicas, mas por tentar resolver expressões diretamente sem utilizar colunas intermediárias.

Exemplo:

(A OR B) XOR C

Quando tentei resolver mentalmente algumas linhas, ocorreram erros de preenchimento.

Ao criar a coluna auxiliar:

A OR B

e só depois calcular:

(A OR B) XOR C

a resolução tornou-se muito mais simples e consistente.

---

### Conclusão Pessoal

O problema não estava na lógica nem nas portas.

O problema estava em tentar pular etapas.

Aprendi que expressões compostas devem ser resolvidas em etapas, utilizando colunas auxiliares para registrar os resultados intermediários.

Quando o problema fica maior, devo confiar no processo e não apenas na memória.

---

### Expressões Resolvidas com Sucesso

- (A OR B) AND C
- (A AND B) OR C
- (A XOR B) AND C
- (A AND B) XOR C
- NOT(A) AND B
- A OR NOT(B)

---

### Situação Atual

Sinto que o bloqueio inicial com tabelas verdade foi superado.

Já consigo:

- montar tabelas de 2 e 3 variáveis;
- criar colunas intermediárias;
- resolver expressões compostas;
- utilizar operadores NOT, AND, OR e XOR dentro de tabelas verdade.

Próximo passo: continuar praticando expressões com NOT e avançar gradualmente para Álgebra Booleana.
