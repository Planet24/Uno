class Jeu:
    """Listes et dictionnaires pour gérer les cartes."""
    # Préparation du jeu
    listeJaune = ['J','J0','J1','J2','J3','J4','J5','J6','J7','J8','J9','JR','JS','J+']
    listeBleu = ['B','B0','B1','B2','B3','B4','B5','B6','B7','B8','B9','BR','BS','B+']
    listeRouge = ['R','R0','R1','R2','R3','R4','R5','R6','R7','R8','R9','RR','RS','R+']
    listeVert = ['V','V0','V1','V2','V3','V4','V5','V6','V7','V8','V9','VR','VS','V+']
    listeNoir = ['C','4+']
    listeplus2 = ['J+','B+','R+','V+']
    listeS = ['JR','BR','RR','VR']
    listeR = ['JS','BS','RS','VS']
    liste0 = ['J0','B0','R0','V0']
    liste1 = ['J1','B1','R1','V1']
    liste2 = ['J2','B2','R2','V2']
    liste3 = ['J3','B3','R3','V3']
    liste4 = ['J4','B4','R4','V4']
    liste5 = ['J5','B5','R5','V5']
    liste6 = ['J6','B6','R6','V6']
    liste7 = ['J7','B7','R7','V7']
    liste8 = ['J8','B8','R8','V8']
    liste9 = ['J9','B9','R9','V9']

    # Pour emplacements des cartes
    nomsEmplacements = ["Centre"]
    # Noms cartes pour affichage
    dicoNomsCartes = {
        'C': 'Changement de couleur',
        '4+': '+4',
        'J': "Changement de couleur jaune",
        'J0': "0 jaune",
        'J1': "1 jaune",
        'J2': "2 jaune",
        'J3': "3 jaune",
        'J4': "4 jaune",
        'J5': "5 jaune",
        'J6': "6 jaune",
        'J7': "7 jaune",
        'J8': "8 jaune",
        'J9': "9 jaune",
        'JR': "Changement de sens jaune",
        'JS': "Passe ton tour jaune",
        'J+': "+2 jaune",
        'B': "Changement de couleur bleu",
        'B0': "0 bleu",
        'B1': "1 bleu",
        'B2': "2 bleu",
        'B3': "3 bleu",
        'B4': "4 bleu",
        'B5': "5 bleu",
        'B6': "6 bleu",
        'B7': "7 bleu",
        'B8': "8 bleu",
        'B9': "9 bleu",
        'BR': "Changement de sens bleu",
        'BS': "Passe ton tour bleu",
        'B+': "+2 bleu",
        'R': "Changement de couleur rouge",
        'R0': "0 rouge",
        'R1': "1 rouge",
        'R2': "2 rouge",
        'R3': "3 rouge",
        'R4': "4 rouge",
        'R5': "5 rouge",
        'R6': "6 rouge",
        'R7': "7 rouge",
        'R8': "8 rouge",
        'R9': "9 rouge",
        'RR': "Changement de sens rouge",
        'RS': "Passe ton tour rouge",
        'R+': "+2 rouge",
        'V': "Changement de couleuV vert",
        'V0': "0 vert",
        'V1': "1 vert",
        'V2': "2 vert",
        'V3': "3 vert",
        'V4': "4 vert",
        'V5': "5 vert",
        'V6': "6 vert",
        'V7': "7 vert",
        'V8': "8 vert",
        'V9': "9 vert",
        'VV': "Changement de sens vert",
        'VS': "Passe ton touV vert",
        'V+': "+2 vert",
    }