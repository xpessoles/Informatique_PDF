def supprimer_doublons_liste(L,y = []) :
    """
    Fonction permettant de supprimer les doublons d'une liste.
    Entr e :
    * L: list(int) : liste d'entiers.
    Sortie :
    * list(int) : liste d'entiers ne comportant aucun doublons.
    """
    if L == [] :
        return y
    else :
        z = L.pop(0)
        if z not in y :
            y.append(z)
        return fonction(L, y)


def produit_scalaire_v2(vecteur1, vecteur2):
    somme = 0
    for i in range(len(vecteur1)):
        somme += vecteur1[i]*vecteur2[i]
    return somme


def test_produit_scalaire_v2_01():
    assert produit_scalaire_v2([1, 1, 1], [1, 1, 1]) == 3

def test_produit_scalaire_v2_02():
    assert produit_scalaire_v2([1, 2, 3, 4], [0, 1, 0, 0]) == 2