class Character():
    def __init__(self, username, character):
        self.username = username

        if(character == "melchor"):
            self.character = "melchor"
            self.character_image = "assets/images/melchor.png"
            self.width, self.height = 140, 140

        elif(character == "gaspar"):
            self.character = "gaspar"
            self.character_image = "assets/images/gaspar.png"
            self.width, self.height = 122, 147

        elif(character == "baltasar"):
            self.character = "baltasar"
            self.character_image = "assets/images/baltasar.png"
            self.width, self.height = 122, 147

        else:
            self.character = "santa"
            self.character_image = "assets/images/santa.png"
            self.width, self.height = 500, 147
        
        self.x = 25
        self.y = 700/2 - self.height
            
