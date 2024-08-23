from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route('/user/<username>')
def profile(username):
    return f'<h1>{username}</h1>'


@app.route('/number/<num>')
def odd_even_num(num):
    return f'<h1>Число {num} {"НЕчётное" if int(num) % 2 else "чётное"}</h1>'


if __name__ == '__main__':
    app.run()
