from util import lire_historique_utilisateur, enregistrer_partie, lire_dictionnaires_mots

dico={
  "facile": [
    "chat",
    "pomme",
    "soleil",
    "mais",
    "lune",
    "roue",
    "lac",
    "arbre",
    "pain",
    "vin",
    "echo",
    "ours",
    "jeu",
    "mur",
    "rose",
    "pont",
    "mer",
    "riz",
    "feu",
    "vent",
    "ciel",
    "livre",
    "miel",
    "lait",
    "cerf",
    "anne",
    "bateau",
    "clé",
    "neige",
    "jour",
    "main",
    "cour"
  ],
  "intermediaire": [
    "ordinateur",
    "bibliotheque",
    "ocean",
    "piano",
    "guitare",
    "elephant",
    "camera",
    "telephone",
    "ordinateur",
    "microphone",
    "chevalier",
    "papillon",
    "chocolat",
    "horizon",
    "calendrier",
    "bicyclette",
    "ascenseur",
    "globule",
    "diamant",
    "serpent",
    "astronome",
    "laboratoire",
    "croissant",
    "perroquet",
    "navire",
    "dinosaure",
    "compositeur",
    "magnolia",
    "tradition",
    "console",
    "corail"
  ],
  "difficile": [
    "cryptographie",
    "photosynthese",
    "ornithorynque",
    "hydrophobe",
    "jazz",
    "un",
    "kiwi",
    "ex",
    "veux",
    "voeux",
    "hippie",
    "zut",
    "anthracite",
    "styx",
    "echolalie",
    "abjection",
    "pilotis",
    "algorithme",
    "schisme",
    "onze",
    "qualification",
    "adjectif",
    "testosterone",
    "zinc",
    "dithyrambique",
    "whisky",
    "sexisme",
    "pixel",
    "sphinx",
    "kryptonite",
    "palindrome",
    "asteroide",
    "convalescence"
  ]
}

username=input("Entrez votre nom d'utilisateur: ")
print((f"Bienvenue, {username}!\n\n\nMenu principal:\n1. Commencer une partie\n2. Afficher l'historique\n3. Quitter"))
choix=int(input('Entrez votre choix: '))
if choix==1:
    niveau=int(input('Choisissez une difficulté:\n1. Facile\n2. Intermediaire\n3. Difficile\n\nEntrez votre choix: '))
    import random
    if niveau==1:
        # mot=random.choice(dico["facile"])
        mot='pomme'
        listemot_cache=('_ '*len(mot)).split()
        mot_cache=' '.join(listemot_cache)
        lettres_trouvees=''
        lettres__ratees=''
        interface=f'Mot:{mot_cache}\nLettres trouvées: {lettres_trouvees}\nLettres ratées: {lettres__ratees}\n\n +---+\n |   |\n     |\n     |\n     |\n     |\n========= '
        print(interface)
        print(mot)
        compteur_derreurs=1
        
        while compteur_derreurs<=6 :
            if mot_cache.replace(' ','')==mot:
                print(f"Félicitations {username} ! Vous avez deviné le mot {mot} en [temps écoulé] secondes et [nombre d'essais] tentatives échouées.")
                break

            lettre=input('Entrez une lettre: ')
            if lettre.isalpha==False:
                print('Vous devez entrer une lettre')
            elif lettre in lettres__ratees+lettres_trouvees:
                print('Cette lettre a deja ete choisie')
            elif lettre in mot:
                for i in range(len(mot)):
                    if lettre==mot[i]:
                        listemot_cache[i]=lettre
                        mot_cache=' '.join(listemot_cache)
                        lettres_trouvees+=lettre
                        interface=f'Mot:{mot_cache}\nLettres trouvées: {lettres_trouvees}\nLettres ratées: {lettres__ratees}\n\n +---+\n |   |\n     |\n     |\n     |\n     |\n========= '
                        print(interface)
                
            elif lettre not in mot:
                    if compteur_derreurs==1:
                        lettres__ratees+=lettre
                        interface=f'Mot:{mot_cache}\nLettres trouvées: {lettres_trouvees}\nLettres ratées: {lettres__ratees}\n\n +---+\n |   |\n o   |\n     |\n     |\n     |\n========= '
                        print(interface)
                   
                    elif compteur_derreurs==2:
                        lettres__ratees+=lettre
                        interface=f'Mot:{mot_cache}\nLettres trouvées: {lettres_trouvees}\nLettres ratées: {lettres__ratees}\n\n +---+\n |   |\n o   |\n |   |\n     |\n     |\n========= '
                        print(interface)
                     
                    elif compteur_derreurs==3:
                        lettres__ratees+=lettre
                        interface=f'Mot:{mot_cache}\nLettres trouvées: {lettres_trouvees}\nLettres ratées: {lettres__ratees}\n\n +---+\n |   |\n o   |\n/|   |\n     |\n     |\n========= '
                        print(interface)
                     
                    elif compteur_derreurs==4:
                        lettres__ratees+=lettre
                        interface=f'Mot:{mot_cache}\nLettres trouvées: {lettres_trouvees}\nLettres ratées: {lettres__ratees}\n\n +---+\n |   |\n o   |\n/|\  |\n     |\n     |\n========= '
                        print(interface)

                    elif compteur_derreurs==5:
                        lettres__ratees+=lettre
                        interface=f'Mot:{mot_cache}\nLettres trouvées: {lettres_trouvees}\nLettres ratées: {lettres__ratees}\n\n +---+\n |   |\n o   |\n/|\  |\n/    |\n     |\n========= '
                        print(interface)
                        
                    elif compteur_derreurs==6:
                        print(f'Vous avez perdu! Le mot etait {mot}\nAppuyez sur Enter pour continuer...')
                    compteur_derreurs+=1
        
            
    elif niveau==2:
        ok=1

    elif niveau==3:
        ok=1

    else:
        print('Choix invalide, veuillez réessayer.')















elif choix==2:
    ok=1











elif choix==3:
    ok=1









else:
    print('Choix invalide, veuillez réessayer.')




# Squelette du menu principal :
# Ce code peut être un bon point de départ.
# Il est possible de le modifier à votre guise ou de l'enlever complètement pour partir de zéro.
while True:
    choix_menu_principal = ...

    if choix_menu_principal == "1":
        # Demander à l'utilisateur de choisir une difficulté,
        # sélectionner un mot aléatoire
        # et commencer la partie.
        ...
    elif choix_menu_principal == "2":
        # Afficher l'historique de l'utilisateur.
        ...
    elif choix_menu_principal == "3":
        # Quitter le programme.
        ...
    else:
        # Afficher un message d'entrée invalide.
        ...
