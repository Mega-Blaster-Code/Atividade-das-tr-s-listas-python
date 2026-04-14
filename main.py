from flask import Flask, render_template, request

app = Flask(__name__)

# ============================================
# ARMAZENAMENTO DE DADOS (EM MEMÓRIA)
# ============================================
lista_ordenada = []
conjunto = set()

# ============================================
# FUNÇÕES PARA ADICIONAR ITENS NAS LISTAS
# ============================================
def adicionar_item_lista_ordenada(item):
    """Adiciona um item na lista ordenada"""
    if item and item.strip():
        lista_ordenada.append(item.strip())
        return True
    return False


def adicionar_item_conjunto(item):
    """Adiciona um item na lista de tarefas"""
    if item and item.strip():
        conjunto.add(item)
        return True
    return False


# ============================================
# ROTAS (PÁGINA INICIAL E CSS)
# ============================================
@app.route("/", methods=["GET"])
def main():
    """Rota para a página inicial"""
    print("INDEX HTML")
    return render_template("index.html")


@app.route("/css.css")
def main_css():
    """Rota para o arquivo CSS"""
    print("CSS")
    return render_template("css.css")


# ============================================
# ROTAS PARA AS LISTAS
# ============================================
@app.route("/lista", methods=["GET", "POST"])
def principal():
    """Rota para Lista Ordenada"""
    print("LISTA ORDENADA")
    if request.method == "POST":
        itemlo = request.form.get("itemlo")
        adicionar_item_lista_ordenada(itemlo)
    return render_template("lista_ordenada.html", lista_ordenada=lista_ordenada)


@app.route("/conjuntos", methods=["GET", "POST"])
def tarefas():
    """Rota para Lista Conjuntos"""
    print("LISTA CONJUNTOS")
    if request.method == "POST":
        item = request.form.get("item_conjunto")
        adicionar_item_conjunto(item)
    return render_template("lista_conjuntos.html", conjunto=conjunto)





# ============================================
# NÂO MEXER JAMAIS 
# ============================================

if __name__ == "__main__":
    app.run(debug=True)

# ============================================
# NÂO MEXER JAMAIS 
# ============================================