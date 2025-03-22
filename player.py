from card import Card

class Player:
    def __init__(self, health):
        self.hp: int = health
        self.weapon: Card = None
        self.selected_card: Card = None
        self.last_enemy: Card = None
        self.already_healed: bool = False
        
    def start(self, health):
        self.hp: int = health
        self.weapon: Card = None
        self.selected_card: Card = None
        self.last_enemy: Card = None
        self.already_healed: bool = False
        
    def equip(self, card: Card):
        self.weapon = card
        self.last_enemy = None
        
    def kill(self, enemy: Card):
        # Se tiver sem arma ou o inimigo for maior que a arma
        if self.weapon == None or enemy.value > self.weapon.value:
            
            # Se for o primeiro inimigo da arma
            if self.last_enemy == None:
                self.hp -= enemy.value - self.weapon.value
                self.last_enemy = enemy
                return
            
            self.hp -= enemy.value
            return
        
        # Se a carta for menor que o último monstro
        self.weapon.value = enemy.value
        self.last_enemy = enemy
        return
    
    def heal(self, card: Card):
        # Se o jogador já se curou nesse round
        if self.already_healed:
            return
        
        self.hp = min(self.hp + card.value, 20)
            
    def __str__(self):
        return f"""🫀 HP: {self.hp}
    \n🗡️ Arma: {self.weapon or "None"}
    \n💀Última kill: {self.last_enemy or "None"}"""
