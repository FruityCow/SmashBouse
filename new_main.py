import pyxel

pyxel.init(256, 144, title="SuperSmashBouse")
key_player_1 = [pyxel.KEY_Z, pyxel.KEY_Q, pyxel.KEY_D, pyxel.KEY_S, pyxel.KEY_SPACE, pyxel.KEY_LCTRL]
key_player_2 = [pyxel.KEY_UP, pyxel.KEY_LEFT, pyxel.KEY_RIGHT, pyxel.KEY_DOWN, pyxel.KEY_RCTRL, pyxel.KEY_DELETE]
ressources = pyxel.load("res.pyxres")
TAILLE = 16


class Jeu:
    def __init__(self):
        self.player1 = Player(c_15, key_player_1, 128, 72, 0)
        self.player2 = Player(accurate_fox, key_player_2, 128, 72, 1)
        pyxel.run(self.update, self.draw)
    

    def update(self):
        self.player1.update()
        self.player2.update()
        for tirs in self.player1.tirs_liste:
            print(tirs[0], tirs[1])
            if tirs[0] in range(self.player2.x -4, self.player2.x +4) and tirs[1] in range(self.player2.y -4, self.player2.y +4):
                if tirs[2] == "droite":
                    self.player2.x += int(50 * (self.player2.hero.weight / 100))
                    self.player1.tirs_liste.remove(tirs)
                if tirs[2] == "gauche":
                    self.player2.x -= int(50 * (self.player2.hero.weight / 100))
                    self.player1.tirs_liste.remove(tirs)
        
        for tirs in self.player2.tirs_liste:
            print(tirs[0], tirs[1])
            if tirs[0] in range(self.player1.x -4, self.player1.x +4) and tirs[1] in range(self.player1.y -4, self.player1.y +4):
                if tirs[2] == "droite":
                    self.player1.x += int(50 * (self.player1.hero.weight / 100))
                    self.player2.tirs_liste.remove(tirs)
                if tirs[2] == "gauche":
                    self.player1.x -= int(50 * (self.player1.hero.weight / 100))
                    self.player2.tirs_liste.remove(tirs)

    def draw(self):
        pyxel.cls(6)
        self.player1.draw()
        self.player2.draw()
        pyxel.rect(32, 136, 192, 32, 0)
        pyxel.text(8, 16, f"{self.player1.hero.name} : {self.player1.vies}", 0)
        pyxel.text(176, 16, f"{self.player2.hero.name} : {self.player2.vies}", 0)

class Player:
    def __init__(self, hero, keys, x, y, team):
        self.hero = hero
        self.direction = "droite"
        self.vitesse = self.hero.speed
        self.speed = self.hero.speed
        self.cooldown = self.hero.cooldown
        self.shield_health = self.hero.shield_health
        self.tir_liste = []
        self.keys = keys
        self.x = x
        self.y = y
        self.dy = 0
        self.vies = 3
        self.tirs_liste = []
        self.team = team
        self.counter = 0

    def degat(self):
        """Enleve une vie au personnage"""
        if self.vies == 0:
            self.die()
        elif self.vies > 0:
            self.vies -= 1
            self.x = 128
            self.y = 0
    def die(self):
        """Fait mourir le personnage"""
        "implementer le tp au milieu / reset"
        exit()

    def update(self):
        "met a jour la position du personnage"
        if pyxel.btn(self.keys[2]):
            self.direction = "droite"
            self.hero.tile_x = 0
            self.x += self.vitesse
        if pyxel.btn(self.keys[1]):
            self.direction = "gauche"
            self.hero.tile_x = 16
            self.x -= self.vitesse
        if pyxel.btn(self.keys[3]):
            self.y += self.vitesse
        # saut si le carré est au sol
        if pyxel.btn(self.keys[0]) and self.y > 130 - TAILLE:
            self.dy = -12

        self.counter += 1

        if pyxel.btnr(self.keys[4]) and self.counter > self.cooldown:
            self.tirs_liste.append([self.x, self.y, self.direction, self.team])
            self.counter = 0

        for tirs in self.tirs_liste:
            if tirs[2] == "droite":
                tirs[0] += 5
            if tirs[2] == "gauche":
                tirs[0] -= 5
            if tirs[0] not in range(0, 256):
                self.tirs_liste.remove(tirs)


        # accélération verticale (gravité)
        self.y += self.dy
        self.dy = min(self.dy + 1, 5)
        # Limitation de la position pour ne pas sortir du cadre
        self.x = max(0, min(256 - TAILLE, self.x))
        self.y = max(0, min(144 - TAILLE, self.y))
        if self.x not in range(32, 225) and self.y > 125:
            self.degat()
        if self.x in range(16, 225):
            self.y = max(0, min(120, self.y))
        if self.vies == 0:
            self.die()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.hero.tile_x, self.hero.tile_y, 16, 16, 10)
        for tirs in self.tirs_liste:
            pyxel.blt(tirs[0], tirs[1], 0, self.hero.proj_tile_x, self.hero.proj_tile_y, 8, 8, 10)


class Heros:
    def __init__(self, name, speed, cooldown, shield_health, tile_x, tile_y, proj_tile_x, proj_tile_y, weight):
        self.name = name
        self.speed = speed
        self.cooldown = cooldown
        self.shield_health = shield_health
        self.tile_x = tile_x
        self.tile_y = tile_y
        self.proj_tile_x = proj_tile_x
        self.proj_tile_y = proj_tile_y
        self.weight = weight


keta_knight = Heros("Keta-Knight", 25,10,10,0,0,0,64,100)
purple_cube = Heros("Purple Cube", 7,10,10,0,16,8,64,50)
c_15 = Heros("Citroen C-15D", 2,10,10,0,32,0,72,25)
accurate_fox = Heros("Accurate Fox", 10,0,10,0,48,8,72,60)


Jeu()