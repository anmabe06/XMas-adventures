import pygame

class Helicopter():
    def __init__(self, height):
        self.__collision_sound = pygame.mixer.Sound("assets/music/crash_sound_effect.mp3")
        self.x = 1100
        self.y = 0
        self.width = 100

        #set of heights = 100, 150, 200, 350
        if height == "one":
            self.height = 100
            self.image =  "assets/images/helicopter_one.png"
        elif height == "one":
            self.height = 150
            self.image =  "assets/images/helicopter_two.png"
        elif height == "one":
            self.height = 200
            self.image =  "assets/images/helicopter_three.png"
        elif height == "one":
            self.height = 350
            self.image =  "assets/images/helicopter_four.png"

    def play_sound(self):
        pygame.mixer.Sound.play(self.__collision_sound)


class Building():
    def __init__(self, height):
        self.__collision_sound = pygame.mixer.Sound("assets/music/crash_sound_effect.mp3")
        self.width = 100

        #set of heights = 100, 150, 200, 350
        if height == "one":
            self.height = 100
            self.image =  "assets/images/building_one.png"
        elif height == "one":
            self.height = 150
            self.image =  "assets/images/building_two.png"
        elif height == "one":
            self.height = 200
            self.image =  "assets/images/building_three.png"
        elif height == "one":
            self.height = 350
            self.image =  "assets/images/building_four.png"

        self.x = 1100
        self.y = 700 - self.height

    def play_sound(self):
        pygame.mixer.Sound.play(self.__collision_sound)


###################################################


class Present():
    def __init__(self):
        self.__coin_sound = pygame.mixer.Sound("assets/music/get_coin_sound_effect.mp3")
        self.image =  "assets/images/present.png"
        self.width = 100
        self.height = 100
        self.x = 1100
        self.y = 700 - self.height/2
    
    def play_sound(self):
        pygame.mixer.Sound.play(self.__coin_sound)