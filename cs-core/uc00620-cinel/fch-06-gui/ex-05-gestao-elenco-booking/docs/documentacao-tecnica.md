# EX-05 | Sistema de Gestão de Elenco e Booking Artístico

## CINEL — Centro de Formação Profissional da Indústria Eletrónica, Energia, Telecomunicações e Tecnologias da Informação

## Identificação

**Curso:** Técnico Especialista em Tecnologias e Programação de Sistemas de Informação
**Turma:** CET.TPSI.D.P.32
**Unidade de Competência:** UC00620 — Desenvolver Aplicações em C#
**Formador:** Cristiano Rocha Ferreira
**Formando:** Fernando Cesar Ferreira Farias - Nº 40953

# 1. Introdução

## Objetivo do Projeto

Desenvolver uma aplicação desktop em C# utilizando Windows Forms integrada com uma base de dados relacional MySQL para a gestão eficiente de elencos e agendamentos (bookings) artísticos.

## Funcionalidades previstas

- Inserir, editar, eliminar e consultar registos de artistas.
- Associar categorias profissionais a cada artista.
- Registar contratos de eventos com validação de valores monetários.
- Carregar, visualizar e associar fotografias aos perfis dos artistas.

## Tecnologias utilizadas

- C# (.NET Framework / .NET Core Windows Forms)
- MySQL Server (Base de dados relacional)
- MySql.Data (Driver de ligação ADO.NET)
- System.IO (Manipulação e armazenamento local de fotografias)

# 2. Arquitetura da Base de Dados

A base de dados foi normalizada de modo a respeitar as restrição, garantindo a integridade referencial através de chaves estrangeiras.

## Estrutura das Tabelas

- **categoria**: Identificador e nome da especialidade artística (Ex: Ator, Cantor).
- **artista**: Dados do profissional, ligação à categoria e referência ao ficheiro de imagem.
- **contrato**: Agendamento de eventos, data do espetáculo, valor do cachet e ligação ao artista.
