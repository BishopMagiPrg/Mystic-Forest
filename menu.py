import pygame
from display import update_display, wait_for_keypress, draw_scene
from scenes import path_forward, path_left, path_right
from display import clock

def show_inventory(inventory):
    text = ["Your inventory contains:"]
    if inventory:
        text += [f"- {item}" for item in inventory]
    else:
        text.append("Nothing yet.")
    draw_scene(text + ["Press any key to return."])
    pygame.display.flip()
    wait_for_keypress()

def main_menu(inventory, player_hp):
    pygame.display.set_caption("Mystic Forest")

    options = [
        "You are at the edge of the Mystic Forest.",
        "What would you like to do?",
    ]

    # Define os botões
    buttons = [
        ("Go forward into the forest", path_forward),
        ("Explore the path to the left", path_left),
        ("Take the path to the right", path_right),
        ("Check your inventory", "inventory"),
        ("Quit", "quit")
    ]

    while True:
        button_rects = update_display(options, buttons)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True, True, player_hp
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = event.pos
                for rect, (label, action) in button_rects:
                    if rect.collidepoint(mouse_pos):
                        show_inventory(inventory)
                    elif action == "inventory":
                        draw_scene(["Goodbye!"])
                        pygame.display.flip()
                        pygame.time.delay(1000)
                        return True, True, player_hp
                    else:
                        msg, inventory, player_hp = action(inventory, player_hp)
                        draw_scene([msg, "", "Press any key to return."])
                        pygame.display.flip()
                        wait_for_keypress()
                        return False, False, player_hp
