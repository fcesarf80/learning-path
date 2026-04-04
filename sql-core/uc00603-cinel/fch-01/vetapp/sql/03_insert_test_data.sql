USE vetapp;

INSERT INTO cliente (nome, telefone, email)
VALUES ('Cesar', '912345678', 'cesar@email.com');

INSERT INTO animal (nome, especie, raca, sexo, data_nascimento, id_cliente)
VALUES ('Zumba', 'Cachorro', 'Bulldog Francês', 'Macho', '2020-05-10', 1);

INSERT INTO funcionario (nome, funcao, telefone, email)
VALUES ('Dr. João', 'Veterinário', '911111111', 'joao@vet.com');

INSERT INTO consulta (data_consulta, descricao, valor, id_animal, id_funcionario)
VALUES ('2026-04-05', 'Consulta de rotina', 50.00, 1, 1);

INSERT INTO fatura (data_emissao, valor_total, estado, id_cliente, id_consulta)
VALUES ('2026-04-05', 50.00, 'Paga', 1, 1);