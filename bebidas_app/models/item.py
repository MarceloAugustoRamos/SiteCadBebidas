# models/item.py

class Item:
    def __init__(self, nome, preco, categoria):
        # atributos públicos compatíveis com código anterior
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

    # métodos compatíveis com templates antigos
    def get_nome(self):
        return self.nome

    def get_categoria(self):
        return self.categoria

    def set_nome(self, novo_nome):
        self.nome = novo_nome

    def set_categoria(self, nova_categoria):
        self.categoria = nova_categoria

    # mantém propriedade preco caso alguém use .preco diretamente
    # (não há necessidade de property aqui, mas você pode adicionar se quiser)
