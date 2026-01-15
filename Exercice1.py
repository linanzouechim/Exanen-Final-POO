class Triangle() :
    def __init__(self,n):
        self.n = n
    def construire_Triangle(self):
        return ('*')


    pass


class Affichage():
    def __init__(self,Tri ):
        self.Tri = Tri

    def Affichage_Triangle(self):
        print(Tri)




yes=1
while yes ==1:
    try:
        n = int(input("Saisir un nombre : "))
        yes=0
    except ValueError:
        print("Veuillez saisir un nombre valide")

for i in range(1,n+1):
    t = Triangle(i)
    aff = t.construire_Triangle()
    a = Affichage(aff)
    a.Affichage_Triangle()

