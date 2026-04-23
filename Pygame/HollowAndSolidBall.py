import pygame
pygame.init()
window = pygame.display.set_mode((400, 400))
green = (0, 255, 0)
pygame.draw.circle(window, green, (300, 300), 50)
pygame.draw.circle(window, green, (300, 300), 50, 3)
pygame.display.update()
done = False
while not done:
    if pygame.event.get() == pygame.QUIT:
        pygame.quit()
    pygame.display.flip()