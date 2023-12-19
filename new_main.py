import pyxel

pyxel.init(256, 144, title="SuperSmashBouse")
key_player_1 = [pyxel.KEY_Z, pyxel.KEY_Q, pyxel.KEY_D, pyxel.KEY_S, pyxel.KEY_SPACE, pyxel.KEY_LCTRL]
key_player_2 = [pyxel.KEY_UP, pyxel.KEY_LEFT, pyxel.KEY_RIGHT, pyxel.KEY_DOWN, pyxel.KEY_RCTRL, pyxel.KEY_DELETE]
ressources = pyxel.load("res.pyxres")
TAILLE = 16
        

class Jeu:
    def __init__(self):
        self.player1 = Player(c_15, key_player_1, 60, 60)
        self.player2 = Player(keta_knight, key_player_2, 60, 60)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player1.update()
        self.player2.update()
        print(self.player1.y, self.player2.y)
    def draw(self):
        pyxel.cls(6)
        self.player1.draw()
        self.player2.draw()

class Player:
    def __init__(self, hero, keys, x, y):
        self.hero = hero
        self.direction = None
        self.vitesse = self.hero.speed
        self.health = self.hero.health
        self.speed = self.hero.speed
        self.cooldown = self.hero.cooldown
        self.shield_health = self.hero.shield_health
        self.tir_liste = []
        self.keys = keys
        self.x = x
        self.y = y
        self.dy = 0

    def degat(self):
        """Afflige des dégats au personnage"""
        if self.shield_health == 0:
            self.health -= 1
        elif self.health > 0:
            self.health -= 1
        else:
            self.die()
    def die(self):
        """Fait mourir le personnage"""
    def update(self):
        "met a jour la position du personnage"
        if pyxel.btn(self.keys[2]):
            self.pointer = "right"
            self.x += self.vitesse
        if pyxel.btn(self.keys[1]):
            self.pointer = "left"
            self.x -= self.vitesse
        if pyxel.btn(self.keys[3]):
            self.y += self.vitesse
        # saut si le carré est au sol
        if pyxel.btn(self.keys[0]) and self.y > 124:
            self.dy = -12

        # accélération verticale (gravité)
        self.y += self.dy
        self.dy = min(self.dy + 1, 5)
        # Limitation de la position pour ne pas sortir du cadre
        self.x = max(0, min(256 - TAILLE, self.x))
        self.y = max(0, min(144 - TAILLE, self.y))

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.hero.tile_x, self.hero.tile_y, 16, 16, 10)

class Heros:
    def __init__(self, health, speed, cooldown, shield_health, tile_x, tile_y):
        self.health = health
        self.speed = speed
        self.cooldown = cooldown
        self.shield_health = shield_health
        self.tile_x = tile_x
        self.tile_y = tile_y


keta_knight = Heros(10,25,10,10,0,0)
purple_cube = Heros(10,7,10,10,0,16)
c_15 = Heros(10,2,10,10,0,32)
accurate_fox = Heros(10,10,10,10,0,48)

Jeu()
