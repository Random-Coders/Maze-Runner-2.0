# goes under background and movement
def collision(x,y):
    gameWindow.blit(collision, (x,y))


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    gameExit = False
    gameMove = True

    while not gameExit and gameMove == True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 gameExit = False

            if event.type ==pygame.KEYDOWN:
               if event.key == pygame.K_LEFT:
                   x_change = -5
               if event.key == pygame.K_RIGHT:
                   x_change = 5
           if event.type == pygame.KEYUP:
               if event.key == pygame.K_LEFTor event.key == pygame.K_RIGHT:
                      x_change = 0
       x += x_change

       gameWindow.fill(white)
       collision(x,y)

       if x > display_width - background_width or x < 0:
            gameMove = False
       elif x < display_width - background_width or x > 0:
                gameMove = True

       pygame.display.update()
       clock.tick(60)


game_loop()
pygame.quit()
