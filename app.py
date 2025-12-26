from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/main")
def main():
    return render_template("main.html")

@app.route("/super")
def super_page():
    return render_template("super.html")

@app.route("/suv")
def suv_page():
    return render_template("suv.html")

@app.route("/mini")
def mini_page():
    return render_template("mini.html")

@app.route("/seddan")
def seddan_page():
    return render_template("seddan.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
