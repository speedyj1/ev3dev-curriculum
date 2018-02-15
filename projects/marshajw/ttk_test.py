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

    for k in range(joystick_count):
        joystick = pygame.joystick.Joystick(k)
        joystick.init()
        axes = joystick.get_numaxes()
        for i in range(axes):
            axis = joystick.get_axis(i)
            label = ttk.Label(frame1, text="Axis {} value: {:>6.3f}".format(i, axis))
            label.grid()
    clock.tick(60)

    root.mainloop()


main()
pygame.quit()
