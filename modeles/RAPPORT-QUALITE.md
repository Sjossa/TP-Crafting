````markdown
# Rapport qualité, module inventaire

Nom : Johnny Sassiat
Date : 15 Septembre 2026
Empreinte du commit de départ : 097fc51

---

## 1. Tableau de bord initial

Mesures relevées avant toute modification.

### Complexité par fonction

| Fonction      | Ligne | Complexité cyclomatique | Rang |
| ------------- | ----- | ----------------------- | ---- |
| `rapport`     | 122   | 22                      | D    |
| `par_cat`     | 94    | 10                      | B    |
| `mouv`        | 37    | 9                       | B    |
| `classer`     | 74    | 5                       | A    |
| `val`         | 19    | 3                       | A    |
| `alerte`      | 29    | 3                       | A    |
| `cout`        | 62    | 3                       | A    |
| `rot`         | 87    | 2                       | A    |
| `maj_prix`    | 175   | 1                       | A    |
| `export_json` | 185   | 1                       | A    |

Commande utilisée :

```bash
radon cc -s -a inventaire/inventaire.py
```
````

### Synthèse du fichier

| Mesure                   | Valeur  | Commande                                                                        |
| ------------------------ | ------- | ------------------------------------------------------------------------------- |
| Lignes de code réelles   | 159     | radon raw inventaire/inventaire.py                                              |
| Complexité moyenne       | 5.9     | radon cc -s -a inventaire/inventaire.py                                         |
| Indice de maintenabilité | 36.80   | radon mi -s inventaire/inventaire.py                                            |
| Score pylint             | 7.76/10 | pylint inventaire/inventaire.py                                                 |
| Problèmes ruff           | 14      | ruff check inventaire/inventaire.py                                             |
| Entrées vulture          | 14      | vulture inventaire/inventaire.py                                                |
| Couverture de branches   | 0%      | pytest --cov=inventaire --cov-branch inventaire/                                |
| Barrière xenon           | échec   | xenon --max-absolute B --max-modules A --max-average A inventaire/inventaire.py |

---

## 2. Catalogue des odeurs

Douze entrées minimum. Trois au moins doivent être invisibles pour les outils.
La colonne conséquence décrit ce qui arrive à la personne qui devra modifier ce
fichier dans six mois.

## 2. Catalogue des odeurs

Douze entrées minimum. Trois au moins doivent être invisibles pour les outils.
La colonne conséquence décrit ce qui arrive à la personne qui devra modifier ce
fichier dans six mois.

| #   | Ligne | Odeur ou défaut                                    | Détecté par | Conséquence concrète                                                                                   |
| --- | ----- | -------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------ |
| 1   | 1     | Absence de docstring (module)                      | Pylint      | Le module n'a pas de description globale, obligeant à parcourir tout le code pour comprendre son rôle. |
| 2   | 19    | Docstring manquante                                | Pylint      | La fonction ne documente ni ses paramètres ni son retour, complexifiant son utilisation.               |
| 3   | 29    | Docstring manquante                                | Pylint      | Absence de documentation sur le comportement de la fonction d'alerte.                                  |
| 4   | 37    | Argument par défaut mutable & trop de paramètres   | Pylint      | Risque de pollution d'état partagé entre les appels et signature difficile à maintenir.                |
| 5   | 46    | Comparaison explicite à un booléen / Else superflu | Pylint      | Alourdissement syntaxique inutile qui nuit à la lisibilité du code.                                    |
| 6   | 62    | Docstring manquante                                | Pylint      | Contrat de la fonction de coût non documenté.                                                          |
| 7   | 74    | Docstring manquante                                | Pylint      | Fonction de tri sans description de ses préconditions.                                                 |
| 8   | 78    | Variable non utilisée (`i`)                        | Pylint      | Laisse des résidus de code mort ou de boucles mal nettoyées, semant la confusion.                      |
| 9   | 90    | Attrape-tout d'exception (Bare except)             | Pylint      | Masque les erreurs critiques inattendues (ex: coupure réseau), rendant le débogage impossible.         |
| 10  | 19    | Variable aux noms cryptiques (`t`, `a`)            | Humain      | Impossible de deviner la sémantique sans lire l'ensemble du corps de la fonction.                      |
| 11  | 74    | Algorithme de tri manuel (Bulles naïf)             | Humain      | Performances dégradées et réinvention d'une roue déjà optimisée dans la bibliothèque standard.         |
| 12  | 175   | Code mort en commentaire (`maj_prix`)              | Humain      | Pollution visuelle et incertitude sur le fait qu'il faille le conserver ou le supprimer.               |

