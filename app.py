from flask import Flask, request, url_for, render_template, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_Host'] = '54.226.240.28'
app.config['MYSQL_USER'] = 'gustavo'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'desafio4'

mysql = MySQL(app)

@app.route("/")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/quem-somos")
def quemsomos():
    return render_template("quem-somos.html")

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']
        
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contato(email, assunto, descricao) VALUES(%s, %s, %s)', (email, assunto, descricao))
        
        mysql.connection.commit()
        
        cur.close()
        
        return 'Sucesso!'
    return render_template("contato.html")   

@app.route('/users')
def users():
    cur = mysql.connection.cursor()

    users = cur.execute("SELECT * FROM contato")
    
    if users > 0:
        userDetails = cur.fetchall()

        return render_template("users.html", userDetails=userDetails)
