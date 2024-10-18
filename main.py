import pygame as py
from pygame.locals import *
import sys
import random

from cards import *

py.init()


clock = py.time.Clock()
fps = 30

board = py.display.set_mode((board_width,board_height))

card_holder = py.image.load('images\card_holder.png')


bg_img = py.image.load('images/map1.png')
bg_img = py.transform.scale(bg_img,(board_width,board_height))

all_sprites_list = py.sprite.Group()

deck = ['dude', 'bro', 'us', 'them']
#random_card = random.randint(0, deck.length)

card1 = ''
card2 = ''
card3 = ''
card4 = ''

def add_sprite(pos, sprite):
    sprite.rect.center = pos
    all_sprites_list.add(sprite)


running = True
while running:

    clock.tick(fps)
    board.blit(bg_img,(0,0))
    board.blit(card_holder, (130, 790))

    # if card1 == '':
    #     card1 = deck[random_card]

    for event in py.event.get():
        if event.type == QUIT:
            runing = False
            sys.exit()

        key=py.key.get_pressed()
        if key[K_1]:
            if event.type == MOUSEBUTTONDOWN:
                x,y = event.pos 
                add_sprite((x,y), Dude())
                print(x,y)
        if key[K_2]:
            if event.type == MOUSEBUTTONDOWN:
                x,y = event.pos 
                add_sprite((x,y), Bro())
        if key[K_3]:
            if event.type == MOUSEBUTTONDOWN:
                x,y = event.pos 
                add_sprite((x,y), Us())
        if key[K_4]:
            if event.type == MOUSEBUTTONDOWN:
                x,y = event.pos 
                add_sprite((x,y), Them())
           


   
    all_sprites_list.update()
    all_sprites_list.draw(board)
    py.display.flip()

py.quit()