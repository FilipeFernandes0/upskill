
CREATE TABLE Campeonato(
	IdCampeonato INT NOT NULL,
	Ano INT NOT NULL,
	Nome VARCHAR(50),
	NomePatrocinador VARCHAR(50),
	CONSTRAINT Campeonato_PK PRIMARY KEY (IdCampeonato, Ano));

 
CREATE TABLE Jornada(
	IdJornada INT NOT NULL PRIMARY KEY,
	Descricao VARCHAR(50),
	IdCampeonato INT NOT NULL,
	Ano INT NOT NULL,
	CONSTRAINT Jornada_IdCampeonato FOREIGN KEY (IdCampeonato, Ano) REFERENCES Campeonato(IdCampeonato, Ano));


CREATE TABLE Jogo(
	IdJogo INT NOT NULL PRIMARY KEY,
	IdJornada INT NOT NULL,
	CONSTRAINT Jogo_IdJornada_FK FOREIGN KEY (IdJornada) REFERENCES Jornada(IdJornada));


CREATE TABLE Equipa(
	IdEquipa INT NOT NULL PRIMARY KEY,
	NomeEquipa VARCHAR(50),
	NomeResponsavel VARCHAR(50),
	EmailResponsavel VARCHAR(50),
	Morada VARCHAR(250),
	IdCampeonato INT NOT NULL,
	Ano INT NOT NULL,
	CONSTRAINT Equipa_IdCampeonato_FK FOREIGN KEY (IdCampeonato, Ano) REFERENCES Campeonato(IdCampeonato, Ano));


CREATE TABLE Jogo_Equipa(
	refIdJogo INT NOT NULL,
	refIdEquipa INT NOT NULL,
	CONSTRAINT Jogo_Equipa_PK PRIMARY KEY (refIdJogo, refIdEquipa),
	CONSTRAINT FK_Jogo FOREIGN KEY (refIdJogo) REFERENCES Jogo(IdJogo),
	CONSTRAINT FK_Equipa FOREIGN KEY (refIdEquipa) REFERENCES Equipa(IdEquipa));



CREATE TABLE Pessoa(
	IdPessoa INT NOT NULL PRIMARY KEY,
	Nome VARCHAR(50) NOT NULL,
	Morada VARCHAR(50) NOT NULL,
	CC INT NOT NULL);


CREATE TABLE Arbitro(
	IdArbitro INT NOT NULL PRIMARY KEY,
	CodIdentificacao INT NOT NULL,
	IdPessoa INT NOT NULL,
	CONSTRAINT Arbitro_IdPessoa_FK FOREIGN KEY (IdPessoa) REFERENCES Pessoa(IdPessoa));


CREATE TABLE Jogador(
	IdJogador INT NOT NULL PRIMARY KEY,
	Posicao VARCHAR(50),
	IdPessoa INT NOT NULL,
	CONSTRAINT Jogador_IdPessoa_FK FOREIGN KEY (IdPessoa) REFERENCES Pessoa(IdPessoa));


CREATE TABLE TipoArbitro(
	IdTipoArbitro INT NOT NULL PRIMARY KEY,
	Descricao VARCHAR(50) NOT NULL);


CREATE TABLE Jogo_Arbitro(
	IdJogo INT NOT NULL,
	IdArbitro INT NOT NULL,
	IdTipoArbitro INT NOT NULL,
	CONSTRAINT Jogo_Arbitro_PK PRIMARY KEY (IdJogo, IdArbitro),
	CONSTRAINT Jogo_Arbitro_IdJogo_FK FOREIGN KEY (IdJogo) REFERENCES Jogo(IdJogo),
	CONSTRAINT Jogo_Arbitro_IdArbitro_FK FOREIGN KEY (IdArbitro) REFERENCES Arbitro(IdArbitro),
	CONSTRAINT Jogo_Arbitro_IdTipoArbitro_FK FOREIGN KEY (IdTipoArbitro) REFERENCES TipoArbitro(IdTipoArbitro));


CREATE TABLE Jogo_Jogador(
	IdJogo INT NOT NULL,
	IdJogador INT NOT NULL,
	Titular BIT NOT NULL,
	TempoEntrada INT,
	TempoSaida INT,
	CONSTRAINT Jogo_Jogador_PK PRIMARY KEY (IdJogo, IdJogador),
	CONSTRAINT Jogo_Jogador_IdJogo_FK FOREIGN KEY (IdJogo) 
		REFERENCES Jogo(IdJogo),
	CONSTRAINT Jogo_Jogador_IdJogador_FK FOREIGN KEY (IdJogador) 
		REFERENCES Jogador(IdJogador));

CREATE TABLE Contrato(
	IdEquipa INT NOT NULL,
	IdJogador INT NOT NULL,
	DataInicio SMALLDATETIME NOT NULL,
	DataFim SMALLDATETIME,
	CONSTRAINT Contrato_PK PRIMARY KEY (IdEquipa, IdJogador),
	CONSTRAINT Contrato_IdEquipa_FK FOREIGN KEY (IdEquipa) 
		REFERENCES Equipa(IdEquipa),
	CONSTRAINT Contrato_IdJogador_FK FOREIGN KEY (IdJogador) 
		REFERENCES Jogador(IdJogador));


CREATE TABLE TipoEvento(
	IdTipoEvento INT NOT NULL PRIMARY KEY,
	Descricao VARCHAR(80) NOT NULL);


CREATE TABLE Evento(
	IdEvento INT NOT NULL PRIMARY KEY,
	IdTipoEvento INT NOT NULL,
	Tempo TIME NOT NULL,
	IdJogador INT NOT NULL,
	IdJogo INT NOT NULL,
	Observacao TEXT,
	CONSTRAINT Evento_IdJogador_FK FOREIGN KEY (IdJogador)
		REFERENCES Jogador(IdJogador),
	CONSTRAINT Evento_IdJogo_FK FOREIGN KEY (IdJogo)
		REFERENCES Jogo(IdJogo),
	CONSTRAINT Evento_IdTipoEvento_FK FOREIGN KEY (IdTipoEvento)
		REFERENCES TipoEvento(IdTipoEvento));