class Point:
    # Description:
    #   A point on the screen with a x and a y value that is used by actors
    #
    # OOP Principles Used:
    #   Encapsulation, Polymorphism
    #
    # Reasoning:
    #   This class uses encapsulation becuase there is functions to set and get attributes of actors but no way 
    #   manually change the data inside 
    #
    #   It also uses polymorphism because it can be many different points on the screen but every point
    #   has a x and y value
    
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def is_zero(self):
        return self._x == 0 and self._y == 0  
