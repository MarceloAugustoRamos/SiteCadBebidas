from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "bebidas-secret"

# Tupla de categorias fixas
CATEGORIAS = ("Refrigerante", "Cerveja", "Suco", "Vodka", "Água", "Vinho", "Whisky",
              "Energético", "Gin", "Rum", "Cachaça", "Tequila", "Saquê", "Licores",
              "Coquetéis", "Sidra", "Hidromel", "Vermute", "Chá", "Espumante",
              "Shot", "Caipirinha", "Drink")

# Dados em memória
bebidas = []
clientes = []


# ===== Classe base =====
class Item:
    def __init__(self, nome, preco, categoria):
        self.__nome = nome
        self.__preco = preco
        self.__categoria = categoria

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if valor >= 0:
            self.__preco = valor
        else:
            raise ValueError("O preço não pode ser negativo.")

    def get_nome(self):
        return self.__nome

    def get_categoria(self):
        return self.__categoria

    def set_nome(self, nome):
        self.__nome = nome

    def set_categoria(self, categoria):
        if categoria in CATEGORIAS:
            self.__categoria = categoria
        else:
            raise ValueError("Categoria inválida.")


# ===== Subclasses =====
class BebidaAlcoolica(Item):
    def __init__(self, nome, preco, categoria, teor_alcoolico, volume_ml):
        super().__init__(nome, preco, categoria)
        self.teor_alcoolico = teor_alcoolico
        self.volume_ml = volume_ml


class BebidaNaoAlcoolica(Item):
    def __init__(self, nome, preco, categoria, volume_ml):
        super().__init__(nome, preco, categoria)
        self.volume_ml = volume_ml


# ===== Classe Cliente =====
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []  # lista de bebidas compradas

    def adicionar_venda(self, bebida):
        self.vendas.append(bebida)


# ===== Funções auxiliares =====
def encontrar_cliente(nome):
    for c in clientes:
        if c.nome.lower() == nome.lower():
            return c
    return None


# ===== Rotas =====
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bebidas')
def listar_bebidas():
    return render_template('listar.html', bebidas=bebidas)


@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_bebida():
    if request.method == 'POST':
        try:
            nome = request.form['nome']
            preco = float(request.form['preco'])
            categoria = request.form['categoria']
            volume = int(request.form['volume'])
            alcoolica = request.form.get('alcoolica') == 's'

            if categoria not in CATEGORIAS:
                raise ValueError("Categoria inválida.")

            if alcoolica:
                teor = float(request.form['teor'])
                bebida = BebidaAlcoolica(nome, preco, categoria, teor, volume)
            else:
                bebida = BebidaNaoAlcoolica(nome, preco, categoria, volume)

            bebidas.append(bebida)
            flash("Bebida cadastrada com sucesso!", "success")
            return redirect(url_for('listar_bebidas'))
        except Exception as e:
            flash(f"Erro: {e}", "danger")

    return render_template('cadastrar.html', categorias=CATEGORIAS)


@app.route('/editar/<int:indice>', methods=['GET', 'POST'])
def editar_bebida(indice):
    try:
        bebida = bebidas[indice]
    except IndexError:
        flash("Bebida não encontrada.", "warning")
        return redirect(url_for('listar_bebidas'))

    if request.method == 'POST':
        try:
            nome = request.form['nome']
            preco = float(request.form['preco'])
            categoria = request.form['categoria']

            bebida.set_nome(nome)
            bebida.preco = preco
            bebida.set_categoria(categoria)

            flash("Bebida atualizada com sucesso!", "success")
            return redirect(url_for('listar_bebidas'))
        except Exception as e:
            flash(f"Erro ao editar: {e}", "danger")

    return render_template('editar.html', bebida=bebida, indice=indice, categorias=CATEGORIAS)


@app.route('/excluir/<int:indice>', methods=['POST'])
def excluir_bebida(indice):
    try:
        del bebidas[indice]
        flash("Bebida excluída com sucesso!", "success")
    except IndexError:
        flash("Índice inválido.", "danger")
    return redirect(url_for('listar_bebidas'))


@app.route('/vendas', methods=['GET', 'POST'])
def registrar_venda():
    if request.method == 'POST':
        nome_cliente = request.form['cliente']
        indices = request.form.getlist('bebidas')

        cliente = encontrar_cliente(nome_cliente)
        if not cliente:
            cliente = Cliente(nome_cliente)
            clientes.append(cliente)

        for i in indices:
            try:
                cliente.adicionar_venda(bebidas[int(i)])
            except (IndexError, ValueError):
                flash("Erro ao registrar venda.", "danger")
                return redirect(url_for('registrar_venda'))

        flash("Venda registrada com sucesso!", "success")
        return redirect(url_for('listar_clientes'))

    return render_template('vendas.html', bebidas=bebidas)


@app.route('/clientes')
def listar_clientes():
    return render_template('clientes.html', clientes=clientes)


if __name__ == '__main__':
    app.run(debug=True)
