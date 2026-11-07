
# ==========================================
# TP5 : Les listes et les listes de listes
# ==========================================

# ETAPE 1 : Creer et modifier une liste

etudiants = ["Alice", "Bob", "Charlie"]

print("Liste initiale :", etudiants)

etudiants.append("Diana")
print("Apres append :", etudiants)

etudiants.insert(1, "Eve")
print("Apres insert :", etudiants)

etudiants.remove("Bob")
print("Apres remove :", etudiants)

dernier = etudiants.pop()
print("Element supprime :", dernier)
print("Liste finale :", etudiants)


# ETAPE 2 : Acceder aux elements par index

print("\n--- Acces par index ---")

print("Premier element :", etudiants[0])
print("Dernier element :", etudiants[-1])
print("Nombre d'elements :", len(etudiants))


# ETAPE 3 : Slicing (tranches)

notes = [12, 15, 9, 18, 14, 16]

print("\n--- Slicing ---")

print("Notes de 1 a 3 :", notes[1:4])
print("Trois premieres notes :", notes[:3])
print("Trois dernieres notes :", notes[3:])
print("Un element sur deux :", notes[::2])
print("Liste inversee :", notes[::-1])


# ETAPE 4 : Liste de listes

classe = [
    ["Alice", 20, 15.5],
    ["Eve", 19, 14.0],
    ["Charlie", 21, 16.5]
]

classe.append(["Diana", 22, 13.0])

print("\n--- Liste de listes ---")

for index, (nom, age, note) in enumerate(classe, start=1):
    print(f"Etudiant {index} : {nom}, {age} ans, note {note}")


# ETAPE 5 : Extraire et modifier une valeur en 2D

print("\n--- Acces en 2D ---")

age_charlie = classe[2][1]
print("Age de Charlie :", age_charlie)

classe[2][2] = 17.0
print("Nouvelle note de Charlie :", classe[2][2])


# ETAPE 6 : Tri et statistiques

print("\n--- Tri et statistiques ---")

classe.sort(key=lambda ligne: ligne[2], reverse=True)

for etudiant in classe:
    print(etudiant)

notes_classe = [etudiant[2] for etudiant in classe]

moyenne = sum(notes_classe) / len(notes_classe)

print("Moyenne :", round(moyenne, 2))


# ETAPE 7 : Recherche d'un etudiant

print("\n--- Recherche ---")

recherche = input("Entrez le nom a rechercher : ").strip()

trouve = False

for nom, age, note in classe:
    if nom.lower() == recherche.lower():
        print("Etudiant trouve :", nom, age, note)
        trouve = True
        break

if not trouve:
    print("Etudiant introuvable.")


# ==========================================
# MINI-PROJET : GESTION D'UNE CLASSE
# ==========================================

classe = [
    ["Alice", 20, 15.5],
    ["Bob", 19, 12.0],
    ["Charlie", 22, 16.0]
]


# Fonction 1 : Afficher les etudiants

def afficher_classe(classe):
    if not classe:
        print("La classe est vide.")
        return

    print("\n--- Liste des etudiants ---")

    for index, (nom, age, note) in enumerate(classe, start=1):
        print(f"{index}. {nom} - {age} ans - Note : {note}")


# Fonction 2 : Ajouter un etudiant

def ajouter_etudiant(classe):
    nom = input("Nom : ").strip()

    if not nom:
        print("Le nom est obligatoire.")
        return

    try:
        age = int(input("Age : "))
        note = float(input("Note : "))

        if age <= 0 or not 0 <= note <= 20:
            print("Age ou note invalide.")
            return

    except ValueError:
        print("Saisie invalide.")
        return

    classe.append([nom, age, note])

    print(nom, "a ete ajoute avec succes.")


# Fonction 3 : Supprimer un etudiant

def supprimer_etudiant(classe):
    if not classe:
        print("Rien a supprimer.")
        return

    afficher_classe(classe)

    try:
        index = int(input("Numero de l'etudiant a supprimer : ")) - 1

        if 0 <= index < len(classe):
            etudiant = classe.pop(index)
            print(etudiant[0], "a ete supprime.")
        else:
            print("Numero invalide.")

    except ValueError:
        print("Veuillez saisir un nombre valide.")


# Fonction 4 : Modifier un etudiant

def mettre_a_jour_etudiant(classe):
    if not classe:
        print("La classe est vide.")
        return

    afficher_classe(classe)

    try:
        index = int(input("Numero de l'etudiant a modifier : ")) - 1

        if not 0 <= index < len(classe):
            print("Numero invalide.")
            return

        etudiant = classe[index]

        print("Modification de", etudiant[0])

        nouveau_nom = input("Nouveau nom : ").strip()

        if nouveau_nom:
            etudiant[0] = nouveau_nom

        nouvel_age = input("Nouvel age : ").strip()

        if nouvel_age:
            try:
                age = int(nouvel_age)
                if age > 0:
                    etudiant[1] = age
                else:
                    print("Age invalide.")
            except ValueError:
                print("Age invalide.")

        nouvelle_note = input("Nouvelle note : ").strip()

        if nouvelle_note:
            try:
                note = float(nouvelle_note)

                if 0 <= note <= 20:
                    etudiant[2] = note
                else:
                    print("Note invalide.")

            except ValueError:
                print("Note invalide.")

        print("Modification terminee.")

    except ValueError:
        print("Veuillez saisir un nombre valide.")


# Fonction 5 : Afficher les statistiques

def afficher_statistiques(classe):
    if not classe:
        print("Aucune donnee disponible.")
        return

    notes = [etudiant[2] for etudiant in classe]

    moyenne = sum(notes) / len(notes)

    meilleure = max(classe, key=lambda e: e[2])
    pire = min(classe, key=lambda e: e[2])

    print("\n--- Statistiques de la classe ---")

    print("Nombre d'etudiants :", len(classe))
    print("Moyenne :", round(moyenne, 2))
    print("Meilleure note :", meilleure[2], "-", meilleure[0])
    print("Moins bonne note :", pire[2], "-", pire[0])


# ==========================================
# BOUCLE PRINCIPALE
# ==========================================

while True:

    print("\n========== GESTION DE LA CLASSE ==========")

    print("1. Afficher tous les etudiants")
    print("2. Ajouter un etudiant")
    print("3. Supprimer un etudiant")
    print("4. Modifier un etudiant")
    print("5. Afficher les statistiques")
    print("q. Quitter")

    choix = input("Votre choix : ").strip().lower()

    if choix == "1":
        afficher_classe(classe)

    elif choix == "2":
        ajouter_etudiant(classe)

    elif choix == "3":
        supprimer_etudiant(classe)

    elif choix == "4":
        mettre_a_jour_etudiant(classe)

    elif choix == "5":
        afficher_statistiques(classe)

    elif choix == "q":
        print("Au revoir !")
        break

    else:
        print("Option inconnue. Reessayez.")
