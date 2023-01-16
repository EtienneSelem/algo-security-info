
import numpy as np;


def chiffrement_affine(texte, clef_a, clef_b):
    texte_chiffre = ""
    for caractere in texte:
        caractere_chiffre = chr(((ord(caractere) - ord('A')) * clef_a + clef_b) % 26 + ord('A'))
        texte_chiffre += caractere_chiffre
    return texte_chiffre

def dechiffrement_affine(texte_chiffre, clef_a, clef_b):
    texte_dechiffre = ""
    clef_a_inverse = 0
    for i in range(26):
        if (clef_a * i) % 26 == 1:
            clef_a_inverse = i
            break
    for caractere in texte_chiffre:
        caractere_dechiffre = chr(((ord(caractere) - ord('A') - clef_b) * clef_a_inverse) % 26 + ord('A'))
        texte_dechiffre += caractere_dechiffre
    return texte_dechiffre

texte = "HELLO WORLD"
clef_a = 5
clef_b = 8

texte_chiffre = chiffrement_affine(texte, clef_a, clef_b)
print("Texte chiffré :", texte_chiffre)

texte_dechiffre = dechiffrement_affine(texte_chiffre, clef_a, clef_b)
print("Texte déchiffré :", texte_dechiffre)