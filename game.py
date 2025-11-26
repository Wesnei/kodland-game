import random
import math
import pgzrun
from pygame import Rect

WIDTH = 800
HEIGHT = 600

STATE = "menu"
sound_on = True

# ---------------- BOTÕES ----------------

class Button:
    def __init__(self, text, pos):
        self.text = text
        self.rect = Rect(pos[0], pos[1], 220, 60)

    def draw(self):
        screen.draw.filled_rect(self.rect, (40, 80, 140))
        screen.draw.rect(self.rect, "white")
        screen.draw.text(self.text, center=self.rect.center, fontsize=40, color="white")

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

start_btn = Button("Start Game", (290, 220))
sound_btn = Button("Sound ON", (290, 300))
exit_btn = Button("Exit", (290, 380))

# ---------------- HERÓI ----------------

class Hero:
    def __init__(self):
        self.idle = ["hero_idle1", "hero_idle2"]
        self.walk = ["hero_walk1", "hero_walk2"]

        self.actor = Actor(self.idle[0], pos=(400, 400))

        self.tx, self.ty = self.actor.x, self.actor.y
        self.speed = 3
        self.frame = 0
        self.counter = 0

    def set_target(self, pos):
        self.tx, self.ty = pos

    def update(self):
        dx = self.tx - self.actor.x
        dy = self.ty - self.actor.y

        dist = math.hypot(dx, dy)

        if dist > 3:
            self.actor.x += dx / dist * self.speed
            self.actor.y += dy / dist * self.speed
            anim = self.walk
        else:
            anim = self.idle

        # animação
        self.counter += 1
        if self.counter > 15:
            self.frame = (self.frame + 1) % 2
            self.actor.image = anim[self.frame]
            self.counter = 0

    def draw(self):
        self.actor.draw()

hero = Hero()

# ---------------- INIMIGO ----------------

class Enemy:
    def __init__(self, x1, x2, y):
        self.idle = ["enemy_idle1", "enemy_idle2"]
        self.walk = ["enemy_walk1", "enemy_walk2"]

        self.actor = Actor(self.idle[0], pos=(x1, y))
        self.x1, self.x2 = x1, x2
        self.dir = 1
        self.frame = 0
        self.counter = 0

    def update(self):
        self.actor.x += self.dir * 2

        if self.actor.x < self.x1:
            self.dir = 1
        if self.actor.x > self.x2:
            self.dir = -1

        # animação
        self.counter += 1
        if self.counter > 20:
            self.frame = (self.frame + 1) % 2
            self.actor.image = self.walk[self.frame]
            self.counter = 0

    def draw(self):
        self.actor.draw()

enemy = Enemy(200, 600, 250)

# ---------------- FUNÇÕES AUX ----------------

def toggle_sound():
    global sound_on
    sound_on = not sound_on
    sound_btn.text = "Sound ON" if sound_on else "Sound OFF"

def play_s(name):
    if not sound_on:
        return

    if name == "click":
        sounds.click.play()
    elif name == "hit":
        sounds.hit.play()

def start_game():
    global STATE
    STATE = "game"
    try:
        if sound_on:
            music.play("bg_music.wav")
    except:
        pass

# ---------------- LOOP PRINCIPAL ----------------

def update():
    if STATE != "game":
        return

    hero.update()
    enemy.update()

    # colisão
    if hero.actor.colliderect(enemy.actor):
        play_s("hit")
        hero.actor.pos = (400, 400)

def draw():
    screen.clear()

    if STATE == "menu":
        screen.draw.text("Simple Adventure", center=(400, 120), fontsize=60, color="white")
        start_btn.draw()
        sound_btn.draw()
        exit_btn.draw()

    else:
        hero.draw()
        enemy.draw()
        screen.draw.text("Click to move", (20, 20), fontsize=30, color="white")

def on_mouse_down(pos):
    global STATE

    if STATE == "menu":
        play_s("click")

        if start_btn.clicked(pos):
            start_game()
        elif sound_btn.clicked(pos):
            toggle_sound()
        elif exit_btn.clicked(pos):
            raise SystemExit

    else:
        play_s("click")
        hero.set_target(pos)

pgzrun.go()
