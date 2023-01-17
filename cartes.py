import pygame


class Images:
    """Importe les images du jeu."""
    image_zero_bleu = pygame.image.load('./images/25km.png')
    image_un_bleu = pygame.image.load('./images/50km.png')
    image_deux_bleu = pygame.image.load('./images/75km.png')
    image_trois_bleu= pygame.image.load('./images/100km.png')
    image_quatre_bleu = pygame.image.load('./images/200km.png')
    image_cinq_bleu = pygame.image.load('./images/feu_rouge.png')
    image_six_bleu = pygame.image.load('./images/limite_de_vitesse.png')
    image_sept_bleu = pygame.image.load('./images/200km.png')
    image_huit_bleu = pygame.image.load('./images/feu_rouge.png')
    image_neuf_bleu = pygame.image.load('./images/limite_de_vitesse.png')
    image_+2_bleu = pygame.image.load('./images/limite_de_vitesse.png')
    image_inverse_bleu = pygame.image.load('./images/limite_de_vitesse.png')
    image_zero_jaune = pygame.image.load('./images/25km.png')
    image_un_jaune = pygame.image.load('./images/50km.png')
    image_deux_jaune = pygame.image.load('./images/75km.png')
    image_trois_jaune = pygame.image.load('./images/100km.png')
    image_quatre_jaune = pygame.image.load('./images/200km.png')
    image_cinq_jaune = pygame.image.load('./images/feu_rouge.png')
    image_six_jaune = pygame.image.load('./images/limite_de_vitesse.png')
    image_sept_jaune = pygame.image.load('./images/200km.png')
    image_huit_jaune = pygame.image.load('./images/feu_rouge.png')
    image_neuf_jaune = pygame.image.load('./images/limite_de_vitesse.png')
    image_+2_jaune = pygame.image.load('./images/limite_de_vitesse.png')
    image_inverse_jaune = pygame.image.load('./images/limite_de_vitesse.png')
    image_zero_vert = pygame.image.load('./images/25km.png')
    image_un_vert = pygame.image.load('./images/50km.png')
    image_deux_vert = pygame.image.load('./images/75km.png')
    image_trois_vert  = pygame.image.load('./images/100km.png')
    image_quatre_vert  = pygame.image.load('./images/200km.png')
    image_cinq_vert  = pygame.image.load('./images/feu_rouge.png')
    image_six_vert  = pygame.image.load('./images/limite_de_vitesse.png')
    image_sept_vert  = pygame.image.load('./images/200km.png')
    image_huit_vert  = pygame.image.load('./images/feu_rouge.png')
    image_neuf_vert  = pygame.image.load('./images/limite_de_vitesse.png')
    image_+2_vert = pygame.image.load('./images/limite_de_vitesse.png')
    image_inverse_vert = pygame.image.load('./images/limite_de_vitesse.png')
    image_zero_rouge = pygame.image.load('./images/25km.png')
    image_un_rouge  = pygame.image.load('./images/50km.png')
    image_deux_rouge = pygame.image.load('./images/75km.png')
    image_trois_rouge  = pygame.image.load('./images/100km.png')
    image_quatre_rouge  = pygame.image.load('./images/200km.png')
    image_cinq_rouge  = pygame.image.load('./images/feu_rouge.png')
    image_six_rouge  = pygame.image.load('./images/limite_de_vitesse.png')
    image_sept_rouge  = pygame.image.load('./images/200km.png')
    image_huit_rouge  = pygame.image.load('./images/feu_rouge.png')
    image_neuf_rouge  = pygame.image.load('./images/limite_de_vitesse.png')
    image_+2_rouge = pygame.image.load('./images/limite_de_vitesse.png')
    image_changement_couleur= pygame.image.load('./images/limite_de_vitesse.png')
    image_plus_quatre= pygame.image.load('./images/limite_de_vitesse.png')
    image_inverse_rouge = pygame.image.load('./images/limite_de_vitesse.png')
    dos_carte = pygame.image.load('./images/dos_carte.png')
    logo = pygame.image.load('./images/logo.png')
    stat_button = pygame.image.load('./images/stat_button.png')

    dicoCartesImages = {'25': image_25km,
                        '50': image_50km,
                        '75': image_75km,
                        '100': image_100km,
                        '200': image_200km,
                        'feu_rouge': image_feu_rouge,
                        'limite_de_vitesse': image_limite_de_vitesse,
                        'panne_essence': image_panne_essence,
                        'creve': image_creve,
                        'accident': image_accident,
                        'feu_vert': image_feu_vert,
                        'fin_limite_de_vitesse': image_fin_limite_de_vitesse,
                        'essence': image_essence,
                        'roue_de_secours': image_roue_de_secours,
                        'reparations': image_reparations,
                        'vehicule_prioritaire': image_vehicule_prioritaire,
                        'citerne': image_citerne,
                        'increvable': image_increvable,
                        'as_du_volant': image_as_du_volant}