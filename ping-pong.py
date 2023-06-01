from pygame import *
window = display.set_mode((700,500))
font.init()
font = font.Font(None, 35)
lose1 = font.render('player 1 lose', True, (150,0,0))
lose2 = font.render('player 2 lose', True, (150,0,0))
clock = time.Clock()
FPS = 60
window_width = 180
window_height = 450
speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__ (self, player_img, player_x, player_y,width, height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_img),(width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed


    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y< 420:
            self.rect.y += self.speed


racket1 = Player('ufo.png', 30,200,50,50,5)
racket2 = Player('ufo.png', 630,200,50,50,5)
ball = GameSprite('asteroid.png', 200,200,50,50,4)

background = transform.scale(image.load('galaxy.jpg'),(700,500))

game = True
finish = False


while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    if finish !=True:
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        racket1.reset()
        racket2.reset()
        racket1.update_l()
        racket2.update_r()
        ball.reset()
        if ball.rect.y > window_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.x <0:
            finish = True
            window.blit(lose1,(200,200))
            game = True

        if ball.rect.x >700:
            finish = True
            window.blit(lose2,(200,200))
            game = True
        

        



        display.update()
        clock.tick(FPS)
