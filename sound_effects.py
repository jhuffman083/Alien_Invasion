import pygame

pygame.mixer.init()
#set a sounnd for shooting to a vairable so we can work with it in alien invasion
bullet_sound = pygame.mixer.Sound('sounds/phasers3.wav')
#set a sounnd for killing an alien to a vairable so we can work with it in alien invasion
explosion_sound = pygame.mixer.Sound('sounds/explosion.mp3')
#set a sound for ehen the ship is hit and the player dies
hit_ship = pygame.mixer.Sound('sounds/hit.wav')
