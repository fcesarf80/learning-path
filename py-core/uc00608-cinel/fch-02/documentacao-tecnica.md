# Documentação Técnica

Curso: Técnico Especialista em Tecnologias e Programação de Sistemas de Informação
UC: 00608 - Desenvolver programas em linguagem orientada a objetos

Formador: Júlio Guilherme Moura Magalhães
Formando: Fernando Cesar Ferreira Farias (Cesar)
Projeto: ex_04_gestor_alunos.py

---

# Histórico de Desenvolvimento

## Etapa 1 - Criação da Classe Aluno

### Objetivo

Criar a classe Aluno e definir os atributos necessários para o sistema.

### Conteúdos Trabalhados

- Classes
- Objetos
- Método construtor (**init**)
- Atributos de instância

### Aprendizagem

...

---

## Etapa 1A - Expansão da Classe Aluno

### Objetivo

Expandir a modelagem da classe para incluir informações adicionais.

### Novos atributos

- numero
- sobrenome
- curso

### Aprendizagem

...

---

# Registros de Decisão de Projeto

## RDP-001 - Turma da Edna Krabappel

### Contexto

Foi necessário definir uma turma de referência para os testes do sistema.

### Decisão

Utilizar exclusivamente os alunos da turma da professora Edna Krabappel (The Simpsons).

### Justificativa

- Maior consistência nos testes.
- Dados mais interessantes que exemplos genéricos.
- Facilita validações e demonstrações.

### Impacto

Apenas os dados de teste foram alterados.
Os requisitos do enunciado permanecem inalterados.

### Estado

Aprovado.

## Etapa 2 - Criação da Lista de Alunos

### Objetivo

Criar uma lista capaz de armazenar objetos da classe Aluno e popular o sistema com dados de teste.

### Implementação

Foi criada a lista principal do sistema:

- lista_alunos

Foram adicionados 13 alunos da turma da professora Edna Krabappel.

### Conteúdos Trabalhados

- Classes
- Objetos
- Instanciação
- Listas
- Método append()
- Ciclo for

### Aprendizagem

Aprendi que listas podem armazenar objetos completos.

Cada objeto Aluno possui os seus próprios atributos e pode ser percorrido através de um ciclo for.

### Estado do Projeto

Classe Aluno concluída.

Lista principal criada.

Turma inicial carregada com sucesso.

Projeto preparado para a implementação do menu principal.

## Etapa 3 - Criação do Menu Principal

### Objetivo

Implementar a estrutura principal de navegação do sistema.

### Funcionalidades Preparadas

- Adicionar aluno
- Listar alunos
- Procurar aluno
- Ordenar por média
- Remover aluno
- Sair

### Conteúdos Trabalhados

- while True
- input()
- if / elif / else
- break

### Aprendizagem

Aprendi a criar menus interativos utilizando ciclos de repetição.

O menu permanece ativo até que o utilizador escolha a opção de saída.

### Estado do Projeto

Menu principal implementado.

Funcionalidades ainda em desenvolvimento.

## Etapa 4 - Adicionar Aluno

### Objetivo

Permitir ao utilizador inserir novos alunos no sistema.

### Implementação

Foi criada a funcionalidade de cadastro de alunos através do menu principal.

O número do aluno é gerado automaticamente com base na quantidade atual de elementos da lista.

### Conteúdos Trabalhados

- input()
- Conversão de tipos (int e float)
- Criação dinâmica de objetos
- append()
- len()

### Aprendizagem

Aprendi a recolher dados do utilizador e utilizá-los para criar novos objetos da classe Aluno.

Os novos alunos são adicionados à lista principal do sistema durante a execução do programa.

### Estado do Projeto

Adicionar aluno concluído.

## Etapa 5 - Listar Alunos

### Objetivo

Permitir visualizar todos os alunos presentes no sistema.

### Implementação

Foi criada uma rotina que percorre a lista principal utilizando um ciclo for.

Para cada objeto Aluno encontrado são apresentados:

- Número
- Nome
- Sobrenome
- Idade
- Curso
- Média

### Conteúdos Trabalhados

- for
- len()
- Listas de objetos
- Atributos de instância
- Formatação de strings

