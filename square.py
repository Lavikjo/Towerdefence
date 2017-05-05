from enum import Enum

class SquareType(Enum):
    START_SQUARE = 0
    ROUTE_SQUARE = 1
    TOWER_SQUARE = 2
    END_SQUARE = 3

class Square():
 


    def __init__(self, square_type):
        
        self.tower = None
        self.enemies = []     
        self.square_type = square_type

    def get_tower(self):

        return self.tower

    def get_enemies(self):
        
        return self.enemies

    def is_start(self):
        
        return self.square_type is SquareType.START_SQUARE

    def is_end(self):

        return self.square_type is SquareType.END_SQUARE

    def is_route(self):
        return self.square_type is SquareType.ROUTE_SQUARE

    def is_tower(self):
        return self.square_type is SquareType.TOWER_SQUARE

    def is_empty(self):
        
        return self.tower is None and not bool(self.enemies)


    def set_enemy(self, enemy):

        if self.square_type is not SquareType.TOWER_SQUARE:
            self.enemies.append(enemy)
            return True
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

    def remove_unit(self, unit = None):
        '''
        Removes unit from square
        '''
        if self.square_type is SquareType.TOWER_SQUARE and self.tower is not None:
            self.tower = None
        elif self.square_type is not SquareType.TOWER_SQUARE and unit in self.enemies:
            self.enemies.remove(unit)
        

