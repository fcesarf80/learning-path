# EX-01 | Gestão de Arquivos

## CINEL — Centro de Formação Profissional da Indústria Eletrónica, Energia, Telecomunicações e Tecnologias da Informação

---

## Identificação

**Curso:** Técnico Especialista em Tecnologias e Programação de Sistemas de Informação
**Turma:** CET.TPSI.D.P.32
**Unidade de Competência:** UC00620 — Desenvolver Aplicações em C#
**Formador:** Cristiano Rocha Ferreira
**Formando:** Fernando Cesar Ferreira Farias

---

# 1. Introdução

## Objetivo do Projeto

Desenvolver uma aplicação desktop em C# utilizando Windows Forms para realizar operações de manipulação de ficheiros.

## Funcionalidades previstas

- Listar ficheiros
- Copiar ficheiros
- Mover ficheiros
- Excluir ficheiros

## Tecnologias utilizadas

- C#
- Windows Forms
- FontAwesome.Sharp
- System.IO

---

# 2. Layout da Aplicação

A interface da aplicação foi dividida em três áreas principais:

- Ações
- Informações
- Resultados

## Estrutura Visual

### Área Ações

Responsável pelas operações principais da aplicação.

### Área Informações

Responsável pela seleção dos diretórios utilizados.

### Área Resultados

Responsável pela exibição dos ficheiros encontrados.

---

# 3. Estrutura da Interface

A interface da aplicação foi organizada utilizando componentes gráficos do Windows Forms.

## Componentes principais utilizados

### Form1

Janela principal da aplicação.

### GroupBox

Responsável pela separação visual das áreas da interface.

### TextBox

Utilizada para receber os caminhos dos diretórios.

### ListView

Responsável pela apresentação dos ficheiros encontrados.

### IconButton

Botões estilizados utilizando a biblioteca FontAwesome.Sharp.

---

# 4. Desenvolvimento da Interface

## Criação do Form1

Foi criada uma janela principal responsável por centralizar os componentes da aplicação.

## Organização dos GroupBox

Os GroupBox foram utilizados para organizar visualmente:

- Ações
- Informações
- Resultados

## Utilização de IconButtons

A biblioteca FontAwesome.Sharp foi utilizada para adicionar ícones vetoriais aos botões.

## Estilização da Interface

Foram aplicadas:

- cores de fundo
- alteração de fontes
- ícones personalizados
- configuração visual dos botões

## Configuração do ListView

O componente ListView foi configurado para:

- exibir dados em formato de tabela
- apresentar colunas
- mostrar linhas de grade
- permitir seleção completa da linha

---

# 5. Implementação das Funcionalidades

## 5.1 Seleção de Diretórios

### Objetivo

Permitir ao utilizador selecionar diretórios do sistema.

### Componentes utilizados

- FolderBrowserDialog
- txtCaminhoRaiz
- txtCaminhoDestino

### Desenvolvimento

Foi utilizado o componente FolderBrowserDialog para permitir a seleção gráfica dos diretórios.

O caminho selecionado é apresentado nas TextBox correspondentes.

### Resultado obtido

O utilizador consegue selecionar diretórios de origem e destino.

---

## 5.2 Listagem de Ficheiros

### Objetivo

Listar os ficheiros existentes no diretório selecionado.

### Componentes utilizados

- Directory.GetFiles()
- FileInfo
- ListView

### Desenvolvimento

Foi utilizado o método Directory.GetFiles() para obter os ficheiros do diretório selecionado.

As informações dos ficheiros são apresentadas no componente ListView.

### Resultado obtido

A aplicação apresenta:

- nome
- extensão
- tamanho

Dos ficheiros encontrados.

---

## 5.3 Seleção de Ações

### Objetivo

Permitir ao utilizador selecionar a operação desejada.

### Componentes utilizados

- btnIconMover
- btnIconCopiar
- variável acaoSelecionada

### Desenvolvimento

Foi criada uma variável responsável por armazenar a ação selecionada pelo utilizador.

A interface altera visualmente o botão selecionado através da propriedade BackColor.

### Resultado obtido

A aplicação consegue identificar a operação selecionada pelo utilizador.

---

# 6. Execução das Operações

## 6.1 Fluxo Lógico do Utilizador

Sequência de utilização da aplicação:

- selecionar ação
- selecionar diretórios
- listar arquivos
- selecionar arquivo
- executar operação

---

# 7. Observações de Teste

Durante os testes foram identificados comportamentos inesperados relacionados com:

- movimentação de múltiplos ficheiros
- duplicação de ficheiros
- atualização da ListView
- mensagens repetidas
- manutenção do estado visual dos botões

Os problemas foram analisados e corrigidos através de refatoração incremental.

---

# 8. Tratamento de Exceções

Foi utilizada a estrutura try/catch para evitar encerramentos inesperados da aplicação durante operações de ficheiros.

Exemplos tratados:

- ficheiro já existente
- diretório inválido
- ficheiro não encontrado

---

# 9. Refatoração e Organização do Código

O código foi reorganizado utilizando:

- regiões (#region)
- métodos auxiliares
- separação de responsabilidades
- padronização de mensagens

Estrutura aplicada:

## Configuração da Interface

## Eventos dos Botões

## Métodos Auxiliares

---

# 10. Melhorias de Interface e Experiência do Utilizador

Melhorias implementadas:

- atualização automática da ListView
- limpeza automática da seleção
- reset visual das ações
- mensagens padronizadas
- prevenção de duplicação
- abertura de ficheiros com duplo clique
- coluna de data de modificação

---

# 11. Encerramento do Projeto

O projeto permitiu consolidar conhecimentos fundamentais de programação desktop com C# Windows Forms.

Durante o desenvolvimento foram aplicados conceitos de:

- organização de código
- eventos
- manipulação de ficheiros
- tratamento de exceções
- refatoração
- UX
- documentação técnica

---

# 12. Melhorias Futuras

Possíveis melhorias:

- pesquisa por nome
- múltipla seleção
- barra de progresso
- histórico de operações
- tema escuro
- atalhos de teclado
- exportação de relatórios

---

# 13. Conclusão Final

O projeto serviu como laboratório de aprendizagem prática, permitindo desenvolver competências técnicas e melhorar a organização do raciocínio lógico através de desenvolvimento incremental, testes, documentação e refatoração contínua.
