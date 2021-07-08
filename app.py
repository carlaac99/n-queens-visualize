from flask import Flask,render_template
from nQueen import *
app= Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)

@app.route("/")
def index():
    #main render
    print('index test')
    return render_template("chessboard.html")