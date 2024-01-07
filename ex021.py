import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
# Aguarda até que a música termine de tocar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Controla a velocidade do loop para reduzir uso de CPU
# Quando a música termina, o programa encerra
