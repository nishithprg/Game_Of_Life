import pygame
import os 
import grid
import fileParser

screen_width = 600
screen_height = 600
screen = 0

folder = "Examples/"

input_file = input("Name of the input file : ").strip()
while(not os.path.exists(folder + input_file)):
    print(input_file + " : Doesn't exist in folder again")
    input_file = input("Name of the input file : ").strip()
print("Done")
# Instantiate parser
parse = fileParser.Parser(folder + input_file)
parse.parseInputFile()
print(parse.rows, parse.columns)


# Instantiate the grid
jdv = grid.Grid(parse, screen_width, screen_height)

if(jdv.isJdV):
    # Initialising variables for pygame
    os.environ["SDL_VIDEO_CENTERED"]='1'
    pygame.init()
    pygame.display.set_caption("Jeu de vie")
    screen = pygame.display.set_mode((screen_width, screen_height))

count = 0
while(True):
    if(count <= parse.num_evolutions):
        print("Generation : " + str(count+1))
        if(jdv.isJdV and jdv.aType == '2D'):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    pygame.quit()
                    exit(0)
            screen.fill((0,0,0))
            jdv.JeuDeVie(screen)
            pygame.display.update()
            pygame.time.delay(300)
        elif(jdv.aType == '1D' or jdv.aType == '2D'):
            jdv.nextGenerationGrid()
            jdv.printGrid()
        else:
            print("Invalid input file format")
            exit(0)
        count += 1
    else:
        if(jdv.isJdV):
            for event in pygame.event.get():
                    if(event.type == pygame.QUIT):
                        pygame.quit()
                        exit(0)
        else:
            break

