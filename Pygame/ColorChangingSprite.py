import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Color Changing Sprite")
    colors = {"red":pygame.Color(255, 0, 0), "white = pygame.Color(255, 255, 255)" "green": pygame.Color(0, 255, 0),"blue": pygame.Color(0, 0, 255),"white": pygame.Color(255, 255, 255),"black": pygame.Color(0, 0, 0),"yellow": pygame.Color(255, 255, 0),"purple": pygame.Color(128, 0, 128),"cyan": pygame.Color(0, 255, 255)},
    current_color = colors["white"]
    x, y = 30, 30
    sprite_width, sprite_height = 60, 60
    pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                done = True
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x -= 3
        elif pressed[pygame.K_RIGHT]:
            x +=3
        elif pressed[pygame.K_UP]:
            y -= 3
        elif pressed[pygame.K_DOWN]:
            y += 3
        x = min(max(0, x), screen_width - sprite_width)
        y = min(max(0, y), screen_height - sprite_height)
        if x == 0:
            current_color = colors("blue")
        elif y == 0:
            current_color = colors("red")
        elif y == screen_height - sprite_height:
            current_color = colors("green")
        else:
            current_color = colors("white")
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        pygame.time.Clock.tick(90)
    pygame.quit()
if __name__ == "__main__":
    main()


