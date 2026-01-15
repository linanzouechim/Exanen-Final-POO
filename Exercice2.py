#EXERCICE 2
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QFrame, QLabel, QLineEdit, QPushButton,QMessageBox

#Fonction de sauvegarde dans le fichier resultats.txt
def sauvegarder():
    fi= open("resultats.txt","w")
    fi.write(str(textE2.text()))
    fi.close()


#Fonction de chargement depuis le fichier resultats.txt
def charger():
    fi = open("resultats.txt", "r")
    textE2.setText(fi.read())
    fi.close()


def popup_warning(titre, message):
    QMessageBox.warning(f, titre, message)

# Fonction qui calcule le double
def double():

        try:
            n = int(textE1.text())
            d = n * 2
            textE2.setText(str(d))

        except ValueError:
            print("La valeur n'est pas valide")

            popup_warning("Attention", "Veuillez entrer un entier!")


# Création de l'application
app = QApplication([])

# Création de la fenêtre
f = QWidget()
grid = QGridLayout(f)
f.setLayout(grid)

l1 = QLabel(f)
l1.setText("Entrer la valeur de N")
grid.addWidget(l1,0,0)

l2 = QLabel(f)
l2.setText("Voici le double")
grid.addWidget(l2,1,0)

textE1 = QLineEdit(f)
grid.addWidget(textE1,0,1)

textE2 = QLineEdit(f)
grid.addWidget(textE2,1,1)

#Bouton valider
boutonV = QPushButton(f)
grid.addWidget(boutonV,2,1)
boutonV.setText("Valider l'opération")
boutonV.clicked.connect(double)

#Bouton charger
boutonV = QPushButton(f)
grid.addWidget(boutonV,2,2)
boutonV.setText("Charger")
boutonV.clicked.connect(charger)

#Bouton sauvegarder
boutonV = QPushButton(f)
grid.addWidget(boutonV,2,0)
boutonV.setText("Sauvegarder")
boutonV.clicked.connect(sauvegarder)

f.show()
app.exec()

