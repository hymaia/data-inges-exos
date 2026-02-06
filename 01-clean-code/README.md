# Clean code by Hymaïa

## Objectif de l'exercice

Dans le fichier `main.py` se trouve un code python qui résoud l'exercice du 25 décembre de l'advent of code 2024.

Ce code est délibérément "crade". Votre objectif est d'utiliser vos connaissances pour le rendre le plus à l'état de l'art possible, comme si demain cela devenait un projet critique et stratégique pour votre entreprise.

Il n'y a aucune limite à votre imagination pour en faire le plus possible et pour rendre le projet le plus beau possible.

Pour vous aider voici une description complète de l'objectif de l'exercice.

## Résumé du code – Advent of Code 2024, Day 25

### 1. Objectif général

Ce programme sert à résoudre le puzzle **Advent of Code 2024 – Day 25**.  
Son objectif est de calculer **combien de paires clé / serrure sont compatibles** à partir de schémas ASCII fournis en entrée.

Une clé est considérée comme compatible avec une serrure si, lorsqu’on les superpose colonne par colonne, **aucune dent de la clé ne chevauche un picot de la serrure**.

Le programme teste toutes les combinaisons possibles et compte celles qui fonctionnent.

---

### 2. C’est quoi une clé ?

Une **clé** est représentée par un dessin ASCII :
- la **première ligne est composée uniquement de `.`**,
- la **dernière ligne est composée uniquement de `#`**,
- les `#` forment des colonnes qui montent depuis le bas.

#### Exemple de clé

```text
.....
#....
#....
#...#
#.#.#
#.###
```

Ce dessin est transformé en une liste de hauteurs, une par colonne : [5, 0, 2, 1, 3]

Chaque nombre indique la hauteur occupée par la clé dans la colonne correspondante.

---

### 3. C’est quoi une serrure ?

Une **serrure** est aussi décrite par un schéma ASCII, mais inversé :
- la **première ligne est entièrement remplie de `#`**,
- la **dernière ligne est entièrement remplie de `.`**,
- les `#` représentent des picots qui descendent depuis le haut.

#### Exemple de serrure

```text
.####
.####
.####
.#.#.
.#...
.....
```

Ce schéma est converti en hauteurs de picots : [0, 5, 3, 4, 3]


Chaque valeur correspond à la profondeur du picot dans la colonne.

---

### 4. Quand une clé et une serrure sont compatibles ?

Une clé et une serrure sont **compatibles** si, pour chaque colonne, la somme : hauteur de la clé + hauteur de la serrure ne dépasse pas l’espace disponible entre le haut et le bas.

#### Exemple de compatibilité

Serrure : [0, 5, 3, 4, 3]

Clé : [3, 0, 2, 0, 1]

Comparaison colonne par colonne :

```text
0 + 3 = OK
5 + 0 = OK
3 + 2 = OK
4 + 0 = OK
3 + 1 = OK
```

➡️ Aucune collision : **la clé peut ouvrir la serrure**.

Si au moins une colonne dépasse l’espace disponible, la paire est rejetée.

---

### 5. À quoi ressemble l’output ?

Le programme affiche **un seul nombre**, par exemple : 3
