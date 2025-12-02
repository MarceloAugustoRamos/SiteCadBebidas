from flask import Flask, render_template
from routes.bebidas_routes import bebidas_bp
from routes.clientes_routes import clientes_bp
from routes.vendas_routes import vendas_bp

app = Flask(__name__)
app.secret_key = "bebidas-secret"

app.register_blueprint(bebidas_bp)
app.register_blueprint(clientes_bp)
app.register_blueprint(vendas_bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
