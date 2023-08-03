import pygame
from pygame import mixer
import random

import hrodebert_engine.variables.variables
from hrodebert_engine.Classes.default import *
from hrodebert_engine.variables.variables import *

# functions

# sound stopper
def clear_sounds():
    pygame.mixer.Channel(1).stop()


# render levels

# create texts
def draw_text(text, font_for_the_thext, color, x, y):
    text_surface = font_for_the_thext.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)
    return text_surface, text_rect.size


# screen render
def render_level(level_number):
    global screen, width, height, bg, rendering, actual_level, enemy, width, height, player_x_pos, player_y_pos, black
    global player_lives, falling_speed, render_level_subpart, sub_part_rendered, invulnerable
    global chance_of_spawning_power_up, number_to_spawn_power_up, booster_list, player_speed, jumping, music, wall_list
    # cheeks which level the player is into
    if level_number == 1:
        # cheeks if the level is already rendered
        if rendering is None:
            # if the rendering is none then it renders the first part of the level<
            actual_level = 1
            player_lives = 1
            mixer.music.load("assets/sfx/bullet.mp3")
            clear_sounds()
            falling_speed = 0
            enemy.clear()
            booster_list.clear()
            bg = pygame.transform.scale(pygame.image.load("assets/image/level1background.png"), (width, height))
            rendering = "level_1"
            render_level_subpart = 1
            player_y_pos = int((height / 2) - player_rect_size / 2)
            player_x_pos = int((width / 2) - player_rect_size / 2)
            chance_of_spawning_power_up = 150
            number_to_spawn_power_up = 150
            sub_part_rendered = 1
            jumping = False
            wall(x_position=120, y_position=120, width=100, height=100, texture=wall_texture,
                 delete_enemy_on_contact=False)
            enemy_class(x_position=70, yaxis=-50, direction="plane1", randomise_x_When_off_screen=True, speed=5,
                        can_summon_minions=True)
            music.stop()
            music.play(loops=-1)

        # cheeks is the player is on stage 2 of the level
        disabled = False
        if not disabled:
            if render_level_subpart == 2:
                # cheeks if the 2 stage is rendered
                if sub_part_rendered == 1:
                    # the second stage is not rendered, so it will be rendered and the stage variable will be set
                    # to 2
                    clear_sounds()
                    actual_level = 1
                    sub_part_rendered = 2
                    falling_speed = 0
                    enemy.clear()
                    bg = pygame.transform.scale(pygame.image.load("assets/image/level1background.png"), (width, height))
                    rendering = "level_1"
                    chance_of_spawning_power_up = 150
                    number_to_spawn_power_up = 150
                    enemy_class(x_position=width + 70, yaxis=-50, direction="plane2", randomise_x_When_off_screen=True,
                                speed=5, can_summon_minions=True)
                    enemy_class(x_position=70, yaxis=-50, direction="plane1", randomise_x_When_off_screen=True, speed=5,
                                can_summon_minions=True)
                    invulnerable = True
                    jumping = False
            if 3 == render_level_subpart and sub_part_rendered == 2:
                # the second stage is not rendered so it will be rendered and the stage variable will be set to 2
                actual_level = 1
                clear_sounds()
                falling_speed = 0
                enemy.clear()
                sub_part_rendered = 3
                bg = pygame.transform.scale(pygame.image.load("assets/image/level1background.png"), (width, height))
                rendering = "level_1"
                chance_of_spawning_power_up = 150
                number_to_spawn_power_up = 150
                player_lives += 1
                enemy_class(x_position=70, yaxis=-50, direction="helicopter", randomise_x_When_off_screen=True,
                            speed=5,
                            can_summon_minions=True)
                invulnerable = True
                print("stage 2")
                sub_part_rendered = 3
                jumping = False
            if 4 == render_level_subpart and sub_part_rendered == 3:
                # the third stage is not rendered so it will be rendered and the stage variable will be set to 3
                actual_level = 1
                player_lives += 1
                clear_sounds()
                falling_speed = 0
                enemy.clear()
                sub_part_rendered = 4
                bg = pygame.transform.scale(pygame.image.load("assets/image/level1background.png"), (width, height))
                rendering = "level_1"
                chance_of_spawning_power_up = 150
                number_to_spawn_power_up = 150
                enemy_class(x_position=70, yaxis=-50, direction="scope", randomise_x_When_off_screen=True,
                            speed=5,
                            can_summon_minions=True)
                invulnerable = True
                print("stage 3")
                sub_part_rendered = 4
                jumping = False
        screen.blit(bg, (0, 0))

