-- 1. Criação da Base de Dados
CREATE DATABASE booking_artistico;
USE booking_artistico;

-- 2. Tabela Categoria (Max 4 campos)
CREATE TABLE categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome_categoria VARCHAR(50) NOT NULL UNIQUE
);

-- 3. Tabela Artista (Max 4 campos)
CREATE TABLE artista (
    id_artista INT AUTO_INCREMENT PRIMARY KEY,
    nome_artistico VARCHAR(100) NOT NULL,
    caminho_foto VARCHAR(255) NOT NULL,
    fk_categoria INT,
    FOREIGN KEY (fk_categoria) REFERENCES categoria(id_categoria) ON DELETE SET NULL
);

-- 4. Tabela Contrato (Max 4 campos)
CREATE TABLE contrato (
    id_contrato INT AUTO_INCREMENT PRIMARY KEY,
    data_evento DATE NOT NULL,
    cachet_euro DECIMAL(10,2) NOT NULL,
    fk_artista INT,
    FOREIGN KEY (fk_artista) REFERENCES artista(id_artista) ON DELETE CASCADE
);
