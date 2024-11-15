#### Fonction secondaire
"""exercice 05-palindrome """
import string
TABLE1 = str.maketrans ("éèëêàçô", "eeeeaco")
TABLE2 =str.maketrans('','',string.punctuation)
def ispalindrome(p):
    """fonction qui vérifie qu'un mot est bien un palindrome """
    if len(p)<=1 :
        return True
    p = p.lower().translate(TABLE1).translate(TABLE2).replace(" ", "")
    if p[0]==p[-1]:
        return ispalindrome(p[1:-1])
    return False
#### Fonction principale


def main():
    """ execute la fonction ispalindrome"""

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
