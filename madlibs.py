"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")

@app.route('/greet')
def return_compliment():

    name = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html", 
                            name=name,
                            compliments=compliments)

@app.route('/question')
def ask_question():
    """Ask if user wants to play a game."""

    player = request.args.get("person")

    return render_template("question.html",
                           person=player)

@app.route('/game')
def show_madlib_form():
    """Show whether user wants to play a game."""

    answer = request.args.get("answer")

    if answer == "yes":

        return render_template("game.html")
    
    return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():

    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjectives = request.args.getlist("adjective")

    madlib_files = ["madlib.html", "madlib2.html", "madlib3.html"]

    return render_template(choice(madlib_files), person=person, 
                                          color=color, 
                                          noun=noun,
                                          adjectives=adjectives)




if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
