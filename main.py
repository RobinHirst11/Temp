import micropython
import machine
import PicoRobotics

board = PicoRobotics.KitronikPicoRobotics()

board.motorOn(1, "f", 100)
