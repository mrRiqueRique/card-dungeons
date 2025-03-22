from random import randint

class Card:
    def __init__(self, type, value):
        self.suit: int = type
        self.value: int = value
    
    def __str__(self):
        letra: str = ""
        match self.value:
            case   1: letra = "A" 
            case 11: letra = "J"
            case 12: letra = "Q"
            case 13: letra = "K"
        
        naipe: str
        match self.suit:
            case 1: naipe = "♦️"
            case 2: naipe = "♠️"
            case 3: naipe = "♥️"
            case 4: naipe = "♣️"
        
        return f"{letra or self.value}{naipe}"


class Table:
    def __init__(self):
        self.ground: list[Card] = []
        self.deck: list[Card] = []

    def init(self):
        self.deck = [
            Card(1, 1), Card(1, 2), Card(1, 3), Card(1, 4),
            Card(1, 5), Card(1, 6), Card(1, 7), Card(1, 8),
            Card(1, 9), Card(1, 10), Card(1, 11), Card(1, 12),
            Card(1, 13), Card(2, 1), Card(2, 2), Card(2, 3),
            Card(2, 4), Card(2, 5), Card(2, 6), Card(2, 7),
            Card(2, 8), Card(2, 9), Card(2, 10), Card(2, 11),
            Card(2, 12), Card(2, 13), Card(3, 1), Card(3, 2),
            Card(3, 3), Card(3, 4), Card(3, 5), Card(3, 6),
            Card(3, 7), Card(3, 8), Card(3, 9), Card(3, 10),
            Card(3, 11), Card(3, 12), Card(3, 13), Card(4, 1),
            Card(4, 2), Card(4, 3), Card(4, 4), Card(4, 5),
            Card(4, 6), Card(4, 7), Card(4, 8), Card(4, 9),
            Card(4, 10), Card(4, 11), Card(4, 12), Card(4, 13),
        ]

        self.ground = []
        for i in range(4):
            self.ground.append(self.deck.pop(randint(0, len(self.deck) - 1)))
        
    def __str__(self):
        cartasMesa: str = "" 
        for card in self.ground:
            cartasMesa += f"  {card}"
        return f"""\nDeck: {len(self.deck)}
=============== ({len(self.deck): ^2}) ================
= {cartasMesa: ^37} =
=====================================""" 
    
    def draw(self):
        for i in range(3):
            self.ground.append(self.deck.pop(randint(0, len(self.deck) - 1)))


class Player:
    def __init__(self, health):
        self.hp: int = health
        self.weapon: Card = None
        self.damage: int = 0
        self.selected_card: Card = None
        self.last_monster: Card = None
        self.already_healed: bool = False
        
    def init(self, health):
        self.hp: int = health
        self.weapon: Card = None
        self.selected_card: Card = None
        self.last_monster: Card = None
        self.already_healed: bool = False
        
    def equip(self, card: Card):
        self.weapon = card
        self.damage = card.value
        self.last_monster = None
        
    def kill(self, card: Card):
        
        # Se tiver sem arma
        if self.weapon == None:
            self.hp -= card.value
            self.last_monster = card
            return

        # Se a carta for maior que o último monstro
        if self.last_monster and card.value >= self.last_monster.value:
            self.hp -= card.value
            return
        
        # Se a carta for menor que o último monstro
        if card.value < self.weapon.value:
            self.damage = card.value
            self.last_monster = card
            return
            
        # Se a carta for o primeiro monstro e maior que a arma
        self.hp -= abs(self.weapon.value - card.value)
        self.damage = card.value
        self.last_monster = card
    
    def heal(self, card: Card):
        # Se o jogador já se curou nesse round
        if self.already_healed:
            return
        
        self.hp = min(self.hp + card.value, 20)
        
    def __str__(self):
        return f"""🫀 HP: {self.hp}
    \n🗡️ Arma: {self.weapon or "None"}
    \n💀Última kill: {self.last_monster or "None"}"""
    

def command_handler(command = None):
    match command:
        case "sair" | "quit":
            quit()
        case "reset":
            table.init()
            player.init(20)
            print(table)
            print(player)
            return command_handler()
        case "1" | "2" | "3" | "4":
            command = int(command)
            if not 0 < command <= len(table.ground):
                return command_handler()
            player.selected_card = table.ground.pop(command - 1)
        case _:
            return command_handler(input(f"> "))
        
def card_handler(card: Card):
    initial_health: int = player.hp
    match card.suit:
        case 1: # ouro
            player.equip(card)
            print(f"Arma {card}  equipada.")
            
        case 2 | 4 : # espada | paus
            player.kill(card)
            print(f"-{initial_health - player.hp}HP")
                            
        case 3: # copas
            player.heal(card)
            print(f"+{player.hp - initial_health}HP")
            
        case _:
            print("Deu errado.")

table: Table  = Table()
player: Player = Player(20)
def main():
    table.init()
    
    # Loop do jogo
    while player.hp:
        print(table)
        print(player)
        command_handler()
        print(f"Carta escolhida: {str(player.selected_card)}\n")
        card_handler(player.selected_card)

        if len(table.ground) == 1:
            table.draw()
            player.already_healed = False
        
main()
