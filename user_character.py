from global_variables import *

class Character():
    def __init__(self, username, character):
        self.username = username
        self.lifes = 1
        self.jump_speed = 20
        self.speed = 500
        self.score = 0
        self.rect = None

        self.hasColided = False

        self.jumping_animation_duration = fps/2
        self.jumping_animation_duration_halved = fps/4
        self.jumping_animation_duration_timer = 0

        if(character == "melchor"):
            self.character = "melchor"
            self.character_image = "assets/images/melchor.png"
            self.width, self.height = 100, 100

        elif(character == "gaspar"):
            self.character = "gaspar"
            self.character_image = "assets/images/gaspar.png"
            self.width, self.height = 100, 100

        elif(character == "baltasar"):
            self.character = "baltasar"
            self.character_image = "assets/images/baltasar.png"
            self.width, self.height = 100, 100

        else:
            self.character = "santa"
            self.character_image = "assets/images/santa.png"
            self.width, self.height = 500, 147
        
        self.x = 25
        self.y = 700/2 - self.height
        self.initial_x = self.x
        self.initial_y = self.y
    
    
    def respawnAnimation(self):
        pass


    def blinkAnimation(self):
        pass
