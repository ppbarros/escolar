from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'escolar'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def autentication():
    if request.method == 'POST':
        user = request.form.get('user')
        password = request.form.get('password')

        if get_idlogin(user, password):
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
