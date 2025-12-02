from flask import Blueprint, render_template, redirect, request, flash, url_for
from models.bebida import bebidas
from models.cliente import clientes, Cliente

vendas_bp = Blueprint('vendas', __name__)

@vendas_bp.route('/vendas', methods=['GET', 'POST'])
def registrar_venda():
    if request.method == 'POST':
        nome_cliente = request.form['cliente']
        indices = request.form.getlist('bebidas')

        cliente = next((c for c in clientes if c.nome == nome_cliente), None)
        if not cliente:
            cliente = Cliente(nome_cliente)
            clientes.append(cliente)

        for i in indices:
            cliente.adicionar_venda(bebidas[int(i)])

        flash("Venda registrada!", "success")
        return redirect(url_for('clientes.listar_clientes'))

    return render_template('vendas.html', bebidas=bebidas)
