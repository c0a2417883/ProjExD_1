import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600)) 
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #　背景画像を描画し，画像Surfaceを生成
    kk_img = pg.image.load("fig/3.png") #　こうかとん画像を読み込み，画像Surfaceを生成
    kk_img = pg.transform.flip(kk_img, True, False) #　こうかとん画像の左右を反転
    bg_img_flip = pg.transform.flip(bg_img, True, False) #　背景画像を反転
    kk_rct = kk_img.get_rect()
    kk_rct.center = 300,200
    tmr = 0
    move = [0, 0]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        move[0] = -1
        if key_lst[pg.K_UP]:
            move[1] = -1
        elif key_lst[pg.K_DOWN]:
            move[1] = 1
        else:
            move[1] = 0
        if key_lst[pg.K_RIGHT]:
            move[0] = 1
        kk_rct.move_ip(move)
        
        x = tmr
        x = tmr%3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_flip, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(kk_img, kk_rct)
        pg.display.update()
        tmr += 1     
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()