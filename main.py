import pygame
import time
import random

pygame.init()

# game variables
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
BLACK = (0,0,0)
GRAY = (50,50,50)
WHITE = (255,255,255)
font = pygame.font.Font("font/alagard.ttf", 32)
font_small = pygame.font.Font("font/Nintendo-DS-BIOS.ttf", 16)
font_large = pygame.font.Font("font/alagard.ttf", 64)
current_level = 0
current_kills = 0
current_remaining = 0
between_rounds = True
game_over = False
typed = ""

# window setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('ZombKeys')
#programIcon = pygame.image.load('img/icon.png').convert_alpha()
#pygame.display.set_icon(programIcon)
clock = pygame.time.Clock()
FPS = 60
run = True

# images
img_0 = pygame.image.load('img/0.png').convert_alpha()
img_1 = pygame.image.load('img/1.png').convert_alpha()
img_2 = pygame.image.load('img/2.png').convert_alpha()
img_3 = pygame.image.load('img/3.png').convert_alpha()
img_4 = pygame.image.load('img/4.png').convert_alpha()
img_5 = pygame.image.load('img/5.png').convert_alpha()
img_6 = pygame.image.load('img/6.png').convert_alpha()
img_7 = pygame.image.load('img/7.png').convert_alpha()
img_8 = pygame.image.load('img/8.png').convert_alpha()
img_9 = pygame.image.load('img/9.png').convert_alpha()
img_a = pygame.image.load('img/a.png').convert_alpha()
img_b = pygame.image.load('img/b.png').convert_alpha()
img_x = pygame.image.load('img/x.png').convert_alpha()
img_e = pygame.image.load('img/explosion/0.png').convert_alpha()

#classes
class Person(pygame.sprite.Sprite):
    def __init__(self,zombkey_word,x,y):
        pygame.sprite.Sprite.__init__(self)
        random_image = random.randint(0,9)
        if random_image == 0:
            self.image = img_0
        elif random_image == 1:
            self.image = img_1
        elif random_image == 2:
            self.image = img_2
        elif random_image == 3:
            self.image = img_3
        elif random_image == 4:
            self.image = img_4
        elif random_image == 5:
            self.image = img_5
        elif random_image == 6:
            self.image = img_6
        elif random_image == 7:
            self.image = img_7
        elif random_image == 8:
            self.image = img_8
        elif random_image == 9:
            self.image = img_9
        self.zombkey_word = zombkey_word
        # print(self.zombkey_word)
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        z_width = self.rect.width
        label = Label(zombkey_word,z_width,x,y)
        label_group.add(label)

    def move_zombkey(self):
        global current_level
        if current_level == 1 or current_level == 2:
            self.x -= 0.3
        if current_level == 3 or current_level == 4:
            self.x -= 0.4
        if current_level == 5 or current_level == 6:
            self.x -= 0.5
        if current_level == 7 or current_level == 8:
            self.x -= 0.6
        if current_level == 9 or current_level == 10:
            self.x -= 0.7
        if current_level == 11 or current_level == 12:
            self.x -= 0.8
        if current_level == 13 or current_level == 14:
            self.x -= 0.9
        if current_level > 14:
            self.x -= 1
        if self.x < 100:
            dead()

    def draw(self):
        screen.blit(self.image,(self.x,self.y))

