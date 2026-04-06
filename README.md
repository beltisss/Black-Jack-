# Blackjack en Python

Petit jeu de Blackjack en console, codé en Python.
Le joueur affronte un banquier selon les règles classiques de base :
- chaque joueur reçoit 2 cartes au départ ;
- le joueur peut piocher autant qu'il veut tant qu'il ne dépasse pas 21 ;
- le banquier pioche jusqu'à atteindre au moins 17 ;
- celui qui a le meilleur score sans dépasser 21 gagne.

## Lancer le projet

Assure-toi d'avoir Python 3 installé, puis place-toi dans le dossier contenant le fichier.

```bash
python3 blackjack_final.py
```

## Comment tester

1. Ouvre un terminal.
2. Va dans le dossier où se trouve le fichier `blackjack_final.py`.
3. Lance :

```bash
python3 blackjack_final.py
```

4. Le jeu démarre dans le terminal.
5. À chaque tour, réponds :
   - `o` pour piocher une nouvelle carte ;
   - `n` pour t'arrêter.

## Exemple

```text
===== BLACKJACK =====

Joueur :
- 8 de coeur
- Roi de trèfle
Score : 18

Banquier :
- [Carte cachée]
- 6 de pique
Score visible : ?

Veux-tu une nouvelle carte ? (o/n) : n
```

## Structure du code

Le programme est organisé avec plusieurs classes :
- `Carte` : représente une carte du jeu ;
- `Paquet` : crée et mélange les 52 cartes ;
- `Main` : stocke les cartes d'un joueur et calcule son score ;
- `BlackJack` : gère le déroulement complet de la partie.

## Remarques

- Le calcul des As est géré correctement : un As vaut 11 tant que cela n'entraîne pas un dépassement de 21, sinon il vaut 1.
- Le projet ne nécessite aucune bibliothèque externe.
- Tout se joue directement dans le terminal.

## Fichiers

- `blackjack_final.py` : fichier principal du jeu
- `README.md` : explication du projet et méthode de lancement
