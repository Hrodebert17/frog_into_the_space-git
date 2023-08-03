import pygame
import random

import hrodebert_engine
from hrodebert_engine.variables.variables import heart,jet_pack
from hrodebert_engine.engine.functions import *
from hrodebert_engine.variables.variables import *
import hrodebert_engine.engine.functions
import hrodebert_engine.database.database as data
import hrodebert_engine.variables.variables as var

class Button:
    def __init__(self, x, y, image, name):
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.clicked_button = True
        self.name = name

    def draw_button(self):
        global main_menu
        self.rect.x = self.x
        self.rect.y = self.y
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # get mouse pos
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                if self.clicked_button:
                    print("clicked")
                    if self.name == "play":
                        var.main_menu = False

                    elif self.name == "retry":
                        var.meter_counter = 0
                        var.rendering = None
                        var.game_over = False
                        var.game_over_rendered = False
                        var.invulnerable = True
                        var.Now_time = 0
                        var.rendering = None
                        var.starter_time = Now_time
                        var.enemy.clear()
                        var.wall_list.clear()
                        var.player_lives = 1
                        var.render_level_subpart = 1
                        var.sub_part_rendered = 1
                        var.jump_cd = 0
                        var.jumping = False
                        hrodebert_engine.engine.functions.render_level(data.get_variable("LEVEL_REACHED"),True)



class player_sprite:
    def __init__(self):
        self.loaded_sprite_run = 0
        self.current_sprite = 0
        var.player_list.append(self)
        self.direction = False
        self.xpos = var.player_x_pos
        self.loaded_idle_sprite = 0

    def walk(self):
        if not jumping:
            print(self.xpos,var.player_x_pos)
            if self.xpos != var.player_x_pos:
                if var.direction == "right":
                    self.direction = True
                else:
                    self.direction = False
                self.loaded_sprite_run += 0.5
                if int(self.loaded_sprite_run) > len(var.running_sprites):
                    self.loaded_sprite_run = 0
                screen.blit(pygame.transform.flip(running_sprites[int(self.loaded_sprite_run) - 1], self.direction,False), (var.player_x_pos, var.player_y_pos))
                self.xpos = var.player_x_pos
            else:
                self.loaded_sprite_run = 0
                self.loaded_idle_sprite += 0.5
                if int(self.loaded_idle_sprite) > len(idle_spite_list):
                    self.loaded_idle_sprite = 0
                screen.blit(pygame.transform.flip(idle_spite_list[int(self.loaded_idle_sprite) - 1], self.direction, False),
                            (var.player_x_pos, var.player_y_pos))
        else:
            screen.blit(pygame.transform.flip(jumping_sprite, self.direction, False),
                        (var.player_x_pos, var.player_y_pos))





class wall:
    def __init__(self, x_position, y_position, width, height, texture: None, delete_enemy_on_contact: bool):
        global wall_list
        self.width = width
        self.height = height
        self.x_position = x_position
        self.y_position = y_position
        self.rectangle = pygame.Rect(self.x_position, self.y_position, self.width, self.width)
        self.texture = texture
        wall_list.append(self)
        if texture is not None:
            pygame.transform.scale(self.texture, (self.width, self.height))
        self.delete_enemy = delete_enemy_on_contact

    def render_wall(self):
        global red
        # draw:
        if self.texture is None:
            pygame.draw.rect(screen, red, self.rectangle)
        else:
            screen.blit(self.texture, (self.x_position, self.y_position))

    def can_player_move(self, player_rect):
        answer = pygame.Rect.colliderect(self.rectangle, player_rect)
        if answer:
            pos_modificator = 0
            position = 0
            while True:
                pygame.Rect(var.player_x_pos, var.player_y_pos, player_rect_size, player_rect_size)
                position1 = var.player_y_pos - pos_modificator
                position2 = var.player_y_pos + pos_modificator
                position3 = var.player_x_pos - pos_modificator
                position4 = var.player_x_pos + pos_modificator
                if not pygame.Rect.colliderect(self.rectangle, pygame.Rect(var.player_x_pos, position1, player_rect_size,
                                                                           player_rect_size)):
                    var.player_y_pos -= pos_modificator
                    break
                elif not pygame.Rect.colliderect(self.rectangle, pygame.Rect(var.player_x_pos, position2, player_rect_size,
                                                                             player_rect_size)):
                    var.player_y_pos += pos_modificator
                    break
                if not pygame.Rect.colliderect(self.rectangle, pygame.Rect(position3, var.player_y_pos, player_rect_size,
                                                                           player_rect_size)):
                    var.player_x_pos -= pos_modificator
                    break
                elif not pygame.Rect.colliderect(self.rectangle, pygame.Rect(position4, var.player_y_pos, player_rect_size,
                                                                             player_rect_size)):
                    var.player_x_pos += pos_modificator
                    break
                pos_modificator += 1
            return True
        else:
            return False

    def physics(self):
        global enemy
        for entity in enemy:
            enemy_rect = pygame.Rect(entity.x_position, entity.yaxis, entity.size_width, entity.size_height)
            if pygame.Rect.colliderect(self.rectangle, enemy_rect):
                if self.delete_enemy:
                    enemy.remove(entity)


