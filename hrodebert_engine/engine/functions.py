import pygame
from pygame import mixer
import random

import hrodebert_engine.variables.variables
from hrodebert_engine.Classes.default import *
from hrodebert_engine.variables.variables import *
import hrodebert_engine.database.database as data
import hrodebert_engine.variables.variables as var

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

rendering = None
# screen render
def render_level(level_number,Rerender = False):
    global rendering,render_level_subpart,bg
    # cheeks which level the player is into
    if Rerender:
        rendering = None
    if level_number == 1:
        print("lvl num 1")
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
            var.player_y_pos = int((height / 2) - player_rect_size / 2)
            var.player_x_pos = int((width / 2) - player_rect_size / 2)
            chance_of_spawning_power_up = 150
            number_to_spawn_power_up = 150
            sub_part_rendered = 1
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
    print(var.meter_counter)
    can_move = True
    if not var.game_over:
        # gravity system

        # cheeks if the player is jumping or not and if it is the script cheeks if it has a power up and
        # it makes the gravity different in base of the player attributes
        if not var.jumping:

            if var.jet_pack_using:
                var.falling_speed = 0
            # if the player is off-screen
            if var.player_y_pos >= var.height - var.player_rect_size:
                # disables the fall and makes the player stay on screen
                var.falling_speed += 0.5
                var.player_y_pos = var.height - var.player_rect_size
            else:
                # if the player is not off-screen make the player fall
                can_move = False
                for walls in wall_list:
                    player_rect = player_rect = pygame.Rect(var.player_x_pos, var.player_y_pos + int(var.falling_speed) + 1,
                                                            var.player_rect_size,
                                                            var.player_rect_size)
                    result = walls.can_player_move(player_rect)
                    walls.physics()
                    if result:
                        can_move = False
                    else:
                        if not can_move:
                            can_move = True
                if can_move:
                    var.falling_speed += 0.5
                    var.player_y_pos += int(var.falling_speed)
                else:
                    var.falling_speed = 0

            # meter counter cant be smaller then 0
            if var.meter_counter >= 0 and var.meter_counter != 0:
                # meter falling manager if the falling speed /4 is not bigger than 200(max value of falling speed)
                # then It's ok for setting the meter_counter: meter_counter - falling_speed / 4
                if var.falling_speed / 4 < 200:
                    var.meter_counter -= var.falling_speed / 4
                else:
                    # if falling speed /4 is bigger than 200 then meter_counter is going to be at meter_counter - 200
                    var.meter_counter -= 200
            else:
                var.meter_counter = 0
        else:
            if var.player_y_pos > 0:
                # if the player is jumping then the meter counter will be added 20
                # for every frame sets the meter counter to + 20
                var.meter_counter += 20
                # by setting falling speed to 0 we make so the acceleration counter starts from 0
                var.falling_speed = 0
                # the "friction" is a counter that makes the acceleration less strong at the moment the hrodebert_engine gets at
                # that frame making a jump effect with a speed loss whit time
                if var.friction <= var.Now_time - 10:
                    # slows down the jump speed
                    var.jump_force -= 1
                    # makes the player y be higher
                    can_move = False
                    for walls in wall_list:
                        walls.physics()
                        player_rect = player_rect = pygame.Rect(var.player_x_pos, var.player_y_pos - var.jump_force * 3,
                                                                var.player_rect_size,
                                                                var.player_rect_size)
                        result = walls.can_player_move(player_rect)
                        if result:
                            can_move = False
                        else:
                            if not can_move:
                                can_move = True
                    if can_move:
                        var.player_y_pos -= var.jump_force * 3
                    else:
                        var.player_y_pos -= 1
                    # resets the counter for the jump speed diminution
                    var.friction = var.Now_time
                else:
                    # makes the player go higher
                    var.can_move = False
                    for walls in wall_list:
                        player_rect = player_rect = pygame.Rect(var.player_x_pos, var.player_y_pos - var.jump_force * 3,
                                                                var.player_rect_size,
                                                                var.player_rect_size)
                        result = walls.can_player_move(player_rect)
                        if result:
                            can_move = False
                        else:
                            if not can_move:
                                can_move = True
                    if can_move:
                        var.player_y_pos -= var.jump_force * 3
                    else:
                        var.player_y_pos -= 1
                    # brakes the loop if the player has no more jumping force
                    if var.jump_force == 0:
                        var.jumping = False
            else:
                var.player_y_pos = 0 +  1
            if var.jet_pack_using:
                if var.jet_pack_starter_time < var.Now_time - 360:
                    var.jet_pack_using = False


        # collision handler:

        # first we will put for in loop, so we can do an action like calling a function for every class
        for power_up in var.booster_list:
            # we call the designated function for every object of the class power up
            power_up.booster_detect_collisions()

        # now we cheek if any enemy rect is colliding with the player by first specific the player rect and the enemy
        # rect then we cheek if they are colliding whit player_rect.colliderect(enemy_rect): which is a function
        # of pygame

        for enemy_npc in enemy:
            enemy_rect = pygame.Rect(enemy_npc.x_position, enemy_npc.yaxis, enemy_npc.size_width,
                                     enemy_npc.size_height)
            player_rect = pygame.Rect(var.player_x_pos, var.player_y_pos - var.jump_force * 3, var.player_rect_size, var.player_rect_size)
            if player_rect.colliderect(enemy_rect):
                # after knowing that the player is colliding or now then we are able to call the enemy action
                # which could be to lose a life or to spawn a mile
                if not var.invulnerable:
                    if enemy_npc.type != "scope":
                        var.player_lives -= 1
                        var.starter_time = Now_time
                        var.invulnerable = True
                    else:
                        enemy_npc.locked_time += 1
                        enemy_npc.locking = True
            else:
                if enemy_npc.type == "scope":
                    enemy_npc.locking = False


