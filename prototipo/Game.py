import pygame
from GameLogic.GUI.GameDisplay import GameDisplay
from Menu.MainMenu import MainMenu

pygame.init()
pygame.display.set_caption("Project Zeus")
pygame.display.set_icon(pygame.transform.scale(pygame.image.load('prototipo/Images/game_icon.png'), (75,75)))

class Game:
    def __init__(self):
        fps = 30
        self.clock = pygame.time.Clock()
        self.clock.tick(fps)
        self.window = GameDisplay(self.clock)
        self.mainMenu = MainMenu(self.window)

    def open_menu(self):
        self.mainMenu.show_main_menu()

game = Game()
game.open_menu()
