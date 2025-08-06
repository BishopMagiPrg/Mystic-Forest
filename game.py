from menu import main_menu
from inventory import create_inventory

def start_game():
    inventory = create_inventory()
    player_hp = 100
    game_over = False

    while not game_over:
        game_over, _, player_hp = main_menu(inventory, player_hp)

if __name__ == "__main__":
    start_game()
