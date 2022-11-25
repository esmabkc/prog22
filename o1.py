import pygame as pg
import sys
pg.init()
en , boy = 800 , 600
siyah = 0 , 0 , 255 # RGB 0- 255
beyaz = 255 , 0 , 255
ekran = pg.display.set_mode ( (en,boy))
x , y = en//2,boy//2
y_cap=30
x_speed=y_speed=1
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT :
            sys.exit();
    ekran.fill(siyah)
    pg.draw.circle(ekran,beyaz,( x , y ),y_cap)
    x += x_speed
    y += y_speed
    if x >= en - y_cap :
        x_speed *= -1
    if x<= 0 + y_cap :
        x_speed *= -1
    if y >= boy - y_cap :
        y_speed *= -1
    if y<= 0 + y_cap :
        y_speed *= -1

    pg.display.flip()