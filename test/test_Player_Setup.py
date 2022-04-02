from testing_base import *
from source.Player_Setup import *

Playerlist = []

Player_Setup(Playerlist)

assert len(Playerlist) == 3

assert Playerlist[0].money == 25
