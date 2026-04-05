CREATE TABLE consulta (
    id_consulta INT AUTO_INCREMENT PRIMARY KEY,
    data_consulta DATE NOT NULL,
    descricao TEXT,
    valor DECIMAL(10,2),
    id_animal INT NOT NULL,
    id_funcionario INT NOT NULL,
    FOREIGN KEY (id_animal) REFERENCES animal(id_animal)
    ON DELETE CASCADE,
    FOREIGN KEY (id_funcionario) REFERENCES funcionario(id_funcionario)
    ON DELETE CASCADE
);