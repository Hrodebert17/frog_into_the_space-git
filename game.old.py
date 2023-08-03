import pygame
from pygame import mixer
import sys
import os
import random

if __name__ == "__main__":
    pygame.init()
# variables setup

jump_force = 0
meteorite_img_path = "assets/image/meteorite.png"
meteorite_img = pygame.transform.scale(pygame.image.load(meteorite_img_path), (20 * 2, 48 * 2))
Plane_Path = "assets/image/plane_0000_Layer-4.png"
plane = pygame.transform.scale(pygame.image.load(Plane_Path), (302 // 2, 95 // 2))
Plane_Path2 = "assets/image/plane_0001_Layer-3.png"
plane2 = pygame.transform.scale(pygame.image.load(Plane_Path2), (302 // 2, 95 // 2))
plane_rotated = pygame.transform.flip(plane, True, False)
plane_rotated2 = pygame.transform.flip(plane2, True, False)
font_path = os.path.join("assets", "fonts", "SuperMario256.ttf")
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
player_rect_size = 60
player_rect_color = (255, 0, 0)
player_y_pos = int((height / 2) - player_rect_size / 2)
player_x_pos = int((width / 2) - player_rect_size / 2)
Now_time = 0
jump_cd = None
Max_fps = int(60)
transparent_surface = pygame.Surface((100, 50), pygame.SRCALPHA)
falling_speed = 0
player_speed = 5
meter_counter = 1
black = (0, 0, 0)
red = (255, 0, 0)
white = (255, 255, 255)
font = pygame.font.Font(font_path, 60)
enemy = []
game_over = False
game_over_rendered = False
invulnerable = True
main_menu = True
pygame.display.set_caption("Lamb into the space")
start_img = pygame.transform.scale(pygame.image.load("assets/image/start_btn.png"), (279 / 2, 126 / 2))
bomb = pygame.transform.scale(pygame.image.load("assets/image/bomb.png"), (20, 40))
retry_button = pygame.transform.scale(pygame.image.load("assets/image/retry.png"), (279 / 2, 126 / 2))
bg = None
rendering = None
actual_level = 0
starter_time = 0
helicopter = pygame.transform.scale(pygame.image.load("assets/image/helicopter.png"), (426 / 2, 170 / 2))
heart = pygame.transform.scale(pygame.image.load("assets/image/heart.png"), (60, 60))
bullet = pygame.transform.scale(pygame.image.load("assets/image/bullet.png"), (39 * 2, 8 * 2))
player_lives = int(1)
booster_list = []
render_level_subpart = 1
sub_part_rendered = 1
chance_of_spawning_power_up = 0
number_to_spawn_power_up = 2
started_guess = 0
bullet_speed = 40
scope_red = pygame.image.load("assets/image/scope_red.png")
scope_green = pygame.image.load("assets/image/scope_green.png")
Missile = pygame.image.load("assets/image/missle.png")
jumping = False
friction = None
jet_pack = pygame.transform.scale(pygame.image.load("assets/image/jetpack.png"), (352 / 4, 356 / 4))
jet_pack_starter_time = 0
jet_pack_using = False
player_gets_power_up = pygame.mixer.Sound("assets/sfx/player_picks_up_power_up.wav")
music = pygame.mixer.Sound("assets/sfx/music.wav")
pygame.mixer.Sound.set_volume(music, 0.2)
is_player_running = False
direction = "right"
wall_list = []
wall_texture = pygame.transform.scale(pygame.image.load("assets/image/wall.jpg"), (100, 100))
running_sprite_1 = pygame.transform.scale(pygame.image.load("assets/image/running/tile000.png"), (60, 60))
running_sprite_2 = pygame.transform.scale(pygame.image.load("assets/image/running/tile001.png"), (60, 60))
running_sprite_3 = pygame.transform.scale(pygame.image.load("assets/image/running/tile002.png"), (60, 60))
running_sprite_4 = pygame.transform.scale(pygame.image.load("assets/image/running/tile003.png"), (60, 60))
running_sprite_5 = pygame.transform.scale(pygame.image.load("assets/image/running/tile004.png"), (60, 60))
running_sprite_6 = pygame.transform.scale(pygame.image.load("assets/image/running/tile005.png"), (60, 60))
running_sprite_7 = pygame.transform.scale(pygame.image.load("assets/image/running/tile006.png"), (60, 60))
running_sprite_8 = pygame.transform.scale(pygame.image.load("assets/image/running/tile007.png"), (60, 60))
running_sprite_9 = pygame.transform.scale(pygame.image.load("assets/image/running/tile008.png"), (60, 60))
running_sprite_10 = pygame.transform.scale(pygame.image.load("assets/image/running/tile009.png"), (60, 60))
running_sprite_11 = pygame.transform.scale(pygame.image.load("assets/image/running/tile010.png"), (60, 60))
running_sprite_12 = pygame.transform.scale(pygame.image.load("assets/image/running/tile011.png"), (60, 60))
running_sprites = [running_sprite_1, running_sprite_2, running_sprite_3, running_sprite_4, running_sprite_5,
                   running_sprite_6, running_sprite_7, running_sprite_8, running_sprite_9, running_sprite_10,
                   running_sprite_11, running_sprite_12]
player_list = []
idle_sprite_1 = pygame.transform.scale(pygame.image.load("assets/image/idle/tile000.png"), (60, 60))
idle_sprite_2 = pygame.transform.scale(pygame.image.load("assets/image/idle/tile001.png"), (60, 60))
idle_sprite_3 = pygame.transform.scale(pygame.image.load("assets/image/idle/tile002.png"), (60, 60))
idle_sprite_4 = pygame.transform.scale(pygame.image.load("assets/image/idle/tile003.png"), (60, 60))
idle_sprite_5 = pygame.transform.scale(pygame.image.load("assets/image/idle/tile004.png"), (60, 60))
idle_sprite_6 = pygame.transform.scale(pygame.image.load("assets/image/idle/tile005.png"), (60, 60))
idle_sprite_7 = pygame.transform.scale(pygame.image.load("assets/image/idle/tile006.png"), (60, 60))
idle_sprite_8 = pygame.transform.scale(pygame.image.load("assets/image/idle/tile007.png"), (60, 60))
idle_sprite_9 = pygame.transform.scale(pygame.image.load("assets/image/idle/tile008.png"), (60, 60))
idle_sprite_10 = pygame.transform.scale(pygame.image.load("assets/image/idle/tile009.png"), (60, 60))
idle_sprite_11 = pygame.transform.scale(pygame.image.load("assets/image/idle/tile010.png"), (60, 60))
idle_spite_list = [idle_sprite_1,idle_sprite_2,idle_sprite_3,idle_sprite_4,idle_sprite_5,idle_sprite_6,idle_sprite_7,idle_sprite_8,idle_sprite_9,idle_sprite_10,idle_sprite_11]

jumping_sprite = pygame.transform.scale(pygame.image.load("assets/image/jump.png"), (60,60))


# classes

class player_sprite:
    def __init__(self):
        global player_x_pos, player_y_pos, player_list
        self.loaded_sprite_run = 0
        self.current_sprite = 0
        player_list.append(self)
        self.direction = False
        self.xpos = player_x_pos
        self.loaded_idle_sprite = 0

    def walk(self):
        global player_y_pos, player_x_pos, running_sprites,direction,idle_spite_list,jumping,jumping_sprite
        if not jumping:
            print(self.xpos,player_x_pos)
            if self.xpos != player_x_pos:
                if direction == "right":
                    self.direction = True
                else:
                    self.direction = False
                self.loaded_sprite_run += 0.5
                if int(self.loaded_sprite_run) > len(running_sprites):
                    self.loaded_sprite_run = 0
                screen.blit(pygame.transform.flip(running_sprites[int(self.loaded_sprite_run) - 1], self.direction,False), (player_x_pos, player_y_pos))
                self.xpos = player_x_pos
            else:
                self.loaded_sprite_run = 0
                self.loaded_idle_sprite += 0.5
                if int(self.loaded_idle_sprite) > len(idle_spite_list):
                    self.loaded_idle_sprite = 0
                screen.blit(pygame.transform.flip(idle_spite_list[int(self.loaded_idle_sprite) - 1], self.direction, False),
                            (player_x_pos, player_y_pos))
        else:
            screen.blit(pygame.transform.flip(jumping_sprite, self.direction, False),
                        (player_x_pos, player_y_pos))





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
        global player_y_pos, player_x_pos, player_rect_size
        answer = pygame.Rect.colliderect(self.rectangle, player_rect)
        if answer:
            pos_modificator = 0
            position = 0
            while True:
                pygame.Rect(player_x_pos, player_y_pos, player_rect_size, player_rect_size)
                position1 = player_y_pos - pos_modificator
                position2 = player_y_pos + pos_modificator
                position3 = player_x_pos - pos_modificator
                position4 = player_x_pos + pos_modificator
                if not pygame.Rect.colliderect(self.rectangle, pygame.Rect(player_x_pos, position1, player_rect_size,
                                                                           player_rect_size)):
                    player_y_pos -= pos_modificator
                    break
                elif not pygame.Rect.colliderect(self.rectangle, pygame.Rect(player_x_pos, position2, player_rect_size,
                                                                             player_rect_size)):
                    player_y_pos += pos_modificator
                    break
                if not pygame.Rect.colliderect(self.rectangle, pygame.Rect(position3, player_y_pos, player_rect_size,
                                                                           player_rect_size)):
                    player_x_pos -= pos_modificator
                    break
                elif not pygame.Rect.colliderect(self.rectangle, pygame.Rect(position4, player_y_pos, player_rect_size,
                                                                             player_rect_size)):
                    player_x_pos += pos_modificator
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
        player_rect = pygame.Rect(player_x_pos, player_y_pos, player_rect_size, player_rect_size)
        # second we define the booster rectangle
        boosters = pygame.Rect(self.x_position, self.y_position, self.width, self.height)
        # third we cheek if the player rectangle is inside the booster rectangle
        if player_rect.colliderect(boosters):
            # now we give the effect to the player
            booster_list.pop(self.booster_id - 1)
            player_gets_power_up.play()
            if self.type == "heart":
                player_lives += 1
            elif self.type == "jet_pack":
                jet_pack_starter_time = Now_time
                jet_pack_using = True


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
                    if Now_time is not None:
                        if self.minion_cd + 60 <= Now_time:
                            enemy_class(self.x_position, self.yaxis, "bomb", randomise_x_When_off_screen=False, speed=5,
                                        can_summon_minions=False)
                            self.minion_cd = Now_time
            elif self.type == "plane2":
                if self.minions:
                    if Now_time is not None:
                        if self.minion_cd + 60 <= Now_time:
                            enemy_class(self.x_position, self.yaxis, "bomb", randomise_x_When_off_screen=False, speed=5,
                                        can_summon_minions=False)
                            self.minion_cd = Now_time
                self.x_position -= self.enemy_speed
            elif self.type == "helicopter":
                if self.minions:
                    if Now_time is not None:
                        if self.minion_cd + 120 <= Now_time:
                            enemy_class(self.x_position + self.size_width, self.yaxis + self.size_height / 2, "bullet1",
                                        randomise_x_When_off_screen=False, speed=5, can_summon_minions=False)
                            self.minion_cd = Now_time
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
                if player_y_pos < self.yaxis:
                    self.yaxis -= 3
                elif player_y_pos > self.yaxis:
                    self.yaxis += 3
                screen.blit(helicopter, (self.x_position, self.yaxis))
            elif self.type == "scope":
                if self.locked_time >= 100:
                    self.x_position = player_x_pos
                    self.yaxis = player_y_pos
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
                    if player_x_pos > self.x_position:
                        self.x_position += self.enemy_speed
                    elif player_x_pos < self.x_position:
                        self.x_position -= self.enemy_speed
                    if player_y_pos < self.yaxis:
                        self.yaxis -= self.enemy_speed
                    elif player_y_pos > self.yaxis:
                        self.yaxis += self.enemy_speed

                if self.locking:
                    screen.blit(scope_green, (self.x_position, self.yaxis))
                else:
                    screen.blit(scope_red, (self.x_position, self.yaxis))
            elif self.type == "Missile":
                print(player_y_pos, self.yaxis)
                if player_y_pos <= self.yaxis:
                    self.angle = 0
                    print("self.yaxis < player_y_pos")
                else:
                    self.angle = -180
                if player_x_pos >= self.x_position:
                    if self.angle == 0:
                        self.angle = -40
                    if self.angle == -180:
                        self.angle = -140
                elif player_x_pos <= self.x_position:
                    if self.angle == -180:
                        self.angle = 140
                    if self.angle == 0:
                        self.angle = 40
                if self.x_position - 100 <= player_x_pos <= self.x_position + 100 and self.yaxis > player_y_pos:
                    self.angle = 0
                if self.x_position - 100 <= player_x_pos <= self.x_position + 100 and self.yaxis < player_y_pos:
                    self.angle = -180
                if player_y_pos > self.yaxis:
                    self.yaxis += self.enemy_speed
                if player_y_pos < self.yaxis:
                    self.yaxis -= self.enemy_speed
                if player_x_pos > self.x_position:
                    self.x_position += self.enemy_speed
                if player_x_pos < self.x_position:
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
                    if self.name == "play":
                        main_menu = False

                    elif self.name == "retry":
                        global actual_level, rendering, game_over, game_over_rendered, invulnerable, starter_time
                        global meter_counter
                        meter_counter = 0
                        rendering = None
                        game_over = False
                        game_over_rendered = False
                        invulnerable = True
                        starter_time = Now_time
                        enemy.clear()
                        render_level(actual_level)


# functions

# sound stopper
def clear_sounds():
    pygame.mixer.Channel(1).stop()


# render levels
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


# create texts
def draw_text(text, font_for_the_thext, color, x, y):
    text_surface = font_for_the_thext.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text_surface, text_rect)
    return text_surface, text_rect.size


# screen render

def render_main_menu():
    global main_menu
    screen.fill("white")
    play = Button(30, 30, start_img, name="play")
    play.draw_button()
    pygame.display.flip()
    clock.tick(Max_fps)


def physics():
    global game_over, player_y_pos, falling_speed, meter_counter, jumping, friction, jump_force, jet_pack_using
    global jet_pack_starter_time, booster_list, player_lives, invulnerable, starter_time

    if not game_over:
        # gravity system

        # cheeks if the player is jumping or not and if it is the script cheeks if it has a power up and
        # it makes the gravity different in base of the player attributes
        if not jumping:

            if jet_pack_using:
                falling_speed = 0
            # if the player is off-screen
            if player_y_pos >= height - player_rect_size:
                # disables the fall and makes the player stay on screen
                falling_speed += 0.5
                player_y_pos = height - player_rect_size
            else:
                # if the player is not off-screen make the player fall
                can_move = False
                for walls in wall_list:
                    player_rect = player_rect = pygame.Rect(player_x_pos, player_y_pos + int(falling_speed) + 1,
                                                            player_rect_size,
                                                            player_rect_size)
                    result = walls.can_player_move(player_rect)
                    walls.physics()
                    if result:
                        can_move = False
                    else:
                        if not can_move:
                            can_move = True
                if can_move:
                    falling_speed += 0.5
                    player_y_pos += int(falling_speed)
                else:
                    falling_speed = 0

            # meter counter cant be smaller then 0
            if meter_counter >= 0 and meter_counter != 0:
                # meter falling manager if the falling speed /4 is not bigger than 200(max value of falling speed)
                # then It's ok for setting the meter_counter: meter_counter - falling_speed / 4
                if falling_speed / 4 < 200:
                    meter_counter -= falling_speed / 4
                else:
                    # if falling speed /4 is bigger than 200 then meter_counter is going to be at meter_counter - 200
                    meter_counter -= 200
            else:
                meter_counter = 0
        else:
            # if the player is jumping then the meter counter will be added 20
            # for every frame sets the meter counter to + 20
            meter_counter += 20
            # by setting falling speed to 0 we make so the acceleration counter starts from 0
            falling_speed = 0
            # the "friction" is a counter that makes the acceleration less strong at the moment the game gets at
            # that frame making a jump effect with a speed loss whit time
            if friction <= Now_time - 10:
                # slows down the jump speed
                jump_force -= 1
                # makes the player y be higher
                can_move = False
                for walls in wall_list:
                    walls.physics()
                    player_rect = player_rect = pygame.Rect(player_x_pos, player_y_pos - jump_force * 3,
                                                            player_rect_size,
                                                            player_rect_size)
                    result = walls.can_player_move(player_rect)
                    if result:
                        can_move = False
                    else:
                        if not can_move:
                            can_move = True
                if can_move:
                    player_y_pos -= jump_force * 3
                else:
                    player_y_pos -= 1
                # resets the counter for the jump speed diminution
                friction = Now_time
            else:
                # makes the player go higher
                can_move = False
                for walls in wall_list:
                    player_rect = player_rect = pygame.Rect(player_x_pos, player_y_pos - jump_force * 3,
                                                            player_rect_size,
                                                            player_rect_size)
                    result = walls.can_player_move(player_rect)
                    if result:
                        can_move = False
                    else:
                        if not can_move:
                            can_move = True
                if can_move:
                    player_y_pos -= jump_force * 3
                else:
                    player_y_pos -= 1
                # brakes the loop if the player has no more jumping force
                if jump_force == 0:
                    jumping = False
        if jet_pack_using:
            if jet_pack_starter_time < Now_time - 360:
                jet_pack_using = False

        # collision handler:

        # first we will put for in loop, so we can do an action like calling a function for every class
        for power_up in booster_list:
            # we call the designated function for every object of the class power up
            power_up.booster_detect_collisions()

        # now we cheek if any enemy rect is colliding with the player by first specific the player rect and the enemy
        # rect then we cheek if they are colliding whit player_rect.colliderect(enemy_rect): which is a function
        # of pygame

        for enemy_npc in enemy:
            enemy_rect = pygame.Rect(enemy_npc.x_position, enemy_npc.yaxis, enemy_npc.size_width,
                                     enemy_npc.size_height)
            player_rect = pygame.Rect(player_x_pos, player_y_pos - jump_force * 3, player_rect_size, player_rect_size)
            if player_rect.colliderect(enemy_rect):
                # after knowing that the player is colliding or now then we are able to call the enemy action
                # which could be to lose a life or to spawn a mile
                if not invulnerable:
                    if enemy_npc.type != "scope":
                        player_lives -= 1
                        starter_time = Now_time
                        invulnerable = True
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
    if not game_over:
        # if the player is higher than 10000 meters
        if meter_counter > 10000:
            # here we cheek if the player has the requirements to enter stage 2
            if render_level_subpart <= 2 and render_level_subpart == 1:
                # we enter stage 2
                render_level_subpart = 2
        if meter_counter > 20000:
            if render_level_subpart <= 3 and render_level_subpart == 2:
                render_level_subpart = 3
        if meter_counter > 30000:
            if render_level_subpart <= 4 and render_level_subpart == 3:
                render_level_subpart = 4

        # cheeks if the spawning chance for power up is enabled
        if chance_of_spawning_power_up != 0:
            # makes a clock that cheeks it every 1/3 of second
            if Now_time - 20 > started_guess:
                # makes a random number that if it's the same as the winner number then a power up spawns
                casual_number = random.randint(0, chance_of_spawning_power_up)
                started_guess = Now_time
                if number_to_spawn_power_up == casual_number:
                    if len(booster_list) == 0:
                        booster(booster_type="random", x_position=int(random.randint(70, width - 70)),
                                y_position=int(random.randint(70, height - 70)))

        # renders every object calling they're rendering option or rendering them manually + it handles the gravity
        # system render the game here V
        screen.fill("white")

        # renders the requested level
        render_level(1)
        if jet_pack_using:
            screen.blit(jet_pack, (player_x_pos - player_rect_size / 4, player_y_pos - 10))
        # pygame.draw.rect(screen, player_rect_color,
        #                pygame.Rect(player_x_pos, player_y_pos, player_rect_size, player_rect_size), )
        print(player_list)
        for player in player_list:
            player.walk()
        screen.blit(heart, ((width - 60) - 20, 20))
        draw_text(str(int(player_lives)), font, black, (width - 120) - 20, 30)

        for boosters in booster_list:
            boosters.render_booster()
        for enemy_npc in enemy:
            enemy_npc.render()
        for walls in wall_list:
            walls.render_wall()
        draw_text(str(int(meter_counter)), font, black, 20, 20)

        # don't put anything under this V
        pygame.display.flip()

        # getting the frame we are in
        if Now_time is None:
            Now_time = 1
            starter_time = Now_time
        else:
            Now_time += 1
        if invulnerable:
            if (Now_time - 180) >= starter_time:
                invulnerable = False

        # top border
        if player_y_pos < 0:
            player_y_pos = 0

        # falling system
        if meter_counter == 0 or meter_counter <= 0:
            if not invulnerable:
                player_lives -= 1
        if player_lives == 0:
            game_over = True

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
        if jump_cd is None or jump_cd <= (Now_time - 70):
            # sets a jump cd gives the player a jump force and sets the jumping var to true
            jump_cd = Now_time
            jump_force = 4
            falling_speed = 0
            jumping = True
            friction = Now_time
            jump = pygame.mixer.Sound("assets/sfx/jump.mp3")
            pygame.mixer.Sound.play(jump)
            player_y_pos -= 2

    if keys[pygame.K_a]:
        can_move = False
        direction = "right"
        returns = []
        for walls in wall_list:
            player_rect = player_rect = pygame.Rect(player_x_pos - player_speed, player_y_pos + 2, player_rect_size,
                                                    player_rect_size)
            result = walls.can_player_move(player_rect)
            if result:
                can_move = False
                player_rect = player_rect = pygame.Rect(player_x_pos - player_speed - 20, player_y_pos - 2,
                                                        player_rect_size,
                                                        player_rect_size)
                result = walls.can_player_move(player_rect)
                if not result:
                    can_move = True
            else:
                if not can_move:
                    can_move = True
        if can_move:
            if player_x_pos - 1 >= 0:
                player_x_pos -= player_speed
    if keys[pygame.K_d]:
        can_move = False
        direction = "left"
        for walls in wall_list:
            player_rect = player_rect = pygame.Rect(player_x_pos + player_speed - 20, player_y_pos + 2,
                                                    player_rect_size,
                                                    player_rect_size)
            result = walls.can_player_move(player_rect)
            if result:
                can_move = False
                player_rect = player_rect = pygame.Rect(player_x_pos - player_speed, player_y_pos - 2, player_rect_size,
                                                        player_rect_size)
                result = walls.can_player_move(player_rect)
                if not result:
                    can_move = True
            else:
                if not can_move:
                    can_move = True
        if player_x_pos + player_rect_size < width:
            if can_move:
                player_x_pos += player_speed

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


# runs the game in a loop.
while running is True:
    # search for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not main_menu:
        # calls the key handler
        key_handler()
        if not game_over_rendered:
            # updates the screen
            physics()
            screen_updater()
    else:
        render_main_menu()

# closes pygame after the loop.
pygame.quit()
sys.exit()
