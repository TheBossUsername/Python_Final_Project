from asciimatics.screen import ManagedScreen
import sys
from time import sleep

class Game_Over:
    # Description:
    #   It contains multiple game over messages that can be called by actions to end the game
    # 
    # OOP Principles Used:
    #   None that I can think of
    #
    # Reasoning:
    #   None that I can think of
    
    def dragon_killed():
        with ManagedScreen() as screen:
            screen.print_at('You have killed the Dragon!', 40, 15)
            screen.print_at('You Win!', 50, 16, 2)
            screen.refresh()
            sleep(5)
            sys.exit()

    def out_of_arrows():
        with ManagedScreen() as screen:
            screen.print_at('You have run out of arrows, soon the beast will find you...', 25, 15)
            screen.print_at('Game Over', 50, 16, 1)
            screen.refresh()
            sleep(7)
            sys.exit()
    
    def ran_into_dragon():
        with ManagedScreen() as screen:
            screen.print_at('You enter the room and are burnt into a crisp, got to close!', 25, 15)
            screen.print_at('Game Over', 50, 16, 1)
            screen.refresh()
            sleep(7)
            sys.exit()
    
    def fell_down_a_hole():
        with ManagedScreen() as screen:
            screen.print_at('You fell down a hole, should have been looking where you were walking', 25, 15)
            screen.print_at('Game Over', 50, 16, 1)
            screen.refresh()
            sleep(7)
            sys.exit()
    
    def start_game():
        with ManagedScreen() as screen:
            screen.print_at('Welcome to Hunt the Beast!', 40, 10, 1)
            screen.print_at('Controls', 10, 14, 4)
            screen.print_at('Use the wasd keys to move', 5, 15, 2)
            screen.print_at('Use the ijkl keys to aim you bow', 5, 16, 2)
            screen.print_at('Press the space bar to fire an arrow', 5, 17, 1)
            screen.print_at('Instructions', 85, 14, 6)
            screen.print_at('You are a hunter with 3 arrows trying to slay a dragon!', 60, 15, 7)
            screen.print_at('You will be warned with a ! if the dragon is near', 60, 16, 1)
            screen.print_at('And you will be warned with a ? if a endless hole is near', 60, 17, 1)
            screen.print_at('The warnings can mean they are adjacent or diagonal from that room', 60, 18, 7)
            screen.print_at('If you run into the dragon or a pit you die', 60, 19, 7)
            screen.print_at('Your arrow will travel in a straight line into adjacent rooms', 60, 20, 7)
            screen.print_at('from where your bow is aimed, if it hits the dragon you win!', 60, 21, 7)
            screen.print_at('The game will begin in 20 seconds', 35, 25, 5)
            screen.refresh()
            sleep(20)