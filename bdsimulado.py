logins = {'xpto': '123', 'abc': '456', 'marcosvafg': '1234'}

disciplinas = {'xpto': [['ltp1', 5, 6.7, 7.8], ['lab prog1', 10, 8, 9.5]],
               'abc': [['ltp2', 7, 9.3, 8.3], ['lab prog2', 1, 3.6, 6.9]],
               'marcosvafg': [['aaa', 4.9, 2.3, 7.4], ['bbb', 4, 8.6, 10]]}

detalhes = {'ltp1': 'Matéria: LTP1, Professor YAG',
            'lab prog1': 'Matéria: Laboratório de Programacao, Professor CGSJ'}

def validar_login(login, senha):
    return (login in logins) and (logins[login] == senha)

def get_disciplinas(login):
    return disciplinas[login]

def get_detalhes(disciplina):
    return detalhes[disciplina]