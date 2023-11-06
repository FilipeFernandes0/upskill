

create table campeonato
(IdCampeonato int not null,
Ano int not null,
nome Varchar(60),
patrocinador Varchar(60),
constraint campeonato_pk primary key(IdCampeonato,Ano)
);

create table jornada
(IdJornada int not null primary key,
descricao Varchar(60),
IdCampeonato int not null,
Ano int not null,
constraint jornada_idCampeonato foreign key (IdCampeonato,Ano) references campeonato(IdCampeonato,Ano));


create table jogo
(IdJogo int not null primary key,
IdJornada int not null,
constraint jogo_jornada_fk foreign key(IdJornada) references jornada(IdJornada));

create table equipa
(IdEquipa int not null primary key,
nmEquipa Varchar(60),
esEquipa varchar(100),
sbEquipa varchar(100),
IdCampeonato int not null, 
Ano int not null,
constraint equipa_campeonato_fk foreign key (IdCampeonato,Ano) references campeonato(IdCampeonato,Ano));

create table jogo_equipa
(refIdJogo int not null,
refIdEquipa int not null,
constraint jogo_equipa_pk primary key (refIdJogo, refIdEquipa),
constraint fk_jogo foreign key (refIdJogo) references jogo(IdJogo),
constraint fk_equipa foreign key (refIdEquipa) references equipa(IdEquipa)
);

create table pessoa
(IdPessoa int not null primary key,
nome varchar(100),
);

create table arbitro
(IdArbitro int not null primary key,
IdPessoa int not null,
nomeArbitro varchar(100),
constraint pessoa_arbitro_fk foreign key(IdPessoa) references pessoa(IdPessoa)
);

create table jogador
(IdJogador int not null primary key,
nome_jogador varchar(100),
posicao varchar(150),
nm_camisola int not null,
IdPessoa int not null,
constraint pessoa_jogador_fk foreign key(IdPessoa) references pessoa(IdPessoa),
);

create table tipoarbitro
(IdTipoArbitro int not null primary key,
descricao varchar(100),
);

create table jogo_arbitro
(IdJogo int not null,
IdArbitro int not null,
IdTipoArbitro int not null,
constraint jogo_arbitro_pk primary key (IdJogo,IdArbitro),
constraint jogo_arbitro_idjogo_fk foreign key(IdJogo) references jogo(IdJogo),
constraint jogo_arbitro_idarbitro_fk foreign key(IdArbitro) references arbitro(Idarbitro),
constraint jogo_arbitro_tipoarbitro_fk foreign key(IdTipoArbitro) references tipoarbitro(IdTipoArbitro));

create table jogo_jogador
(IdJogo int not null,
IdJogador int not null,
titular bit not null,
tempoEntrada int,
tempoSaida int,
constraint jogo_jogador_pk primary key(IdJogo,IdJogador),
constraint jogo_jogador_idJogo_fk foreign key(IdJogo) references jogo (IdJogo),
constraint jogo_jogador_idJogador_fk foreign key(IdJogador) references jogador (IdJogador));

create table  tipo_evento(
	IdTipoEvento INT NOT NULL PRIMARY KEY,
	Descricao VARCHAR(80) NOT NULL);


create table evento(
IdEvento int not null primary key,
IdTipoEvento int not null,
IdJogo int not null,
IdJogador int not null,
descricao text,
tempo int not null
constraint jogo_evento_fk foreign key(IdJogo) references jogo(IdJogo),
constraint jogador_evento_fk foreign key(IdJogador) references jogador(IdJogador),
constraint evento_fk foreign key (IdTipoEvento) references tipo_evento(IdTipoEvento));


insert into campeonato(IdCampeonato, Ano, nome,patrocinador)
values(1,2023,'1 divisao','betclic')

insert into jornada(IdJornada,descricao,IdCampeonato,Ano)
values(1,'equipas para disputar',1,2023)

insert into jogo(IdJogo,IdJornada)
values(1,1)
 
