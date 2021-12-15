from game import constants
from game.action import Action
from game.actor import Actor
from game.point import Point
from game.game_over import Game_Over

class HandleCollisionsAction(Action):
    # Description:
    #   It checks if the player has run into any warnings, walls, or hazards, and reveals, redirects, or
    #   ends the game accordingly
    # 
    # OOP Principles Used:
    #   Inheritance, Abstraction
    #
    # Reasoning:
    #   It uses inheritance by inheriting the class action, so when the director executes actions it
    #   will activate this class as well

    def execute(self, cast):
        hunter = cast["hunter"][0]
        dragon = cast["dragon"][0]
        dragon_warnings = cast["dragon_warning"]
        hole_warnings = cast["hole_warning"]
        bow = cast["bow"][0]
        holes = cast["hole"]
        dragon_position = dragon.get_position()
        hunter_position = hunter.get_position()

        if dragon_position.get_x() == hunter_position.get_x() - 2 and dragon_position.get_y() == hunter_position.get_y():
            Game_Over.ran_into_dragon()
        
        for hole in holes:
            hole_position = hole.get_position()
            if hole_position.get_x() == hunter_position.get_x() - 2 and hole_position.get_y() == hunter_position.get_y():
                Game_Over.fell_down_a_hole()

        for dragon_warning in dragon_warnings:
            dragon_warning_position = dragon_warning.get_position()
            if dragon_warning_position.get_x() == hunter_position.get_x() - 2 and dragon_warning_position.get_y() == hunter_position.get_y() - 1:
                dragon_warning.set_text("!")
        
        for hole_warning in hole_warnings:
            hole_warning_position = hole_warning.get_position()
            if hole_warning_position.get_x() == hunter_position.get_x() - 2 and hole_warning_position.get_y() == hunter_position.get_y() + 1:
                hole_warning.set_text("?")
        
        if hunter_position.get_x() >= constants.MAX_X or hunter_position.get_x() <= 0:
            start = Point(53, 28)
            hunter.set_position(start)
            bow_start = Point(53, 27)
            bow.set_text("^")
            bow.set_position(bow_start)
        
        if hunter_position.get_y() >= constants.MAX_Y or hunter_position.get_y() <= 0:
            start = Point(53, 28)
            hunter.set_position(start)
            bow_start = Point(53, 27)
            bow.set_text("^")
            bow.set_position(bow_start)