def render_main_menu():
    global main_menu
    screen.fill("white")
    play = Button(30, 30, start_img, name="play")
    play.draw_button()
    pygame.display.flip()
    clock.tick(Max_fps)


def physics():
    print(hrodebert_engine.variables.variables.meter_counter)
    can_move = True
    if not hrodebert_engine.variables.variables.game_over:
        # gravity system

        # cheeks if the player is jumping or not and if it is the script cheeks if it has a power up and
        # it makes the gravity different in base of the player attributes
        if not hrodebert_engine.variables.variables.jumping:

            if hrodebert_engine.variables.variables.jet_pack_using:
                hrodebert_engine.variables.variables.falling_speed = 0
            # if the player is off-screen
            if hrodebert_engine.variables.variables.player_y_pos >= hrodebert_engine.variables.variables.height - hrodebert_engine.variables.variables.player_rect_size:
                # disables the fall and makes the player stay on screen
                hrodebert_engine.variables.variables.falling_speed += 0.5
                hrodebert_engine.variables.variables.player_y_pos = hrodebert_engine.variables.variables.height - hrodebert_engine.variables.variables.player_rect_size
            else:
                # if the player is not off-screen make the player fall
                can_move = False
                for walls in wall_list:
                    player_rect = player_rect = pygame.Rect(hrodebert_engine.variables.variables.player_x_pos, hrodebert_engine.variables.variables.player_y_pos + int(hrodebert_engine.variables.variables.falling_speed) + 1,
                                                            hrodebert_engine.variables.variables.player_rect_size,
                                                            hrodebert_engine.variables.variables.player_rect_size)
                    result = walls.can_player_move(player_rect)
                    walls.physics()
                    if result:
                        can_move = False
                    else:
                        if not can_move:
                            can_move = True
                if can_move:
                    hrodebert_engine.variables.variables.falling_speed += 0.5
                    hrodebert_engine.variables.variables.player_y_pos += int(hrodebert_engine.variables.variables.falling_speed)
                else:
                    hrodebert_engine.variables.variables.falling_speed = 0

            # meter counter cant be smaller then 0
            if hrodebert_engine.variables.variables.meter_counter >= 0 and hrodebert_engine.variables.variables.meter_counter != 0:
                # meter falling manager if the falling speed /4 is not bigger than 200(max value of falling speed)
                # then It's ok for setting the meter_counter: meter_counter - falling_speed / 4
                if hrodebert_engine.variables.variables.falling_speed / 4 < 200:
                    hrodebert_engine.variables.variables.meter_counter -= hrodebert_engine.variables.variables.falling_speed / 4
                else:
                    # if falling speed /4 is bigger than 200 then meter_counter is going to be at meter_counter - 200
                    hrodebert_engine.variables.variables.meter_counter -= 200
            else:
                hrodebert_engine.variables.variables.meter_counter = 0
        else:
            if hrodebert_engine.variables.variables.player_y_pos > 0:
                # if the player is jumping then the meter counter will be added 20
                # for every frame sets the meter counter to + 20
                hrodebert_engine.variables.variables.meter_counter += 20
                # by setting falling speed to 0 we make so the acceleration counter starts from 0
                hrodebert_engine.variables.variables.falling_speed = 0
                # the "friction" is a counter that makes the acceleration less strong at the moment the hrodebert_engine gets at
                # that frame making a jump effect with a speed loss whit time
                if hrodebert_engine.variables.variables.friction <= hrodebert_engine.variables.variables.Now_time - 10:
                    # slows down the jump speed
                    hrodebert_engine.variables.variables.jump_force -= 1
                    # makes the player y be higher
                    can_move = False
                    for walls in wall_list:
                        walls.physics()
                        player_rect = player_rect = pygame.Rect(hrodebert_engine.variables.variables.player_x_pos, hrodebert_engine.variables.variables.player_y_pos - hrodebert_engine.variables.variables.jump_force * 3,
                                                                hrodebert_engine.variables.variables.player_rect_size,
                                                                hrodebert_engine.variables.variables.player_rect_size)
                        result = walls.can_player_move(player_rect)
                        if result:
                            can_move = False
                        else:
                            if not can_move:
                                can_move = True
                    if can_move:
                        hrodebert_engine.variables.variables.player_y_pos -= hrodebert_engine.variables.variables.jump_force * 3
                    else:
                        hrodebert_engine.variables.variables.player_y_pos -= 1
                    # resets the counter for the jump speed diminution
                    hrodebert_engine.variables.variables.friction = hrodebert_engine.variables.variables.Now_time
                else:
                    # makes the player go higher
                    hrodebert_engine.variables.variables.can_move = False
                    for walls in wall_list:
                        player_rect = player_rect = pygame.Rect(hrodebert_engine.variables.variables.player_x_pos, hrodebert_engine.variables.variables.player_y_pos - hrodebert_engine.variables.variables.jump_force * 3,
                                                                hrodebert_engine.variables.variables.player_rect_size,
                                                                hrodebert_engine.variables.variables.player_rect_size)
                        result = walls.can_player_move(player_rect)
                        if result:
                            can_move = False
                        else:
                            if not can_move:
                                can_move = True
                    if can_move:
                        hrodebert_engine.variables.variables.player_y_pos -= hrodebert_engine.variables.variables.jump_force * 3
                    else:
                        hrodebert_engine.variables.variables.player_y_pos -= 1
                    # brakes the loop if the player has no more jumping force
                    if hrodebert_engine.variables.variables.jump_force == 0:
                        hrodebert_engine.variables.variables.jumping = False
            else:
                hrodebert_engine.variables.variables.player_y_pos = 0 +  1
            if hrodebert_engine.variables.variables.jet_pack_using:
                if hrodebert_engine.variables.variables.jet_pack_starter_time < hrodebert_engine.variables.variables.Now_time - 360:
                    hrodebert_engine.variables.variables.jet_pack_using = False


        # collision handler:

        # first we will put for in loop, so we can do an action like calling a function for every class
        for power_up in hrodebert_engine.variables.variables.booster_list:
            # we call the designated function for every object of the class power up
            power_up.booster_detect_collisions()

        # now we cheek if any enemy rect is colliding with the player by first specific the player rect and the enemy
        # rect then we cheek if they are colliding whit player_rect.colliderect(enemy_rect): which is a function
        # of pygame

        for enemy_npc in enemy:
            enemy_rect = pygame.Rect(enemy_npc.x_position, enemy_npc.yaxis, enemy_npc.size_width,
                                     enemy_npc.size_height)
            player_rect = pygame.Rect(hrodebert_engine.variables.variables.player_x_pos, hrodebert_engine.variables.variables.player_y_pos - hrodebert_engine.variables.variables.jump_force * 3, hrodebert_engine.variables.variables.player_rect_size, hrodebert_engine.variables.variables.player_rect_size)
            if player_rect.colliderect(enemy_rect):
                # after knowing that the player is colliding or now then we are able to call the enemy action
                # which could be to lose a life or to spawn a mile
                if not hrodebert_engine.variables.variables.invulnerable:
                    if enemy_npc.type != "scope":
                        hrodebert_engine.variables.variables.player_lives -= 1
                        hrodebert_engine.variables.variables.starter_time = Now_time
                        hrodebert_engine.variables.variables.invulnerable = True
                    else:
                        enemy_npc.locked_time += 1
                        enemy_npc.locking = True
            else:
                if enemy_npc.type == "scope":
                    enemy_npc.locking = False


