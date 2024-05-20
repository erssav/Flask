from flask import Flask , render_template
import requests

app = Flask(__name__)
titol = "ciao sito"

@app.route('/')
def hello_world():
    bottoni = {
        'b1': {'v' : 'I nostri film', 'url': 'movies'},
        'b2': {'v' : 'I nostri libri', 'url': 'movies'},
        'b3': {'v' : 'La nostra musica ', 'url': 'movies'},
        'b4': {'v' : 'I nostri videogioch', 'url': 'movies'},
    }
    return render_template("home.html", titolo = "Benvenuto su Film...non solo! ", bottoni = bottoni)


@app.route('/data')
def data():
    return 'Ciao, data!'

@app.route('/movies')
def movies():
    return render_template("movies.html")

@app.route("/datisito/titolo")
def tornatitolo():
    return titol

@app.route("/api/generi")
def tornageneri():
    return ["Horror", "Fantasy", "Comedy", "Sci-Fi"]

@app.route('/movies2')
def movies2():
    response = requests.get('https://api.chucknorris.io/jokes/categories')
    print(response)
    dati = response.json()
    print(dati)
    return render_template("movies2.html", dati = dati)

if __name__ == '__main__':
    app.run(debug=True)