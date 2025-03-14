from flask import Flask  # Importamos a classe Flask do módulo flask para criar nossa aplicação web
import sqlite3  # Importamos o módulo sqlite3 para manipulação do banco de dados SQLite

# Criamos uma instância do Flask e armazenamos na variável "app"
# O parâmetro __name__ indica que este arquivo será reconhecido como a aplicação principal
app = Flask(__name__)

# Criamos uma rota para o endpoint "/pague"
# Quando acessarmos http://127.0.0.1:5000/pague, a função abaixo será executada
@app.route("/pague")
def exiba_mensagem():
    # Retorna um texto formatado em HTML que será exibido no navegador ao acessar a rota "/pague"
    return "<h2>Pagar as pessoas, faz bem as pessoas!!!</h2>"

# Criamos outra rota para o endpoint "/devedora"
# Quando acessarmos http://127.0.0.1:5000/devedora, essa função será chamada automaticamente
@app.route("/devedora")
def mensagem_do_calote():
    # Retorna um texto formatado em HTML que será exibido no navegador ao acessar a rota "/devedora"
    return "<h3>Pessoas que não pagam, é triste viu...</h3>"

# Função para inicializar o banco de dados SQLite
# Criamos uma conexão com o banco de dados chamado 'database.db'
# Se o banco de dados ainda não existir, ele será criado automaticamente

def init_db():
    # Conectamos ao banco de dados SQLite e usamos "with" para garantir que a conexão seja fechada corretamente após a execução
    with sqlite3.connect("database.db") as conn:
        # Executamos um comando SQL para criar a tabela LIVROS, caso ela ainda não exista
        conn.execute(
            """
                CREATE TABLE IF NOT EXISTS LIVROS(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,  # Identificador único para cada livro, gerado automaticamente
                    titulo TEXT NOT NULL,  # O título do livro, armazenado como texto e obrigatório
                    categoria TEXT NOT NULL,  # A categoria do livro (exemplo: ficção, tecnologia), armazenada como texto e obrigatória
                    autor TEXT NOT NULL,  # O nome do autor do livro, armazenado como texto e obrigatório
                    imagem_url TEXT NOT NULL  # O URL da imagem da capa do livro, armazenado como texto e obrigatório
                )
            """
        )  # A execução desse comando cria a tabela caso ela ainda não exista, garantindo que nossa estrutura de banco esteja configurada

# Chamamos a função para inicializar o banco de dados quando o programa for executado
init_db()

# Aqui verificamos se o script está sendo executado diretamente e não importado como módulo
if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuração
    # O modo debug permite que mudanças no código sejam aplicadas automaticamente sem reiniciar o servidor manualmente
    app.run(debug=True)
