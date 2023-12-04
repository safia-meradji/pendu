import pygame
import random

# Initialisation de Pygame
pygame.init()

# Paramètres
largeur_fenetre = 800
hauteur_fenetre = 600
fps = 60
clock = pygame.time.Clock()

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)

# Chargement des mots depuis le fichier
with open("/Applications/MAMP/htdocs/work/Python/pendu/mots.txt", "r") as fichier_mots:
    mots = fichier_mots.read().splitlines()

import os
os.chdir("/Applications/MAMP/htdocs/work/Python/pendu/")

# Chargement des scores depuis le fichier
scores = {}

# Fonction pour choisir un mot aléatoire
def choisir_mot():
    return random.choice(mots).upper()

# Fonction pour dessiner le pendu
def dessiner_pendu(erreurs):
    # Implémentez ici la logique pour dessiner le pendu en fonction du nombre d'erreurs
    pass

# Fonction principale du jeu
def jouer():
    mot_a_trouver = choisir_mot()
    lettres_trouvees = ["_" for _ in mot_a_trouver]
    erreurs = 0

    while "_" in lettres_trouvees and erreurs < 6:
        # Afficher l'état actuel du mot et le pendu
        print("Mot:", " ".join(lettres_trouvees))
        dessiner_pendu(erreurs)

        # Obtenir une lettre de l'utilisateur
        lettre = input("Entrez une lettre : ").upper()

        if lettre.isalpha() and len(lettre) == 1:
            if lettre in mot_a_trouver:
                # La lettre est correcte
                print("Bonne lettre !")
                for i in range(len(mot_a_trouver)):
                    if mot_a_trouver[i] == lettre:
                        lettres_trouvees[i] = lettre
            else:
                # La lettre est incorrecte
                print("Mauvaise lettre !")
                erreurs += 1
        else:
            print("Entrée invalide. Veuillez entrer une lettre.")

    if "_" not in lettres_trouvees:
        print(f"Bravo ! Vous avez trouvé le mot : {mot_a_trouver}")
        # Ajoutez le score dans le fichier scores.txt
    else:
        print(f"Dommage ! Le mot était : {mot_a_trouver}")

# Menu principal
def menu():
    while True:
        choix = input("Menu :\n1. Jouer\n2. Insérer un mot\n3. Tableau des scores\n4. Quitter\nChoisissez une option : ")

        if choix == "1":
            jouer()
        elif choix == "2":
            # Implémentez ici la logique pour insérer un mot dans le fichier mots.txt
            pass
        elif choix == "3":
            # Implémentez ici la logique pour afficher le tableau des scores
            pass
        elif choix == "4":
            print("Merci d'avoir joué ! Au revoir.")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    menu()
