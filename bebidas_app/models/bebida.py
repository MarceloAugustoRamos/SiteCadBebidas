from .item import Item

CATEGORIAS = (
    "Refrigerante", "Cerveja", "Suco", "Vodka", "Água", "Vinho", "Whisky",
    "Energético", "Gin", "Rum", "Cachaça", "Tequila", "Saquê", "Licores",
    "Coquetéis", "Sidra", "Hidromel", "Vermute", "Chá", "Espumante",
    "Shot", "Caipirinha", "Drink"
)

class BebidaAlcoolica(Item):
    def __init__(self, nome, preco, categoria, teor_alcoolico, volume_ml):
        super().__init__(nome, preco, categoria)
        self.teor_alcoolico = teor_alcoolico
        self.volume_ml = volume_ml

class BebidaNaoAlcoolica(Item):
    def __init__(self, nome, preco, categoria, volume_ml):
        super().__init__(nome, preco, categoria)
        self.volume_ml = volume_ml

bebidas = []
