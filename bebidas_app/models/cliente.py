class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = []

    def adicionar_venda(self, bebida):
        self.vendas.append(bebida)

clientes = []
