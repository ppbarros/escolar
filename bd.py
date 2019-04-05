def get_idlogin(cursor, login, senha):
    cursor.execute(f'select idlogin from login where user = "{login}" and senha = "{senha}"')

    idlogin = cursor.fetchone()

    cursor.close()
    return idlogin


def get_notas(cursor, idlogin):
    cursor.execute(f'select notas.iddisciplinas, disciplinas.nome, notas.nota1, notas.nota2, notas.nota3 from notas join disciplinas on notas.iddisciplinas = disciplinas.iddisciplinas  where notas.idlogin = {idlogin};')
    disciplinas = cursor.fetchall()
    cursor.close()
    return disciplinas


def get_detalhes(cursor, disciplina):
    cursor.execute(f'select nome, descricao from disciplinas where iddisciplinas = "{disciplina}"')
    detalhe = cursor.fetchone()
    cursor.close()
    return detalhe