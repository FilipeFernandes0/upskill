Create table alunos
(IdAluno int primary key,
nmAluno Character Varying(60),
dsEndereco Character Varying(120),
cdCurso char(6),
dtNascimento date)


Create table curso
(IdCurso int primary key,
nmcurso Character Varying(60))


Create table participacao_curso
(refIdAluno Int,
refIdCurso Int,
constraint participacao_curso_pk primary key
(refIdAluno, refIdCurso),
constraint partic_curso_curso_fk foreign key(refIdCurso) references curso
(idCurso),
constraint partic_curso_aluno_fk foreign key (refIdAluno) references Alunos
(idAluno))

