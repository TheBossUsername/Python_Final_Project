import random
from game import constants
from game.director import Director
from game.actor import Actor
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.input_service import InputService
from game.output_service import OutputService
from asciimatics.screen import Screen 

def main(screen):

    cast = {}
    cast["brick"] = []
    for x in range(7, 100, 7):
        for y in range(3, 30, 6):
            for t in range(0, 3, 1):
                position = Point(x, y + t)
                brick = Actor()
                brick.set_text("|")
                brick.set_position(position)
                cast["brick"].append(brick)
    
    
    for x in range(8, 100, 14):
        i = 0
        z = 0
        for y in range(2, 40, 4):
            i += 1
            if i ==3:
                    z += 2
                    i = 1
            for t in range(0, 6, 1):
                position = Point(x + t, y - z)
                brick = Actor()
                brick.set_text("~")
                brick.set_position(position)
                cast["brick"].append(brick)
    
    position = Point(53, 28)
    hunter = Actor()
    hunter.set_text("@")
    hunter.set_position(position)
    cast["hunter"] = [hunter]

    position = hunter.get_position()
    x = position.get_x()
    y = position.get_y()
    position = Point(x, y - 1)
    bow = Actor()
    bow.set_text("^")
    bow.set_position(position)
    cast["bow"] = [bow]

    x = random.randrange(9, 94, 14)
    y = random.randrange(4, 17, 6)
    position = Point(x, y)
    dragon = Actor()
    dragon.set_text("")
    dragon.set_position(position)
    cast["dragon"] = [dragon]

    cast["warning"] = []
    position = dragon.get_position()
    x = position.get_x()
    y = position.get_y()
    for z in range(x - 14, x + 15, 28):
        warning = Actor()
        warning.set_text("")
        position = Point(z, y - 1)
        warning.set_position(position)
        cast["warning"].append(warning)
    for t in range(y - 7, y + 12, 12):
        warning = Actor()
        warning.set_text("")
        position = Point(x, t)
        warning.set_position(position)
        cast["warning"].append(warning)
    for z in range(x - 14, x + 15, 28):
        for t in range(y - 7, y + 12, 12):
            warning = Actor()
            warning.set_text("")
            position = Point(z, t)
            warning.set_position(position)
            cast["warning"].append(warning)
    
    
    dragon_position = dragon.get_position()
    z = dragon_position.get_x()
    t = dragon_position.get_y()
    cast["hole"] = []
    for w in range(0, 3):
        x = random.randrange(9, 94, 14)
        y = random.randrange(4, 17, 6)
        while x == z and y == t:
            x = random.randrange(9, 94, 14)
            y = random.randrange(4, 17, 6)
        position = Point(x, y)
        hole = Actor()
        hole.set_text("")
        hole.set_position(position)
        cast["hole"].append(hole)
    
    holes = cast["hole"]
    cast["hwarning"] = []
    for hole in holes:
        position = hole.get_position()
        x = position.get_x()
        y = position.get_y()
        for z in range(x - 14, x + 15, 28):
            hwarning = Actor()
            hwarning.set_text("")
            position = Point(z, y + 1)
            hwarning.set_position(position)
            cast["hwarning"].append(hwarning)
        for t in range(y - 5, y + 14, 12):
            hwarning = Actor()
            hwarning.set_text("")
            position = Point(x, t)
            hwarning.set_position(position)
            cast["hwarning"].append(hwarning)
        for z in range(x - 14, x + 15, 28):
            for t in range(y - 5, y + 14, 12):
                hwarning = Actor()
                hwarning.set_text("")
                position = Point(z, t)
                hwarning.set_position(position)
                cast["hwarning"].append(hwarning)
    
    position = Point(1, 1)
    arrows = Actor()
    arrows.set_text("Arrows: 3")
    arrows.set_position(position)
    cast["arrows"] = [arrows]



    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    director = Director(cast, script)
    director.start_game()

Screen.wrapper(main)