#this is a copy of person class for label
class Label(pygame.sprite.Sprite):
    def __init__(self,zombkey_word,z_width,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.zombkey_word = zombkey_word
        self.img = font_small.render(zombkey_word,True,BLACK,WHITE)
        self.rect = self.img.get_rect()
        label_width = self.rect.width
        if label_width >= z_width:
            difference = label_width - z_width
            self.x = x - difference/2
        else:
            difference = z_width - label_width
            self.x = x + difference/2
        self.y = y-12

    def move_label(self):
        global current_level
        if current_level == 1 or current_level == 2:
            self.x -= 0.3
        if current_level == 3 or current_level == 4:
            self.x -= 0.4
        if current_level == 5 or current_level == 6:
            self.x -= 0.5
        if current_level == 7 or current_level == 8:
            self.x -= 0.6
        if current_level == 9 or current_level == 10:
            self.x -= 0.7
        if current_level == 11 or current_level == 12:
            self.x -= 0.8
        if current_level == 13 or current_level == 14:
            self.x -= 0.9
        if current_level > 14:
            self.x -= 1

    def draw(self):
        screen.blit(self.img,(self.x,self.y))

class Explosion(pygame.sprite.Sprite):
    def __init__(self,explosion_x,explosion_y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1,6):
            img = pygame.image.load(f'img/explosion/{num}.png').convert_alpha()
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.x = explosion_x
        self.y = explosion_y
        self.rect = self.image.get_rect()
        explosion_sprite = (self.image,(self.x,self.y))
        self.counter = 0

    def update(self):
        EXPLOSION_SPEED = 4
        self.counter += 1
        if self.counter >= EXPLOSION_SPEED:
            self.counter = 0
            self.frame_index += 1
            # if the animation is complete then delete the explosion
            if self.frame_index >= len(self.images):
                self.kill()
            else:
                self.image = self.images[self.frame_index]

    def draw(self):
        for explosion in explosion_group:
            screen.blit(explosion.image,(explosion.x,explosion.y))

#functions
def draw_bg():
    screen.fill(BLACK)
    screen.blit(img_b,((0,50)))
    screen.blit(img_x,((50,50)))
    screen.blit(img_a,((5,(SCREEN_HEIGHT-50)/2)))

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

def type_updater(letter):
    global typed
    if len(typed) < 12:
        typed = typed + letter
    else:
        typed = typed[1:]
        typed = typed + letter

def shoot():
    global typed, current_kills, current_remaining, between_rounds
    for zombkey in zombkey_group:
        if typed == zombkey.zombkey_word:
            zombkey.kill()
            current_kills += 1
            current_remaining -= 1
            explosion_sprite = Explosion(zombkey.x,zombkey.y)
            explosion_group.add(explosion_sprite)
    for label in label_group:
        if typed == label.zombkey_word:
            label.kill()
    typed = ""
    if current_remaining == 0:
        between_rounds = True

def get_zombkeys():
    number_of_zombkeys = 4 + current_level
    global current_remaining
    current_remaining = number_of_zombkeys
    if current_level == 1 or current_level == 2 or current_level == 3:
        my_file = open("texts/4.txt", "r")
    if current_level == 4 or current_level == 5 or current_level == 6:
        my_file = open("texts/5.txt", "r")
    if current_level == 7 or current_level == 8 or current_level == 9:
        my_file = open("texts/6.txt", "r")
    if current_level == 10 or current_level == 11 or current_level == 12:
        my_file = open("texts/7.txt", "r")
    if current_level == 13 or current_level == 14 or current_level == 15:
        my_file = open("texts/8.txt", "r")
    if current_level == 16 or current_level == 17 or current_level == 18:
        my_file = open("texts/9.txt", "r")
    if current_level == 19 or current_level == 20 or current_level == 21:
        my_file = open("texts/10.txt", "r")
    if current_level == 22 or current_level == 23 or current_level == 24:
        my_file = open("texts/11.txt", "r")
    if current_level > 24:
        my_file = open("texts/12.txt", "r")
    word_list = my_file.read()
    word_list = word_list.split("\n")
    x = 0
    while x < number_of_zombkeys:
        word_to_get = random.randint(0,len(word_list)-1)
        zombkey_word = word_list.pop(word_to_get)
        zombkey = Person(zombkey_word,random.randint(1000,1300),random.randint(62,542))
        zombkey_group.add(zombkey)
        x += 1
    my_file.close()

def dead():
    global between_rounds, game_over
    zombkey_group.empty()
    label_group.empty()
    between_rounds = True
    game_over = True

# sprite groups
zombkey_group = pygame.sprite.Group()
label_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

# game loop
while run:

    # calls
    draw_bg()
    draw_text("Level: " + str(current_level),font,WHITE,12,12)
    draw_text("Kills: " + str(current_kills),font,WHITE,182,12)
    draw_text("Remaining: " + str(current_remaining),font,WHITE,362,12)
    draw_text("Shot: " + str(typed),font,WHITE,612,12)

    if between_rounds == True:
        draw_text("Press [SPACE] to begin",font,BLACK,340,300)
    if game_over == True:
        draw_text("GAME OVER!",font_large,BLACK,325,200)

    for zombkey in zombkey_group:
        zombkey.update()
        zombkey.draw()
        zombkey.move_zombkey()

    for label in label_group:
        label.update()
        label.draw()
        label.move_label()

    for explosion in explosion_group:
        explosion.update()
        explosion.draw()

    # event checkers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if between_rounds == False:
                if event.key == pygame.K_a:
                    type_updater("a")
                if event.key == pygame.K_b:
                    type_updater("b")
                if event.key == pygame.K_c:
                    type_updater("c")
                if event.key == pygame.K_d:
                    type_updater("d")
                if event.key == pygame.K_e:
                    type_updater("e")
                if event.key == pygame.K_f:
                    type_updater("f")
                if event.key == pygame.K_g:
                    type_updater("g")
                if event.key == pygame.K_h:
                    type_updater("h")
                if event.key == pygame.K_i:
                    type_updater("i")
                if event.key == pygame.K_j:
                    type_updater("j")
                if event.key == pygame.K_k:
                    type_updater("k")
                if event.key == pygame.K_l:
                    type_updater("l")
                if event.key == pygame.K_m:
                    type_updater("m")
                if event.key == pygame.K_n:
                    type_updater("n")
                if event.key == pygame.K_o:
                    type_updater("o")
                if event.key == pygame.K_p:
                    type_updater("p")
                if event.key == pygame.K_q:
                    type_updater("q")
                if event.key == pygame.K_r:
                    type_updater("r")
                if event.key == pygame.K_s:
                    type_updater("s")
                if event.key == pygame.K_t:
                    type_updater("t")
                if event.key == pygame.K_u:
                    type_updater("u")
                if event.key == pygame.K_v:
                    type_updater("v")
                if event.key == pygame.K_w:
                    type_updater("w")
                if event.key == pygame.K_x:
                    type_updater("x")
                if event.key == pygame.K_y:
                    type_updater("y")
                if event.key == pygame.K_z:
                    type_updater("z")

            if event.key == pygame.K_ESCAPE:
                run = False
            if event.key == pygame.K_SPACE:
                if between_rounds == False:
                    shoot()
                else:
                    if game_over == True:
                        current_level = 0
                        current_kills = 0
                        typed = ""
                        game_over = False
                    current_level += 1
                    between_rounds = False
                    get_zombkeys()
            if event.key == pygame.K_RETURN:
                if between_rounds == False:
                    shoot()
            if event.key == pygame.K_BACKSPACE:
                if between_rounds == False:
                    typed = typed[:-1]

    pygame.display.update()
    clock.tick(FPS)