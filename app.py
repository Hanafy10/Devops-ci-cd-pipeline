from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
        <body style="background-color: #F91717FF;">
            <h1 style="color: red;">CI/CD Pipeline is Working </h1>
            <p style="font-size: 20px;">Flask app running on</p>
        </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
