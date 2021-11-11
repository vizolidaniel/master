from config import *
from modelo import Produto

@app.route("/")
def inicio():
    return 'Sistema de cadastro de produtos. '+\
        '<a href="/listar_produtos">Operação listar</a>'

@app.route("/listar_produtos")
def listar_produtos():
    # obter os produtos do cadastro
    produtos = db.session.query(Produto).all()
    # fornecer a lista de produtos para a página que exibe os produtos
    return render_template("listar-produtos.html", listagem = produtos)

app.run(debug=True)