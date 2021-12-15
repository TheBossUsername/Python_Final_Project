import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    # Description:
    #   It takes the users input from the keyboard and converts it into point values that the actions can use
    # 
    # OOP Principles Used:
    #   Abstraction
    #
    # Reasoning:
    #   It uses abstraction by being able to take many different inputs and canvert them into points so the 
    #   other classes do not have to

    def __init__(self, screen):
        self._screen = screen
        self._keys = {}
        self._keys[97] = Point(-14, 0) # a
        self._keys[100] = Point(14, 0) # d
        self._keys[115] = Point(0, 6) # s
        self._keys[119] = Point(0, -6) # w
        self._keys[106] = Point(-1, 0) # j
        self._keys[107] = Point(0, 1) # k
        self._keys[108] = Point(1, 0) # l
        self._keys[105] = Point(0, -1) # i
        self._keys[32] = Point(5, 0) # spacebar
        
    def get_direction(self):
        direction = Point(0, 0)
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            direction = self._keys.get(event.key_code, Point(0, 0))
        return direction
        