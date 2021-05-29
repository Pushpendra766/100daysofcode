from flask import Flask
from random import randint
app = Flask(__name__)

rand_num = randint(0, 9)
@app.route("/")
def home_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<int:num>")
def guess_page(num):
    if num == rand_num:
        return '<h2 style="color:Green">You Found me !</h2>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
    elif num > rand_num:
        return '<h2 style="color:Green">Too high, try again!</h2>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif num < rand_num:
        return '<h2 style="color:Green">Too low, try again!</h2>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'



if __name__ == "__main__":
    app.run(debug=True)