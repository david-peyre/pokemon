# menu.py
import pygame
import sys
import json
from pokemon import Pokemon
from pokedex import Pokedex
from ig_pokedex import IG_Pokedex
from ig_combat import IG_Combat
from combat import Combat

pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Mise en place du fond
pikachu = pygame.image.load('classes/assets/menu.jpg') # Charger l'image de fond
pikachu = pygame.transform.scale(pikachu, (1000, 600)) # Redimensionner l'image de fond

# Taille de la fenêtre
largeur, hauteur = 1000, 600 # Définition de la taille de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur)) # Création de la fenêtre
pygame.display.set_caption("Pokemon") # Définition du titre de la fenêtre

# Police pour le texte
police = pygame.font.Font(None, 36) # Initialisation de la police

class Menu:
    POKEDEX_FILE = 'pokedex.json' # Initialisation du fichier du Pokédex

    def __init__(self):
        self.pokedex = Pokedex()  # Initialisation du Pokédex
        self.pokedex.load_from_file()  # Chargement du Pokédex
        self.ig_pokedex = IG_Pokedex(self) # Initialisation de l'interface graphique du Pokédex

    # Méthode pour afficher le menu
    def charger_pokedex(self):
        try: # Gestion des exceptions
            with open(self.POKEDEX_FILE, "r") as fichier: # Ouverture du fichier en mode lecture
                data = fichier.read() # Lecture du contenu du fichier
                if data: # Si le contenu du fichier n'est pas vide
                    loaded_data = json.loads(data) # Chargement des données
                    self.pokedex.pokedex = loaded_data.get("Pokemons apercus", []) # Mise à jour du Pokédex
                else:
                    self.pokedex.pokedex = {"Pokemons apercus": []} # Initialisation du Pokédex
        except FileNotFoundError: # Gestion de l'exception FileNotFoundError
            self.sauvegarder_pokedex() # Appel de la méthode pour sauvegarder le Pokédex
        except json.decoder.JSONDecodeError: # Gestion de l'exception JSONDecodeError
            self.pokedex.pokedex = {"Pokemons apercus": []} # Initialisation du Pokédex
            self.sauvegarder_pokedex() # Appel de la méthode pour sauvegarder le Pokédex

    # Méthode pour sauvegarder le Pokédex
    def sauvegarder_pokedex(self): # Méthode pour sauvegarder le Pokédex
        with open(self.POKEDEX_FILE, "w") as f: # Ouverture du fichier en mode écriture
            json.dump(self.pokedex.pokedex, f, indent=2) # Écriture des données dans le fichier

    # Méthode pour lancer une partie
    def lancer_partie(self):
        img_pokemon = { # Initialisation des images des Pokémon
            "Bulbizarre": pygame.image.load("classes/assets/Pokemon/Sprite_1.png"),
            "Herbizarre": pygame.image.load("classes/assets/Pokemon/Sprite_2.png"),
            "Florizarre": pygame.image.load("classes/assets/Pokemon/Sprite_3.png"),
            "Carapuce": pygame.image.load("classes/assets/Pokemon/Sprite_4.png"),
            "Carabaffe": pygame.image.load("classes/assets/Pokemon/Sprite_5.png"),
            "Tortank": pygame.image.load("classes/assets/Pokemon/Sprite_6.png"),
            "Salamèche": pygame.image.load("classes/assets/Pokemon/Sprite_7.png"),
            "Reptincel": pygame.image.load("classes/assets/Pokemon/Sprite_8.png"),
            "Dracofeu": pygame.image.load("classes/assets/Pokemon/Sprite_9.png"),
            "Roucool": pygame.image.load("classes/assets/Pokemon/Sprite_10.png"),
            "Roucoups": pygame.image.load("classes/assets/Pokemon/Sprite_11.png"),
            "Roucarnage": pygame.image.load("classes/assets/Pokemon/Sprite_12.png"),
            "Tentacool": pygame.image.load("classes/assets/Pokemon/Sprite_13.png"),
            "Tentacruel": pygame.image.load("classes/assets/Pokemon/Sprite_14.png"),
            "Ramoloss": pygame.image.load("classes/assets/Pokemon/Sprite_15.png"),
            "Flagadoss": pygame.image.load("classes/assets/Pokemon/Sprite_16.png"),
            "Doduo": pygame.image.load("classes/assets/Pokemon/Sprite_17.png"),
            "Dodrio": pygame.image.load("classes/assets/Pokemon/Sprite_18.png"),
            "Otaria": pygame.image.load("classes/assets/Pokemon/Sprite_19.png"),
            "Lamantine": pygame.image.load("classes/assets/Pokemon/Sprite_20.png"),
            "Goupix": pygame.image.load("classes/assets/Pokemon/Sprite_21.png"),
            "Feunard": pygame.image.load("classes/assets/Pokemon/Sprite_22.png"),
            "Miaouss": pygame.image.load("classes/assets/Pokemon/Sprite_23.png"),
            "Persian": pygame.image.load("classes/assets/Pokemon/Sprite_24.png"),
        }

        ig_combat_instance = IG_Combat(img_pokemon, adversaire=Combat.choose_opponent()) # Initialisation de l'instance de l'interface graphique du combat
        ig_combat_instance.afficher_choix_pokemon() # Affichage du choix du Pokémon
        ig_combat_instance.commencer_combat() # Initialisation du combat
        ig_combat_instance.fin_combat() # Récupération du résultat de la fin du combat
        self.afficher_menu() # Affichage du menu

    # Méthode pour ajouter un Pokémon
    def ajouter_pokemon(self):
        print("Ajout d'un Pokémon")
        name = self.saisir_texte("Nom du Pokémon:")  # Saisie du nom du Pokémon
        pokemon_num = self.saisir_entier("Numéro:") # Saisie du numéro du Pokémon
        poke_type = self.saisir_texte("Type du Pokémon:") # Saisie du type du Pokémon 
        evo_lvl = self.saisir_entier("Stade d'évolution:") # Saisie du stade d'évolution du Pokémon
        hp = self.saisir_entier("Points de vie:") # Saisie des points de vie du Pokémon
        attack_pt = self.saisir_entier("Puissance d'attaque:") # Saisie de la puissance d'attaque du Pokémon
        defense = self.saisir_entier("Point de défense:") # Saisie du point de défense du Pokémon
        xp_points = self.saisir_entier("Points d'experience:") # Saisie des points d'expérience du Pokémon
        base_hp = self.saisir_entier("Point de vie de base:") # Saisie du point de vie de base du Pokémon
        image_path = "classes/assets/Pokemon/Sprite_M.png" # Initialisation du chemin de l'image du Pokémon
        pokemon = Pokemon(pokemon_num, name, poke_type, evo_lvl, hp, attack_pt, defense, xp_points, base_hp, image_path) # Initialisation du Pokémon

        # Enregistrez le Pokémon dans le Pokédex
        self.pokedex.add_to_pokedex(pokemon.to_dict()) # Ajout du Pokémon dans le Pokédex
        self.pokedex.load_from_file() # Chargement du Pokédex
        self.sauvegarder_pokedex() # Sauvegarde du Pokédex
        self.afficher_menu() # Affichage du menu

    # Méthode pour afficher le Pokédex
    def afficher_pokedex(self):
        self.ig_pokedex.afficher_pokedex() # Affichage du Pokédex
        self.afficher_menu() # Affichage du menu

    # Méthode pour gérer le clic sur le menu
    def saisir_texte(self, message):
        font = pygame.font.Font(None, 36) # Initialisation de la police
        input_box = pygame.Rect(300, 300, 200, 32) # Initialisation de la zone de saisie
        color_inactive = pygame.Color('lightskyblue3') # Initialisation de la couleur inactive
        color_active = pygame.Color('dodgerblue2') # Initialisation de la couleur active
        color = color_inactive # Initialisation de la couleur
        active = False # Initialisation de la variable pour gérer l'activation
        text = '' # Initialisation du texte
        clock = pygame.time.Clock() # Initialisation de l'horloge

        while True: # Boucle pour la saisie du texte
            for event in pygame.event.get(): # Parcours des événements
                if event.type == pygame.QUIT: # Vérifier si l'événement est de type QUIT
                    pygame.quit() # Quitter Pygame
                    sys.exit() # Quitter le programme
                if event.type == pygame.MOUSEBUTTONDOWN: # Vérifier si l'événement est de type MOUSEBUTTONDOWN
                    if input_box.collidepoint(event.pos): # Vérifier si la zone de saisie est cliquée
                        active = not active 
                    else: # Si la zone de saisie n'est pas cliquée
                        active = False  # Désactiver la zone de saisie
                    color = color_active if active else color_inactive # Mise à jour de la couleur
                if event.type == pygame.KEYDOWN: # Vérifier si l'événement est de type KEYDOWN
                    if active: # Si la zone de saisie est active
                        if event.key == pygame.K_RETURN: # Vérifier si la touche appuyée est RETURN
                            try: # Gestion des exceptions
                                return text # Retour du texte
                            except ValueError: # Gestion de l'exception ValueError
                                print("Invalid input. Please enter a valid value.") # Affichage du message d'erreur
                                return  # Retour
                        elif event.key == pygame.K_BACKSPACE: # Vérifier si la touche appuyée est BACKSPACE
                            text = text[:-1] # Supprimer le dernier caractère
                        else: # Si la touche appuyée n'est pas BACKSPACE
                            text += event.unicode # Ajouter le caractère à la fin du texte

            fenetre.fill(BLANC) # Remplir la fenêtre avec la couleur blanche
            txt_surface = font.render(message + " " + text, True, color) # Création de la surface de texte
            width = max(200, txt_surface.get_width() + 10) # Calcul de la largeur
            input_box.w = width # Mise à jour de la largeur
            fenetre.blit(txt_surface, (input_box.x + 5, input_box.y + 5)) # Affichage de la surface de texte
            pygame.draw.rect(fenetre, color, input_box, 2) # Affichage de la zone de saisie
            pygame.display.flip() # Mettre à jour l'affichage
            clock.tick(30) # Mise à jour de l'horloge

    def saisir_entier(self, message): # Méthode pour saisir un entier
        font = pygame.font.Font(None, 36) # Initialisation de la police
        input_box = pygame.Rect(300, 300, 200, 32) # Initialisation de la zone de saisie
        color_inactive = pygame.Color('lightskyblue3') # Initialisation de la couleur inactive
        color_active = pygame.Color('dodgerblue2') # Initialisation de la couleur active
        color = color_inactive # Initialisation de la couleur
        active = False # Initialisation de la variable pour gérer l'activation
        text = ''   # Initialisation du texte
        clock = pygame.time.Clock() # Initialisation de l'horloge

        while True: # Boucle pour la saisie de l'entier
            for event in pygame.event.get(): # Parcours des événements
                if event.type == pygame.QUIT: # Vérifier si l'événement est de type QUIT
                    pygame.quit() # Quitter Pygame
                    sys.exit() # Quitter le programme
                if event.type == pygame.MOUSEBUTTONDOWN: # Vérifier si l'événement est de type MOUSEBUTTONDOWN
                    if input_box.collidepoint(event.pos): # Vérifier si la zone de saisie est cliquée
                        active = not active # Activer ou désactiver la zone de saisie
                    else: # Si la zone de saisie n'est pas cliquée
                        active = False # Désactiver la zone de saisie
                    color = color_active if active else color_inactive # Mise à jour de la couleur
                if event.type == pygame.KEYDOWN: # Vérifier si l'événement est de type KEYDOWN
                    if active: # Si la zone de saisie est active
                        if event.key == pygame.K_RETURN: # Vérifier si la touche appuyée est RETURN
                            try: # Gestion des exceptions
                                return int(text) # Retour de l'entier
                            except ValueError: # Gestion de l'exception ValueError
                                print("Invalid input. Please enter a valid value.") # Affichage du message d'erreur
                                return  # Retour
                        elif event.key == pygame.K_BACKSPACE: # Vérifier si la touche appuyée est BACKSPACE
                            text = text[:-1] # Supprimer le dernier caractère
                        else: # Si la touche appuyée n'est pas BACKSPACE
                            text += event.unicode # Ajouter le caractère à la fin du texte

            fenetre.fill(BLANC) # Remplir la fenêtre avec la couleur blanche
            txt_surface = font.render(message + " " + text, True, color) # Création de la surface de texte
            width = max(200, txt_surface.get_width() + 10) # Calcul de la largeur
            input_box.w = width # Mise à jour de la largeur
            fenetre.blit(txt_surface, (input_box.x + 5, input_box.y + 5)) # Affichage de la surface de texte
            pygame.draw.rect(fenetre, color, input_box, 2) # Affichage de la zone de saisie
            pygame.display.flip() # Mettre à jour l'affichage
            clock.tick(30) # Mise à jour de l'horloge

    def saisir_entree(self, message, conversion_func): # Méthode pour saisir une entrée
        font = pygame.font.Font(None, 36) # Initialisation de la police
        input_box = pygame.Rect(300, 300, 200, 32) # Initialisation de la zone de saisie
        color_inactive = pygame.Color('lightskyblue3') # Initialisation de la couleur inactive
        color_active = pygame.Color('dodgerblue2') # Initialisation de la couleur active
        color = color_inactive # Initialisation de la couleur
        active = False # Initialisation de la variable pour gérer l'activation
        text = '' # Initialisation du texte
        clock = pygame.time.Clock() # Initialisation de l'horloge

        while True: # Boucle pour la saisie de l'entrée
            for event in pygame.event.get(): # Parcours des événements
                if event.type == pygame.QUIT: # Vérifier si l'événement est de type QUIT
                    pygame.quit() # Quitter Pygame
                    sys.exit() # Quitter le programme
                if event.type == pygame.MOUSEBUTTONDOWN: # Vérifier si l'événement est de type MOUSEBUTTONDOWN
                    if input_box.collidepoint(event.pos): # Vérifier si la zone de saisie est cliquée
                        active = not active # Activer ou désactiver la zone de saisie
                    else: # Si la zone de saisie n'est pas cliquée
                        active = False # Désactiver la zone de saisie
                    color = color_active if active else color_inactive # Mise à jour de la couleur
                if event.type == pygame.KEYDOWN: # Vérifier si l'événement est de type KEYDOWN
                    if active: # Si la zone de saisie est active
                        if event.key == pygame.K_RETURN: # Vérifier si la touche appuyée est RETURN
                            try: # Gestion des exceptions
                                return conversion_func(text) # Retour de la valeur convertie
                            except ValueError: # Gestion de l'exception ValueError
                                print("Invalid input. Please enter a valid value.") # Affichage du message d'erreur
                                return # Retour
                        elif event.key == pygame.K_BACKSPACE: # Vérifier si la touche appuyée est BACKSPACE
                            text = text[:-1] # Supprimer le dernier caractère
                        else: # Si la touche appuyée n'est pas BACKSPACE
                            text += event.unicode # Ajouter le caractère à la fin du texte

            fenetre.fill(BLANC) # Remplir la fenêtre avec la couleur blanche
            txt_surface = font.render(message + " " + text, True, color) # Création de la surface de texte
            width = max(200, txt_surface.get_width() + 10) # Calcul de la largeur
            input_box.w = width # Mise à jour de la largeur
            fenetre.blit(txt_surface, (input_box.x + 5, input_box.y + 5)) # Affichage de la surface de texte
            pygame.draw.rect(fenetre, color, input_box, 2) # Affichage de la zone de saisie
            pygame.display.flip() # Mettre à jour l'affichage
            clock.tick(30) # Mise à jour de l'horloge

    # Méthode pour afficher le menu
    def afficher_menu(self):
        fenetre.blit(pikachu, (0, 0)) # Affichage de l'image de fond
        titre = police.render("Pokemon", True, NOIR) # Création du titre
        fenetre.blit(titre, (largeur // 2 - titre.get_width() // 2, 50)) # Affichage du titre

        options = ["Lancer une partie", "Ajouter un Pokémon", "Accéder à son Pokedex", "Quitter"] # Initialisation des options
        y_position = 200 # Initialisation de la position en y
        option_rects = [] # Initialisation de la liste des rectangles pour les options

        for option in options: # Parcours des options
            texte = police.render(option, True, NOIR) # Création du texte
            rect = texte.get_rect(center=(largeur // 2, y_position)) # Création du rectangle pour le texte
            fenetre.blit(texte, rect) # Affichage du texte
            option_rects.append(rect) # Ajout du rectangle dans la liste
            y_position += 50 # Mise à jour de la position en y

        pygame.display.flip() # Mettre à jour l'affichage

        
        while True: # Boucle principale du menu
            for event in pygame.event.get(): # Parcours des événements
                if event.type == pygame.QUIT: # Vérifier si l'événement est de type QUIT
                    pygame.quit() # Quitter Pygame
                    sys.exit() # Quitter le programme
                elif event.type == pygame.MOUSEBUTTONDOWN: # Vérifier si l'événement est de type MOUSEBUTTONDOWN
                    mouse_pos = pygame.mouse.get_pos() # Récupération de la position de la souris
                    for i, rect in enumerate(option_rects): # Parcours des rectangles des options
                        if rect.collidepoint(mouse_pos): # Vérifier si le clic est sur l'option
                            self.gerer_clic_menu(i)  # Appeler la fonction appropriée en fonction de l'option cliquée

    def gerer_clic_menu(self, option_index): # Méthode pour gérer le clic sur le menu
        if option_index == 0: # Si l'option est "Lancer une partie"
            self.lancer_partie() # Appel de la méthode pour lancer une partie
        elif option_index == 1: # Si l'option est "Ajouter un Pokémon"
            self.ajouter_pokemon() # Appel de la méthode pour ajouter un Pokémon
        elif option_index == 2: # Si l'option est "Accéder à son Pokédex"
            self.pokedex.load_from_file() # Chargement du Pokédex
            self.afficher_pokedex() # Appel de la méthode pour afficher le Pokédex
        elif option_index == 3: # Si l'option est "Quitter"
            pygame.quit() # Quitter Pygame
            sys.exit() # Quitter le programme

# Lancer l'application
if __name__ == "__main__":
    menu_instance = Menu()
    menu_instance.afficher_menu()
