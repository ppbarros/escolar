from flask import Flask, request, render_template
from bdsimulado import *

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def autentication():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')

        if validar_login(user, password):
            return render_template('oi.html', nome=user, disciplinas=get_disciplinas(user))
        else:
            return render_template('index.html', erro='Login/Senha Incorretos!')
    else:
        return render_template('index.html', erro='Método Incorreto. Use POST!')

@app.route('/detalhar/<disciplina>')
def detalhar(disciplina):
    return render_template('detalhes.html', disciplina=disciplina, detalhes=get_detalhes(disciplina))

if __name__ == "__main__":
    app.run(debug=True)
