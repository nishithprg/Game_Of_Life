import pygame
import copy

class Grid:
    def __init__(self, parsed_data, width, height):
        self.aType = parsed_data.automataType
        self.rows = parsed_data.rows
        self.columns = parsed_data.columns

        self.scale = None if(self.aType == '1D') else int(width / self.columns)

        self.isJdV = False if len(parsed_data.dead_rules) == 0 else True
        self.grid = copy.deepcopy(parsed_data.initial_grid)
        self.living_rules = copy.deepcopy(parsed_data.living_rules)
        self.dead_rules = copy.deepcopy(parsed_data.dead_rules)

    # Prints current grid's state
    def printGrid(self):
        if(self.aType == '1D'):
            for elem in self.grid:
                print(elem, end=' ')
            print()
        else:
            for i in range(self.rows):
                for j in range(self.columns):
                    print(self.grid[i][j], end=' ')
                print()
        print()

    # Returns a 1D-list with all neighbours of cell[i]
    def formatRule1D(self, i):
        rule = [self.grid[i-1], self.grid[i], self.grid[i+1]]
        return rule

    # Returns a 1D-list with all neighbours of cell[i][j]
    def formatRule2D(self, i, j):
        rule = []
        if(i == 0):
            if(j == 0):
                rule = [0, 0, 0, 0, self.grid[i][j], self.grid[i][j+1], 0, self.grid[i+1][j], self.grid[i+1][j+1]]
            elif( j == self.columns-1):
                rule = [0, 0, 0, self.grid[i][j-1], self.grid[i][j], 0, self.grid[i+1][j-1], self.grid[i+1][j], 0]
            else:
                rule = [0, 0, 0, self.grid[i][j-1], self.grid[i][j], self.grid[i][j+1], self.grid[i+1][j-1], self.grid[i+1][j], self.grid[i+1][j+1]]
        elif(i == self.rows-1):
            if(j == 0):
                rule = [0, self.grid[i-1][j], self.grid[i-1][j+1], 0, self.grid[i][j], self.grid[i][j+1], 0, 0, 0]
            elif( j == self.columns-1):
                rule = [self.grid[i-1][j-1], self.grid[i-1][j], 0, self.grid[i][j-1], self.grid[i][j], 0, 0, 0, 0]
            else:
                rule = [self.grid[i-1][j-1], self.grid[i-1][j], self.grid[i-1][j+1], self.grid[i][j-1], self.grid[i][j], self.grid[i][j+1], 0, 0, 0]
        else:
            if(j == 0):
                rule = [0, self.grid[i-1][j], self.grid[i-1][j+1], 0, self.grid[i][j], self.grid[i][j+1], 0, self.grid[i+1][j], self.grid[i+1][j+1]]
            elif( j == self.columns-1):
                rule = [self.grid[i-1][j-1], self.grid[i-1][j], 0, self.grid[i][j-1], self.grid[i][j], 0, self.grid[i+1][j-1], self.grid[i+1][j], 0]
            else:
                rule = [self.grid[i-1][j-1], self.grid[i-1][j], self.grid[i-1][j+1], self.grid[i][j-1], self.grid[i][j], self.grid[i][j+1], self.grid[i+1][j-1], self.grid[i+1][j], self.grid[i+1][j+1]]
        return rule

    # Return evoled cell value if rule in array
    def matchElem(self, array, rule):
        return [item[1] for item in array if str(item[0]) == str(rule)]

    # Applies a rule on cell[i][j] in next generation grid
    def applyRule(self, next, i, j=None):
        #Rule evaluation for regular 1-D cellular automata
        if(j == None):
            rule = self.formatRule1D(i)
            tmp = self.matchElem(self.living_rules, rule)
            if(len(tmp) == 1):
                next[i] = tmp[0]
            elif(len(tmp) > 1): 
                print("Transition ambiguity, rule : " + str(rule))
                exit(0)
            else:
                next[i] = self.grid[i]

        # Rule evaluation for regular 2-D cellular automata
        elif(not self.isJdV):
            rule = self.formatRule2D(i,j)
            tmp = self.matchElem(self.living_rules, rule)
            if(len(tmp) > 1):
                print("Transition ambiguity, rule : " + str(rule))
                exit(0)
            elif(len(tmp) == 1):
                next[i][j] = tmp[0]
            else:
                next[i][j] = self.grid[i][j]

        
        # Specific rule evaluation for game of life
        else:
            rule = self.formatRule2D(i,j)
            tmp = self.matchElem(self.living_rules, rule)
            if(len(tmp) == 1):
                next[i][j] = int(1)
            else:
                tmp = self.matchElem(self.dead_rules, rule)
                if(len(tmp) == 1):
                    next[i][j] = int(1)
                else:
                    next[i][j] = int(0)
    
    # Calculate next generation grid and update current grid
    def nextGenerationGrid(self):
        new_grid = 0
        # Next generation 1-D grid
        if(self.aType == '1D'):
            new_grid = ['0']*self.columns
            for i in range(1,self.columns-1):
                self.applyRule(new_grid, i)

        # Next generation 2-D grid
        else:
            new_grid = []
            for i in range(self.rows):
                new_grid.append([0]*self.columns)
                for j in range(self.columns):
                    self.applyRule(new_grid, i, j)
        self.grid = new_grid

    def JeuDeVie(self, screen):
        
        for i in range(self.rows):
            for j in range(self.columns):

            # Draw cells from self.grid
                x_pos = j * self.scale
                y_pos = i * self.scale
                
                # Draw black cell if dead
                if(self.grid[i][j] == 0):
                    pygame.draw.rect(screen, (255,255,255), [x_pos, y_pos, self.scale - 1, self.scale - 1])
                # Draw white cell if living
                elif(self.grid[i][j] == 1):
                    pygame.draw.rect(screen, (0,14,71), [x_pos, y_pos, self.scale - 1, self.scale - 1])
        
        # Update current 
        self.nextGenerationGrid()