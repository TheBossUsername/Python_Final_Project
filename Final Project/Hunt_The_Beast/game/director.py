from time import sleep
from game import constants

class Director:
    # Description:
    #   It takes the cast and script of all the actors and actions and runs the game
    # 
    # OOP Principles Used:
    #   Encapsulation
    #
    # Reasoning:
    #   This class uses encapsulation because it stores the script and cast that it was passed to by main
    #   

    def __init__(self, cast, script):
        """The class constructor.
        
        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        self._cast = cast
        self._script = script
        
    def start_game(self):
        """Starts the game loop to control the sequence of play."""
        while True:
            self._cue_action("input")
            self._cue_action("update")
            self._cue_action("output")
            sleep(constants.FRAME_LENGTH)

    def _cue_action(self, tag):
        for action in self._script[tag]:
            action.execute(self._cast)