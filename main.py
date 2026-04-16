from flask import Flask, render_template, request

app = Flask(__name__)

lista_ordenada = []
conjunto = set()
lista_chaveada = {}

def add_array_item(item: str) -> bool:
    if item and item.strip():
        lista_ordenada.append(item.strip())
        return True
    return False

def add_item_conjunto(item: str) -> bool:
    if item and item.strip():
        conjunto.add(item)
        return True
    return False

def add_item_dictionary(key: str, item: str) -> bool:
    if item and item.strip():
        lista_chaveada[key] = item
        return True
    return False

@app.route("/", methods=["GET"])
def main():
    return render_template("index.html")

@app.route("/css.css")
def main_css():
    return render_template("css.css")

@app.route("/lista", methods=["GET", "POST"])
def filmes_a_ser_assistido():
    if request.method == "POST":
        itemlo = request.form.get("itemlo")
        add_array_item(itemlo)
    return render_template("lista_ordenada.html", lista_ordenada=lista_ordenada)

@app.route("/conjuntos", methods=["GET", "POST"])
def generos_mais_gostei():
    print("LISTA CONJUNTOS")
    if request.method == "POST":
        item = request.form.get("item_conjunto")
        add_item_conjunto(item)
    return render_template("lista_conjuntos.html", conjunto=conjunto)

@app.route("/chaveada", methods=["GET", "POST"])
def nota_filmes():
    print("LISTA CHAVEADA")
    if request.method == "POST":
        item = request.form.get("item_chaveada")
        key = request.form.get("key_chaveada")
        add_item_dictionary(key, item)
    return render_template("lista_chaveada.html", lista_chaveada=lista_chaveada)

@app.route("/assitir.jpg", methods=["GET"])
def assistir_img():
    return render_template("assistir.jpg")

@app.route("/nota.png", methods=["GET"])
def nota_img():
    return render_template("nota.png")

@app.route("/like.jpg", methods=["GET"])
def like_img():
    return render_template("like.jpg")


if __name__ == "__main__":
    app.run(debug=True)