### Aprendizagem

Aprendi a percorrer listas contendo objetos e a apresentar os seus atributos ao utilizador.

Também foi implementada uma verificação para listas vazias.

### Estado do Projeto

Adicionar aluno concluído.

Listar alunos concluído.

## Etapa 6 - Procurar Aluno

### Objetivo

Permitir localizar alunos pelo nome.

### Implementação

Foi criada uma pesquisa sequencial na lista principal.

O sistema percorre todos os objetos Aluno até encontrar uma correspondência.

### Conteúdos Trabalhados

- Pesquisa em listas
- for
- if
- break
- Variáveis booleanas
- lower()

### Aprendizagem

Aprendi a percorrer uma lista de objetos e comparar atributos.

Também aprendi a utilizar uma variável booleana para indicar se um elemento foi encontrado.

### Estado do Projeto

Adicionar aluno concluído.

Listar alunos concluído.

Procurar aluno concluído.

## Etapa 7 - Ordenação por Média

### Objetivo

Listar os alunos ordenados da maior média para a menor.

### Implementação

Foi utilizada a função sorted() para gerar uma cópia ordenada da lista principal.

O atributo utilizado como critério de ordenação foi a média do aluno.

### Conteúdos Trabalhados

- sorted()
- lambda
- key
- reverse=True
- Listas de objetos

### Aprendizagem

Aprendi a ordenar objetos utilizando um atributo específico.

Também aprendi a utilizar funções lambda para definir critérios de ordenação.

### Estado do Projeto

Adicionar aluno concluído.

Listar alunos concluído.

Procurar aluno concluído.

Ordenar por média concluído.

## Etapa 8 - Remover Aluno

### Objetivo

Permitir remover alunos da lista principal.

### Implementação

Foi criada uma pesquisa por nome.

Quando o aluno é encontrado, o objeto correspondente é removido da lista utilizando o método remove().

### Conteúdos Trabalhados

- remove()
- Pesquisa em listas
- for
- if
- break
- Variáveis booleanas

### Aprendizagem

Aprendi a localizar objetos numa lista e removê-los durante a execução do programa.

Também compreendi que a remoção altera imediatamente o conteúdo da lista.

### Estado do Projeto

Todos os requisitos obrigatórios do enunciado foram concluídos.

## Extensão 1 - Média da Turma

### Objetivo

Calcular a média geral dos alunos cadastrados.

### Implementação

Foi criada uma rotina que percorre todos os alunos da lista e acumula as respetivas médias.

No final, a soma é dividida pela quantidade de alunos existentes.

### Conteúdos Trabalhados

- Acumuladores
- Operadores aritméticos
- for
- len()
- Formatação decimal

### Aprendizagem

Aprendi a utilizar uma variável acumuladora para calcular totais e médias.

Também aprendi a formatar números decimais para apresentação ao utilizador.

### Estado do Projeto

Extensão opcional concluída.

## Extensão 2 - Ordenação por Nome

### Objetivo

Permitir visualizar os alunos em ordem alfabética.

### Implementação

Foi utilizada a função sorted() com o atributo nome como chave de ordenação.

### Conteúdos Trabalhados

- sorted()
- lambda
- Ordenação de texto
- Listas de objetos

### Aprendizagem

Aprendi que a função sorted() pode ordenar tanto valores numéricos quanto texto.

Também compreendi que diferentes atributos podem ser utilizados como critério de ordenação.

### Estado do Projeto

Extensão opcional concluída.

## Extensão 3 - Melhor Aluno

### Objetivo

Identificar o aluno com a maior média.

### Implementação

Foi utilizada a função max() para localizar o objeto Aluno que possui o maior valor no atributo media.

### Conteúdos Trabalhados

- max()
- lambda
- key
- Listas de objetos

### Aprendizagem

Aprendi a localizar o maior elemento de uma coleção utilizando um atributo específico como critério.

Também compreendi a diferença entre ordenar toda a lista e obter apenas o maior elemento.

### Estado do Projeto

Extensão opcional concluída.

## Extensão 4 - Pior Aluno

### Objetivo

Identificar o aluno com a menor média.

