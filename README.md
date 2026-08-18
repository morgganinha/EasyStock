# 📦 EasyStock

Sistema de controle de estoque desenvolvido em **Python** utilizando **Flask**.

O EasyStock permite cadastrar, visualizar, editar e excluir produtos, funcionando como uma aplicação web simples de gerenciamento de estoque.

## 🚀 Tecnologias utilizadas

* 🐍 Python
* 🌐 Flask
* 🗄️ Flask-SQLAlchemy
* 💾 SQLite
* 🎨 HTML5
* 🖌️ Bootstrap

## ✨ Funcionalidades

* [x] Cadastro de produtos
* [x] Listagem de produtos
* [x] Edição de produtos
* [x] Exclusão de produtos
* [x] Pesquisa de produtos
* [ ] Dashboard de estoque
* [ ] Controle de estoque baixo
* [ ] Sistema de login
* [ ] Upload de imagens
* [ ] Publicação na internet

## 📁 Estrutura do projeto

```text
EasyStock/
│
├── static/
│
├── templates/
│   ├── index.html
│   ├── cadastrar.html
│   └── editar.html
│
├── app.py
├── models.py
├── .gitignore
├── README.md
└── venv/
```

> A pasta `venv` não deve ser enviada para o GitHub.

## ⚙️ Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/morgganinha/EasyStock.git
```

### 2. Entrar na pasta

```bash
cd EasyStock
```

### 3. Criar o ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

No Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Depois:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Instalar as dependências

```bash
pip install flask flask_sqlalchemy
```

### 6. Executar o projeto

```bash
python app.py
```

### 7. Acessar no navegador

```text
http://127.0.0.1:5000
```

## 🖥️ Funcionalidades do sistema

### Cadastro

Permite cadastrar produtos informando:

* Nome
* Preço
* Quantidade

### Edição

Permite alterar as informações de um produto já cadastrado.

### Exclusão

Permite remover produtos do estoque.

### Pesquisa

Permite localizar produtos pelo nome.

## 🎯 Objetivo do projeto

O EasyStock foi desenvolvido como projeto de estudo para praticar conceitos de **desenvolvimento backend com Python**, incluindo:

* Rotas
* CRUD
* Banco de dados
* ORM
* Templates
* Formulários
* Ambiente virtual
* Git e GitHub

## 📚 Próximas melhorias

O projeto continuará sendo desenvolvido com novas funcionalidades, incluindo:

* Dashboard
* Indicador de estoque baixo
* Autenticação de usuários
* Melhorias na interface
* Upload de imagens
* API REST
* Deploy na nuvem

## 👩‍💻 Desenvolvedora

**Morgana Bezerra**

Projeto desenvolvido para estudos e construção de portfólio em desenvolvimento backend.

---

⭐ Se este projeto foi útil para você, considere deixar uma estrela no repositório!
