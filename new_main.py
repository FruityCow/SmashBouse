import pyxel
from time import sleep
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

pyxel.init(256, 144, title="SuperSmashBouse")
key_player_1 = [pyxel.KEY_Z, pyxel.KEY_Q, pyxel.KEY_D, pyxel.KEY_S, pyxel.KEY_SPACE, pyxel.KEY_LCTRL]
key_player_2 = [pyxel.KEY_UP, pyxel.KEY_LEFT, pyxel.KEY_RIGHT, pyxel.KEY_DOWN, pyxel.KEY_RCTRL, pyxel.KEY_DELETE]
ressources = pyxel.load("res.pyxres")
TAILLE = 16
keta_knight = Heros("Keta-Knight", 25,10,10,0,0,0,64,100)
purple_cube = Heros("Purple Cube", 7,10,10,0,16,8,64,50)
c_15 = Heros("Citroen C-15D", 2,10,10,0,32,0,72,25)
accurate_fox = Heros("Accurate Fox", 10,0,10,0,48,8,72,60)
choice1_input = int(input("Joueur 1 Séléctionnez votre héro, 1 : KétaKnight, 2 : PurpleCube, 3 : C15D, 4 : Accurate Fox"))
if choice1_input == 1:
    choice1 = keta_knight
elif choice1_input == 2:
    choice1 = purple_cube
elif choice1_input == 3:
    choice1 = c_15
elif choice1_input == 4:
    choice1 = accurate_fox
else:
    choice1 = keta_knight
choice2_input = int(input("Joueur 2 Séléctionnez votre héro, 1 : KétaKnight, 2 : PurpleCube, 3 : C15D, 4 : Accurate Fox"))
if choice2_input == 1:
    choice2 = keta_knight
elif choice2_input == 2:
    choice2 = purple_cube
elif choice2_input == 3:
    choice2 = c_15
elif choice2_input == 4:
    choice2 = accurate_fox
else:
    choice2 = keta_knight


class Jeu:
    def __init__(self):
        self.player1 = Player(choice1, key_player_1, 128, 72, 0)
        self.player2 = Player(choice2, key_player_2, 128, 72, 1)
        pyxel.run(self.update, self.draw)
    def die(self, name_gagnant, teamg):
            print("giga chibre")
            pyxel.cls(0)
            pyxel.text(16, 64, f"Le joueur {teamg + 1} ({name_gagnant}) REMPORTE LA VICTOIRE", 7)
            pyxel.show()
            sleep(10)
            exit()
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
        if self.player1.vies == 0:
            self.die(self.player2.hero.name, self.player2.team)
        if self.player2.vies == 0:
            self.die(self.player1.hero.name, self.player1.team)
    

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
        if self.vies > 0:
            self.vies -= 1
            self.x = 128
            self.y = 0

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

    def draw(self):
        pyxel.blt(self.x, self.y, 0, self.hero.tile_x, self.hero.tile_y, 16, 16, 10)
        for tirs in self.tirs_liste:
            pyxel.blt(tirs[0], tirs[1], 0, self.hero.proj_tile_x, self.hero.proj_tile_y, 8, 8, 10)


keta_knight = Heros("Keta-Knight", 25,10,10,0,0,0,64,100)
purple_cube = Heros("Purple Cube", 7,10,10,0,16,8,64,50)
c_15 = Heros("Citroen C-15D", 2,10,10,0,32,0,72,25)
accurate_fox = Heros("Accurate Fox", 10,0,10,0,48,8,72,60)



Jeu()