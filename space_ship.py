import pygame
import sys


class Ship_Yellow(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        img = pygame.image.load("space/pixel_ship_yellow.png").convert_alpha()
        self.image = pygame.transform.rotozoom(img, -90, 1.7)
        self.rect = self.image.get_rect(center=(x, y))
        self.shoot_allowed = True

    def kretanje_shipa(self):
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_w]:
            self.rect.y -= 6
        if key_press[pygame.K_s]:
            self.rect.y += 6

    def update(self):
        self.kretanje_shipa()
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 800:
            self.rect.bottom = 800


class Laser_Yellow(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        img = pygame.image.load("space/pixel_laser_yellow.png").convert_alpha()
        self.image = pygame.transform.rotozoom(img, -90, 1.1)
        self.rect = self.image.get_rect(center=(100, y))

    def kretanje_lasera(self):
        self.rect.x += 10
        if self.rect.left > 800:
            self.kill()

    def update(self):
        self.kretanje_lasera()


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


def laser_collision():
    pygame.sprite.groupcollide(
        laser_yellow, laser_red, True, True, pygame.sprite.collide_mask)


pygame.init()

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
game_font = pygame.font.Font("space/space_font.otf", 80)
text_font = game_font = pygame.font.Font("space/space_font.otf", 60)

# Grupe_Yellow
ship_yellow = pygame.sprite.GroupSingle()
ship_yellow.add(Ship_Yellow(80, 400))

laser_yellow = pygame.sprite.Group()

# Grupe_Red
ship_red = pygame.sprite.GroupSingle()
ship_red.add(Ship_Red(720, 400))

laser_red = pygame.sprite.Group()

# Slike
img_yellow = pygame.image.load("space/pixel_ship_yellow.png").convert_alpha()
img_yellow = pygame.transform.rotozoom(img_yellow, -180, 1.7)
img_yellow_rect = img_yellow.get_rect(center=(80, 200))

img_red = pygame.image.load("space/pixel_ship_red.png").convert_alpha()
img_red = pygame.transform.rotozoom(img_red, 180, 1.7)
img_red_rect = img_red.get_rect(center=(720, 600))

# Tekstovi
text_1 = text_font.render("Space Ships Battle.", True, "blue")
text_1_rect = text_1.get_rect(center=(400, 400))

text_2 = text_font.render("Press any key to start.", True, "blue")
text_2_rect = text_2.get_rect(center=(400, 470))


FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active == True:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and ship_yellow.sprite.shoot_allowed:
                laser_yellow.add(Laser_Yellow(ship_yellow.sprite.rect.centery))
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
                ship_yellow.add(Ship_Yellow(80, 400))
                ship_red.empty()
                ship_red.add(Ship_Red(720, 400))

        if game_active == None:
            if event.type == pygame.KEYDOWN:
                score_yellow = 0
                score_red = 0
                ship_yellow.empty()
                ship_yellow.add(Ship_Yellow(80, 400))
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
            score_rect_yellow = score_surf_yellow.get_rect(center=(370, 300))

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

        else:
            screen.blit(bg_surf, (0, 0))

            screen.blit(img_yellow, img_yellow_rect)

            screen.blit(img_red, img_red_rect)

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

    pygame.display.update()
    clock.tick(FPS)