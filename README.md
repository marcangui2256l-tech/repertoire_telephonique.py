# Gestion de contacts en Python

Programme en ligne de commande qui permet de gérer un répertoire téléphonique.
Les contacts sont organisés avec des **dictionnaires** Python.

Projet réalisé en classe de Terminale (spécialité NSI).

## Fonctionnalités

- Ajouter un contact (nom, prénom, téléphone, e-mail facultatif)
- Afficher tous les contacts, triés par nom puis prénom
- Rechercher un contact par nom ou prénom
- Modifier une partie d'un champ (par exemple changer seulement les premiers chiffres d'un numéro)
- Supprimer un contact

## Lancer le programme

Il faut avoir [Python 3](https://www.python.org/downloads/) installé.

```bash
python répertoire.py
```

## Exemple d'utilisation

```
===== GESTION DES CONTACTS =====
1 - Ajouter un contact
2 - Afficher tous les contacts
3 - Rechercher un contact
4 - Modifier un contact
5 - Supprimer un contact
0 - Quitter
Votre choix : 1
Nom : Dupont
Prénom : Marie
Téléphone : 0612345678
E-mail (facultatif) :
Contact ajouté avec l'identifiant 1
```

## Structure des données

Chaque contact possède un identifiant unique, utilisé comme clé du dictionnaire.
Cela permet d'avoir plusieurs contacts avec le même nom.

```python
contacts = {
    1: {"nom": "Dupont", "prenom": "Marie", "telephone": "0612345678", "email": ""},
    2: {"nom": "Dupont", "prenom": "Paul", "telephone": "0698765432", "email": ""}
}
```

## Limites et améliorations possibles

- Les contacts ne sont pas sauvegardés : ils disparaissent à la fermeture du programme.
- Idée d'amélioration : enregistrer les contacts dans un fichier JSON.
- Idée d'amélioration : vérifier que le numéro de téléphone contient 10 chiffres.

## Auteur

Angui Koffi
