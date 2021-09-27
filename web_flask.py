from flask import Flask, redirect, url_for, render_template, request, session, jsonify, make_response
from flask_cors import CORS
import main

names = ["felix", "victor"]

joueur1 = main.Game(names[0], names)
joueur2 = main.Game(names[1], names)
changeTurn = False
orders = main.orders

app = Flask(__name__)
app.secret_key = "PaRiS"
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        user1 = request.form["name1"]
        user2 = request.form["name2"]
        session["user1"] = user1
        session["user2"] = user2
        return redirect("/game/1")
    else:
        if ("user1" in session) and (session["user1"] != '') and ("user2" in session) and (session["user2"] != ''):
            return redirect("/game/1")
        return render_template("home_page.html")

@app.route('/score', methods=('GET', 'POST'))
def score():
    if ("user1" in session) and (session["user1"] != '') and ("user2" in session) and (session["user2"] != ''):
        return render_template("score.html")
    return redirect(url_for("home"))

@app.route('/game/<pos>', defaults='', methods=['GET'])
def game(pos):
    if ("user1" in session) and (session["user1"] != '') and ("user2" in session) and (session["user2"] != ''):
        posPlayer = tuple(int(x) for x in pos)
        if orders[-1] == 'r':
            orders.append('y')
            joueur2.askPos(posPlayer)
            posDir = joueur2.checkPosition()
            if joueur2.checkWinCL() or joueur1.checkWinDiago():
                return "Joueur1 won nice job !!"
        else:
            orders.append('r')
            joueur1.askPos(posPlayer)
            posDir = joueur1.checkPosition()
            if joueur1.checkWinCL() or joueur1.checkWinDiago():
                return "Joueur2 won nice job !!"

        dic1 = joueur1.posDirPerson
        dic2 = joueur2.posDirPerson
        array = []
        for i in range(len(posDir)):
            innerArray = []
            for j in range(len(posDir[0])):
                innerArray.append(posDir[i][j])
            array.append(innerArray)
        return render_template("game.html", name1=session["user1"], name2=session["user2"], \
            posDir=array, posDir1=dic1, posDir2=dic2)
    else:
        return redirect(url_for('home'))

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop("user1", None)
    session.pop("user2", None)
    return redirect(url_for("home"))

@app.route('/json', methods=["POST", "GET"])
def json():
    j_pos = joueur1.checkPosition()
    response = {
        "possibleDir": {
            'joueur': j_pos
        }
    }
    res = make_response(jsonify(response), 200)
    return res


# @app.route('/win/<name>', methods=["GET"])
# def win(name):
#     # render_template("win.html", winner=name)
#     return "hey"

if __name__ == '__main__':
    app.run(debug=True)
