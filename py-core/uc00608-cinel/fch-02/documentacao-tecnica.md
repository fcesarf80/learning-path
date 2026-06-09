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
