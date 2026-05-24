# EX-05 | Sistema de Gestão de Elenco e Booking Artístico
## CINEL — Centro de Formação Profissional da Indústria Eletrónica, Energia, Telecomunicações e Tecnologias da Informação

## Identificação
**Curso:** Técnico Especialista em Tecnologias e Programação de Sistemas de Informação
**Turma:** CET.TPSI.D.P.32
**Unidade de Competência:** UC00620 — Desenvolver Aplicações em C#
**Formador:** Cristiano Rocha Ferreira
**Formando:** Fernando Cesar Ferreira Farias - Nº 40953.

# 1. Introdução
## Objetivo do Projeto
Desenvolver uma aplicação desktop em C# utilizando Windows Forms integrada com uma base de dados relacional MySQL para gerir o elenco e reservas (booking) de artistas.

## Funcionalidades previstas
- Inserir, editar, eliminar e listar artistas.
- Associar categorias dinâmicas aos artistas.
- Carregar, visualizar e associar fotografias aos registos.
- Validação de campos obrigatórios e integridade dos dados.

## Tecnologias utilizadas
- C# (.NET Framework 4.8)
- Windows Forms
- MySQL (Driver MySql.Data)
- System.IO (Manipulação de ficheiros de imagem)

# 2. Base de Dados
A base de dados `booking_artistico` foi desenhada respeitando o limite máximo de 4 campos por tabela.
- **categoria**: id_categoria (PK), nome_categoria.
- **artista**: id_artista (PK), nome_artistico, caminho_foto, fk_categoria (FK).
- **contrato**: id_contrato (PK), data_evento, cachet_euro, fk_artista (FK).

# 3. Layout da Aplicação
A interface adota a proporção 4:3 (1024x768 píxeis), estruturada de forma a garantir uma usabilidade fluida, dividindo-se em duas secções operacionais.

## Componentes principais utilizados
- **Form1**: Contentor principal centralizado no ecrã.
- **GroupBox**: Utilizados para segmentar logicamente os "Dados do Artista" e a "Fotografia do Artista".
- **txtNomeArtistico & cmbCategoria**: Elementos de recolha de dados controlados.
- **picFotografia**: Visualizador com redimensionamento automático em modo Zoom.
- **dgvArtistas**: Grelha configurada para exibição tabular com seleção de linha completa (`FullRowSelect`).

# 4. Conectividade e Operações de Leitura (Commit 3)
## 4.1 Ligação ao Motor MySQL
A integração com o servidor de base de dados relacional foi concebida por intermédio da biblioteca `MySql.Data`. A string de ligação centraliza as credenciais de acesso locais e o esquema do projeto.

## 4.2 Alimentação de Controlos Gráficos
- **cmbCategoria**: Preenchida por consulta direta à tabela `categoria`, mapeando o par chave-valor com o identificador numérico.
- **dgvArtistas**: Executa uma junção relacional `INNER JOIN` para unificar os registos de artistas às suas devidas categorias nominais, listando o conteúdo de forma transparente em ambiente tabular.

## 4.2 Manipulação de Ficheiros de Imagem
### Objetivo
Dar cumprimento ao requisito de trabalho com fotografias, permitindo carregamento local e previsualização em tempo real.
### Componentes utilizados
- OpenFileDialog
- picFotografia (PictureBox)
### Desenvolvimento
O método `OpenFileDialog` filtra formatos gráficos comuns. O caminho absoluto do ficheiro selecionado é armazenado temporariamente para persistência posterior na base de dados.
