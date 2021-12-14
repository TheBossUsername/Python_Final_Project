from asciimatics.screen import ManagedScreen
import sys
from time import sleep

class Game_Over:
    
    def dragon_killed():
        with ManagedScreen() as screen:
            screen.print_at('You have killed the Dragon!', 0, 0)
            screen.refresh()
            sleep(10)
            sys.exit()

    def out_of_arrows():
        with ManagedScreen() as screen:
            screen.print_at('You have run out of arrows, soon the beast will find you', 50, 20)
            screen.refresh()
            sleep(10)
            sys.exit()