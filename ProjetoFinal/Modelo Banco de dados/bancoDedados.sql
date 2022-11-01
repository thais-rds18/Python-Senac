--
-- File generated with SQLiteStudio v3.3.3 on ter nov 1 16:26:33 2022
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: curso
CREATE TABLE curso (nome VARCHAR (80) NOT NULL, hora_total TIME NOT NULL, hora_diaria TIME NOT NULL, entrada_inicio DATE NOT NULL, entrada_fim DATE NOT NULL, CPF_professor VARCHAR (14) REFERENCES professor (cpf) NOT NULL, nomeSala VARCHAR (60) NOT NULL, polo VARCHAR (45) NOT NULL, andar INT REFERENCES salas (andar) NOT NULL);

-- Table: login
CREATE TABLE login (usuario VARCHAR (30) NOT NULL, senha VARCHAR (15) NOT NULL, idInicial INTEGER PRIMARY KEY AUTOINCREMENT);

-- Table: professor
CREATE TABLE professor (nome VARCHAR (60) NOT NULL, cpf VARCHAR (14) PRIMARY KEY NOT NULL, email VARCHAR (100) NOT NULL, telefone INT (11) NOT NULL, conhecimento VARCHAR (80));

-- Table: salas
CREATE TABLE salas (nome VARCHAR (30) NOT NULL, andar INT, polo VARCHAR (10) NOT NULL, cadeiras INT NOT NULL, computadores INT NOT NULL, televisores INT NOT NULL, tela_retratil INT NOT NULL, mesas INT NOT NULL, projetores INT NOT NULL, quadros INT NOT NULL, ar_condicionado INT NOT NULL, PRIMARY KEY (nome, andar));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
