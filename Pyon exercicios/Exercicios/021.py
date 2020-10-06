#executar um audio mp3

import pygame
pygame.init()
pygame.mixer.music.load('BlackDog.mp3')
pygame.mixer.music.play()
pygame.event.wait()
