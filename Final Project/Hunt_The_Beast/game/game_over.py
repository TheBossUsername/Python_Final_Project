from asciimatics.screen import ManagedScreen
import sys
from time import sleep

class Game_Over:
    
    def dragon_killed():
        with ManagedScreen() as screen:
            screen.print_at('You have killed the Dragon!', 40, 15)
            screen.print_at('You Win!', 50, 16)
            screen.refresh()
            sleep(5)
            sys.exit()

    def out_of_arrows():
        with ManagedScreen() as screen:
            screen.print_at('You have run out of arrows, soon the beast will find you...', 25, 15)
            screen.print_at('Game Over', 50, 16)
            screen.refresh()
            sleep(7)
            sys.exit()
    
    def ran_into_dragon():
        with ManagedScreen() as screen:
            screen.print_at('You enter the room and are burnt into a crisp, got to close!', 25, 15)
            screen.print_at('Game Over', 50, 16)
            screen.refresh()
            sleep(7)
            sys.exit()
    
    def fell_down_a_hole():
        with ManagedScreen() as screen:
            screen.print_at('You fell down a hole, should have been looking where you where walking', 25, 15)
            screen.print_at('Game Over', 50, 16)
            screen.refresh()
            sleep(7)
            sys.exit()