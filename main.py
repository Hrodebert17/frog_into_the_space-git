import pygame
import sys
import hrodebert_engine.engine.functions
import hrodebert_engine.variables.variables
from hrodebert_engine.variables.variables import running
from hrodebert_engine.engine.functions import *
import hrodebert_engine.variables.variables as var

# runs the hrodebert_engine in a loop.
while running is True:
    # search for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not hrodebert_engine.variables.variables.main_menu:
        # calls the key handler
        hrodebert_engine.engine.functions.key_handler()
        if not game_over_rendered:
            # updates the screen
            hrodebert_engine.engine.functions.physics()
            hrodebert_engine.engine.functions.screen_updater()
    else:
        hrodebert_engine.engine.functions.render_main_menu()
# closes pygame after the loop.
pygame.quit()
sys.exit()
