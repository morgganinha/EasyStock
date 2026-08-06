from flask import Flask, render_template, request, redirect
from models import db, Produto

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


    @app.route("/")
    def nome():
        produtos = Produto.query.all()
        return render_template("index.html", produtos=produtos)


@app.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form["nome"]
        preco = float(request.form["preco"])
        quantidade = int(request.form["quantidade"])

        produto = Produto(
            nome=nome,
            preco=preco,
            quantidade=quantidade
        )

        db.session.add(produto)
        db.session.commit()

        return redirect("/")

    return render_template("cadastrar.html")

@app.route("/editar/<int:id>", methods=["get", "post"])
def editar(id):

    produto = Produto.query.get_or_404(id)

    if request.method == "post":
        produto.nome = request.form["nome"]
        produto.preco = Float(request.form["preco"])
        produto.quantidade = int(request.form["quantidade" ])

        db.session.commit()

        return redirect("/")

    return render_template("editar.html", produto=produto)

@app.route("/excluir/<int:id>")
def excluir(id):
    produto = Produto.query.get_or_404(id)

    db.session.delete(produto)
    db.session.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)