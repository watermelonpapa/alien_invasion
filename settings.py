class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #1 right -1 left
        self.fleet_direction = 1
        #ship settings
        self.ship_speed = 2
        self.ship_limit = 3
