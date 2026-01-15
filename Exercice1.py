class Triangle() :
    pass


class Affichage():
    pass
yes=1
while yes ==1:
    try:
        n = int(input("Saisir un nombre : "))
        yes=0
    except ValueError:
        print("Veuillez saisir un nombre valide")

