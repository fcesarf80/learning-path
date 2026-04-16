# 📒 Agenda de Contatos (Java Swing)

## 📌 Descrição

Aplicação desktop desenvolvida em Java com Swing, que permite gerenciar uma agenda de contatos utilizando armazenamento em ficheiro de texto.

O projeto foi desenvolvido com foco na aprendizagem prática de:

* Interface gráfica (Swing)
* Manipulação de ficheiros
* Estruturação em camadas (Model, DAO, View)
* Implementação de operações CRUD

---

## 🎯 Funcionalidades

✔ Inserir novo contato
✔ Procurar contato (busca parcial)
✔ Atualizar contato
✔ Excluir contato
✔ Armazenamento em ficheiro (`contatos.txt`)

---

## 🧱 Estrutura do Projeto

```
src/
 ├── model/
 │    └── Contato.java
 │
 ├── dao/
 │    └── ContatoDAO.java
 │
 └── view/
      ├── TelaPrincipal.java
      ├── TelaNovoContato.java
      └── TelaProcurar.java
```

---

## 🧠 Arquitetura

O projeto segue uma separação em camadas:

* **Model** → representa os dados (Contato)
* **DAO** → acesso e manipulação do ficheiro
* **View** → interface gráfica com o utilizador

---

## 💾 Persistência de Dados

Os dados são guardados no ficheiro:

```
contatos.txt
```

Formato de cada linha:

```
Nome;Telefone;Email;Grupo
```

Exemplo:

```
João;912345678;joao@email.com;Amigos
```

---

## 🖥️ Interface

### Tela Principal

* Menu:

  * Ficheiro → Sair
  * Contatos → Novo
  * Procurar → Abrir tela de busca

### Tela Novo Contato

* Inserção de dados
* Botão Guardar (validação)
* Botão Cancelar (limpa campos)

### Tela Procurar

* Filtros por:

  * Nome
  * Telefone
  * Email
  * Grupo
* Busca parcial
* Permite:

  * Atualizar contato
  * Excluir contato

---

## ⚙️ Tecnologias Utilizadas

* Java
* Swing (GUI)
* IO (BufferedReader / BufferedWriter)

---

## 🚀 Como executar

1. Abrir o projeto no NetBeans
2. Executar a classe principal:

```
TelaPrincipal
```

---

## 📚 Objetivo do Projeto

Este projeto foi desenvolvido com finalidade educativa, visando consolidar conceitos fundamentais de programação orientada a objetos, manipulação de ficheiros e desenvolvimento de interfaces gráficas.

---

## 👨‍💻 Autor

Fernando Cesar (Cesar)
