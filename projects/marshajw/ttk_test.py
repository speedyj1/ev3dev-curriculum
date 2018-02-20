import pygame
import tkinter
from tkinter import ttk


def main():
    pygame.init()
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    root = tkinter.Tk()
    root.title('Testing')
    frame1 = ttk.Frame(root)
    frame1.grid()
    clock = pygame.time.Clock()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
        for k in range(joystick_count):
            joystick = pygame.joystick.Joystick(k)
            joystick.init()
            axes = joystick.get_numaxes()
            for i in range(axes):
                axis = joystick.get_axis(i)
                print(joystick.get_axis(1))
                label = ttk.Label(frame1, text="Axis {} value: {:>6.3f}".format(i, axis))
                label.grid()
            # buttons = joystick.get_numbuttons()
            # for i in range(buttons):
            #     button = joystick.get_button(i)
            #     print("Button {:>2} value: {}".format(i, button))
        clock.tick(20)
        root.mainloop()


def main_1():
    pygame.init()
    pygame.joystick.init()
    # joystick_count = pygame.joystick.get_count()
    root = tkinter.Tk()
    root.title('Testing')
    frame1 = ttk.Frame(root)
    frame1.grid()
    clock = pygame.time.Clock()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    axis = joystick.get_axis(1)
    print(joystick.get_axis(1))
    label = ttk.Label(frame1, text="Axis {} value: {:>6.3f}".format(1, axis))
    label.grid()
    clock.tick(20)
    root.mainloop()


def main_2():
    pygame.init()
    pygame.joystick.init()
    joystick_count = pygame.joystick.get_count()
    root = tkinter.Tk()
    root.title('Testing')
    frame1 = ttk.Frame(root)
    frame1.grid()
    clock = pygame.time.Clock()
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    axis = axis_value(joystick_count, 1)
    label = ttk.Label(frame1, text="Axis {} value: {:>6.3f}".format(1, axis))
    label.grid()
    clock.tick(20)
    root.mainloop()


def axis_value(joystick_count, axis_number):
    clock = pygame.time.Clock()
    for k in range(joystick_count):
        joystick = pygame.joystick.Joystick(k)
        joystick.init()
        axes = joystick.get_numaxes()
        for i in range(axes):
            axis = joystick.get_axis(i)
            print(joystick.get_axis(axis_number))
            return axis
    clock.tick(20)


def if_else():
    pygame.init()
    clock = pygame.time.Clock()
    pygame.joystick.init()
    done = False
    while done:

        joystick_count = pygame.joystick.get_count()
        print(joystick_count)
        for k in range(joystick_count):
            joystick = pygame.joystick.Joystick(k)
            joystick.init()
            print(joystick.get_axis(1))
        clock.tick(20)


def last_one(axiz):
    pygame.init()
    done = False
    clock = pygame.time.Clock()
    pygame.joystick.init()
    while done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True
        joystick_count = pygame.joystick.get_count()

        for k in range(joystick_count):
            joystick = pygame.joystick.Joystick(k)
            joystick.init()
            axes = joystick.get_numaxes()
            for i in range(axes):
                axis = joystick.get_axis(axiz)
                print(axis)
                return axis

        clock.tick(20)
        pygame.quit()


print(last_one(1))
pygame.quit()
