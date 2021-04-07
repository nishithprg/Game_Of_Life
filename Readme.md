# Game_Of_Life
The following code is written as per the questions and specifications mention in the following project :
http://membres-lig.imag.fr/prost/L3_INFO_MCAL_MT/projet.html

## French Version
Le code demandé pour les question 1, 2 et 3 est implanté à l’aide des classes en python dans grid.py, une classe pour parser le fichier d’entré dans fileparser.py et le corps 
principal du code dans main.py. Veuillez lire les instructions sur comment formater le fichier d'entrée selon ce qu'on veut tester dans “Input file format.txt”.  En plus, il y 
a 3 fichiers d’entrée fournis dans le répertoire Examples pour tester un automate cellulaire de 1-dimension, de 2-dimension et le Jeu de Vie; et déposer dans ce répertoire tout 
autre fichier à tester.

Si le fichier d’entrée s’agit de celui d’un automate cellulaire, l’évolution des états de la grille sont affichés sur la console après chaque génération jusqu’à un certain nombre 
d’évolution fournis par le fichier d’entrée. Si le fichier d’entrée s’agit de celui du jeu de vie, une nouvelle fenêtre s’ouvre avec un affichage graphique des états. On peut régler
la vitesse d’actualisation de la fenêtre en changeant l’argument du temps en millisecondes de pygame.time.delay(temps), ligne 45 de main.py.

Le jeu de vie est implémenté comme une automate cellulaire de 2-dimension, dont que certaines transitions nécessaire ont été fournis dans “Input file format.txt”; et toutes les 
transitions de question 1; celles qui permet les cellules d’évoluer dans des cellules vivantes à la génération prochaine, et on considère toutes autres configuration de voisins 
comme des transition menant une cellule à mourir; car ces dernières ont beaucoup de configuration qui s’agit juste d’une énumération de configuration aux conditions opposées de 
celles décrits dans l’énoncé.

## English Version
The code required for questions 1, 2 and 3 is implemented using a python class in grid.py, a class for parsing the input file in fileparser.py and the main body of the code in 
main.py. Please read the instructions on how to format the input file for a 1D or 2D cellular automaton, or Game of Life in "Input file format.txt". In addition, there are 3 input
files provided in the Examples directory and drop any other files to be tested into this directory.

If the input file is a cellular automaton, the evolution of the grid states are displayed on the console after each generation up to a certain number of evolutions provided in 
the input file. If the input file is that of Game of Life, a new window opens with a graphic display of the states. The refresh rate of the window can be set by changing the time
argument in milliseconds of pygame.time.delay(time), line 45 of main.py.

The Game of life is implemented as a 2-dimensional cellular automaton, of which certain necessary transitions have been provided in "Input file format.txt"; and all the transitions
in question 1; those that allow cells to evolve into living cells at the next generation, and all other neighbouring configurations are considered to be transitions leading to a 
cell's death; as these have many configurations that are just an enumeration of configurations of opposing conditions to those described in the projet.
