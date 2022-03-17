from GameLogic.Characters.Character import Character
from GameLogic.Characters.Skill import Skill
from GameLogic.Characters.Weapon import Weapon

class Boss(Character):
    def __init__(self, name: str, sprites: list, health: int, max_health: int, 
                x_position: int, y_position: int, hitbox_x: int, 
                hitbox_y: int, speed: int, jump_height: int, 
                skill: Skill, weak_point_x: int, weak_point_y: int, surface):
        super().__init__(name, sprites, health, max_health, 
                        x_position, y_position, hitbox_x, 
                        hitbox_y, speed, jump_height, 
                        skill)
        self.__weak_point_x: weak_point_x
        self.__weak_point_y: weak_point_y
        self.__x_position = x_position
        self.__y_position = y_position
        self.__speed = speed
        self.__jump_height = jump_height
        self.__sprites = sprites
        self.__counter = 0
        self.window = surface
        self.__hitbox_x = hitbox_x
        self.__hitbox_y = hitbox_y

    @property
    def x_position(self):
        return self.__x_position
    
    @x_position.setter
    def x_position(self, x_position):
        self.__x_position = x_position

    @property
    def y_position(self):
        return self.__y_position

    @y_position.setter
    def y_position(self, y_position):
        self.__y_position = y_position

    @property
    def weak_point_x(self):
        return self.__weak_point_x

    @weak_point_x.setter
    def weak_point_x(self, weak_point_x):
        self.__weak_point_x = weak_point_x

    @property
    def weak_point_y(self):
        return self.__weak_point_y

    @weak_point_y.setter
    def weak_point_y(self, weak_point_y):
        self.__weak_point_y = weak_point_y
        
    @property
    def sprites(self):
        return self.__sprites

    @property
    def counter(self):
        return self.__counter
    
    @counter.setter
    def counter(self, counter):
        self.__counter = counter

    def summon_minions(self):
        pass
    
    def move(self):
        distance = 400

        if self.counter >= 0 and self.counter <= distance:
            self.x_position += self.speed
        elif self.counter >= distance and self.counter <= distance*2:
            self.x_position -= self.speed
        else:
            self.counter = 0

        self.counter += 1

    def skill_reset(self):
        self.skill.reset(self.x_position, self.y_position + self.hitbox_y)

    def draw(self):
        self.window.draw_scaled_image("prototipo\Images\pygame_boss.png", 
                    self.__hitbox_x, self.__hitbox_y, 
                    self.__x_position, self.__y_position)