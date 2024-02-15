# ig_pokedex.py
import pygame
import sys
from pokedex import Pokedex
from pokemon import Pokemon

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Initialisation de la fenêtre
largeur, hauteur = 800, 600 # Définition de la taille de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur)) # Création de la fenêtre
pygame.display.set_caption("Pokemon - Pokédex") # Définition du titre de la fenêtre

# Initialisation de la police
police = pygame.font.Font(None, 36)

# Classe pour gérer l'interface graphique du Pokédex
class IG_Pokedex:
    # Initialisation de la classe
    def __init__(self, menu_instance):
        self.menu = menu_instance # Ajout de l'instance de Menu
        self.quitter_pokedex = False  # Ajout de la variable pour gérer la sortie de la boucle

    def afficher_pokedex(self):
        while not self.quitter_pokedex:  # Utilisation de la variable pour contrôler la boucle
            for event in pygame.event.get(): # Parcours des événements
                if event.type == pygame.QUIT: # Vérifier si l'événement est de type QUIT
                    pygame.quit() # Quitter Pygame
                    sys.exit() # Quitter le programme
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self._retour_clic(event.pos): # Vérifier si le clic est sur "Retour"
                        self.quitter_pokedex = True  # Sortir de la boucle lors du clic sur "Retour"

            self._afficher_contenu_pokedex() # Appel de la méthode pour afficher le contenu du Pokédex
            pygame.display.flip() # Mettre à jour l'affichage

    # Méthode pour vérifier si le clic est sur "Retour"
    def _retour_clic(self, pos):
        retour_rect = pygame.Rect(largeur // 2 - 100, hauteur - 50, 200, 40) # Création du rectangle pour "Retour"
        return retour_rect.collidepoint(pos) # Vérification de la collision avec le rectangle
    
    # Méthode pour afficher le contenu du Pokédex
    def _afficher_contenu_pokedex(self):
        fenetre.fill(BLANC)  # Remplir la fenêtre avec la couleur blanche

        titre = police.render("Pokédex", True, NOIR)  # Création du titre
        fenetre.blit(titre, (largeur // 2 - titre.get_width() // 2, 50)) # Affichage du titre

        y_position = 150 # Initialisation de la position en y
        for pokemon_data in self.menu.pokedex.pokedex.get("Pokemons apercus", []): # Parcours des données des pokémons dans le Pokédex
            pokemon_info = f"{pokemon_data['name']} - Type: {pokemon_data['poke_type']} - HP: {pokemon_data['hp']}" # Création de la chaîne d'informations
            texte = police.render(pokemon_info, True, NOIR) # Création du texte
            rect = texte.get_rect(center=(largeur // 2, y_position)) # Création du rectangle pour le texte
            fenetre.blit(texte, rect) # Affichage du texte
            y_position += 50 # Mise à jour de la position en y

        retour_texte = police.render("Retour", True, NOIR) # Création du texte pour "Retour"
        retour_rect = retour_texte.get_rect(center=(largeur // 2, hauteur - 50)) # Création du rectangle pour "Retour"
        fenetre.blit(retour_texte, retour_rect) # Affichage du texte pour "Retour"

        # Mettez à jour l'affichage une seule fois à la fin de la boucle
        pygame.display.flip()

# Lancer l'application
if __name__ == "__main__":
    from menu import Menu

    menu_instance = Menu()
    ig_pokedex = IG_Pokedex(menu_instance)
    ig_pokedex.afficher_pokedex()
