## Sommaire
- [POO](#poo)
  - [Sommaire](#sommaire)
  - [Intro](#intro)
  - [I. Card (3 points)](#i-card-3-points)
  - [II. Cards (5 points)](#ii-cards-5-points)
  - [III. Game (7 points)](#iii-game-7-points)
  - [IV. Rendu (5 points)](#iv-rendu-5-points)
  - [Sommaire](#sommaire-1)
  - [Intro](#intro-1)
  - [I. Card (3 points)](#i-card-3-points-1)
  - [II. Cards (5 points)](#ii-cards-5-points-1)
  - [III. Game (7 points)](#iii-game-7-points-1)
  - [Bonus](#bonus)
  - [IV. Rendu (5 points)](#iv-rendu-5-points-1)

## Intro

Dans ce tp vous aurez 3 parties à réaliser. Ces parties sont complémentaires, et sont en réalité la séparation d'un projet en 3 étapes.

Chaque partie vaut un certain nombre de points qui vous est indiqué à chaque fois. Mais pour vous donner une idée globale, dans la notation il y est compris la clarté du code ainsi que la fonctionnalité de ce dernier (faites donc attention au nom de vos variables/fonctions).

Comme il est question de point, vous vous doutez que le TP sera à rendre et contribuera à la note du ydays. Sur ces mots, bonne chance à vous :)

## I. Card (3 points)

Créer une classe *card*:

Attributs:
- *value* 
- *color*

Méthodes :
- *getters* 
- *display*

Un getter est un *get* d'un attribut, permettant d'y accéder d'une manière dite "propre". 
La méthode *Display* permet d'afficher le nom d'une carte sous forme de Valeur + Couleur.

## II. Cards (5 points)

Créer une classe *cards* :

Attributs :
- Liste de cartes
- Compteur de cartes

Méthodes :
- Piocher (return la carte)

## III. Game (7 points)

Dans cette partie nous allons reproduire une version simplifiée du BlackJack. Dans cette version nous aurons les règles suivantes :

- Distribuer 2 cartes au Joueur et une au croupier dans l'ordre : Joueur - croupier - Joueur.
- Tour Joueur
  - Tant que le joueur est en jeu et qu'il le souhaite, il pioche :
    - Si le total de points dans sa main excède 21 il perd.
    - Si le total de points dans sa main est inférieur à 21 :
      - Il peut continuer de piocher
      - Il peut s'arrêter là
    - Si le total de points dans sa main est égale à 21 il gagne
- Si le Joueur est toujours en jeu :
  - Tour du Croupier 
    - Tant que le total de point dans sa main n'excède pas 16 il continue de piocher. Au-dessus de 16 il s'arrête.
- Si le Joueur et le Croupier sont toujours en jeu, on vérifie qui a le plus de points. Ce dernier l'emporte.

Attention, la valeur des cartes se fait suivant le tableau suivant:

|     2 - 10     | Têtes |   AS   | 
|----------------|------ |--------|
| Valeur Faciale |  10   | 1 ou 11|

Ici, vous pouvez continuer avec une classe *Game* ou alors avec des fonctions gérant le jeu ou encore avec des class pour le Joueur et le Croupier, à vous de voir ce qui est le plus judicieux et ce qui vous convient le mieux.
Dans tous les cas, à la fin de cette partie, Vous devriez avoir un pseudo-BlackJack fonctionnel.

## Bonus 

Modifier le programme de manière à ajouter un système de mise, le Joueur indique dans un premier temps le montant total qu'il pourra dépenser et ceux avant le distribution des cartes. A la fin de la manche il faut actualiser la balance du Joueur en fonction du résultat de la partie, si le Joueur remporte la partie il remporte 1x sa mise sinon il la perd.

Quand le Joueur décide d'arrêter de jouer on affiche la somme finale de sa balance.

## IV. Rendu (5 points)

Afin de pouvoir noter l'avancée sur chaque point, il faudra nous rendre votre script python ainsi qu'une documentation expliquant ce que vous avez fait à chaque partie et pourquoi ce choix. Cette documentation devra être sous format pdf ou bien md. 

Pour le rendu de ce TP vous avez jusqu'à 18h pour le finir. Vous pouvez le rendre en mp discord à travers un ZIP ou bien avec git en public bien entendu pour qu'on puisse y accéder.

Comme vous pouvez le constater, cette partie est sur 5 :
- A l'heure & Bon Format -> 1 point
- Clarté du code -> 1 point
- Contenue de la documentation -> 3 points