import pygame as py
board_width = 600
board_height = 900


class Dude(py.sprite.Sprite):

    def __init__(self):
        
        super(Dude, self).__init__()
        self.image = py.image.load('images\dude\dude_up.png')
        self.rect = self.image.get_rect()

    
        self.cost = 2
        self.hp = 100
        self.defense = 10
        self.speed = 1
        self.atk_type = 'melee'
        self.atk_power = 10
        self.atk_speed = 5

    def update(self):
        self.rect.y -= self.speed
        self.rect.x -= self.speed


class Bro(py.sprite.Sprite):

    def __init__(self):
        
        super(Bro, self).__init__()
        self.image = py.image.load('images\\bro\\bro_up.png')
        self.rect = self.image.get_rect()

    
        self.cost = 2
        self.hp = 100
        self.defense = 10
        self.speed = 1
        self.atk_type = 'melee'
        self.atk_power = 10
        self.atk_speed = 5

    def update(self):
        self.rect.y -= self.speed

class Them(py.sprite.Sprite):

    def __init__(self):
        
        super(Them, self).__init__()
        self.image = py.image.load('images\\them\\them_up.png')
        self.rect = self.image.get_rect()

    
        self.cost = 2
        self.hp = 100
        self.defense = 10
        self.speed = 1
        self.atk_type = 'melee'
        self.atk_power = 10
        self.atk_speed = 5

    def update(self):
        self.rect.y -= self.speed

class Us(py.sprite.Sprite):

    def __init__(self):
        
        super(Us, self).__init__()
        self.image = py.image.load('images\\us\\us_up.png')
        self.rect = self.image.get_rect()

    
        self.cost = 2
        self.hp = 100
        self.defense = 10
        self.speed = 1
        self.atk_type = 'melee'
        self.atk_power = 10
        self.atk_speed = 5

    def update(self):
        self.rect.y -= self.speed
