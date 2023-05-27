# space_escaper
# importing the libries
import pygame
import random
import time

# font
pygame.font.init()

# defing or i would say variable

height = 600
width = 700


windows = pygame.display.set_mode((height,width))
pygame.display.set_caption("Escaper by wahid najim")
background = pygame.transform.scale(pygame.image.load("bg_flying.jpg"), (width, height))



playerwidth = 40
playerheight = 60

playervelo = 5
ball_width = 10
ball_height = 20
ballvelo = 3

FONT = pygame.font.SysFont("comicsans", 30)






def draw(player,passed_time,ball):
    windows.blit(background, (0, 0))
    
    time_text = FONT.render(f"Time: {round(passed_time)}s", 1, "white")
    windows.blit(time_text, (10, 10))
    pygame.draw.rect(windows,"blue",player)

    for ball in ball:
        pygame.draw.rect(windows, "white", ball)

    pygame.display.update()


def maingame():
    run = True

    player = pygame.Rect(200, height - playerheight,
                         playerwidth, playerheight)
    clock = pygame.time.Clock()
    start_time = time.time()
    passed_time = 0

    ball_added = 2000
    ball_count = 0

    ball = []
    hit = False

    while run:
        star_count += clock.tick(60)
        passed_time = time.time() - start_time

        if ball_count > ball:
            for _ in range(3):
                ball_y = random.randint(0, height - ball_height)
                ball = pygame.Rect(ball, -ball_height,
                                   ball_width, ball_height)
                ball.append(balls)

            ball_added = max(200, ball_added - 50)
            ball_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - playervelo >= 0:
            player.x -= playervelo
        if keys[pygame.K_RIGHT] and player.x + playervelo + player.width <= width:
            player.x += playervelo

        for balls in ball[:]:
            ball.y += ballvelo
            if ball.y > height:
                ball.remove(ball)
            elif ball.y + ball.height >= player.y and ball.colliderect(player):
                ball.remove(ball)
                hit = True
                break

        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            windows.blit(lost_text, (width/2 - lost_text.get_width()/2, height/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, passed_time, ball)

    pygame.quit()




if __name__ == "__main__":
    main()

