import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = self.settings.bg_color
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()#bullets group

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bulltes()
            self._update_screen()

    def _update_bulltes(self):
        self.bullets.update()
        for bullet in self.bullets.copy():# 遍历的时候不能删除，因此遍历副本
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

            
    def _check_events(self):#辅助方法，加下划线
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self,event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
            elif event.key == pygame.K_q:
                sys.exit()
            elif event.key == pygame.K_SPACE:
                self._fire_bullets()
    
    def _check_keyup_events(self,event):
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False  
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False  
    
    def _fire_bullets(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_screen(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()#双缓冲技术显示
        

if __name__ == '__main__':#__name__是内置属性，看模块是否是按主程序运行。
    ai = AlienInvasion()
    ai.run_game()
