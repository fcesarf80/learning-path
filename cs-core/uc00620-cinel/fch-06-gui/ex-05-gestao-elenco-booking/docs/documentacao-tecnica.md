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

A base de dados foi normalizada de forma a reduzir a redundância de dados e garantir a integridade referencial através da utilização de chaves primárias e chaves estrangeiras.

## Estrutura das Tabelas

- **categoria**: Identificador e nome da especialidade artística (Ex: Ator, Cantor).
- **artista**: Dados do profissional, ligação à categoria e referência ao ficheiro de imagem.
- **booking**: Agendamento de eventos, data do espetáculo, valor do cachet e ligação ao artista.

### Tabela Categoria

Responsável pelo armazenamento das categorias artísticas disponíveis no sistema.

Campos:

- id_categoria (INT) – Identificador único da categoria.
- nome_categoria (VARCHAR(100)) – Nome da categoria artística.

Exemplos:

- Músico
- Vocalista
- Bailarina
- Ator/Atriz
- Animador(a)

### Tabela Artista

Responsável pelo armazenamento dos dados dos artistas.

Campos:

- id_artista (INT) – Identificador único do artista.
- nome_artistico (VARCHAR(100)) – Nome artístico.
- caminho_foto (VARCHAR(255)) – Caminho da fotografia armazenada localmente.
- fk_categoria (INT) – Chave estrangeira para a tabela categoria.

### Tabela Booking

Responsável pelo armazenamento dos eventos associados aos artistas.

Campos:

- id_booking (INT) – Identificador único do booking.
- nome_evento (VARCHAR(100)) – Nome do evento.
- cache (DECIMAL(10,2)) – Valor contratado.
- fk_artista (INT) – Chave estrangeira para a tabela artista.
- data_evento (DATE) – Data do evento.
- hora_evento (TIME) – Hora do evento.
- local_evento (VARCHAR(150)) – Local do evento.
- observacoes (TEXT) – Informações complementares.

Relacionamentos:

Categoria (1) → (N) Artista

Artista (1) → (N) Booking

# 3. Interface Gráfica

A interface foi desenvolvida utilizando Windows Forms.

Os principais componentes utilizados foram:

- Label: apresentação de títulos e descrições.
- TextBox: introdução de dados pelo utilizador.
- ComboBox: seleção de categorias artísticas.
- Button: execução das operações CRUD.
- DataGridView: visualização e seleção dos registos.
- PictureBox: visualização das fotografias dos artistas.
- GroupBox: organização visual dos diferentes grupos de informação.

A interface encontra-se dividida em três áreas principais:

- Dados do Artista;
- Dados do Booking;
- Lista de Artistas.

# 4. Funcionalidades Implementadas

A aplicação permite executar operações CRUD (Create, Read, Update e Delete).

## Inserção

Permite registar artistas e respetivos bookings.

## Consulta

Os dados são apresentados através de um DataGridView com atualização automática.

## Edição

Permite alterar informações dos artistas e dos eventos associados.

## Eliminação

Ao eliminar um artista, os respetivos bookings associados são removidos previamente para garantir a integridade referencial da base de dados.

## Pesquisa

Permite pesquisar artistas pelo nome artístico utilizando consultas SQL com o operador LIKE.

## Gestão de Fotografias

Permite carregar, visualizar e associar fotografias aos artistas através de um PictureBox.

# 5. Validação de Dados

Foram implementadas diversas validações para garantir a consistência da informação:

- Verificação de campos obrigatórios;
- Impedimento de registos duplicados de artistas;
- Validação de datas e horas;
- Validação de valores numéricos para o campo cache;
- Verificação da existência de fotografias associadas aos artistas quando aplicável.