## 3. Faut-il tout réécrire

Au premier abord, le score Pylint de 7.76/10 peut sembler flatteur et donner une fausse donnée de sécurité. Mais quand on regarde les autres chiffres, on voit direct qu'avec 0 % de couverture de tests et une fonction `rapport` qui explose le plafond avec une complexité de 22, ce code est hyper fragile. C'est une vraie bombe à retardement.

Même si ça donne envie de jeter à la poubelle pour repartir au propre , c'est la pire idée. Comme on l'a vu en cours avec des exemples historiques comme Netscape ou Digg, réécrire un logiciel de 0 est une erreur fatale. C'est le meilleur moyen de perdre toute la logique métier qui a été fait et corrigée au fil des années.

Au lieu de tout casser, on va utiliser une approche progressive. Le plan d'attaque est de ne rien jeter, mais de commencer par sécuriser le pire endroit : la fonction `rapport`. On va d'abord écrire des tests , et une fois que ce sera fait on pourra la nettoyer sereinement sans risquer de créer de nouveaux bugs.

---

## 4. Écarts constatés entre le code et les règles métier

Rempli pendant la mission 3, sans rien corriger.

Rapport des écarts constatés entre le code existant et les règles officielles du cahier des charges (2019).

| Règle  | Fonction / Élément                 | Ce que le code fait                                                                                                        | Ce que la règle dit (Cahier des charges)                                                                                                                                                                                                       |
| :----- | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **M1** | `val` (L. 17-25)                   | Ignore les articles dont la quantité est négative ou nulle (`if a["q"] > 0`) et ajoute 0.                                  | La valeur du stock est la somme des quantités multipliées par les prix unitaires hors taxe, arrondie au centime.                                                                                                                               |
| **M2** | `alerte` (L. 28-34)                | Vérifie si `q < seuil` de manière stricte, ignorant le cas où la quantité est égale au seuil.                              | Un article est en alerte lorsque sa quantité est inférieure ou égale à son seuil. Un article dont la quantité est exactement au seuil est en alerte.                                                                                           |
| **M3** | `mouv` (L. 37-64)                  | Modifie le stock en mémoire avant de valider le stock insuffisant, modifiant la quantité malgré le refus (`return False`). | Un mouvement de sortie dont la quantité dépasse le stock disponible est refusé, et le stock reste inchangé.                                                                                                                                    |
| **M4** | `mouv` (L. 37-43)                  | Vérifie `if q <= 0:` et retourne `False` avec un message.                                                                  | Un mouvement dont la quantité est nulle ou négative est refusé.                                                                                                                                                                                |
| **M5** | `cout` (L. 67-78)                  | Calcule le coût avec les constantes globales et applique la remise avec un test strict (`n > Q`).                          | Le coût de réapprovisionnement d'un article en alerte correspond à la quantité nécessaire pour remonter à trois fois le seuil, multipliée par le prix unitaire. Une remise de 10 % s'applique à partir de 100 unités commandées, 100 incluses. |
| **M6** | `classer` (L. 81-93)               | Trie les articles selon leur valeur (`q * pu`) par ordre décroissant via un tri à bulles.                                  | Le classement par valeur trie les articles par valeur de stock décroissante.                                                                                                                                                                   |
| **M7** | `rot` (L. 96-102)                  | Utilise `try...except` pour étouffer l'erreur de division par zéro (`v=0`) et renvoyer `0`.                                | La rotation renvoie le nombre de jours de stock restant, arrondi à l'entier inférieur, à partir des ventes des 30 derniers jours. Si aucune vente n'a eu lieu, la fonction lève une erreur explicite plutôt que de renvoyer une valeur.        |
| **M8** | `rapport` / `par_cat` (L. 105-181) | Effectue des affichages console, écrit des fichiers sur le disque, dépend de l'heure système (`datetime.now()`).           | Le rapport mensuel ne modifie aucune donnée et ne dépend d'aucune ressource extérieure au moment où il calcule.                                                                                                                                |

## 5. Tableau de bord après refactoring

Mêmes mesures, mêmes commandes qu'en partie 1.

| Mesure | Avant | Après | Écart |
| ------ | ----- | ----- | ----- |
|        |       |       |       |

Ce que ce delta prouve, en trois phrases maximum :

---

## 6. Bugs prouvés puis corrigés

| Règle violée | Ligne d'origine | Commit red | Commit fix | Conséquence métier |
| ------------ | --------------- | ---------- | ---------- | ------------------ |
|              |                 |            |            |                    |

Pour au moins un de ces bugs, la conséquence est chiffrée en euros ou en ruptures de stock.

```

```
