from flask import Flask  # Importamos a classe Flask do módulo flask para criar nossa aplicação web

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
# Quando acessarmos http://127.0.0.1:5000/devedora, essa função será chamada
@app.route("/devedora")
def mensagem_do_calote():
    # Retorna um texto formatado em HTML que será exibido no navegador ao acessar a rota "/devedora"
    return "<h3>Pessoas que não pagam, é triste viu...</h3>"

# Aqui verificamos se o script está sendo executado diretamente e não importado como módulo
if __name__ == "__main__":
    # Inicia o servidor Flask no modo de depuração
    # O modo debug permite que mudanças no código sejam aplicadas automaticamente sem reiniciar o servidor manualmente
    app.run(debug=True)
