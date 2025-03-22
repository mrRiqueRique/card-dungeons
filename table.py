from random import randint
from card import Card, full_deck


class Table:
    def __init__(self):
        self.ground: list[Card] = []
        self.deck: list[Card] = []

    def start(self):
        self.ground = []
        self.deck = temp_deck
        self.__temp_deck__: list[Card] = full_deck.copy()
        
        # Primeiro grupo de 4 cartas
        for _ in range(4):
            self.ground.append(self.deck.pop(randint(0, len(self.deck) - 1)))
        
        # Grupos subsequentes de 3 cartas
        while len(self.deck) >= 3:
            for _ in range(3):
                self.ground.append(self.deck.pop(randint(0, len(self.deck) - 1)))
    
    def draw(self):
        for i in range(3):
            self.ground.append(self.deck.pop(randint(0, len(self.deck) - 1)))
    
    def __str__(self):
        cartasMesa: str = "" 
        for card in self.ground:
            cartasMesa += f"  {card}"
        return f"""
=============== ({len(self.deck): ^2}) ================
= {cartasMesa: ^37} =
=====================================""" 

table = Table()
table.start()
print(table.deck)
for deck in table.deck:    
    print(deck)