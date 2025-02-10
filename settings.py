class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #bullet settings
        self.bullet_width = 300
        self.bullet_height = 5
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        #alien settings
        self.fleet_drop_speed = 10
        #ship settings
        self.ship_limit = 3
        #increase difficult
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 2
        self.alien_speed = 1.0
        self.bullet_speed = 2.0
        #1 right -1 left
        self.fleet_direction = 1
        #kill one alien get score 
        self.alien_point = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_point = int(self.alien_point*self.score_scale)
