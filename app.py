from flask import Flask, render_template, request, redirect
from models import db, Produto

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def home():

    busca = request.args.get("busca", "")

    if busca:
        produtos = Produto.query.filter(
            Produto.nome.contains(busca)
        ).all()
    else:
        produtos = Produto.query.all()

    total_produtos = len(produtos)

    valor_total = sum(
        produto.preco * produto.quantidade
        for produto in produtos
    )

    estoque_baixo = sum(
        1 for produto in produtos
        if produto.quantidade < 5
    )

    nomes_produtos = [produto.nome for produto in produtos]
    quantidades = [produto.quantidade for produto in produtos]

    return render_template(
        "index.html",
        produtos=produtos,
        total_produtos=total_produtos,
        valor_total=valor_total,
        estoque_baixo=estoque_baixo,
        nomes_produtos=nomes_produtos,
        quantidades=quantidades,
        busca=busca
    )


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


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):

    produto = Produto.query.get_or_404(id)

    if request.method == "POST":

        produto.nome = request.form["nome"]
        produto.preco = float(request.form["preco"])
        produto.quantidade = int(request.form["quantidade"])

        db.session.commit()

        return redirect("/")

    return render_template(
        "editar.html",
        produto=produto
    )


@app.route("/excluir/<int:id>")
def excluir(id):

    produto = Produto.query.get_or_404(id)

    db.session.delete(produto)
    db.session.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)

@app.route("/dashboard")
def dashboard():
    produtos = Produto.query.all()

    total_produtos = len(produtos)

    quantidade_total = sum(
        produto.quantidade * produto.quantidade
        for produto in produtos
    )

    valor_total = sum(
        produto.preco * produto.quantidade
        for produto in produtos
    )

    estoque_baixo = sum(
        1 for produto in produtos
        if produto.quantidade <= 5
    )

    return render_template(
        "dashboard.html",
        produtos=produtos,
        total_produtos=total_produtos,
        quantidade_total=quantidade_total,
        valor_total=valor_total,
        estoque_baixo=estoque_baixo
    )