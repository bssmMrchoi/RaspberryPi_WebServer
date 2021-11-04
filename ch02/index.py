from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def loginschedul():
    return render_template("login.html")

@app.route("/index")
def afterlogin():
    return render_template("index.html")

@app.route("/post", methods=['POST'])
def post():
    value = request.form['submit']
    msg = '%s 님 환영함'%value
    return msg


if __name__ == "__main__":
    app.run(host="0.0.0.0")
