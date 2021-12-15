from game import constants
from game.action import Action
from game.point import Point
from game.actor import Actor
from game.game_over import Game_Over

class ControlActorsAction(Action):
    #
    # Description:
    #   A visible, moveable thing that participates in the game. 
    #   The responsibility of Actor is to keep track of its appearance, position, value 
    #   and velocity in 2d space.
    #
    # OOP Principles Used:
    #   Encapsulation, Polymorphism
    #
    # Reasoning:
    #   This class uses encapsulation becuase there is functions to set and get attributes of actors but no way 
    #   manually change the data inside 
    #
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
        if x1 == 5 or x1 == -1 or x1 == 1 or y1 == -1 or y1 == 1:
            pass
        else:
            hunter = cast["hunter"][0] # there's only one in the cast
            hunter.set_velocity(direction)   
            bow = cast["bow"][0] # there's only one in the cast
            bow.set_velocity(direction)      
