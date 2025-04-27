import pygame
from pygame import *
from random import choice


pygame.init()


win_width = 800
win_height = 600
window = display.set_mode((800, 600))
display.set_caption('pin pong')


# white = (255, 255, 255)
# black = (0, 0, 0)
red = (255, 0, 0)    
blue = (0, 0, 255)  


background = transform.scale(image.load('background.jpg'), (800, 600))


class Rocket(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = Surface((10, 100))
        self.image.fill(red)  
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= 10
        if keys[K_DOWN] and self.rect.y < 800 - 100:
            self.rect.y += 10


class Ball(sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = Surface((20, 20))
        self.image.fill(blue) 
        self.rect = self.image.get_rect()
        self.rect.x = 600 // 2
        self.rect.y = 800 // 2
        self.speed_x = choice([-5, 5])
        self.speed_y = choice([-5, 5])

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1


rocket1 = Rocket(30, 800 // 2 - 50)
rocket2 = Rocket(800 - 40, 600 // 2 - 50)
ball = Ball()

font.init()
font2 = font.Font(None,70)


Sprites = sprite.Group()
Sprites.add(rocket1)
Sprites.add(rocket2)
Sprites.add(ball)

lose = font2.render('YOU LOSE!', True,(180,0,0))
win = font2.render('YOU WIN!', True, (255,215, 0))


score = 0

clock = time.Clock()
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    
    Sprites.update()

    
    if sprite.collide_rect(ball, rocket1) or sprite.collide_rect(ball, rocket2):
        ball.speed_x *= -1

    
    if ball.rect.left <= 0 or ball.rect.right >= 800:
        ball.rect.x = 600 // 2
        ball.rect.y = 800 // 2
        ball.speed_x *= choice([-1, 1])
    
    
    window.blit(background, (0, 0)) 
    Sprites.draw(window)

    display.flip()
    clock.tick(60)

    if ball > win_width or ball > win_height:
        score = score+1

        text = font2.render('Счётчик:'+ str(score), 1,(255, 255,255))
        window.blit(text, (10,20))
        text_lose = font2.render('Пропущено:' + str(lost), 1 , (255, 255,255))
        window.blit(text_lose,(10,60))








pygame.quit()