insert into equipa(IdEquipa, nmEquipa ,esEquipa,sbEquipa,IdCampeonato,Ano)
values(1,'benfica','estadio da luz','aguia',1,2023),
	  (2,'porto','estadio do dragao','dragao',1,2023);


insert into jogo_equipa(refIdJogo,refIdEquipa)
values(1,1),
	  (1,2);

insert into pessoa(IdPessoa,nome)
values(1,'filipe'),
	(2,'diogo'),
	(3,'uira'),
	(4,'bruno'),
	(5,'ronaldo'),
	(6,'messi'),
	(7,'neymar'),
	(8,'rivaldo'),
	(9,'bernardo'),
	(10,'bruno'),
	(11,'rafael'),
	(12,'pedro'),
	(13,'joao'),
	(14,'alex'),
	(15,'mbappe'),
	(16,'halland'),
	(17,'kevin'),
	(18,'saka'),
	(19,'gabriel'),
	(20,'martinelli'),
	(21,'rice'),
	(22,'lukaku'),
	(23,'carlos')

insert into arbitro(IdArbitro,IdPessoa,nomeArbitro)
values(1,23,'carlos')

insert into jogador(IdJogador,IdPessoa,nome_jogador,nm_camisola,posicao)
values(1,1,'filipe',45,'st'),
		(2,2,'diogo',12,'dc'),
		(3,3,'uira',1,'gk'),
		(4,4,'bruno',2,'dc'),
		(5,5,'ronaldo',7,'lw'),
		(6,6,'messi',10,'cf'),
		(7,7,'neymar',11,'cam'),
		(8,8,'rivaldo',9,'st'),
		(9,9,'bernardo',14,'cm'),
		(10,10,'bruno',21,'cm'),
		(11,11,'rafael',24,'cdm'),
		(12,12,'pedro',3,'lb'),
		(13,13,'joao',99,'rb'),
		(14,14,'alex',29,'lb'),
		(15,15,'mbappe',29,'lw'),
		(16,16,'halland',9,'dc'),
		(17,17,'kevin',15,'dc'),
		(18,18,'saka',8,'rw'),
		(19,19,'gabriel',37,'cam'),
		(20,20,'martinelli',67,'gk'),
		(21,21,'rice',20,'cdm'),
		(22,22,'lukaku',85,'lb')


insert into tipoarbitro(IdTipoArbitro,descricao)
values(1,'titular')

insert into jogo_arbitro(IdArbitro,IdJogo,IdTipoArbitro)
values(1,1,1)

insert into jogo_jogador(IdJogador,IdJogo,titular,tempoEntrada,tempoSaida)
values (1,1,'True',0,90),
		(2,1,'True',0,90),
		(3,1,'True',0,90),
		(4,1,'True',0,90),
		(5,1,'True',0,90),
		(6,1,'True',0,90),
		(7,1,'True',0,90),
		(8,1,'True',0,90),
		(9,1,'True',0,90),
		(10,1,'True',0,90),
		(11,1,'True',0,90),
		(12,1,'True',0,90),
		(13,1,'True',0,90),
		(15,1,'True',0,90),
		(16,1,'True',0,90),
		(17,1,'True',0,90),
		(18,1,'True',0,90),
		(19,1,'True',0,90),
		(20,1,'True',0,90),
		(21,1,'True',0,90),
		(22,1,'True',0,90)

insert into tipo_evento(IdTipoEvento,Descricao)
values(1,'expulsao neymar'),
		(2,'golo uira'),
		(3,'assistencia bruno'),
		(4, 'fora de jogo diogo')

insert into evento(IdEvento,IdJogador,IdJogo,IdTipoEvento,descricao,tempo)
values(1,7,1,1,'expulsao', 45),
	(2,3,1,2,'golo', 90),
	(3,7,1,3,'assistencia', 90),
(	4,7,1,4,'fora de jogo',87)


SELECT * FROM jogo_jogador;
