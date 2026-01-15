#classe Triangle
class Triangle() :
    def __init__(self,i,n):
        self.i = i
        self.n = n
    def construire_Triangle(self):
        total_Espace =" "
        etoiles = ""
        total_Espace = ""
        for y in range(1, n-i+1):
            total_Espace += " "
        for x in range(0, i):
            etoiles += "*"
        ligneI = total_Espace + etoiles + "  " + etoiles
        return (ligneI)


#Classe Affichage
class Affichage():
    def __init__(self,aff):
        self.aff = aff

    def Affichage_Triangle(self):
        print(aff)



yes=1
while yes ==1:
    try:
        n = int(input("Saisir un nombre : "))
        yes=0
    except ValueError:
        print("Veuillez saisir un nombre valide")

for i in range(1,n+1):
    t = Triangle(i,n)
    aff = t.construire_Triangle()
    a = Affichage(aff)
    a.Affichage_Triangle()

