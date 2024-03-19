import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
speed_x = 5
speed_y = 5
x = 400
y = 300
clock = pygame.time.Clock()
radius = 25

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y - radius > 0:
        y -= 20
    if pressed[pygame.K_DOWN] and y + radius < 600:
        y += 20
    if pressed[pygame.K_LEFT] and x - radius > 0:
        x -= 20
    if pressed[pygame.K_RIGHT] and x + radius < 800:
        x += 20
    
    if x - radius <= 0 or x + radius >= 800:
        speed_x *= -1
    if y - radius <= 0 or y + radius >= 600:
        speed_y *= -1
    

    screen.fill((0, 0, 0))
    color = (255, 0, 0)
    pygame.draw.circle(screen, color, (x, y), radius)

    clock.tick(60)
    pygame.display.flip()
