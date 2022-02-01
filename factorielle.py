def factorielle(x):
    '''
    Fonction factorielle qui calcule le factoriel d'un nombre

        Entree : Nombre
        Sortie : liste de nombre
    '''
    fact = 1
    for num in range(2, x + 1):
        fact *= num
    return fact