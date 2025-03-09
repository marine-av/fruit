import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres de la fenêtre
LARGEUR, HAUTEUR = 600, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Attrape le fruit !")

# Couleurs
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

# Charger les images
panier = pygame.image.load("panier.png")  # À remplacer par une vraie image
fruit = pygame.image.load("pomme.png")  # À remplacer par une vraie image

# Redimensionner les images
panier = pygame.transform.scale(panier, (80, 50))
fruit = pygame.transform.scale(fruit, (40, 40))

# Position du panier
panier_x = LARGEUR // 2
panier_y = HAUTEUR - 60
panier_vitesse = 5

# Position du fruit
fruit_x = random.randint(0, LARGEUR - 40)
fruit_y = 0
fruit_vitesse = 3

# Score
score = 0
police = pygame.font.Font(None, 36)

# Boucle du jeu
jeu_en_cours = True
while jeu_en_cours:
    pygame.time.delay(30)  # Pour ralentir un peu la boucle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeu_en_cours = False

    # Déplacement du panier
    touches = pygame.key.get_pressed()
    if touches[pygame.K_LEFT] and panier_x > 0:
        panier_x -= panier_vitesse
    if touches[pygame.K_RIGHT] and panier_x < LARGEUR - 80:
        panier_x += panier_vitesse

    # Faire tomber le fruit
    fruit_y += fruit_vitesse
    if fruit_y > HAUTEUR:  # Si le fruit atteint le bas, on le remet en haut
        fruit_y = 0
        fruit_x = random.randint(0, LARGEUR - 40)
        score -= 1  # Perte d’un point si raté

    # Vérifier la collision
    if panier_x < fruit_x < panier_x + 80 and panier_y < fruit_y < panier_y + 50:
        score += 1
        fruit_y = 0
        fruit_x = random.randint(0, LARGEUR - 40)

    # Affichage
    fenetre.fill(BLANC)
    fenetre.blit(panier, (panier_x, panier_y))
    fenetre.blit(fruit, (fruit_x, fruit_y))

    # Afficher le score
    texte_score = police.render(f"Score: {score}", True, ROUGE)
    fenetre.blit(texte_score, (10, 10))

    pygame.display.update()

pygame.quit()

