import random
from game import constants
from game.action import Action
from game.actor import Actor
from game.point import Point
from game.game_over import Game_Over

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
        hwarnings = cast["hwarning"]
        holes = cast["hole"]

        
        dragon_position = dragon.get_position()
        hunter_position = hunter.get_position()



        if dragon_position.get_x() == hunter_position.get_x() - 2 and dragon_position.get_y() == hunter_position.get_y():
            Game_Over.ran_into_dragon()
            
        
        for hole in holes:
            hole_position = hole.get_position()
            if hole_position.get_x() == hunter_position.get_x() - 2 and hole_position.get_y() == hunter_position.get_y():
                Game_Over.fell_down_a_hole()

        for warning in warnings:
            warning_position = warning.get_position()
            if warning_position.get_x() == hunter_position.get_x() - 2 and warning_position.get_y() == hunter_position.get_y() - 1:
                warning.set_text("D")
        
        for hwarning in hwarnings:
            hwarning_position = hwarning.get_position()
            if hwarning_position.get_x() == hunter_position.get_x() - 2 and hwarning_position.get_y() == hunter_position.get_y() + 1:
                hwarning.set_text("H")