### Implementação

Foi utilizada a função min() para localizar o objeto Aluno que possui o menor valor no atributo media.

### Conteúdos Trabalhados

- min()
- lambda
- key
- Listas de objetos

### Aprendizagem

Aprendi a localizar o menor elemento de uma coleção utilizando um atributo específico como critério.

Também compreendi a diferença entre ordenar uma lista e obter diretamente o menor elemento.

### Estado do Projeto

Extensão opcional concluída.

## Extensão 5 - Contar Alunos

### Objetivo

Mostrar a quantidade total de alunos cadastrados no sistema.

### Implementação

Foi utilizada a função len() para obter a quantidade de objetos presentes na lista principal.

### Conteúdos Trabalhados

- len()
- Listas
- Variáveis temporárias

### Aprendizagem

Aprendi a determinar rapidamente a quantidade de elementos existentes numa lista.

### Estado do Projeto

Extensão opcional concluída.

## Refatoração R1 - Função listar_alunos

### Objetivo

Separar a lógica de listagem do menu principal.

### Implementação

Foi criada a função listar_alunos() contendo toda a lógica de apresentação dos alunos.

O menu passou a chamar a função em vez de conter diretamente o código.

### Conteúdos Trabalhados

* Funções
* Organização de código
* Reutilização

### Aprendizagem

Aprendi que funções permitem encapsular responsabilidades específicas e tornar o código mais limpo e legível.

### Estado

Refatoração concluída sem alteração de comportamento.

## Refatoração R2 - Função adicionar_aluno

### Objetivo

Separar a lógica de cadastro de alunos do menu principal.

### Implementação

Foi criada a função adicionar_aluno() contendo toda a lógica de criação e inserção de novos alunos.

O menu passou a chamar a função em vez de executar diretamente o código.

### Conteúdos Trabalhados

* Funções
* Organização de código
* Encapsulamento de responsabilidades

### Aprendizagem

Aprendi a concentrar toda a lógica de cadastro numa função específica, tornando o menu mais limpo e fácil de compreender.

### Estado

Refatoração concluída sem alteração de comportamento.

## Refatoração R3 - Função procurar_aluno

### Objetivo

Separar a lógica de pesquisa de alunos do menu principal.

### Implementação

Foi criada a função procurar_aluno() contendo toda a lógica de pesquisa por nome.

### Conteúdos Trabalhados

* Funções
* Pesquisa em listas
* Organização de código

### Aprendizagem

Aprendi a encapsular funcionalidades completas em funções independentes, facilitando a manutenção e compreensão do programa.

### Estado

Refatoração concluída sem alteração de comportamento.

## Refatoração R4 - Função remover_aluno

### Objetivo

Separar a lógica de remoção de alunos do menu principal.

### Implementação

Foi criada a função remover_aluno() contendo toda a lógica de pesquisa e remoção.

### Conteúdos Trabalhados

* Funções
* Remoção em listas
* Organização de código

### Aprendizagem

Aprendi a encapsular operações de remoção em funções independentes, tornando o programa mais organizado e fácil de manter.

### Estado

Refatoração concluída sem alteração de comportamento.

## Refatoração R5 - Função ordenar_por_media

### Objetivo

Separar a lógica de ordenação por média do menu principal.

### Implementação

Foi criada a função ordenar_por_media() contendo toda a lógica de ordenação e apresentação dos alunos.

### Conteúdos Trabalhados

* Funções
* sorted()
* lambda
* Organização de código

### Aprendizagem

Aprendi a encapsular processos de ordenação em funções independentes, facilitando a reutilização e manutenção.

### Estado

Refatoração concluída sem alteração de comportamento.

## Refatoração R6 - Função media_da_turma

### Objetivo

Separar a lógica de cálculo da média da turma do menu principal.

### Implementação

Foi criada a função media_da_turma() contendo toda a lógica de cálculo e apresentação da média geral.

### Conteúdos Trabalhados

* Funções
* Acumuladores
* Organização de código

### Aprendizagem

Aprendi a encapsular cálculos em funções específicas, tornando o programa mais organizado e legível.

### Estado

Refatoração concluída sem alteração de comportamento.
