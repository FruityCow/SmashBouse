import pyxel

# Initialisation de Pyxel
pyxel.init(160, 120)

# Couleurs
NOIR = 0
BLANC = 7
key_player_1 = [pyxel.KEY_Z, pyxel.KEY_Q, pyxel.KEY_D, pyxel.KEY_S, pyxel.KEY_SPACE, pyxel.KEY_LCTRL]
key_player_2 = [pyxel.KEY_UP, pyxel.KEY_LEFT, pyxel.KEY_RIGHT, pyxel.KEY_DOWN, pyxel.KEY_RCTRL, pyxel.KEY_DELETE]

class CarreBlanc:
    "classe qui créée un carre blanc"
    def __init__(self, x, y, taille, vitesse, color, keys):
        self.x = x
        self.y = y
        self.taille = taille
        self.vitesse = vitesse
        self.color = color
        self.keys = keys
        self.dy = 0

    def draw(self):
        "dessine un carré à la position (x,y) de côté (taille) et de couleur BLANC"
        pyxel.rect(self.x, self.y, self.taille, self.taille, self.color)

    def update(self):
        "mat à jour la position du carré"
        if pyxel.btn(self.keys[2]):
            self.x += self.vitesse
        if pyxel.btn(self.keys[1]):
            self.x -= self.vitesse
        if pyxel.btn(self.keys[3]):
            self.y += self.vitesse

        # saut si le carré est au sol
        if pyxel.btn(self.keys[0]) and self.y > 106 :
            self.dy = -10

        # accélération verticale (gravité)
        self.y += self.dy
        self.dy = min(self.dy + 1, 5)
        # Limitation de la position pour ne pas sortir du cadre
        self.x = max(0, min(160 - self.taille, self.x))
        self.y = max(0, min(120 - self.taille, self.y))


class Jeu :
    "classe qui lance le jeu"
    def __init__(self):
        "créée une instance de CarreBlanc et lance le jeu"
        self.carre = CarreBlanc(15, 15, 10, 3, 0, key_player_1)
        self.carre2 = CarreBlanc(1, 1, 10, 3, 2, key_player_2)
        pyxel.run(self.draw, self.update)

    def update(self) -> None:
        "met à jour la position du carre"
        self.carre.update()
        self.carre2.update()
    def draw(self):
        "dessine la fenêtre du jeu avec un fond bleu et le carré dedans"
        pyxel.cls(1)
        self.carre.draw()
        self.carre2.draw()

Jeu()