-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 12/05/2026 às 22:33
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `catalogo_filmesapp`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `categorias`
--

CREATE TABLE `categorias` (
  `id_categoria` int(11) NOT NULL,
  `designacao` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `categorias`
--

INSERT INTO `categorias` (`id_categoria`, `designacao`) VALUES
(1, 'Ação'),
(2, 'Comédia'),
(3, 'Drama'),
(4, 'Ficção Científica'),
(5, 'Terror');

-- --------------------------------------------------------

--
-- Estrutura para tabela `filmes`
--

CREATE TABLE `filmes` (
  `id_filmes` int(11) NOT NULL,
  `nome` varchar(80) NOT NULL,
  `realizador` varchar(50) NOT NULL,
  `duracao` smallint(6) NOT NULL,
  `ano` smallint(6) NOT NULL,
  `resumo` text NOT NULL,
  `foto` longblob NOT NULL,
  `id_categoria` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `filmes`
--

INSERT INTO `filmes` (`id_filmes`, `nome`, `realizador`, `duracao`, `ano`, `resumo`, `foto`, `id_categoria`) VALUES
(1, 'Inception', 'Christopher Nolan', 148, 2010, 'Um ladrão especializado em roubar segredos através dos sonhos recebe a missão de implantar uma ideia na mente de um empresário.', '', 4),
(2, 'The Dark Knight', 'Christopher Nolan', 152, 2008, 'Batman enfrenta o Joker, um criminoso caótico que ameaça Gotham City.', '', 1),
(3, 'Forrest Gump', 'Robert Zemeckis', 142, 1994, 'A história de um homem simples que presencia vários acontecimentos históricos dos Estados Unidos.', '', 3),
(4, 'The Hangover', 'Todd Phillips', 100, 2009, 'Três amigos acordam em Las Vegas sem memória da noite anterior e tentam encontrar o noivo desaparecido.', '', 2),
(5, 'The Conjuring', 'James Wan', 112, 2013, 'Investigadores paranormais ajudam uma família aterrorizada por uma presença demoníaca numa quinta isolada.', '', 5);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `categorias`
--
ALTER TABLE `categorias`
  ADD PRIMARY KEY (`id_categoria`);

--
-- Índices de tabela `filmes`
--
ALTER TABLE `filmes`
  ADD PRIMARY KEY (`id_filmes`),
  ADD KEY `fk_cat` (`id_categoria`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `filmes`
--
ALTER TABLE `filmes`
  MODIFY `id_filmes` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `filmes`
--
ALTER TABLE `filmes`
  ADD CONSTRAINT `fk_cat` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