class booster:

    def __init__(self, booster_type: str, x_position, y_position, ):
        global booster_list
        # adds the booster to the booster list (for rendering)
        booster_list.append(self)
        print(booster_list)
        # creates the variables for the booster
        # here we put those variables to create teh booster
        self.type = booster_type
        self.x_position = x_position
        self.y_position = y_position
        self.booster_id = len(booster_list)
        self.width = 60
        self.height = 60
        # here a section of the code which gets a random answer between "heart" and "jetpack" and creates the booster
        # with the current choice
        if booster_type == "random":
            booster_type = random.choice(["heart", "jet_pack"])
            if booster_type == "heart":
                self.type = "heart"
            elif booster_type == "jet_pack":
                self.type = "jet_pack"
                self.width = int(352 / 4)
                self.height = int(356 / 4)

    def render_booster(self):
        global screen, booster_list, player_lives, invulnerable, jet_pack_starter_time, jet_pack_using
        global player_gets_power_up
        # checks which type of booster the self is
        if self.type == "heart":
            screen.blit(heart, (self.x_position, self.y_position))
        elif self.type == "jet_pack":
            screen.blit(jet_pack, (self.x_position, self.y_position))

    def booster_detect_collisions(self):
        global player_lives, jet_pack_starter_time, jet_pack_using
        # detect collisions by:
        # first we define the variable "player rect" which is the player rectangle
        player_rect = pygame.Rect(var.player_x_pos, var.player_y_pos, player_rect_size, player_rect_size)
        # second we define the booster rectangle
        boosters = pygame.Rect(self.x_position, self.y_position, self.width, self.height)
        # third we cheek if the player rectangle is inside the booster rectangle
        if player_rect.colliderect(boosters):
            # now we give the effect to the player
            booster_list.pop(self.booster_id - 1)
            player_gets_power_up.play()
            if self.type == "heart":
                var.player_lives += 1
            elif self.type == "jet_pack":
                var.jet_pack_starter_time = var.Now_time
                var.jet_pack_using = True


