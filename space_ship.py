import pygame
import sys
import random


class Ship_Yellow(pygame.sprite.Sprite):
    def __init__(self, x, y, gm):
        super().__init__()
        img = pygame.image.load("space/pixel_ship_yellow.png").convert_alpha()
        if gm == "pvp":
            self.image = pygame.transform.rotozoom(img, -90, 1.7)
            self.rect = self.image.get_rect(center=(x, y))
            self.gmod = "pvp"
        elif gm == "pvc":
            self.max_health = 3
            self.health = 3
            self.image = pygame.transform.rotozoom(img, 0, 1.2)
            self.rect = self.image.get_rect(center=(x, y))
            self.gmod = "pvc"
        self.shoot_allowed = True

    def kretanje_shipa_pvp(self):
        key_press = pygame.key.get_pressed()

        if key_press[pygame.K_w]:
            self.rect.y -= 6

        if key_press[pygame.K_s]:
            self.rect.y += 6

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= 800:
            self.rect.bottom = 800

    def kretanje_shipa_pvc(self):
        key_press = pygame.key.get_pressed()

        if key_press[pygame.K_a]:
            self.rect.x -= 6

        if key_press[pygame.K_d]:
            self.rect.x += 6

        if self.rect.right >= 800:
            self.rect.right = 800

        if self.rect.left <= 0:
            self.rect.left = 0

    def healthbar(self):
        rect_red = pygame.Rect(self.rect.centerx - 58,
                               760, self.image.get_width(), 20)
        pygame.draw.rect(screen, (255, 0, 0), rect_red)

        rect_green = pygame.Rect(
            self.rect.centerx - 58, 760, self.image.get_width() * (self.health / self.max_health), 20)
        pygame.draw.rect(screen, (0, 255, 0), rect_green)

    def update(self):
        if self.gmod == "pvp":
            self.kretanje_shipa_pvp()
        elif self.gmod == "pvc":
            self.kretanje_shipa_pvc()
            self.healthbar()


class Laser_Yellow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        img = pygame.image.load("space/pixel_laser_yellow.png").convert_alpha()
        if ship_yellow.sprite.gmod == "pvp":
            self.image = pygame.transform.rotozoom(img, -90, 1.1)
            self.rect = self.image.get_rect(center=(x, y))
        elif ship_yellow.sprite.gmod == "pvc":
            self.image = img
            self.rect = self.image.get_rect(center=(x, y))

    def kretanje_lasera_pvp(self):
        self.rect.x += 10
        if self.rect.left > 800:
            self.kill()

    def kretanje_lasera_pvc(self):
        self.rect.y -= 10
        if self.rect.bottom < 0:
            self.kill()

    def update(self):
        if ship_yellow.sprite.gmod == "pvp":
            self.kretanje_lasera_pvp()
        elif ship_yellow.sprite.gmod == "pvc":
            self.kretanje_lasera_pvc()


class Ship_Red(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        img = pygame.image.load("space/pixel_ship_red.png").convert_alpha()
        self.image = pygame.transform.rotozoom(img, 90, 1.7)
        self.rect = self.image.get_rect(center=(x, y))
        self.shoot_allowed = True

    def kretanje_shipa(self):
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_UP]:
            self.rect.y -= 6
        if key_press[pygame.K_DOWN]:
            self.rect.y += 6

    def update(self):
        self.kretanje_shipa()
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 800:
            self.rect.bottom = 800


