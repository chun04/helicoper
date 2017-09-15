import time
from random import randint,randrange
import pygame



blue = (135,206,250)
black = (0,0,0)
white = (255,255,255)
red = (255,69,0)


sunset = (253,72,47)
white = (255,255,255)
brightblue = (47,228,253)
yellow = (225,236,0)
purple = (253,67,255)

colorchoices = [sunset,white,brightblue,yellow,purple]

pygame.init()

x_button = 100
y_button = 500
button_height = 200
button_width = 100

surfaceWidth = 800
surfaceHeight = 500

imageHeight = 45
imageWidth = 82

surface = pygame.display.set_mode((surfaceWidth,surfaceHeight))
pygame.display.set_caption('Helicopter')
clock = pygame.time.Clock()

img = pygame.image.load('Helicopter.png')

def score(count):
    font = pygame.font.Font('freesansbold.ttf', 20)
    text = font.render('Score: '+str(count), True, white)
    surface.blit(text, [0,0])

def blocks(x_block, y_block, block_width, block_height, gap, colorchoice):
    pygame.draw.rect(surface, colorchoice, [x_block,y_block,block_width,block_height])
    pygame.draw.rect(surface, colorchoice, [x_block,y_block+block_height+gap,block_width, surfaceHeight])


def button(x_button, y_button, button_width, button_height):
    pygame.draw.rect(surface, red, [x_button,y_button,button_width,button_height])

    

def replay_or_quit():
    for event in pygame.event.get([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            continue

        return event.key
    
    return None

def makeTextObjs(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()

def msgSurface(text):
    smallText = pygame.font.Font('freesansbold.ttf', 20)
    largeText = pygame.font.Font('freesansbold.ttf', 150)

    titleTextSurf, titleTextRect = makeTextObjs(text, largeText)
    titleTextRect.center = surfaceWidth / 2, surfaceHeight / 2
    surface.blit(titleTextSurf, titleTextRect)

    typTextSurf, typTextRect = makeTextObjs('Press any key to continue', smallText)
    typTextRect.center =  surfaceWidth / 2, ((surfaceHeight / 2) + 100)
    buttons = button(x_button,y_button,button_width,button_height)
    surface.blit(typTextSurf, typTextRect,buttons)

    


    pygame.display.update()
    time.sleep(1)

    while replay_or_quit() == None:
        clock.tick()

    main()

    

def gameOver():
    msgSurface('Kaboom!')

    
    
def helicopter(x, y, image):
    surface.blit(img, (x,y))


def main():
    x = 150
    y = 200
    y_move = 0

    x_block = surfaceWidth
    y_block = 0

    block_width = 75
    block_height = randint(0,(surfaceHeight/2))
    gap = 135
    block_move = 6


    
    
    game_over = False

    current_score = 0
    blockcolor = colorchoices[randrange(0,len(colorchoices))]
    while not game_over:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_move = -4
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_move = 4

        y += y_move

        surface.fill(blue)
        helicopter(x ,y, img)
        score(current_score)

        blocks(x_block, y_block, block_width, block_height, gap, blockcolor)
        x_block -= block_move

        if y > surfaceHeight-40 or y < 0:
            gameOver()

        if x_block < (-1*block_width):
            x_block = surfaceWidth
            block_height = randint(0, (surfaceHeight / 2))
            blockcolor = colorchoices[randrange(0,len(colorchoices))]


        if x + imageWidth > x_block:
            if x < x_block + block_width:
                #print('posssibly within the boundaries of x')
                if y < block_height:
                    #print ("y crossover upper")
                    if x - imageWidth < block_width + x_block:
                        #print ('gg hit upper')
                        gameOver()
        if x + imageWidth > x_block:
            #print('x cross over')

            if y + imageHeight > block_height+gap:
                #print ("y cross over")

                if x < block_width + x_block:
                    #print("gg lower")
                    gameOver()

        if x_block < (x - block_width) < x_block + block_move:
            current_score += 1
            

        if 8 <= current_score < 13:
            block_move = 7
            gap = 130

        if 13 <= current_score < 16:
            block_move = 8
            gap = 125

        if 16 <= current_score < 20:
            block_move = 9
            gap = 120

        if 20 <= current_score < 26:
            block_move = 10
            gap = 115
            

        pygame.display.update()
        clock.tick(60)

main()
pygame.quit()
quit()















    















    
