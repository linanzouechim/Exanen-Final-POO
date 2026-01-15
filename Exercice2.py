#EXERCICE 2
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QFrame, QLabel, QLineEdit, QPushButton

# Fonction qui calcule le double
def double():
    pass

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

boutonV = QPushButton(f)
grid.addWidget(boutonV,2,1)
boutonV.setText("Valider l'opération")
boutonV.clicked.connect(double)


f.show()
app.exec()

