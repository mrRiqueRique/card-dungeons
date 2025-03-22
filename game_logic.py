from player import *

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
        case "run":
            
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
