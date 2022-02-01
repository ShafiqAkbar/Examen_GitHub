def polynome(x):
    '''
    Fonction polynome qui calcule le polynome.
    La fonction retourne une erreur si on renseigne une chaine de caractere ou un nombre complexe
    ou une valeur negative.
        Entree : Nombre
        Sortie : Nombre
    '''

    petit_nombre = 0.5
    grand_nombre = 9999

    if (type(x) == str):
        print("")
        print("Entrée Str invalide")
        print("Saisir un valeur numérique valide : ")

    elif (type(x) == complex):
        print("")
        print("Entrée Nombre complexe invalide")
        print("Rentrer une valeur numérique valide")

    elif (x < 0):
        print("")
        print("Entrée Négative invalide")
        print("Rentrer une valeur numérique valide")

    elif (x < petit_nombre) or (x > grand_nombre):
        print("")
        print("Valeur trop petite ou trop grande")
        print("Rentrer une valeur numérique valide")

    else:
        res = x ** 3 - 1.5 * x ** 2 - 6 * x + 5
        return res
