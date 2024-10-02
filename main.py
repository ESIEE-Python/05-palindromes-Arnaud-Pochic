#### Fonction secondaire
"""
Auteur : Arnaud POCHIC
"""

def ispalindrome(p):
    """
    Retourne True si la chaîne de caractères p est un palindrome,
    et retourne Faux dans le cas contraire

    Args:
        p: chaîne de caractères

    Returns:
        True or False
    """
    p=p.lower()
    dic =  str.maketrans("âäàéêëèôöçûüùîïÿ", "aaaeeeeoocuuuiiy", " '&~#{(-|_\\^@)°])}=+-$£!:;?.,")
    p = p.translate(dic)
    if p != p[::-1]:
        return False

    return True

#### Fonction principale


def main():
    """
    programme principal qui appelle et teste la fonction ispalindrome()
    """
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
