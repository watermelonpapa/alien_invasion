import sys
import pygame
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230,230,230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.bg_color)
            pygame.display.flip()#双缓冲技术显示

if __name__ == '__main__':#__name__是内置属性，看模块是否是按主程序运行。
    ai = AlienInvasion()
    ai.run_game()
