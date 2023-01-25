import pygame
from skimage.transform import resize

class Images:
    """Importe les images du jeu."""
    image_zero_bleu = pygame.transform.scale(pygame.image.load('./images/Blue_0.jpg'),(110, 150))
    image_un_bleu = pygame.transform.scale(pygame.image.load('./images/Blue_1.jpg'),(110, 150))
    image_deux_bleu = pygame.transform.scale(pygame.image.load('./images/Blue_2.jpg'),(110, 150))
    image_trois_bleu= pygame.transform.scale(pygame.image.load('./images/Blue_3.jpg'),(110, 150))
    image_quatre_bleu = pygame.transform.scale(pygame.image.load('./images/Blue_4.jpg'),(110, 150))
    image_cinq_bleu = pygame.transform.scale(pygame.image.load('./images/Blue_5.jpg'),(110, 150))
    image_six_bleu = pygame.transform.scale(pygame.image.load('./images/Blue_6.jpg'),(110, 150))
    image_sept_bleu = pygame.transform.scale(pygame.image.load('./images/Blue_7.jpg'),(110, 150))
    image_huit_bleu = pygame.transform.scale(pygame.image.load('./images/Blue_8.jpg'),(110, 150))
    image_neuf_bleu = pygame.transform.scale(pygame.image.load('./images/Blue_9.jpg'),(110, 150))
    image_plus2_bleu = pygame.transform.scale(pygame.image.load('./images/Blue_Draw_2.jpg'),(110, 150))
    image_inverse_bleu = pygame.transform.scale(pygame.image.load('./images/Blue_Reverse.jpg'),(110, 150))
    image_stop_bleu = pygame.transform.scale(pygame.image.load('./images/Blue_Skip.jpg'),(110, 150))
    image_zero_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_0.jpg'),(110, 150))
    image_un_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_1.jpg'),(110, 150))
    image_deux_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_2.jpg'),(110, 150))
    image_trois_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_3.jpg'),(110, 150))
    image_quatre_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_4.jpg'),(110, 150))
    image_cinq_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_5.jpg'),(110, 150))
    image_six_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_6.jpg'),(110, 150))
    image_sept_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_7.jpg'),(110, 150))
    image_huit_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_8.jpg'),(110, 150))
    image_neuf_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_9.jpg'),(110, 150))
    image_plus2_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_Draw_2.jpg'),(110, 150))
    image_inverse_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_Reverse.jpg'),(110, 150))
    image_stop_jaune = pygame.transform.scale(pygame.image.load('./images/Yellow_Skip.jpg'),(110, 150))
    image_zero_vert = pygame.transform.scale(pygame.image.load('./images/Green_0.jpg'),(110, 150))
    image_un_vert = pygame.transform.scale(pygame.image.load('./images/Green_1.jpg'),(110, 150))
    image_deux_vert = pygame.transform.scale(pygame.image.load('./images/Green_2.jpg'),(110, 150))
    image_trois_vert  = pygame.transform.scale(pygame.image.load('./images/Green_3.jpg'),(110, 150))
    image_quatre_vert  = pygame.transform.scale(pygame.image.load('./images/Green_4.jpg'),(110, 150))
    image_cinq_vert  = pygame.transform.scale(pygame.image.load('./images/Green_5.jpg'),(110, 150))
    image_six_vert  = pygame.transform.scale(pygame.image.load('./images/Green_6.jpg'),(110, 150))
    image_sept_vert  = pygame.transform.scale(pygame.image.load('./images/Green_7.jpg'),(110, 150))
    image_huit_vert  = pygame.transform.scale(pygame.image.load('./images/Green_8.jpg'),(110, 150))
    image_neuf_vert  = pygame.transform.scale(pygame.image.load('./images/Green_9.jpg'),(110, 150))
    image_plus2_vert = pygame.transform.scale(pygame.image.load('./images/Green_Draw_2.jpg'),(110, 150))
    image_inverse_vert = pygame.transform.scale(pygame.image.load('./images/Green_Reverse.jpg'),(110, 150))
    image_stop_vert = pygame.transform.scale(pygame.image.load('./images/Green_Skip.jpg'),(110, 150))
    image_zero_rouge = pygame.transform.scale(pygame.image.load('./images/Red_0.jpg'),(110, 150))
    image_un_rouge  = pygame.transform.scale(pygame.image.load('./images/Red_1.jpg'),(110, 150))
    image_deux_rouge = pygame.transform.scale(pygame.image.load('./images/Red_2.jpg'),(110, 150))
    image_trois_rouge  = pygame.transform.scale(pygame.image.load('./images/Red_3.jpg'),(110, 150))
    image_quatre_rouge  = pygame.transform.scale(pygame.image.load('./images/Red_4.jpg'),(110, 150))
    image_cinq_rouge  = pygame.transform.scale(pygame.image.load('./images/Red_5.jpg'),(110, 150))
    image_six_rouge  = pygame.transform.scale(pygame.image.load('./images/Red_6.jpg'),(110, 150))
    image_sept_rouge  = pygame.transform.scale(pygame.image.load('./images/Red_7.jpg'),(110, 150))
    image_huit_rouge  = pygame.transform.scale(pygame.image.load('./images/Red_8.jpg'),(110, 150))
    image_neuf_rouge  = pygame.transform.scale(pygame.image.load('./images/Red_9.jpg'),(110, 150))
    image_plus2_rouge = pygame.transform.scale(pygame.image.load('./images/Red_Draw_2.jpg'),(110, 150))
    image_inverse_rouge = pygame.transform.scale(pygame.image.load('./images/RED_Reverse.jpg'),(110, 150))
    image_stop_rouge = pygame.transform.scale(pygame.image.load('./images/Red_Skip.jpg'),(110, 150))
    image_changement_couleur= pygame.transform.scale(pygame.image.load('./images/Wild.jpg'),(110, 150))
    image_plus_quatre= pygame.transform.scale(pygame.image.load('./images/Wild_Draw_4.jpg'),(110, 150))
    image_back= pygame.transform.scale(pygame.image.load('./images/Back.png'), (110, 150))
    image_bleu = pygame.transform.scale(pygame.image.load('./images/bleu.png'), (110, 150))
    image_jaune = pygame.transform.scale(pygame.image.load('./images/jaune.png'), (110, 150))
    image_rouge = pygame.transform.scale(pygame.image.load('./images/rouge.png'), (110, 150))
    image_vert = pygame.transform.scale(pygame.image.load('./images/vert.png'), (110, 150))


    dicoCartesImages = {'B0': image_zero_bleu,
                        'B1': image_un_bleu,
                        'B2': image_deux_bleu,
                        'B3': image_trois_bleu,
                        'B4': image_quatre_bleu,
                        'B5': image_cinq_bleu,
                        'B6': image_six_bleu,
                        'B7': image_sept_bleu,
                        'B8': image_huit_bleu,
                        'B9': image_neuf_bleu,
                        'BR': image_inverse_bleu,
                        'BS': image_stop_bleu,
                        'B+': image_plus2_bleu,
                        'V0': image_zero_vert,
                        'V1': image_un_vert,
                        'V2': image_deux_vert,
                        'V3': image_trois_vert,
                        'V4': image_quatre_vert,
                        'V5': image_cinq_vert,
                        'V6': image_six_vert,
                        'V7': image_sept_vert,
                        'V8': image_huit_vert,
                        'V9': image_neuf_vert,
                        'VR': image_inverse_vert,
                        'VS': image_stop_vert,
                        'V+': image_plus2_vert,
                        'J0': image_zero_jaune,
                        'J1': image_un_jaune,
                        'J2': image_deux_jaune,
                        'J3': image_trois_jaune,
                        'J4': image_quatre_jaune,
                        'J5': image_cinq_jaune,
                        'J6': image_six_jaune,
                        'J7': image_sept_jaune,
                        'J8': image_huit_jaune,
                        'J9': image_neuf_jaune,
                        'JR': image_inverse_jaune,
                        'JS': image_stop_jaune,
                        'J+': image_plus2_jaune,
                        'R0': image_zero_rouge,
                        'R1': image_un_rouge,
                        'R2': image_deux_rouge,
                        'R3': image_trois_rouge,
                        'R4': image_quatre_rouge,
                        'R5': image_cinq_rouge,
                        'R6': image_six_rouge,
                        'R7': image_sept_rouge,
                        'R8': image_huit_rouge,
                        'R9': image_neuf_rouge,
                        'RR': image_inverse_rouge,
                        'RS': image_stop_rouge,
                        'R+': image_plus2_rouge,
                        'C': image_changement_couleur,
                        '4+': image_plus_quatre,
                        'J': image_jaune,
                        'V': image_vert,
                        'B': image_bleu,
                        'R': image_rouge,
                        'D' : image_back
                        }