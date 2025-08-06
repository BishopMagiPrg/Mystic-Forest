import pygame
from display import draw_scene, wait_for_keypress
from scenes import path_forward, path_left, path_right

def show_inventory(inventory):
    text = ["Your inventory contains:"]
    if inventory:
        text += [f"- {item}" for item in inventory]
    else:
        text.append("Nothing yet.")
    draw_scene(text + ["Press any key to return."])
    wait_for_keypress()

def main_menu(inventory, player_hp):
    while True:
        options = [
            "You are at the edge of the Mystic Forest.",
            "What would you like to do?",
            "",
            "1. Go forward into the forest",
            "2. Explore the path to the left",
            "3. Take the path to the right",
            "4. Check your inventory",
            "5. Quit"
        ]
        draw_scene(options)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True, True, player_hp
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    msg, inventory, player_hp = path_forward(inventory, player_hp)
                    draw_scene([msg, "", "Press any key to return."])
                    wait_for_keypress()
                    return False, False, player_hp
                elif event.key == pygame.K_2:
                    msg, inventory, player_hp = path_left(inventory, player_hp)
                    draw_scene([msg, "", "Press any key to return."])
                    wait_for_keypress()
                    return False, False, player_hp
                elif event.key == pygame.K_3:
                    msg, inventory, player_hp = path_right(inventory, player_hp)
                    draw_scene([msg, "", "Press any key to return."])
                    wait_for_keypress()
                    return False, False, player_hp
                elif event.key == pygame.K_4:
                    show_inventory(inventory)
                elif event.key == pygame.K_5:
                    draw_scene(["Goodbye!"])
                    pygame.time.delay(1000)
                    return True, True, player_hp