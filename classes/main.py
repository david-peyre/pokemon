# main.py
import pygame
from menu import Menu
from ig_combat import IG_Combat
import sys
from pokemon import Pokemon, POKEMON_LIST
from combat import Combat
from pokedex import Pokedex

# Classe pour gérer le jeu
def __init__(self, image_path, pokemon_images):
    pokemon_images = charger_images_pokemon() # Chargement des images des Pokémon
    image_path = "assets/Pokemon/Sprite_{}.png" # Chemin des images des Pokémon
    self.pokemon_images = pokemon_images # Initialisation des images des Pokémon
    self.image = pygame.image.load(image_path.format(self.pokemon_num)) # Chargement de l'image du Pokémon

# Méthode pour charger les images des Pokémon
def charger_images_pokemon():
    pokemon_images = {} # Initialisation du dictionnaire pour les images des Pokémon
    for pokemon in POKEMON_LIST: # Parcours des Pokémon
        image = pygame.image.load(f"classes/assets/Pokemon/Sprite_{pokemon.pokemon_num}.png") # Chargement de l'image du Pokémon
        pokemon_images[pokemon.pokemon_num] = image # Ajout de l'image dans le dictionnaire
    return pokemon_images # Retour du dictionnaire des images des Pokémon

# Méthode principale
def main():
    pygame.init() # Initialisation de Pygame

    largeur, hauteur = 1000, 600 # Définition de la taille de la fenêtre
    fenetre = pygame.display.set_mode((largeur, hauteur)) # Création de la fenêtre
    pygame.display.set_caption("Pokemon") # Définition du titre de la fenêtre

    menu_instance = Menu() # Initialisation de l'instance de Menu
    pokedex_instance = Pokedex() # Initialisation de l'instance de Pokédex
    pokemon_images = charger_images_pokemon() # Chargement des images des Pokémon

    ig_combat_instance = IG_Combat(pokemon_images, adversaire=Combat.choose_opponent()) # Initialisation de l'instance de l'interface graphique du combat
    combat_en_cours = False # Initialisation de la variable pour gérer le combat en cours

    while True: # Boucle principale
        for event in pygame.event.get(): # Parcours des événements
            if event.type == pygame.QUIT: # Vérifier si l'événement est de type QUIT
                pygame.quit() # Quitter Pygame
                sys.exit() # Quitter le programme

        menu_instance.afficher_menu() # Affichage du menu
        choix = menu_instance.recuperer_choix_menu() # Récupération du choix du menu

        if choix == Menu.ACTION_QUITTER: # Si le choix est "Quitter"
            pygame.quit() # Quitter Pygame
            sys.exit() # Quitter le programme
        elif choix == Menu.ACTION_NOUVELLE_PARTIE: # Si le choix est "Nouvelle partie"
            ig_combat_instance.afficher_choix_pokemon() # Affichage du choix du Pokémon
            ig_combat_instance.commencer_combat() # Initialisation du combat
            combat_en_cours = True # Mise à jour de la variable pour gérer le combat en cours
        elif combat_en_cours: # Si le combat est en cours
            ig_combat_instance.gerer_combat() # Gestion du combat
            fin_combat_result = ig_combat_instance.fin_combat() # Récupération du résultat de la fin du combat

            if fin_combat_result == "quitter": # Si le résultat est "quitter"
                combat_en_cours = False # Mise à jour de la variable pour gérer le combat en cours
                menu_instance.afficher_menu() # Affichage du menu
            else:
                ig_combat_instance.fin_combat(vainqueur=fin_combat_result) # Affichage du résultat de la fin du combat

        pygame.display.update()  # Forcez la mise à jour de l'écran à la fin de chaque itération de la boucle principale

if __name__ == "__main__":
    main()
