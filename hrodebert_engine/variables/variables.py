import pygame
from pygame import mixer
import sys
import os
import random


pygame.init()

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
events = []
reached_meter = 0
