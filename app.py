from flask import Flask, request, jsonify, send_from_directory
import mysql.connector

app = Flask(__name__)

# Conexão com o banco de dados
def get_db_connection():
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='123456789',
        database='gerenciador_livros'
    )
    return conn

# Rota para servir o HTML
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Funcionalidade 1: Adicionar Livro
@app.route('/adicionar_livro', methods=['POST'])
def adicionar_livro():
    titulo = request.json['titulo']
    autor = request.json['autor']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO livros (titulo, autor) VALUES (%s, %s)', (titulo, autor))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Livro adicionado com sucesso!'}), 201

# Funcionalidade 2: Listar Livros
@app.route('/listar_livros', methods=['GET'])
def listar_livros():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(livros), 200

if __name__ == '__main__':
    app.run(debug=True)
