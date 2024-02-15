#combat.py
import random
from pokemon import Pokemon, POKEMON_LIST
from pokedex import Pokedex

# Classe pour gérer les combats
class Combat:
    # Initialisation de la classe
    def __init__(self, pokemon_joueur, adversaire):
        self.pokemon_joueur = pokemon_joueur # Initialisation du Pokémon du joueur
        self.adversaire = adversaire # Initialisation de l'adversaire

    # Méthode pour choisir un adversaire aléatoire
    @staticmethod
    def choose_opponent():
        opponent = random.choice(POKEMON_LIST) # Choix aléatoire d'un Pokémon
        print(f"Votre nouvel adversaire est {opponent.name}") # Affichage du nom de l'adversaire
        return opponent # Retour du Pokémon choisi

    # Méthode pour réinitialiser l'adversaire
    def reset_opponent(self):
        self.adversaire = self.choose_opponent() # Choix d'un nouvel adversaire aléatoire

    # Méthode pour vérifier si la fuite est réussie
    def fuite_reussie(self):
        return random.random() > 1/3 # Retourne True si le nombre aléatoire est supérieur à 1/3

    # Méthode pour vérifier si le type de Pokémon est supérieur
    def is_superior(self, attacker_type, defender_type):
        relations_types_sup = { # Initialisation des relations de types
            "plante": {"eau"}, # Relation de type plante -> eau
            "eau": {"feu"}, # Relation de type eau -> feu
            "feu": {"plante"}, # Relation de type feu -> plante
        }
        return defender_type in relations_types_sup.get(attacker_type, set()) # Retourne True si le type du défenseur est dans les types supérieurs

    # Méthode pour attaquer un Pokémon
    def attack(self, attacker, defender):
        if self.is_superior(attacker.poke_type, defender.poke_type): # Si le type du Pokémon attaquant est supérieur
            damage = (attacker.attack_pt * 2) - defender.defense # Calcul des dégâts
        elif self.is_superior(defender.poke_type, attacker.poke_type): # Si le type du Pokémon défenseur est supérieur
            damage = max(10, ((attacker.attack_pt * 0.5) - defender.defense)) # Calcul des dégâts
        else:
            damage = max(0, (attacker.attack_pt - defender.defense)) # Calcul des dégâts

        defender.hp -= damage # Réduction des points de vie du défenseur
        return f"{attacker.name} inflige {damage} points de dégâts à {defender.name}, il lui reste {defender.hp}" # Retour du message d'attaque

    # Méthode pour attaquer par l'adversaire
    def attack_by_adversary(self):
        result = self.attack(self.adversaire, self.pokemon_joueur) # Appel de la méthode d'attaque
        return f"L'adversaire attaque ! {result}" # Retour du message d'attaque

    # Méthode pour utiliser une potion
    def use_potion(self):
        if self.pokemon_joueur.hp < self.pokemon_joueur.base_hp: # Si les points de vie du Pokémon sont inférieurs à sa vie maximale
            recovered_hp = min(100, self.pokemon_joueur.base_hp - self.pokemon_joueur.hp) # Calcul des points de vie récupérés
            self.pokemon_joueur.hp += recovered_hp # Ajout des points de vie récupérés
            return f"{self.pokemon_joueur.name} récupère {recovered_hp} points de vie grâce à la potion." # Retour du message de récupération
        else:
            return f"{self.pokemon_joueur.name} a déjà tous ses points de vie. La potion n'a aucun effet." # Retour du message d'erreur

    # Méthode pour gérer le combat
    def do_combat(self, action_joueur):
        result = { # Initialisation du résultat
            "message": "", # Initialisation du message
            "winner": None, # Initialisation du vainqueur
            "loser": None # Initialisation du perdant
        }

        if self.pokemon_joueur.hp > 0: # Si le Pokémon du joueur a des points de vie
            if action_joueur == 1: # Si le joueur choisit d'attaquer
                result["message"] = self.attack(self.pokemon_joueur, self.adversaire) # Appel de la méthode d'attaque
                result["message"] += "\n" + self.attack_by_adversary() # Appel de la méthode d'attaque par l'adversaire
            elif action_joueur == 4: # Si le joueur choisit d'utiliser une potion
                result["message"] = self.use_potion() # Appel de la méthode pour utiliser une potion
                result["message"] += "\n" + self.attack_by_adversary() # Appel de la méthode d'attaque par l'adversaire
            elif action_joueur == 7: # Si le joueur choisit de fuir
                if self.fuite_reussie(): # Si la fuite est réussie
                    result["message"] = "Vous avez fui le combat." # Message de fuite réussie
                    result["winner"] = self.adversaire.name # Initialisation du vainqueur
                    result["loser"] = self.pokemon_joueur.name # Initialisation du perdant
                else:
                    result["message"] = "La fuite a échoué. L'adversaire contre-attaque !" # Message de fuite échouée
                    result["message"] += "\n" + self.attack_by_adversary() # Appel de la méthode d'attaque par l'adversaire

        if self.adversaire.hp <= 0: # Si l'adversaire n'a plus de points de vie
            result["message"] = f"{self.adversaire.name} a été vaincu. Vous avez remporté le combat!" # Message de victoire
            result["winner"] = self.pokemon_joueur.name # Initialisation du vainqueur
            result["loser"] = self.adversaire.name # Initialisation du perdant
        elif self.pokemon_joueur.hp <= 0: # Si le Pokémon du joueur n'a plus de points de vie
            result["message"] = f"{self.pokemon_joueur.name} a été vaincu. Vous avez perdu le combat." # Message de défaite
            result["winner"] = self.adversaire.name # Initialisation du vainqueur
            result["loser"] = self.pokemon_joueur.name # Initialisation du perdant

        return result # Retour du résultat
