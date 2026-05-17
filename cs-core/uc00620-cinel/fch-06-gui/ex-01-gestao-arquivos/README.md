# 📁 Gestão de Arquivos — Windows Forms App

Aplicação desktop desenvolvida em C# utilizando Windows Forms.

O projeto foi criado com objetivo de praticar:

- manipulação de ficheiros
- organização de interface gráfica
- tratamento de exceções
- validações
- refatoração
- experiência do utilizador (UX)
- estruturação e modularização de código
- documentação técnica

---

# 🚀 Funcionalidades

✔ Listar arquivos de um diretório
✔ Copiar arquivos
✔ Mover arquivos
✔ Excluir arquivos
✔ Abrir arquivos com duplo clique
✔ Seleção visual de ações
✔ Atualização automática da lista
✔ Limpeza automática de seleção
✔ Reset visual dos botões de ação
✔ Validação de diretórios
✔ Prevenção de duplicação de ficheiros
✔ Mensagens padronizadas
✔ Tratamento de exceções com try/catch
✔ Organização do código por regiões

---

# 🖥️ Interface

A interface foi organizada em três áreas principais:

## Ações

- mover
- copiar
- listar
- excluir

## Informações

- diretório raiz
- diretório destino

## Resultados

ListView contendo:

- nome
- tipo
- tamanho
- data de modificação

---

# 🧠 Estrutura do Código

O código foi reorganizado utilizando regiões:

## Configuração da Interface

- ConfigurarTela
- ConfigurarBotoes
- EstilizarBotaoPrincipal
- EstilizarBotaoPequeno
- ConfigurarListView

## Eventos dos Botões

- btnIconlocalizarPastaRaiz_Click
- btnIconlocalizarPastaDestino_Click
- btnIconListarArq_Click
- btnIconMover_Click
- btnIconCopiar_Click
- btnIconIniciar_Click
- btnIconExcluir_Click
- lstvResultados_DoubleClick

## Métodos Auxiliares

- ResetarBotoesAcao
- AtualizarListaArquivos
- MostrarAviso
- MostrarErro
- MostrarSucesso

---

# 🛠️ Tecnologias Utilizadas

- C#
- Windows Forms
- .NET
- FontAwesome.Sharp
- System.IO

---

# 📚 Aprendizados

Durante o desenvolvimento foram praticados:

- eventos
- métodos auxiliares
- manipulação de caminhos
- File.Copy()
- File.Move()
- File.Delete()
- Directory.GetFiles()
- FileInfo
- Path.Combine()
- ListView
- ListViewItem
- validações preventivas
- tratamento de exceções
- refatoração
- organização de código
- UX básica

---

# 📖 Documentação Técnica

O projeto possui documentação técnica manuscrita contendo:

- análise da interface
- fluxo lógico
- implementação
- testes realizados
- problemas encontrados
- validações
- tratamento de erros
- melhorias de UX
- refatoração
- organização por regiões
- melhorias futuras
- conclusão final

---

# 🎯 Objetivo Académico

Este projeto foi desenvolvido como exercício prático da unidade curricular:

UC00620 — Desenvolver Aplicações em C#

CINEL — CET.TPSI.D.P.32

---

# 👨‍💻 Autor

Fernando Cesar Ferreira Farias
CINEL — CET.TPSI.D.P.32
