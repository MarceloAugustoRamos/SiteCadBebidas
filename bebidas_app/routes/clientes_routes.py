from flask import Blueprint, render_template
from models.cliente import clientes

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/clientes')
def listar_clientes():
    return render_template('clientes.html', clientes=clientes)