class enemy_class:
    def __init__(self, x_position, yaxis, direction: str, randomise_x_When_off_screen: bool, speed,
                 can_summon_minions: bool):
        global enemy, Now_time
        # sets all the variables for the enemy's
        self.loaded_frame = 0
        self.x_position = x_position
        self.yaxis = yaxis
        self.size_width = 60
        self.size_height = 60
        self.enemy_speed = speed
        self.type = direction
        self.change_after_death = randomise_x_When_off_screen
        self.minions = can_summon_minions
        self.minion_cd = 0
        # sets the enemy size
        if direction == "meteor":
            self.size_width = 20 * 2
            self.size_height = 48 * 2
        if direction == "plane1" or direction == "plane2":
            self.size_width = 302 / 2
            self.size_height = 95 / 2
        if direction == "bomb":
            self.size_width = 10
            self.size_height = 20
        if direction == "helicopter":
            self.size_width = 426 / 2
            self.size_height = 170 / 2
        if direction == "bullet1":
            self.size_height = 8 * 2
            self.size_width = 38 * 2
        if direction == "scope":
            self.size_height = 60
            self.size_width = 60
            self.locking = False
            self.locked_time = 0
            self.time_before_disappearing = 0
        if direction == "Missile":
            self.size_height = 134
            self.size_width = 134
            self.starting_time = Now_time
        if direction == "Missile":
            self.angle = 0
        # adds the current enemy to the enemy rendering and collision list
        enemy.append(self)

    def render(self):
        global height, width, transparent_surface, Now_time, bullet_speed
        if self in enemy:
            # this function is used to edit the position / sprites / variables of the enemy, it's called every frame

            # shooting part
            if self.type == "plane1":
                self.x_position += self.enemy_speed
                if self.minions:
                    if var.Now_time is not None:
                        if self.minion_cd + 60 <= var.Now_time:
                            enemy_class(self.x_position, self.yaxis, "bomb", randomise_x_When_off_screen=False, speed=5,
                                        can_summon_minions=False)
                            self.minion_cd = var.Now_time
            elif self.type == "plane2":
                if self.minions:
                    if var.Now_time is not None:
                        if self.minion_cd + 60 <= var.Now_time:
                            enemy_class(self.x_position, self.yaxis, "bomb", randomise_x_When_off_screen=False, speed=5,
                                        can_summon_minions=False)
                            self.minion_cd = var.Now_time
                self.x_position -= self.enemy_speed
            elif self.type == "helicopter":
                if self.minions:
                    if var.Now_time is not None:
                        if self.minion_cd + 120 <= var.Now_time:
                            enemy_class(self.x_position + self.size_width, self.yaxis + self.size_height / 2, "bullet1",
                                        randomise_x_When_off_screen=False, speed=5, can_summon_minions=False)
                            self.minion_cd = var.Now_time
                            mixer.music.load("assets/sfx/bullet.mp3")
                            mixer.music.set_volume(0.3)
                            mixer.music.play()
            # render part were I render all the sprites and rectangles moving the items too
            if self.type == "meteor":
                screen.blit(meteorite_img, (self.x_position, self.yaxis))
            elif self.type == "plane1":
                self.yaxis += 1
                if self.loaded_frame < 60:
                    screen.blit(plane_rotated, (self.x_position, self.yaxis))
                else:
                    screen.blit(plane_rotated2, (self.x_position, self.yaxis))
                if self.loaded_frame > 120:
                    self.loaded_frame = 0
                self.loaded_frame += 1
            elif self.type == "plane2":
                self.yaxis += 1
                if self.loaded_frame < 60:
                    screen.blit(plane, (self.x_position, self.yaxis))
                else:
                    screen.blit(plane2, (self.x_position, self.yaxis))
                if self.loaded_frame > 120:
                    self.loaded_frame = 0
                self.loaded_frame += 1
            elif self.type == "bomb":
                self.yaxis += 10
                screen.blit(bomb, (self.x_position, self.yaxis))
            if self.type == "bullet1":
                self.x_position += bullet_speed
                screen.blit(bullet, (self.x_position, self.yaxis))
            elif self.type == "helicopter":
                if var.player_y_pos < self.yaxis:
                    self.yaxis -= 3
                elif var.player_y_pos > self.yaxis:
                    self.yaxis += 3
                screen.blit(helicopter, (self.x_position, self.yaxis))
            elif self.type == "scope":
                if self.locked_time >= 100:
                    self.x_position = var.player_x_pos
                    self.yaxis = var.player_y_pos
                    if self.time_before_disappearing == 0:
                        self.time_before_disappearing = 1
                    else:
                        self.time_before_disappearing += 1
                    if self.time_before_disappearing >= 120:
                        enemy.remove(self)
                        enemy_class(x_position=-50, yaxis=-50, direction="Missile", randomise_x_When_off_screen=True,
                                    speed=2,
                                    can_summon_minions=True)
                else:
                    if var.player_x_pos > self.x_position:
                        self.x_position += self.enemy_speed
                    elif var.player_x_pos < self.x_position:
                        self.x_position -= self.enemy_speed
                    if var.player_y_pos < self.yaxis:
                        self.yaxis -= self.enemy_speed
                    elif var.player_y_pos > self.yaxis:
                        self.yaxis += self.enemy_speed

                if self.locking:
                    screen.blit(scope_green, (self.x_position, self.yaxis))
                else:
                    screen.blit(scope_red, (self.x_position, self.yaxis))
            elif self.type == "Missile":
                print(var.player_y_pos, self.yaxis)
                if var.player_y_pos <= self.yaxis:
                    self.angle = 0
                    print("self.yaxis < var.player_y_pos")
                else:
                    self.angle = -180
                if var.player_x_pos >= self.x_position:
                    if self.angle == 0:
                        self.angle = -40
                    if self.angle == -180:
                        self.angle = -140
                elif var.player_x_pos <= self.x_position:
                    if self.angle == -180:
                        self.angle = 140
                    if self.angle == 0:
                        self.angle = 40
                if self.x_position - 100 <= var.player_x_pos <= self.x_position + 100 and self.yaxis > var.player_y_pos:
                    self.angle = 0
                if self.x_position - 100 <= var.player_x_pos <= self.x_position + 100 and self.yaxis < var.player_y_pos:
                    self.angle = -180
                if var.player_y_pos > self.yaxis:
                    self.yaxis += self.enemy_speed
                if var.player_y_pos < self.yaxis:
                    self.yaxis -= self.enemy_speed
                if var.player_x_pos > self.x_position:
                    self.x_position += self.enemy_speed
                if var.player_x_pos < self.x_position:
                    self.x_position -= self.enemy_speed
                if self.starting_time <= Now_time - 700:
                    enemy_class(x_position=20, yaxis=20, direction="scope", randomise_x_When_off_screen=True,
                                speed=player_speed - 2, can_summon_minions=True)
                    enemy.remove(self)
                screen.blit(pygame.transform.rotate(Missile, self.angle), (self.x_position, self.yaxis))
            # in this part I decide what to do when the enemy is off-screen which could be start from the beginning or
            # follow a random path
            if self.type == "plane1" and self.x_position > width:
                if self.change_after_death:
                    self.type = "plane2"
                else:
                    self.x_position = (self.size_height * -1) - 20
                    self.yaxis += 60
                    self.enemy_speed = int(random.randint(10, 20))
            elif self.type == "plane2" and self.x_position < 0 - self.size_width:
                if self.change_after_death:
                    self.type = "plane1"
                else:
                    self.x_position = width + self.size_width + 20
                    self.yaxis += 60
                    self.enemy_speed = int(random.randint(10, 20))
            if self.yaxis >= height:
                if self.type != "bomb":
                    self.yaxis = -30
                self.x_position = int(random.randint(20, width - 20))



