from game import constants
from game.action import Action
from game.point import Point
from game.actor import Actor

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        direction = self._input_service.get_direction()
        x1 = direction.get_x()
        y1 = direction.get_y()
        if x1 == -1 or x1 == 1 or y1 == -1 or y1 == 1:
            bow = cast["bow"][0]
            hunter = cast["hunter"][0]
            if x1 == -1:
                bow.set_text("<")
            elif x1 == 1:
                bow.set_text(">")
            elif y1 == -1:
                bow.set_text("^")
            elif y1 == 1:
                bow.set_text("v")
            position = hunter.get_position()
            x = position.get_x()
            y = position.get_y()
            position = Point(x + x1, y + y1)
            bow.set_position(position) 
        elif x1 == 5:
            bow = cast["bow"][0]
            hunter = cast["hunter"][0]
            dragon = cast["dragon"][0]
            arrows = cast["arrows"][0]
            x = arrows.get_value()
            x -= 1
            arrows.set_value(x)
            bposition = bow.get_position()
            hposition = hunter.get_position()
            dposition = dragon.get_position()
            bx = bposition.get_x()
            by = bposition.get_y()
            hx = hposition.get_x()
            hy = hposition.get_y()
            dx = dposition.get_x()
            dy = dposition.get_y()
            if bx == hx + 1:
                for t in range(12, 80, 14):
                    if dx == hx + t and dy == hy:
                        hunter.set_text("R")
            if bx == hx - 1:
                for t in range(16, 80, 14):
                    if dx == hx - t and dy == hy:
                        hunter.set_text("L")
            if by == hy + 1:
                for t in range(6, 30, 6):
                    if dx + 2 == hx and dy == hy + t:
                        hunter.set_text("D")
            if by == hy - 1:
                for t in range(6, 30, 6):
                    if dx + 2 == hx and dy == hy - t:
                        hunter.set_text("U")
            elif arrows.get_value() == 0:
                hunter.set_text("out")



        else:   
            hunter = cast["hunter"][0] # there's only one in the cast
            hunter.set_velocity(direction)   
            bow = cast["bow"][0] # there's only one in the cast
            bow.set_velocity(direction)      