player_sprite()


# updates the skin

def screen_updater():
    global Now_time, Max_fps, player_x_pos, enemy, game_over, game_over_rendered, invulnerable, rendering, retry_button
    global starter_time, player_lives, booster_list, render_level_subpart, chance_of_spawning_power_up
    global number_to_spawn_power_up, started_guess, player_y_pos, jet_pack_using, wall_list, player_list
    if not hrodebert_engine.variables.variables.game_over:
        # if the player is higher than 10000 meters
        if hrodebert_engine.variables.variables.meter_counter > 10000:
            # here we cheek if the player has the requirements to enter stage 2
            if hrodebert_engine.variables.variables.render_level_subpart <= 2 and hrodebert_engine.variables.variables.render_level_subpart == 1:
                # we enter stage 2
                hrodebert_engine.variables.variables.render_level_subpart = 2
        if hrodebert_engine.variables.variables.meter_counter > 20000:
            if hrodebert_engine.variables.variables.render_level_subpart <= 3 and hrodebert_engine.variables.variables.render_level_subpart == 2:
                hrodebert_engine.variables.variables.render_level_subpart = 3
        if hrodebert_engine.variables.variables.meter_counter > 30000:
            if hrodebert_engine.variables.variables.render_level_subpart <= 4 and hrodebert_engine.variables.variables.render_level_subpart == 3:
                hrodebert_engine.variables.variables.render_level_subpart = 4

        # cheeks if the spawning chance for power up is enabled
        if hrodebert_engine.variables.variables.chance_of_spawning_power_up != 0:
            # makes a clock that cheeks it every 1/3 of second
            if hrodebert_engine.variables.variables.Now_time - 20 > hrodebert_engine.variables.variables.started_guess:
                # makes a random number that if it's the same as the winner number then a power up spawns
                casual_number = random.randint(0, hrodebert_engine.variables.variables.chance_of_spawning_power_up)
                hrodebert_engine.variables.variables.started_guess = hrodebert_engine.variables.variables.Now_time
                if hrodebert_engine.variables.variables.number_to_spawn_power_up == casual_number:
                    if len(hrodebert_engine.variables.variables.booster_list) == 0:
                        booster(booster_type="random", x_position=int(random.randint(70, width - 70)),
                                y_position=int(random.randint(70, height - 70)))

        # renders every object calling they're rendering option or rendering them manually + it handles the gravity
        # system render the hrodebert_engine here V
        screen.fill("white")

        # renders the requested level
        hrodebert_engine.engine.functions.render_level(1)
        if jet_pack_using:
            screen.blit(jet_pack, (player_x_pos - player_rect_size / 4, player_y_pos - 10))
        # pygame.draw.rect(screen, player_rect_color,
        #                pygame.Rect(player_x_pos, player_y_pos, player_rect_size, player_rect_size), )
        print(player_list)
        for player in player_list:
            player.walk()
        screen.blit(heart, ((width - 60) - 20, 20))
        draw_text(str(int(hrodebert_engine.variables.variables.player_lives)), font, black, (width - 120) - 20, 30)

        for boosters in booster_list:
            boosters.render_booster()
        for enemy_npc in enemy:
            enemy_npc.render()
        for walls in wall_list:
            walls.render_wall()
        draw_text(str(int(hrodebert_engine.variables.variables.meter_counter)), font, black, 20, 20)

        # don't put anything under this V
        pygame.display.flip()

        # getting the frame we are in
        if hrodebert_engine.variables.variables.Now_time is None:
            hrodebert_engine.variables.variables.Now_time = 1
            hrodebert_engine.variables.variables.starter_time = hrodebert_engine.variables.variables.Now_time
        else:
            hrodebert_engine.variables.variables.Now_time += 1
        if hrodebert_engine.variables.variables.invulnerable:
            if (hrodebert_engine.variables.variables.Now_time - 180) >= hrodebert_engine.variables.variables.starter_time:
                hrodebert_engine.variables.variables.invulnerable = False

        # top border
        if player_y_pos < 0:
            player_y_pos = 0

        # falling system
        if hrodebert_engine.variables.variables.meter_counter == 0 or hrodebert_engine.variables.variables.meter_counter <= 0:
            if not hrodebert_engine.variables.variables.invulnerable:
                hrodebert_engine.variables.variables.player_lives -= 1
        if hrodebert_engine.variables.variables.player_lives == 0:
            hrodebert_engine.variables.variables.game_over = True

        # setting the max frame rate
        clock.tick(Max_fps)
    else:
        if not game_over_rendered:
            music.stop()
            screen.fill("black")
            text, text_size = draw_text(str(int(meter_counter)), font, black, (width / 2), (height / 2) - 230)
            text_width = text_size[0]
            draw_text(str(int(meter_counter)), font, white, (width / 2) - (text_width / 2), (height / 2) - 230)
            text, text_size = draw_text(str("Game Over!"), font, black, (width / 2), (height / 2))
            text_width = text_size[0]
            draw_text(str("Game Over!"), font, red, (width / 2) - (text_width / 2), (height / 2))
            retry = Button(x=(width / 2) - 65, y=(height / 2) + 200, image=retry_button, name="retry")
            retry.draw_button()
            # don't put anything under this V
            pygame.display.flip()
            # setting the max frame rate
            rendering = None
        clock.tick(Max_fps)


