from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.bebida import bebidas, BebidaAlcoolica, BebidaNaoAlcoolica, CATEGORIAS

bebidas_bp = Blueprint('bebidas', __name__)

# =========================
# LISTAR BEBIDAS
# =========================
@bebidas_bp.route('/bebidas')
def listar_bebidas():
    return render_template('listar.html', bebidas=bebidas)

# =========================
# CADASTRAR BEBIDA
# =========================
@bebidas_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_bebida():
    if request.method == 'POST':
        try:
            nome = request.form['nome']
            preco = float(request.form['preco'])
            categoria = request.form['categoria']
            volume = int(request.form['volume'])
            alcoolica = request.form.get('alcoolica') == 's'

            if alcoolica:
                teor = float(request.form['teor'])
                bebida = BebidaAlcoolica(nome, preco, categoria, teor, volume)
            else:
                bebida = BebidaNaoAlcoolica(nome, preco, categoria, volume)

            bebidas.append(bebida)
            flash("Bebida cadastrada com sucesso!", "success")
            return redirect(url_for('bebidas.listar_bebidas'))

        except Exception as e:
            flash(f"Erro: {e}", "danger")

    return render_template('cadastrar.html', categorias=CATEGORIAS)

# =========================
# EDITAR BEBIDA
# =========================
@bebidas_bp.route('/editar/<int:indice>', methods=['GET', 'POST'])
def editar_bebida(indice):
    try:
        bebida = bebidas[indice]
    except IndexError:
        flash("Bebida não encontrada.", "warning")
        return redirect(url_for('bebidas.listar_bebidas'))

    if request.method == 'POST':
        try:
            nome = request.form['nome']
            preco = float(request.form['preco'])
            categoria = request.form['categoria']

            bebida.set_nome(nome)
            bebida.preco = preco
            bebida.set_categoria(categoria)

            flash("Bebida atualizada com sucesso!", "success")
            return redirect(url_for('bebidas.listar_bebidas'))
        except Exception as e:
            flash(f"Erro ao editar: {e}", "danger")

    return render_template('editar.html', bebida=bebida, indice=indice, categorias=CATEGORIAS)

# =========================
# EXCLUIR BEBIDA
# =========================
@bebidas_bp.route('/excluir/<int:indice>', methods=['POST'])
def excluir_bebida(indice):
    try:
        del bebidas[indice]
        flash("Bebida excluída com sucesso!", "success")
    except IndexError:
        flash("Índice inválido.", "danger")

    return redirect(url_for('bebidas.listar_bebidas'))
