import pygame

pygame.mixer.init()
#set a sound for shooting to a vairable so we can work with it in alien invasion
bullet_sound = pygame.mixer.Sound('sounds/phasers3.wav')
bullet_sound.set_volume(0.1)
#set a sound for when the ship is hit and the player dies
hit_ship = pygame.mixer.Sound('sounds/hit.wav')
hit_ship.set_volume(0.2)
#add background music using pygame mixer module
bg_music = pygame.mixer.Sound('sounds/actiontheme-v3.mp3')
bg_music.set_volume(0.2)