# key handler
def key_handler():
    global player_x_pos, player_y_pos, jump_cd, Now_time, falling_speed, player_speed, game_over, jumping, jump_force
    global friction, jump_force, jet_pack_using,direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        # we cheek if exists the cool down, if it doesn't then we jump if it exists we cheek if it's smaller than the
        # frames - 3 seconds of frame
        if hrodebert_engine.variables.variables.jump_cd is None or hrodebert_engine.variables.variables.jump_cd <= (hrodebert_engine.variables.variables.Now_time - 70):
            # sets a jump cd gives the player a jump force and sets the jumping var to true
            print("works")
            hrodebert_engine.variables.variables.jump_cd = hrodebert_engine.variables.variables.Now_time
            hrodebert_engine.variables.variables.jump_force = 4
            hrodebert_engine.variables.variables.falling_speed = 0
            hrodebert_engine.variables.variables.jumping = True
            hrodebert_engine.variables.variables.friction = hrodebert_engine.variables.variables.Now_time
            jump = pygame.mixer.Sound("assets/sfx/jump.mp3")
            pygame.mixer.Sound.play(jump)
            hrodebert_engine.variables.variables.player_y_pos -= 2

    if keys[pygame.K_a]:
        can_move = False
        hrodebert_engine.variables.variables.direction = "right"
        returns = []
        for walls in wall_list:
            player_rect = player_rect = pygame.Rect(hrodebert_engine.variables.variables.player_x_pos - hrodebert_engine.variables.variables.player_speed, hrodebert_engine.variables.variables.player_y_pos + 2, hrodebert_engine.variables.variables.player_rect_size,
                                                    hrodebert_engine.variables.variables.player_rect_size)
            result = walls.can_player_move(player_rect)
            if result:
                can_move = False
                player_rect = player_rect = pygame.Rect(hrodebert_engine.variables.variables.player_x_pos - hrodebert_engine.variables.variables.player_speed - 20, hrodebert_engine.variables.variables.player_y_pos - 2,
                                                        hrodebert_engine.variables.variables.player_rect_size,
                                                        hrodebert_engine.variables.variables.player_rect_size)
                result = walls.can_player_move(player_rect)
                if not result:
                    can_move = True
            else:
                if not can_move:
                    can_move = True
        if can_move:
            if hrodebert_engine.variables.variables.player_x_pos - 1 >= 0:
                hrodebert_engine.variables.variables.player_x_pos -= hrodebert_engine.variables.variables.player_speed
                print("moving")
    if keys[pygame.K_d]:
        can_move = False
        hrodebert_engine.variables.variables.direction = "left"
        for walls in wall_list:
            player_rect = player_rect = pygame.Rect(hrodebert_engine.variables.variables.player_x_pos + hrodebert_engine.variables.variables.player_speed - 20, hrodebert_engine.variables.variables.player_y_pos + 2,
                                                    hrodebert_engine.variables.variables.player_rect_size,
                                                    hrodebert_engine.variables.variables.player_rect_size)
            result = walls.can_player_move(player_rect)
            if result:
                can_move = False
                player_rect = player_rect = pygame.Rect(hrodebert_engine.variables.variables.player_x_pos - hrodebert_engine.variables.variables.player_speed, hrodebert_engine.variables.variables.player_y_pos - 2, hrodebert_engine.variables.variables.player_rect_size,
                                                        hrodebert_engine.variables.variables.player_rect_size)
                result = walls.can_player_move(player_rect)
                if not result:
                    can_move = True
            else:
                if not can_move:
                    can_move = True
        if hrodebert_engine.variables.variables.player_x_pos + hrodebert_engine.variables.variables.player_rect_size < width:
            if can_move:
                hrodebert_engine.variables.variables.player_x_pos += hrodebert_engine.variables.variables.player_speed

    # makes the go height / go down key usable only if the player has a jetpack
    if jet_pack_using:
        if keys[pygame.K_w]:
            can_move = False
            for walls in wall_list:
                player_rect = player_rect = pygame.Rect(player_x_pos, player_y_pos - player_speed, player_rect_size,
                                                        player_rect_size)
                result = walls.can_player_move(player_rect)
                if result:
                    can_move = False
                else:
                    if not can_move:
                        can_move = True
            if player_y_pos - player_rect_size > 0:
                if can_move:
                    player_y_pos -= player_speed

        if keys[pygame.K_s]:
            can_move = False
            for walls in wall_list:
                player_rect = player_rect = pygame.Rect(player_x_pos, player_y_pos + player_speed, player_rect_size,
                                                        player_rect_size)
                result = walls.can_player_move(player_rect)
                if result:
                    can_move = False
                else:
                    if not can_move:
                        can_move = True
            if player_y_pos + player_rect_size < height:
                if can_move:
                    player_y_pos += player_speed
