import PicoRobotics
import time

board = PicoRobotics.KitronikPicoRobotics()

def set_motor_speeds():
    while True:
        try:
            speed_str = input("Enter speed for both motors (0-100, or 'stop' or 'reverse'): ")
            if speed_str.lower() == 'stop':
                board.motorOff(1)
                board.motorOff(2)
                print("Both motors stopped.")
                return
            elif speed_str.lower() == 'reverse':
                speed = int(input("Enter speed for reverse (0-100): "))
                if 0 <= speed <= 100:
                    board.motorOn(1, 'r', speed)
                    board.motorOn(2, 'r', speed)
                    print(f"Both motors set to speed {speed} in reverse.")
                else:
                    print("Invalid speed. Please enter a value between 0 and 100.")

            else:
                speed = int(speed_str)
                if 0 <= speed <= 100:
                    board.motorOn(1, 'f', speed)
                    board.motorOn(2, 'f', speed)
                    print(f"Both motors set to speed {speed} in forward.")
                else:
                    print("Invalid speed. Please enter a value between 0 and 100.")

        except ValueError:
            print("Invalid input. Please enter a number, 'stop', or 'reverse'.")
        except OSError as e:
            print(f"Error communicating with motor board: {e}")
            print("Ensure Pico Robotics board is connected and powered.")
            return

while True:
    set_motor_speeds()
    time.sleep(0.1)
