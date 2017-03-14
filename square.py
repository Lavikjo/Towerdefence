from enum import Enum

class SquareType(Enum):
    START_SQUARE = 0
    ROUTE_SQUARE = 1
    TOWER_SQUARE = 2
    END_SQUARE = 3

class Square():
 


    def __init__(self, square_type):
        
        self.tower = None
        self.enemy = None     
        self.square_type = square_type

    def get_tower(self):

        return self.tower

    def get_enemy(self):
        
        return self.enemy

    def is_start(self):
        
        return self.square_type is SquareType.START_SQUARE

    def is_end(self):

        return self.square_type is SquareType.END_SQUARE

    def is_empty(self):
        
        return self.tower is None and self.enemy is None


    def set_enemy(self, enemy):
        
        if self.is_empty():
            if self.square_type is SquareType.ROUTE_SQUARE:
                self.enemy = enemy
                return True
            else:
                return False
        else:
            return False

    def set_tower(self, tower):

        if self.is_empty():
            if self.square_type is SquareType.TOWER_SQUARE:
                self.tower = tower
                return True
            else:
                return False
        else:
            return False

    def remove_unit(self):
        remove_unit = None
        if self.square_type is SquareType.TOWER_SQUARE and self.tower is not None:
            removed_unit = self.get_tower()
            self.tower = None
        elif self.square_type is SquareType.ROUTE_SQUARE and self.enemy is not None:
            remove_unit = self.get_enemy()
            self.enemy = None
        
        return removed_unit

