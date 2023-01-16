
import numpy as np

def chiffrer_playfair(texte, cle):
    #remplacer des espaces par des x 
    texte = texte.replace("", "X")
    #construire la grille de chiffrement
    grille = np.array([[cle[i] for i in range(j, j + 5)] for j in range(0, 25, 5)])

    #initialiser le texte chiffré

    chiffre = ""
    #traiter par paires de lettres
    for i in range(0, len(texte) -1, 2):
        #recuperer les coordonnées des lettres dans la grille
        coord1 = np.where(grille == texte[i])
        coord2 = np.where(grille == texte[i + 1])
        
        #cas où les lettres se trouvent sur la meme ligne
        if coord1[0] == coord2[0]:
            chiffre += grille[coord1[0], (coord1[1] + 1) % 5]
            chiffre += grille[coord2[0], (coord2[1] + 1) % 5]