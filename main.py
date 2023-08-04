import pygame
import sys
import hrodebert_engine.engine.functions
import hrodebert_engine.variables.variables
from hrodebert_engine.variables.variables import running
from hrodebert_engine.engine.functions import *
import hrodebert_engine.variables.variables as var
import hrodebert_engine.database.database as data
import hrodebert_engine.variables.variables as var
import hrodebert_engine.Classes.default as cl

# runs the hrodebert_engine in a loop.
cl.event(type="upon_reaching_meter", one_time_only=True, type_args=10000)
cl.event(type="upon_reaching_meter", one_time_only=True, type_args=20000)
cl.event(type="upon_reaching_meter", one_time_only=True, type_args=30000)


def render_level(level_number):
    # cheeks which level the player is into by getting it from the arguments
    if level_number == 1:
        # cheeks if the level is already rendered
        if var.rendering is None:
            if var.reached_meter < 10000:
                # now here we put the code to render the level which can contain making classes changing vars and play music

                # we set the rendered var to a str which will be "level 1" so that the machine knows that there is no need
                # to re-render it

                var.rendering = "level 1"

                # to specify global vars (vars for all the code) we use var.variable
                # variables:
                var.bg = pygame.transform.scale(pygame.image.load("assets/image/level1background.png"), (width, height))

                var.player_y_pos = var.height/2
                var.player_x_pos = var.width/2
                var.jumping = False
                var.falling_speed = 0

                var.actual_level = 1

                var.chance_of_spawning_power_up = 150
                var.number_to_spawn_power_up = 150

                # classes:
                enemy_class(x_position=width + 70, yaxis=-50, direction="plane2", randomise_x_When_off_screen=True,
                            speed=15, can_summon_minions=True)

                # cheeks is the player is on stage 2 of the level
            else:
                disabled = False
                if not disabled:
                    if var.reached_meter == 10000:
                        var.rendering = "level 1"
                        # the second stage is not rendered, so it will be rendered and the stage variable will be set
                        # to 2
                        clear_sounds()
                        for walls in var.wall_list:
                            var.wall_list.remove(walls)
                        var.actual_level = 1
                        var.sub_part_rendered = 2
                        var.falling_speed = 0
                        var.enemy.clear()
                        bg = pygame.transform.scale(pygame.image.load("assets/image/level1background.png"), (width, height))
                        var.chance_of_spawning_power_up = 150
                        var.number_to_spawn_power_up = 150
                        enemy_class(x_position=width + 70, yaxis=-50, direction="plane2", randomise_x_When_off_screen=True,
                                    speed=5, can_summon_minions=True)
                        enemy_class(x_position=70, yaxis=-50, direction="plane1", randomise_x_When_off_screen=True, speed=5,
                                    can_summon_minions=True)
                        var.invulnerable = True
                        var.jumping = False
                    if var.reached_meter == 100:
                        # the second stage is not rendered so it will be rendered and the stage variable will be set to 2
                        var.actual_level = 1
                        clear_sounds()
                        var.falling_speed = 0
                        enemy.clear()
                        var.sub_part_rendered = 3
                        bg = pygame.transform.scale(pygame.image.load("assets/image/level1background.png"), (width, height))
                        rendering = "level_1"
                        var.chance_of_spawning_power_up = 150
                        var.number_to_spawn_power_up = 150
                        var.player_lives += 1
                        enemy_class(x_position=70, yaxis=-50, direction="helicopter", randomise_x_When_off_screen=True,
                                    speed=5,
                                    can_summon_minions=True)
                        var.invulnerable = True
                        var.sub_part_rendered = 3
                        var.jumping = False
                    if 4 == var.render_level_subpart and var.sub_part_rendered == 3:
                        # the third stage is not rendered so it will be rendered and the stage variable will be set to 3
                        var.actual_level = 1
                        var.player_lives += 1
                        clear_sounds()
                        var.falling_speed = 0
                        enemy.clear()
                        var.sub_part_rendered = 4
                        bg = pygame.transform.scale(pygame.image.load("assets/image/level1background.png"), (width, height))
                        rendering = "level_1"
                        var.chance_of_spawning_power_up = 150
                        var.number_to_spawn_power_up = 150
                        enemy_class(x_position=70, yaxis=-50, direction="scope", randomise_x_When_off_screen=True,
                                    speed=5,
                                    can_summon_minions=True)
                        var.invulnerable = True
                        var.sub_part_rendered = 4
                        var.jumping = False


render_level(data.get_variable("LEVEL_REACHED"))
while var.running is True:
    for event in var.events:
        event.cheek_for_event()
    # search for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            var.running = False
    if not var.main_menu:
        # calls the key handler
        hrodebert_engine.engine.functions.key_handler()
        if not game_over_rendered:
            # updates the screen
            hrodebert_engine.engine.functions.physics()
            hrodebert_engine.engine.functions.screen_updater()
            if var.rendering is None:
                render_level(data.get_variable("LEVEL_REACHED"))

    else:
        hrodebert_engine.engine.functions.render_main_menu()
# closes pygame after the loop.
pygame.quit()
data.close_database()
sys.exit()
