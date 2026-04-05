from flask import *

methods = ["GET", "POST"]

app = Flask(__name__)

@app.route("/css.css")
def main_css():
    print("CSS")
    return render_template("css.css")

@app.route("/", methods=methods)
def main():
    print("INDEX HTML")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)