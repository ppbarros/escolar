def get_idlogin(cursor, login, senha):
    cursor.execute(f'select idlogin from login where user = "{login}" and senha = "{senha}"')

    idlogin = cursor.fetchone()

    cursor.close()

    return idlogin[0]


def get_notas(cursor, idlogin):
    cursor.execute(f'select disciplinas.nome, notas.nota1, notas.nota2, notas.nota3 from disciplinas, notas where idlogin = {idlogin}')

    