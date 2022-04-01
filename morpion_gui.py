import pygame
# Couleurs sur pygame : ce sont des tuples contenant 3 int représentant le code rgb de la couleur
white = 255,255,255
black = 0,0,0
def display_grid():
        for i in range(3):
            for j in range(3):
                pygame.draw.rect(screen,black,[100 * j,100 * i,100,100,],1,)

pygame.init() # lancement de l'interface
pygame.display.set_caption('Morpion') # Nom de l'interface
screen = pygame.display.set_mode((300,300)) #Définition de la taille de l'interface
ended = False
screen.fill(white)
display_grid()
while not ended: # On créer une boucle infinie pour garder l'interface
    for event in pygame.event.get(): # Fonction pour récupérer les event ( clics souris, touches du clavier)
        if event.type == pygame.QUIT: 
            ended = True
    pygame.display.flip() # On refresh l'interface graphique pour ajouter les modifications