from pygame import joystick
from time import sleep
import pygame

joystick.init()
pygame.init()
joy_count = joystick.get_count()
joysticks = {}
for x in range(joy_count):
    current_joy = joystick.Joystick(x)
    joysticks[current_joy.get_instance_id()] = current_joy

def Setup():
    right = False
    left = False
    joystick = False

    print('Press your right pedal...')
    while not right:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                joystick = joysticks[event.instance_id]
                right = event.axis
    sleep(1)
    print('Press your left pedal...')
    while not left:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION and event.axis != right and event.instance_id == joystick.get_instance_id():
                left = event.axis

    print('===Summary===\nJoystick: ', joystick.get_name(), '\nLeft axis: ', left, '\nRight axis: ', right)
    return joystick, str(left), str(right)

#  TODO: Add threadding, vjoy setup
def Main(joystick, left, right):
    print('axes: ', left, right)
    values = {}
    values[left] = 0
    values[right] = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION and event.instance_id == joystick.get_instance_id():
                values[str(event.axis)] = event.value
                rudder = (values[left] - values[right]) / 2
                print('left: ', values[left], 'right: ', values[right], 'rudder: ', rudder)

if __name__ == '__main__':
    joystick, left, right = Setup()
    sleep(1)
    Main(joystick, left, right)

joystick.quit()
pygame.quit()
