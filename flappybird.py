import pygame
import time

black = (0,0,0)
blue = (180, 216, 231)
white = (255,255,255)

pygame.init()

surfaceWidth = 800
surfaceHeight = 500
surface = pygame.display.set_mode((800,400))
pygame.display.set_caption('helicopter')
clock = pygame.time.Clock()

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            contiue
        return event.key

    return None



img = pygame.image.load('Helicopter.png')
def makeTextObjs(text,font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to contiue', smallText)
    titleTextRect.center = surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    surface.blit(typTextSurf, typTextRect)

    pygame.display.update()
    time.sleep(2)

    while replay_or_quit == None:
        clock.tick()

    main()


def gameOver():
    msgSurface('Kaboom!')

def helicopter(x, y, image):
    surface.blit(img, (x, y))

def main():
    x = 150
    y = 200
    y_move = 0 

    game_over = False

    while not game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 5

        y += y_move


        surface.fill(blue)
        helicopter(x, y, img)

        if y > 318 or y < 0:
            gameOver()

        pygame.display.update()
        clock.tick(60)
main()
pygame.quit()
quit()
