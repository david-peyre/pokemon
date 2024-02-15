#ig_combat.py
import pygame
import sys
from combat import Combat
from pokemon import POKEMON_LIST
from pokemon import Pokemon
from pokedex import Pokedex

# Initialisation de Pygame
pygame.init()

# Initialisation des couleurs
BLANC = (255, 255, 255) # Couleur blanche
NOIR = (0, 0, 0) # Couleur noire

# Initialisation de la taille de la fenêtre
largeur, hauteur = 1000, 600 # Largeur et hauteur de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur)) # Initialisation de la fenêtre
pygame.display.set_caption("Pokémon - Combat") # Titre de la fenêtre

# Initialisation de la police
police = pygame.font.Font(None, 36) 

# Initialisation des actions
ACTION_ATTAQUER = 1 # Attaquer
ACTION_POTION = 4 # Utiliser une potion
ACTION_FUITE = 7 # Fuir

# Initialisation de la map des actions
ACTION_MAP = { 
    pygame.K_1: ACTION_ATTAQUER, 
    pygame.K_2: ACTION_POTION,
    pygame.K_3: ACTION_FUITE
}

# Classe pour gérer le combat en mode interface graphique
class IG_Combat:
    # Initialisation de la classe
    def __init__(self, pokemon_images, adversaire):
        self.pokemon_choisi = None # Initialisation du Pokémon choisi
        self.pokemon_images = pokemon_images # Initialisation des images des Pokémon
        self.combat_instance = None # Initialisation de l'instance de combat
        self.adversaire = adversaire # Initialisation de l'adversaire
        self.pokedex_instance = Pokedex() # Initialisation de l'instance du Pokédex

    # Méthode pour afficher le choix du Pokémon
    def afficher_choix_pokemon(self):
        choix = self.afficher_interface_choix_pokemon() # Affichage de l'interface de choix du Pokémon

        if choix in range(1, len(POKEMON_LIST) + 1): # Si le choix est valide
            self.pokemon_choisi = POKEMON_LIST[choix - 1] # Choix du Pokémon
            print(f"Vous avez choisi {self.pokemon_choisi.name}!") # Affichage du message de choix
        else:
            print("Choix invalide. Fermeture du jeu.") # Affichage du message d'erreur
            pygame.quit() # Fermeture de Pygame
            sys.exit() # Fermeture du programme

    # Méthode pour afficher l'interface de choix du Pokémon
    def afficher_interface_choix_pokemon(self):
        choix = 0 # Initialisation du choix
        while choix not in [1, 4, 7]: # Tant que le choix n'est pas valide
            for event in pygame.event.get(): # Parcours des événements
                if event.type == pygame.QUIT: # Si l'événement est de type "Quitter"
                    pygame.quit() # Fermeture de Pygame
                    sys.exit() # Fermeture du programme
 
            fenetre.fill(BLANC) # Remplissage de la fenêtre en blanc

            titre = police.render("Choisissez votre Pokémon de départ : 1.Bulbizarre / 2.Carapuce / 3.Salamèche", True, NOIR) # Initialisation du titre
            fenetre.blit(titre, (largeur // 2 - titre.get_width() // 2, 50)) # Affichage du titre

            valid_choices = [1, 4, 7] # Initialisation des choix valides

            image_width, image_height = int(140), int(140) # Initialisation de la largeur et de la hauteur de l'image

            for i, pokemon in enumerate(POKEMON_LIST): # Parcours des Pokémon
                if i + 1 in valid_choices: # Si le choix est valide
                    nom_texte = police.render(f" {pokemon.name} ({pokemon.poke_type})", True, NOIR) # Initialisation du texte du nom
                    nom_rect = nom_texte.get_rect(topleft=(200, 150 + i * 50))   # Initialisation du rectangle du nom
                    fenetre.blit(nom_texte, nom_rect) # Affichage du nom

                    pokemon_image_resized = pygame.transform.scale(self.pokemon_images[pokemon.name], (image_width, image_height)) # Redimensionnement de l'image du Pokémon
                    image_rect = pokemon_image_resized.get_rect(topleft=(500, 80 + i * 50)) # Initialisation du rectangle de l'image
                    fenetre.blit(pokemon_image_resized, image_rect) # Affichage de l'image

            pygame.display.flip() # Mise à jour de l'affichage

            choix = self.recuperer_choix_pokemon() # Récupération du choix du Pokémon

        return choix # Retour du choix

    # Méthode pour récupérer le choix du Pokémon
    def recuperer_choix_pokemon(self): 
        for event in pygame.event.get(): # Parcours des événements
            if event.type == pygame.QUIT: # Si l'événement est de type "Quitter"
                pygame.quit() # Fermeture de Pygame
                sys.exit() # Fermeture du programme
            elif event.type == pygame.KEYDOWN: # Si une touche est pressée
                return ACTION_MAP.get(event.key, 0) # Retour du choix de l'action
            
        return 0 # Retour de la valeur par défaut
    
    # Méthode pour commencer le combat
    def commencer_combat(self): 
        adversaire = Combat.choose_opponent() # Choix de l'adversaire
        self.adversaire = adversaire # Initialisation de l'adversaire
        self.pokedex_instance.add_to_pokedex(adversaire.to_dict()) # Ajout de l'adversaire au Pokédex
        self.combat_instance = Combat(self.pokemon_choisi, adversaire) # Initialisation de l'instance de combat
        self.gerer_combat() # Gestion du combat
        self.fin_combat() # Fin du combat

    # Méthode pour gérer le combat
    def gerer_combat(self):
        clock = pygame.time.Clock() # Initialisation de l'horloge

        while self.combat_instance.pokemon_joueur.hp > 0: # Tant que le Pokémon du joueur a des points de vie
            for event in pygame.event.get(): # Parcours des événements
                if event.type == pygame.QUIT: # Si l'événement est de type "Quitter"
                    pygame.quit() # Fermeture de Pygame
                    sys.exit() # Fermeture du programme

            fenetre.fill(BLANC) # Remplissage de la fenêtre en blanc

            joueur_image = pygame.transform.scale(self.pokemon_images[self.combat_instance.pokemon_joueur.name], (140, 140)) # Redimensionnement de l'image du Pokémon du joueur
            fenetre.blit(joueur_image, (100, 200)) # Affichage de l'image du Pokémon du joueur
            joueur_info_texte = police.render(f"{self.combat_instance.pokemon_joueur.name} - HP: {self.combat_instance.pokemon_joueur.hp}", True, NOIR) # Initialisation du texte des informations du Pokémon du joueur
            fenetre.blit(joueur_info_texte, (100, 170)) # Affichage des informations du Pokémon du joueur

            adversaire_image = pygame.transform.scale(self.pokemon_images[self.combat_instance.adversaire.name], (140, 140)) # Redimensionnement de l'image de l'adversaire
            fenetre.blit(adversaire_image, (690, 200)) # Affichage de l'image de l'adversaire
            adversaire_info_texte = police.render(f"{self.combat_instance.adversaire.name} - HP: {self.combat_instance.adversaire.hp}", True, NOIR) # Initialisation du texte des informations de l'adversaire
            fenetre.blit(adversaire_info_texte, (670, 170)) # Affichage des informations de l'adversaire

            actions = ["1.Attaquer", "2.Potion", "3.Fuite"] # Initialisation des actions
            for i, action in enumerate(actions): # Parcours des actions
                texte = police.render(action, True, NOIR) # Initialisation du texte de l'action
                rect = texte.get_rect(topleft=(100 + i * 350, 500)) # Initialisation du rectangle du texte
                fenetre.blit(texte, rect) # Affichage du texte

            pygame.display.flip() # Mise à jour de l'affichage
            clock.tick(3) # Mise à jour de l'horloge

            action_joueur = self.recuperer_choix_pokemon() # Récupération de l'action du joueur
            result = self.combat_instance.do_combat(action_joueur) # Résultat du combat

            message_texte = police.render(result["message"], True, NOIR) # Initialisation du texte du message
            fenetre.blit(message_texte, (20, 60)) # Affichage du message

            pygame.display.flip() # Mise à jour de l'affichage
            clock.tick(30) # Mise à jour de l'horloge

            if result["winner"] or result["loser"]: # Si un vainqueur ou un perdant est trouvé
                self.fin_combat() # Fin du combat
                break # Sortie de la boucle
    
    # Méthode pour afficher le résultat du combat
    def check_evolution(self):
        if self.pokemon_choisi.evo_ok(): # Si le Pokémon peut évoluer
            print(f"{self.pokemon_choisi.name} peut évoluer au prochain stade.") # Affichage du message d'évolution
            self.pokemon_choisi.evolve() # Évolution du Pokémon
        else:
            print(f"{self.pokemon_choisi.name} n'a plus d'évolution possible.") # Affichage du message d'erreur

    # Méthode pour afficher le résultat du combat
    def get_winner_name(self):
        result = { # Initialisation du résultat
            "message": "",
            "winner": None,
            "loser": None
        }
        if self.adversaire.hp <= 0: # Si l'adversaire n'a plus de points de vie
            result["message"] = f"{self.adversaire.name} a été vaincu. Vous avez remporté le combat!" # Message de victoire
            result["winner"] = self.pokemon_choisi.name # Initialisation du vainqueur
            result["loser"] = self.adversaire.name # Initialisation du perdant
        elif self.pokemon_choisi.hp <= 0: # Si le Pokémon du joueur n'a plus de points de vie
            result["message"] = f"{self.pokemon_choisi.name} a été vaincu. Vous avez perdu le combat." # Message de défaite
            result["winner"] = self.adversaire.name # Initialisation du vainqueur
            result["loser"] = self.pokemon_choisi.name # Initialisation du perdant

        return result # Retour du résultat
    
    # Méthode pour afficher le résultat du combat
    def fin_combat(self):
        clock = pygame.time.Clock() # Initialisation de l'horloge
        
        # Attendre 2.5 secondes avant d'afficher les boutons
        pygame.time.delay(2500) # Délai de 2.5 secondes

        while True: # Boucle infinie
            for event in pygame.event.get(): # Parcours des événements
                if event.type == pygame.QUIT: # Si l'événement est de type "Quitter"
                    pygame.quit() # Quitter le jeu si la fenêtre est fermée
                    sys.exit() # Quitter le programme si la fenêtre est fermée
                elif event.type == pygame.KEYDOWN: # Si une touche est pressée
                    if event.key == pygame.K_1: # Si la touche "1" est pressée
                        self.combat_instance.pokemon_joueur.hp = self.combat_instance.pokemon_joueur.base_hp # Réinitialisation des points de vie du Pokémon du joueur
                        self.combat_instance.adversaire.hp = self.combat_instance.adversaire.base_hp # Réinitialisation des points de vie de l'adversaire
                        self.combat_instance.pokemon_joueur.gain_xp(1) # Gain d'expérience pour le Pokémon du joueur
                        self.check_evolution() # Vérification de l'évolution du Pokémon
                        self.pokemon_choisi.evolve() # Évolution du Pokémon
                        self.combat_instance.adversaire = Combat.choose_opponent() # Choix d'un nouvel adversaire
                        self.gerer_combat() # Recommencer le combat si la touche "1" est pressée
                    elif event.key == pygame.K_2: # Si la touche "2" est pressée
                        return "quitter"  # Retourner "quitter" si la touche "2" est pressée

            # Dessiner les boutons "Continuer" et "Retour au menu" sur un fond blanc
            fenetre.fill(BLANC) # Remplissage de la fenêtre en blanc
            continuer_texte = police.render("1.Continuer", True, NOIR) # Initialisation du texte "Continuer"
            retour_menu_texte = police.render("2.Retour au menu", True, NOIR) # Initialisation du texte "Retour au menu"
            continuer_rect = continuer_texte.get_rect(center=(largeur // 2 - 100, hauteur // 2)) # Initialisation du rectangle "Continuer"
            retour_menu_rect = retour_menu_texte.get_rect(center=(largeur // 2 + 150, hauteur // 2)) # Initialisation du rectangle "Retour au menu"
            self.continuer_rect = continuer_rect # Initialisation du rectangle "Continuer"
            self.retour_menu_rect = retour_menu_rect # Initialisation du rectangle "Retour au menu"
            fenetre.blit(continuer_texte, continuer_rect) # Affichage du texte "Continuer"
            fenetre.blit(retour_menu_texte, retour_menu_rect) # Affichage du texte "Retour au menu"

            pygame.display.flip() # Mise à jour de l'affichage
            clock.tick(30) # Mise à jour de l'horloge


        





