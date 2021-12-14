import random
from game import constants
from game.action import Action
from game.actor import Actor
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        hunter = cast["hunter"][0]
        dragon = cast["dragon"][0]
        warnings = cast["warning"]
        
        dragon_position = dragon.get_position()
        hunter_position = hunter.get_position()



        if dragon_position.get_x() == hunter_position.get_x() - 2 and dragon_position.get_y() == hunter_position.get_y():
            dragon.set_text("D")
            hunter.set_text("x")

        for warning in warnings:
            warning_position = warning.get_position()
            if warning_position.get_x() == hunter_position.get_x() - 2 and warning_position.get_y() == hunter_position.get_y() - 1:
                warning.set_text("D")
                hunter.set_text("W")