player_sprite()


# updates the skin

def screen_updater():
    if not var.game_over:
        # if the player is higher than 10000 meters
        if var.meter_counter > 10000:
            # here we cheek if the player has the requirements to enter stage 2
            if var.render_level_subpart <= 2 and var.render_level_subpart == 1:
                # we enter stage 2
                var.render_level_subpart = 2
        if var.meter_counter > 20000:
            if var.render_level_subpart <= 3 and var.render_level_subpart == 2:
                var.render_level_subpart = 3
        if var.meter_counter > 30000:
            if var.render_level_subpart <= 4 and var.render_level_subpart == 3:
                var.render_level_subpart = 4

        # cheeks if the spawning chance for power up is enabled
        if var.chance_of_spawning_power_up != 0:
            # makes a clock that cheeks it every 1/3 of second
            if var.Now_time - 20 > var.started_guess:
                # makes a random number that if it's the same as the winner number then a power up spawns
                casual_number = random.randint(0, var.chance_of_spawning_power_up)
                var.started_guess = var.Now_time
                if var.number_to_spawn_power_up == casual_number:
                    if len(var.booster_list) == 0:
                        booster(booster_type="random", x_position=int(random.randint(70, width - 70)),
                                y_position=int(random.randint(70, height - 70)))

        # renders every object calling they're rendering option or rendering them manually + it handles the gravity
        # system render the hrodebert_engine here V
        screen.fill("white")

        # renders the requested level
        hrodebert_engine.engine.functions.render_level(data.get_variable("LEVEL_REACHED"))
        if jet_pack_using:
            screen.blit(jet_pack, (player_x_pos - player_rect_size / 4, player_y_pos - 10))
        # pygame.draw.rect(screen, player_rect_color,
        #                pygame.Rect(player_x_pos, player_y_pos, player_rect_size, player_rect_size), )
        print(player_list)
        for player in player_list:
            player.walk()
        screen.blit(heart, ((width - 60) - 20, 20))
        draw_text(str(int(var.player_lives)), font, black, (width - 120) - 20, 30)

        for boosters in booster_list:
            boosters.render_booster()
        for enemy_npc in enemy:
            enemy_npc.render()
        for walls in wall_list:
            walls.render_wall()
        draw_text(str(int(var.meter_counter)), font, black, 20, 20)

        # don't put anything under this V
        pygame.display.flip()

        # getting the frame we are in
        if var.Now_time is None:
            var.Now_time = 1
            var.starter_time = var.Now_time
        else:
            var.Now_time += 1
        if var.invulnerable:
            if (var.Now_time - 180) >= var.starter_time:
                var.invulnerable = False

        # top border
        if var.player_y_pos < 0:
            var.player_y_pos = 0

        # falling system
        if var.meter_counter == 0 or var.meter_counter <= 0:
            if not var.invulnerable:
                var.player_lives -= 1
        if var.player_lives == 0:
            var.game_over = True

        # setting the max frame rate
        clock.tick(Max_fps)
    else:
        if not game_over_rendered:
            music.stop()
            screen.fill("black")
            text, text_size = draw_text(str(int(var.meter_counter)), font, black, (width / 2), (height / 2) - 230)
            text_width = text_size[0]
            print(f"text widt ={text_width}")
            draw_text(str(int(var.meter_counter)), font, white, int(((width / 2) - text_width / 2)), (height / 2) - 230)
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
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        # we cheek if exists the cool down, if it doesn't then we jump if it exists we cheek if it's smaller than the
        # frames - 3 seconds of frame
        if var.jump_cd is None or var.jump_cd <= (var.Now_time - 70):
            # sets a jump cd gives the player a jump force and sets the jumping var to true
            print("works")
            var.jump_cd = var.Now_time
            var.jump_force = 4
            var.falling_speed = 0
            var.jumping = True
            var.friction = var.Now_time
            jump = pygame.mixer.Sound("assets/sfx/jump.mp3")
            pygame.mixer.Sound.play(jump)
            var.player_y_pos -= 2

    if keys[pygame.K_a]:
        can_move = False
        var.direction = "right"
        returns = []
        for walls in wall_list:
            player_rect = player_rect = pygame.Rect(var.player_x_pos - var.player_speed, var.player_y_pos + 2, var.player_rect_size,
                                                    var.player_rect_size)
            result = walls.can_player_move(player_rect)
            if result:
                can_move = False
                player_rect = player_rect = pygame.Rect(var.player_x_pos - var.player_speed - 20, var.player_y_pos - 2,
                                                        var.player_rect_size,
                                                        var.player_rect_size)
                result = walls.can_player_move(player_rect)
                if not result:
                    can_move = True
            else:
                if not can_move:
                    can_move = True
        if can_move:
            if var.player_x_pos - 1 >= 0:
                var.player_x_pos -= var.player_speed
                print("moving")
    if keys[pygame.K_d]:
        can_move = False
        var.direction = "left"
        for walls in wall_list:
            player_rect = player_rect = pygame.Rect(var.player_x_pos + var.player_speed - 20, var.player_y_pos + 2,
                                                    var.player_rect_size,
                                                    var.player_rect_size)
            result = walls.can_player_move(player_rect)
            if result:
                can_move = False
                player_rect = player_rect = pygame.Rect(var.player_x_pos - var.player_speed, var.player_y_pos - 2, var.player_rect_size,
                                                        var.player_rect_size)
                result = walls.can_player_move(player_rect)
                if not result:
                    can_move = True
            else:
                if not can_move:
                    can_move = True
        if var.player_x_pos + var.player_rect_size < width:
            if can_move:
                var.player_x_pos += var.player_speed

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