class Laser_Red(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        img = pygame.image.load("space/pixel_laser_red.png").convert_alpha()
        self.image = pygame.transform.rotozoom(img, 90, 1.1)
        self.rect = self.image.get_rect(center=(700, y))

    def kretanje_lasera(self):
        self.rect.x -= 10
        if self.rect.right < 0:
            self.kill()

    def update(self):
        self.kretanje_lasera()


class Enemy_Blue(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("space/pixel_ship_blue_small.png")
        self.rect = self.image.get_rect(center=(x, y))

    def kretanje(self):
        self.rect.y += 100
        if self.rect.bottom > 100:
            self.rect.bottom = 100

    def update(self):
        self.kretanje()


class Laser_Blue(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("space/pixel_laser_blue.png")
        self.rect = self.image.get_rect(center=(x, y))

    def kretanje(self):
        self.rect.y += 10
        if self.rect.top > 800:
            self.kill()

    def update(self):
        self.kretanje()


class Enemy_Green(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("space/pixel_ship_green_small.png")
        self.rect = self.image.get_rect(center=(x, y))

    def kretanje(self):
        self.rect.y += 100
        if self.rect.bottom > 100:
            self.rect.bottom = 100

    def update(self):
        self.kretanje()


class Laser_Green(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("space/pixel_laser_green.png")
        self.rect = self.image.get_rect(center=(x, y))

    def kretanje(self):
        self.rect.y += 10
        if self.rect.top > 800:
            self.kill()

    def update(self):
        self.kretanje()


class Enemy_Red(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("space/pixel_ship_red_small.png")
        self.rect = self.image.get_rect(center=(x, y))

    def kretanje(self):
        self.rect.y += 100
        if self.rect.bottom > 100:
            self.rect.bottom = 100

    def update(self):
        self.kretanje()


class Laser_Red_2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("space/pixel_laser_red.png")
        self.rect = self.image.get_rect(center=(x, y))

    def kretanje(self):
        self.rect.y += 10
        if self.rect.top > 800:
            self.kill()

    def update(self):
        self.kretanje()


class Big_Boss(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.max_health = 5
        self.health = 5
        self.img = pygame.image.load("space/pixel_ship_red.png")
        self.image = pygame.transform.rotozoom(self.img, 180, 1.2)
        self.rect = self.image.get_rect(center=(x, y))

    def healthbar(self):
        rect_red = pygame.Rect(self.rect.centerx - 58,
                               20, self.image.get_width(), 20)
        pygame.draw.rect(screen, (255, 0, 0), rect_red)

        rect_green = pygame.Rect(
            self.rect.centerx - 58, 20, self.image.get_width() * (self.health / self.max_health), 20)
        pygame.draw.rect(screen, (0, 255, 0), rect_green)

    def kretanje_shipa(self):
        key_press = pygame.key.get_pressed()

        if key_press[pygame.K_a]:
            self.rect.x -= 6

        if key_press[pygame.K_d]:
            self.rect.x += 6

        if self.rect.right >= 800:
            self.rect.right = 800

        if self.rect.left <= 0:
            self.rect.left = 0

    def update(self):
        self.healthbar()
        self.kretanje_shipa()


class Boss_Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("space/pixel_laser_red.png")
        self.rect = self.image.get_rect(center=(x, y))

    def kretanje(self):
        self.rect.y += 10
        if self.rect.top > 800:
            self.kill()

    def update(self):
        self.kretanje()


def laser_collision():
    pygame.sprite.groupcollide(
        laser_yellow, laser_red, True, True, pygame.sprite.collide_mask)


pygame.init()

game_mode_list = ["pvp", "pvc"]

game_mode = None

game_mode_chosen = False

home_screen = True

screen = pygame.display.set_mode((800, 800))

pygame.display.set_caption("Space Ships Battle")

space_ship_icon = pygame.image.load("space/space_ship_image.png")
pygame.display.set_icon(space_ship_icon)

bg_surf = pygame.image.load("space/background-black.png").convert()

clock = pygame.time.Clock()

# Music
laser_shot_music = pygame.mixer.Sound("space/laser_shot.mp3")

game_active = None

score_yellow = 0
score_red = 0

# Fonts
game_font = pygame.font.Font("space/space_font.otf", 60)
game_mode_font = pygame.font.Font("space/space_font.otf", 30)
font = pygame.font.Font("space/space_font.otf", 50)

# Grupe_Yellow
ship_yellow = pygame.sprite.GroupSingle()
laser_yellow = pygame.sprite.Group()

# Grupe_Red
ship_red = pygame.sprite.GroupSingle()
ship_red.add(Ship_Red(720, 400))
laser_red = pygame.sprite.Group()

# Grupe Enemies
enemy_blue = pygame.sprite.GroupSingle()
enemy_green = pygame.sprite.GroupSingle()
enemy_red = pygame.sprite.GroupSingle()

laser_blue = pygame.sprite.Group()
laser_green = pygame.sprite.Group()
laser_red_2 = pygame.sprite.Group()

# Grupa Big_Boss
big_boss = pygame.sprite.GroupSingle()
boss_laser = pygame.sprite.Group()

# Slike
img_yellow = pygame.image.load("space/pixel_ship_yellow.png").convert_alpha()
img_yellow = pygame.transform.rotozoom(img_yellow, -180, 1.7)
img_yellow_rect = img_yellow.get_rect(center=(80, 200))
img_yellow_rect_2 = img_yellow.get_rect(center=(80, 150))

img_red = pygame.image.load("space/pixel_ship_red.png").convert_alpha()
img_red = pygame.transform.rotozoom(img_red, 180, 1.7)
img_red_rect = img_red.get_rect(center=(720, 600))
img_red_rect_2 = img_red.get_rect(center=(720, 630))

# Tekstovi
text_1 = game_font.render("Space Ships Battle.", True, "blue")
text_1_rect = text_1.get_rect(center=(400, 400))

text_2 = game_font.render("Press any key to start.", True, "blue")
text_2_rect = text_2.get_rect(center=(400, 470))

pvp = game_mode_font.render("Player vs Player", True, "red", "yellow")
pvp_rect = pvp.get_rect(center=(200, 500))

pvc = game_mode_font.render("Player vs Computer", True, "red", "yellow")
pvc_rect = pvc.get_rect(center=(600, 500))

odabir_game_mode = font.render("Choose game mode!", True, "blue")

# Timers
enemy_timer = pygame.USEREVENT + 4

laser_timer = pygame.USEREVENT + 5
pygame.time.set_timer(laser_timer, 2000)

big_boss_timer = pygame.USEREVENT + 6
pygame.time.set_timer(big_boss_timer, 1000)

# Brojac
brojac = 3

# Životi
zivot_blue = True
zivot_green = True
zivot_red = True
zivot_yellow = True
zivot_boss = True

FPS = 60

while True:

    if home_screen and game_mode_chosen == False:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if pvp_rect.collidepoint(event.pos):
                    game_mode = game_mode_list[0]
                    home_screen = False
                    game_mode_chosen = True
                    game_active = True
                    ship_yellow.add(Ship_Yellow(80, 400, "pvp"))
                elif pvc_rect.collidepoint(event.pos):
                    game_mode = game_mode_list[1]
                    home_screen = False
                    game_mode_chosen = True
                    game_active = True
                    ship_yellow.add(Ship_Yellow(400, 700, "pvc"))

        screen.blit(bg_surf, (0, 0))

        screen.blit(img_yellow, img_yellow_rect_2)

        screen.blit(img_red, (img_red_rect_2))

        screen.blit(odabir_game_mode,
                    odabir_game_mode.get_rect(center=(400, 350)))

        screen.blit(pvp, pvp_rect)

        screen.blit(pvc, pvc_rect)

    if (game_mode_chosen == True) and (game_mode == game_mode_list[0]):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_active == True:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and ship_yellow.sprite.shoot_allowed:
                    laser_yellow.add(Laser_Yellow(
                        100, ship_yellow.sprite.rect.centery))
                    laser_shot_music.play()
                    ship_yellow.sprite.shoot_allowed = False
                    pygame.time.set_timer(pygame.USEREVENT + 2, 200)

                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ship_red.sprite.shoot_allowed:
                    laser_red.add(Laser_Red(ship_red.sprite.rect.centery))
                    laser_shot_music.play()
                    ship_red.sprite.shoot_allowed = False
                    pygame.time.set_timer(pygame.USEREVENT + 3, 200)

            if event.type == pygame.USEREVENT + 2:
                ship_yellow.sprite.shoot_allowed = True
                pygame.time.set_timer(pygame.USEREVENT + 2, 0)

            if event.type == pygame.USEREVENT + 3:
                ship_red.sprite.shoot_allowed = True
                pygame.time.set_timer(pygame.USEREVENT + 3, 0)

            if game_active == False:
                if event.type == reset_timer:
                    pygame.time.set_timer(reset_timer, 0)
                    game_active = True
                    ship_yellow.empty()
                    ship_yellow.add(Ship_Yellow(80, 400, "pvp"))
                    ship_red.empty()
                    ship_red.add(Ship_Red(720, 400))

            if game_active == None:
                if event.type == pygame.KEYDOWN:
                    score_yellow = 0
                    score_red = 0
                    ship_yellow.empty()
                    ship_yellow.add(Ship_Yellow(80, 400, "pvp"))
                    ship_red.empty()
                    ship_red.add(Ship_Red(720, 400))
                    laser_red.empty()
                    laser_yellow.empty()
                    game_active = True

        if game_active == None:
            if score_red == 5 or score_yellow == 5:
                screen.blit(bg_surf, (0, 0))

                screen.blit(img_yellow, img_yellow_rect)

                screen.blit(img_red, img_red_rect)

                score_surf_yellow = game_font.render(
                    f"{score_yellow}", True, "yellow")
                score_rect_yellow = score_surf_yellow.get_rect(
                    center=(370, 300))

                score_surf_red = game_font.render(
                    f"{score_red}", True, "red")
                score_rect_red = score_surf_red.get_rect(center=(430, 300))

                dvotocka = game_font.render(f":", True, "blue")
                dvotocka_rect = dvotocka.get_rect(center=(400, 300))

                screen.blit(score_surf_yellow, score_rect_yellow)

                screen.blit(dvotocka, dvotocka_rect)

                screen.blit(score_surf_red, score_rect_red)

                screen.blit(text_1, text_1_rect)

                screen.blit(text_2, text_2_rect)

        if game_active == True:
            screen.blit(bg_surf, (0, 0))

            # ship_yellow
            ship_yellow.draw(screen)
            ship_yellow.update()

            # laser_yellow
            laser_yellow.draw(screen)
            laser_yellow.update()

            # ship_red
            ship_red.draw(screen)
            ship_red.update()

            # laser_red
            laser_red.draw(screen)
            laser_red.update()

            # laser_collision
            laser_collision()

            if pygame.sprite.spritecollide(ship_yellow.sprite, laser_red, True, pygame.sprite.collide_mask):
                # Timer
                reset_timer = pygame.USEREVENT + 1
                pygame.time.set_timer(reset_timer, 500)
                game_active = False
                laser_red.empty()
                laser_yellow.empty()
                score_red += 1

            if pygame.sprite.spritecollide(ship_red.sprite, laser_yellow, True, pygame.sprite.collide_mask):
                # Timer
                reset_timer = pygame.USEREVENT + 1
                pygame.time.set_timer(reset_timer, 500)
                game_active = False
                laser_red.empty()
                laser_yellow.empty()
                score_yellow += 1

            if score_yellow == 5 or score_red == 5:
                game_active = None

            score_surf_yellow = game_font.render(
                f"{score_yellow}", True, "yellow")
            score_rect_yellow = score_surf_yellow.get_rect(center=(370, 80))

            score_surf_red = game_font.render(
                f"{score_red}", True, "red")
            score_rect_red = score_surf_red.get_rect(center=(430, 80))

            dvotocka = game_font.render(f":", True, "blue")
            dvotocka_rect = dvotocka.get_rect(center=(400, 80))

            screen.blit(score_surf_yellow, score_rect_yellow)
            screen.blit(dvotocka, dvotocka_rect)
            screen.blit(score_surf_red, score_rect_red)

    elif (game_mode_chosen == True) and (game_mode == game_mode_list[1]):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if game_active:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and ship_yellow.sprite.shoot_allowed:
                    laser_yellow.add(Laser_Yellow(
                        ship_yellow.sprite.rect.centerx, ship_yellow.sprite.rect.centery))
                    laser_shot_music.play()
                    ship_yellow.sprite.shoot_allowed = False
                    pygame.time.set_timer(pygame.USEREVENT + 2, 200)

                if event.type == pygame.USEREVENT + 2:
                    ship_yellow.sprite.shoot_allowed = True
                    pygame.time.set_timer(pygame.USEREVENT + 2, 0)

                if event.type == enemy_timer:
                    x1 = random.randint(50, 200)
                    y1 = random.randint(-200, -100)
                    enemy_blue.add(Enemy_Blue(x1, y1))

                    x2 = random.randint(210, 500)
                    y2 = random.randint(-200, -100)
                    enemy_green.add(Enemy_Green(x2, y2))

                    x3 = random.randint(510, 750)
                    y3 = random.randint(-200, -100)
                    enemy_red.add(Enemy_Red(x3, y3))

                    pygame.time.set_timer(enemy_timer, 0)

                if (event.type == laser_timer) and (len(enemy_blue) > 0):
                    laser_blue.add(Laser_Blue(
                        enemy_blue.sprite.rect.centerx, enemy_blue.sprite.rect.centery))
                    laser_shot_music.play()

                if (event.type == laser_timer) and (len(enemy_green) > 0):
                    laser_green.add(Laser_Green(
                        enemy_green.sprite.rect.centerx, enemy_green.sprite.rect.centery))
                    laser_shot_music.play()

                if (event.type == laser_timer) and (len(enemy_red) > 0):
                    laser_red_2.add(Laser_Red_2(
                        enemy_red.sprite.rect.centerx, enemy_red.sprite.rect.centery))
                    laser_shot_music.play()

                if event.type == big_boss_timer and big_boss:
                    boss_laser.add(Boss_Laser(
                        big_boss.sprite.rect.centerx, big_boss.sprite.rect.centery))
                    laser_shot_music.play()
                    
            if game_active == False:
                if event.type == pygame.KEYDOWN:
                    if zivot_boss == False or zivot_yellow == False:
                        game_active = True
                        brojac = 3
                        ship_yellow.add(Ship_Yellow(400, 700, "pvc"))
                        pygame.time.set_timer(enemy_timer, 17)
                        pygame.time.set_timer(laser_timer, 2000)
                        pygame.time.set_timer(big_boss_timer, 1000)
                        zivot_blue = True
                        zivot_green = True
                        zivot_red = True
                        zivot_yellow = True
                        zivot_boss = True

        screen.blit(bg_surf, (0, 0))

        if game_active:
            if (not enemy_red) and (not enemy_blue) and (not enemy_green) and zivot_blue and zivot_green and zivot_red and brojac > 0:
                pygame.time.set_timer(enemy_timer, 17)

            ship_yellow.draw(screen)
            ship_yellow.update()
            laser_yellow.draw(screen)
            laser_yellow.update()

            enemy_blue.draw(screen)
            enemy_blue.update()
            laser_blue.draw(screen)
            laser_blue.update()

            enemy_green.draw(screen)
            enemy_green.update()
            laser_green.draw(screen)
            laser_green.update()

            enemy_red.draw(screen)
            enemy_red.update()
            laser_red_2.draw(screen)
            laser_red_2.update()

            big_boss.draw(screen)
            big_boss.update()
            boss_laser.draw(screen)
            boss_laser.update()

            if len(big_boss) == 1:
                if pygame.sprite.spritecollide(big_boss.sprite, laser_yellow, True, pygame.sprite.collide_mask):
                    big_boss.sprite.health -= 1
                    if big_boss.sprite.health == 0:
                        game_active = False
                        zivot_boss = False

            if pygame.sprite.spritecollide(ship_yellow.sprite, boss_laser, True, pygame.sprite.collide_mask):
                ship_yellow.sprite.health -= 1
                if ship_yellow.sprite.health == 0:
                    game_active = False
                    zivot_yellow = False

            pygame.sprite.groupcollide(
                laser_yellow, boss_laser, True, True, pygame.sprite.collide_mask)

            if pygame.sprite.spritecollide(ship_yellow.sprite, laser_blue, True, pygame.sprite.collide_mask):
                ship_yellow.sprite.health -= 1
                if ship_yellow.sprite.health == 0:
                    game_active = False
                    zivot_yellow = False

            if pygame.sprite.spritecollide(ship_yellow.sprite, laser_green, True, pygame.sprite.collide_mask):
                ship_yellow.sprite.health -= 1
                if ship_yellow.sprite.health == 0:
                    game_active = False
                    zivot_yellow = False

            if pygame.sprite.spritecollide(ship_yellow.sprite, laser_red_2, True, pygame.sprite.collide_mask):
                ship_yellow.sprite.health -= 1
                if ship_yellow.sprite.health == 0:
                    game_active = False
                    zivot_yellow = False

            if len(enemy_blue) > 0 and len(laser_yellow) > 0:
                if pygame.sprite.spritecollide(enemy_blue.sprite, laser_yellow, 1, pygame.sprite.collide_mask):
                    enemy_blue.empty()
                    laser_blue.empty()
                    zivot_blue = False

            if len(enemy_green) > 0 and len(laser_yellow) > 0:
                if pygame.sprite.spritecollide(enemy_green.sprite, laser_yellow, 1, pygame.sprite.collide_mask):
                    enemy_green.empty()
                    laser_green.empty()
                    zivot_green = False

            if len(enemy_red) > 0 and len(laser_yellow) > 0:
                if pygame.sprite.spritecollide(enemy_red.sprite, laser_yellow, 1, pygame.sprite.collide_mask):
                    enemy_red.empty()
                    laser_red_2.empty()
                    zivot_red = False

            pygame.sprite.groupcollide(
                laser_yellow, laser_red_2, True, True, pygame.sprite.collide_mask)
            pygame.sprite.groupcollide(
                laser_yellow, laser_green, True, True, pygame.sprite.collide_mask)
            pygame.sprite.groupcollide(
                laser_yellow, laser_blue, True, True, pygame.sprite.collide_mask)

            if zivot_red == False and zivot_blue == False and zivot_green == False and brojac > 0:
                brojac -= 1
                zivot_green = True
                zivot_red = True
                zivot_blue = True
                if brojac == 0:
                    zivot_green = False
                    zivot_red = False
                    zivot_blue = False
                    enemy_blue.empty()
                    laser_blue.empty()
                    enemy_green.empty()
                    laser_green.empty()
                    enemy_red.empty()
                    laser_red_2.empty()
                    pygame.time.set_timer(enemy_timer, 0)
                    pygame.time.set_timer(laser_timer, 0)
                    big_boss.add(
                        Big_Boss(ship_yellow.sprite.rect.centerx, 100))

        elif game_active == False:
            big_boss.empty()
            boss_laser.empty()
            ship_yellow.empty()
            laser_yellow.empty()
            enemy_blue.empty()
            laser_blue.empty()
            enemy_green.empty()
            laser_green.empty()
            enemy_red.empty()
            laser_red_2.empty()
            pygame.time.set_timer(big_boss_timer, 0)
            if zivot_boss == False:
                win_text = game_font.render("You Win!", True, "blue")
                win_text_rect = win_text.get_rect(center=(400, 200))
                screen.blit(win_text, win_text_rect)
                screen.blit(text_1, text_1_rect)
                screen.blit(text_2, text_2_rect)
            elif zivot_yellow == False:
                lose_text = game_font.render("You Lose!", True, "blue")
                lose_text_rect = lose_text.get_rect(center=(400, 200))
                screen.blit(lose_text, lose_text_rect)
                screen.blit(text_1, text_1_rect)
                screen.blit(text_2, text_2_rect)

    pygame.display.update()
    clock.tick(FPS)
