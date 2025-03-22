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


full_deck: list[Card] = [
    Card(1, 1),  Card(1, 2),  Card(1, 3),  Card(1, 4),
    Card(1, 5),  Card(1, 6),  Card(1, 7),  Card(1, 8),
    Card(1, 9),  Card(1, 10), Card(1, 11), Card(1, 12),
    Card(1, 13), Card(2, 1),  Card(2, 2),  Card(2, 3),
    Card(2, 4),  Card(2, 5),  Card(2, 6),  Card(2, 7),
    Card(2, 8),  Card(2, 9),  Card(2, 10), Card(2, 11),
    Card(2, 12), Card(2, 13), Card(3, 1),  Card(3, 2),
    Card(3, 3),  Card(3, 4),  Card(3, 5),  Card(3, 6),
    Card(3, 7),  Card(3, 8),  Card(3, 9),  Card(3, 10),
    Card(3, 11), Card(3, 12), Card(3, 13), Card(4, 1),
    Card(4, 2),  Card(4, 3),  Card(4, 4),  Card(4, 5),
    Card(4, 6),  Card(4, 7),  Card(4, 8),  Card(4, 9),
    Card(4, 10), Card(4, 11), Card(4, 12), Card(4, 13)
]