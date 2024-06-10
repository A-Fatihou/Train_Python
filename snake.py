import pygame
import random


pygame.init()

# Configuration de la fenêtre de jeu
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Jeu du Snake")


horloge = pygame.time.Clock()

# Définition des couleurs
noir = (0, 0, 0)
blanc = (255, 255, 255)
vert = (255, 0, 0)

# Configuration du serpent
taille_serpent = 20
vitesse_serpent = 10
position_serpent_x = largeur_fenetre / 2
position_serpent_y = hauteur_fenetre / 2
changement_serpent_x = 0
changement_serpent_y = 0
corps_serpent = []
longueur_serpent = 1

# Configuration de la nourriture
taille_nourriture = 20
position_nourriture_x = round(random.randrange(0, largeur_fenetre - taille_nourriture) / 20) * 20
position_nourriture_y = round(random.randrange(0, hauteur_fenetre - taille_nourriture) / 20) * 20


en_cours = True
while en_cours:
    # Gestion des événements
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            en_cours = False

    # Gestion du mouvement du serpent
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT]:
        changement_serpent_x = -taille_serpent
        changement_serpent_y = 0
    elif touches[pygame.K_RIGHT]:
        changement_serpent_x = taille_serpent
        changement_serpent_y = 0
    elif touches[pygame.K_UP]:
        changement_serpent_y = -taille_serpent
        changement_serpent_x = 0
    elif touches[pygame.K_DOWN]:
        changement_serpent_y = taille_serpent
        changement_serpent_x = 0

    # Mise à jour de la position du serpent
    position_serpent_x += changement_serpent_x
    position_serpent_y += changement_serpent_y

    # Vérification de la collision avec la nourriture
    if position_serpent_x == position_nourriture_x and position_serpent_y == position_nourriture_y:
        position_nourriture_x = round(random.randrange(0, largeur_fenetre - taille_nourriture) / 20) * 20
        position_nourriture_y = round(random.randrange(0, hauteur_fenetre - taille_nourriture) / 20) * 20
        longueur_serpent += 1

    # Mise à jour de la fenêtre de jeu
    fenetre.fill(noir)
    pygame.draw.rect(fenetre, vert, [position_nourriture_x, position_nourriture_y, taille_nourriture, taille_nourriture])
    tete_serpent = []
    tete_serpent.append(position_serpent_x)
    tete_serpent.append(position_serpent_y)
    corps_serpent.append(tete_serpent)
    if len(corps_serpent) > longueur_serpent:
        del corps_serpent[0]
    for segment in corps_serpent[:-1]:
        if segment == tete_serpent:
            en_cours = False
    for segment in corps_serpent:
        pygame.draw.rect(fenetre, blanc, [segment[0], segment[1], taille_serpent, taille_serpent])

    pygame.display.update()
    horloge.tick(vitesse_serpent)


pygame.quit()
