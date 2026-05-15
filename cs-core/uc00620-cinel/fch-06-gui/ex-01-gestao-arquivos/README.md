# 📁 Gestão de Arquivos — Windows Forms App

Aplicação desktop desenvolvida em C# utilizando Windows Forms.

O projeto foi criado com objetivo de praticar:

- manipulação de ficheiros
- organização de interface gráfica
- tratamento de exceções
- validações
- estruturação de código
- documentação técnica

---

# 🚀 Funcionalidades

✔ Listar arquivos de um diretório  
✔ Copiar arquivos  
✔ Mover arquivos  
✔ Excluir arquivos  
✔ Seleção visual de ações  
✔ Atualização automática da lista  
✔ Validação de diretórios  
✔ Prevenção de duplicação de ficheiros  
✔ Mensagens padronizadas  
✔ Tratamento de exceções com try/catch

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

- ListView com:
  - nome
  - tipo
  - tamanho do ficheiro

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

## Métodos Auxiliares

- ResetarBotoesAcao
- MostrarAviso
- MostrarErro
- MostrarSucesso

---

# 🛠️ Tecnologias Utilizadas

- C#
- Windows Forms
- .NET
- FontAwesome.Sharp

---

# 📚 Aprendizados

Durante o desenvolvimento foram praticados:

- eventos
- métodos
- manipulação de caminhos
- File.Copy()
- File.Move()
- File.Delete()
- Directory.GetFiles()
- FileInfo
- ListView
- validações preventivas
- tratamento de exceções
- organização e refatoração de código

---

# 📖 Documentação Técnica

O projeto possui documentação técnica manuscrita contendo:

- análise da interface
- fluxo lógico
- implementação
- testes realizados
- problemas encontrados
- refatoração
- validações
- melhorias aplicadas

---

# 👨‍💻 Autor

Fernando Cesar Ferreira Farias  
CINEL — CET.TPSI.N32
