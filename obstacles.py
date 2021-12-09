from global_variables import *
import pygame

class Helicopter():
    def __init__(self, height):
        self.__collision_sound = pygame.mixer.Sound("assets/music/crash_sound_effect.mp3")
        self.x = screen_width
        self.y = 0
        self.width = 100

        #set of heights = 100, 150, 200, 350
        if height == "0":
            self.height = 100
            self.image =  "assets/images/helicopter_one.png"
        elif height == "1":
            self.height = 150
            self.image =  "assets/images/helicopter_two.png"
        elif height == "2":
            self.height = 200
            self.image =  "assets/images/helicopter_three.png"
        elif height == "3":
            self.height = 350
            self.image =  "assets/images/helicopter_four.png"
        
        self.helicopter_obstacle = pygame.image.load(self.image)

    def play_sound(self):
        pygame.mixer.Sound.play(self.__collision_sound)


class Building():
    def __init__(self, height):
        self.__collision_sound = pygame.mixer.Sound("assets/music/crash_sound_effect.mp3")
        self.width = 100

        #set of heights = 100, 150, 200, 350
        if height == "0":
            self.height = 100
            self.image =  "assets/images/building_one.png"
        elif height == "1":
            self.height = 150
            self.image =  "assets/images/building_two.png"
        elif height == "2":
            self.height = 200
            self.image =  "assets/images/building_three.png"
        elif height == "3":
            self.height = 350
            self.image =  "assets/images/building_four.png"

        self.x = screen_width
        self.y = screen_height - self.height

        self.building_obstacle = pygame.image.load(self.image)

    def play_sound(self):
        pygame.mixer.Sound.play(self.__collision_sound)


class Present():
    def __init__(self):
        self.__present_sound = pygame.mixer.Sound("assets/music/get_present_sound_effect.mp3")
        self.image =  "assets/images/present.png"
        self.width = 100
        self.height = 100
        self.x = screen_width
        self.y = screen_height - self.height/2
    
    def play_sound(self):
        pygame.mixer.Sound.play(self.__present_sound)