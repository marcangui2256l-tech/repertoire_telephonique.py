# Gestion de contacts avec des dictionnaires
#
# Structure : chaque contact a un identifiant unique (entier) pour clé.
# Cela permet d'avoir plusieurs contacts avec le même nom.
#
# contacts = {
#     1: {"nom": "Dupont", "prenom": "Marie", "telephone": "0612345678", "email": "marie@mail.fr"},
#     2: {"nom": "Dupont", "prenom": "Paul",  "telephone": "0698765432", "email": ""}
# }

contacts = {}
prochain_id = 1


def ajouter_contact(nom, prenom, telephone, email=""):
    """Ajoute un contact et renvoie son identifiant."""
    global prochain_id
    contacts[prochain_id] = {
        "nom": nom,
        "prenom": prenom,
        "telephone": telephone,
        "email": email
    }
    identifiant = prochain_id
    prochain_id = prochain_id + 1
    return identifiant


def afficher_contact(identifiant):
    """Affiche un contact à partir de son identifiant."""
    c = contacts[identifiant]
    ligne = str(identifiant) + " - " + c["nom"].upper() + " " + c["prenom"] + " : " + c["telephone"]
    if c["email"] != "":
        ligne = ligne + " (" + c["email"] + ")"
    print(ligne)


def afficher_tous():
    """Affiche tous les contacts triés par nom puis prénom."""
    if len(contacts) == 0:
        print("Aucun contact.")
        return
    # On trie les identifiants selon (nom, prénom)
    ids_tries = sorted(contacts, key=lambda i: (contacts[i]["nom"].lower(), contacts[i]["prenom"].lower()))
    for identifiant in ids_tries:
        afficher_contact(identifiant)
    print(len(contacts), "contact(s) au total.")


def rechercher(texte):
    """Renvoie la liste des identifiants dont le nom ou le prénom contient le texte."""
    texte = texte.lower()
    resultats = []
    for identifiant in contacts:
        c = contacts[identifiant]
        if texte in c["nom"].lower() or texte in c["prenom"].lower():
            resultats.append(identifiant)
    return resultats


def modifier_contact(identifiant, champ, ancienne_partie, nouvelle_partie):
    """Remplace seulement une partie du champ ('nom', 'prenom', 'telephone' ou 'email').
    Renvoie False si le champ n'existe pas ou si la partie n'est pas trouvée."""
    if identifiant in contacts and champ in contacts[identifiant]:
        valeur = contacts[identifiant][champ]
        if ancienne_partie in valeur:
            contacts[identifiant][champ] = valeur.replace(ancienne_partie, nouvelle_partie, 1)
            return True
    return False


def supprimer_contact(identifiant):
    """Supprime un contact. Renvoie False si l'identifiant n'existe pas."""
    if identifiant in contacts:
        del contacts[identifiant]
        return True
    return False


def lire_identifiant():
    """Demande un identifiant et renvoie un entier (ou None si invalide)."""
    saisie = input("Identifiant du contact : ")
    if saisie.isdigit():
        return int(saisie)
    return None


def menu():
    print()
    print("===== GESTION DES CONTACTS =====")
    print("1 - Ajouter un contact")
    print("2 - Afficher tous les contacts")
    print("3 - Rechercher un contact")
    print("4 - Modifier un contact")
    print("5 - Supprimer un contact")
    print("0 - Quitter")


# ----- Programme principal -----
choix = ""
while choix != "0":
    menu()
    choix = input("Votre choix : ")

    if choix == "1":
        nom = input("Nom : ")
        prenom = input("Prénom : ")
        telephone = input("Téléphone : ")
        email = input("E-mail (facultatif) : ")
        if nom == "" or prenom == "" or telephone == "":
            print("Nom, prénom et téléphone sont obligatoires.")
        else:
            identifiant = ajouter_contact(nom, prenom, telephone, email)
            print("Contact ajouté avec l'identifiant", identifiant)

    elif choix == "2":
        afficher_tous()

    elif choix == "3":
        texte = input("Nom ou prénom à rechercher : ")
        resultats = rechercher(texte)
        if len(resultats) == 0:
            print("Aucun contact trouvé.")
        else:
            for identifiant in resultats:
                afficher_contact(identifiant)

    elif choix == "4":
        identifiant = lire_identifiant()
        if identifiant in contacts:
            champ = input("Champ à modifier (nom, prenom, telephone, email) : ")
            if champ in contacts[identifiant]:
                print("Valeur actuelle :", contacts[identifiant][champ])
                ancienne = input("Partie à remplacer : ")
                nouvelle = input("Remplacer par : ")
                if modifier_contact(identifiant, champ, ancienne, nouvelle):
                    print("Nouvelle valeur :", contacts[identifiant][champ])
                else:
                    print("Cette partie n'a pas été trouvée dans le champ.")
            else:
                print("Champ invalide.")
        else:
            print("Identifiant introuvable.")

    elif choix == "5":
        identifiant = lire_identifiant()
        if supprimer_contact(identifiant):
            print("Contact supprimé.")
        else:
            print("Identifiant introuvable.")

    elif choix == "0":
        print("Au revoir !")

    else:
        print("Choix invalide.")