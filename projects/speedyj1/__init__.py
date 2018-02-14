"""
This is my CSSE120 final project.
"""

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
from PIL import ImageTk, Image
import ev3dev.ev3 as ev3
import time
import robot_controller as robo




def main():

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title = 'Golf hole'

    my_frame = ttk.Frame(root, padding=5)
    my_frame.grid()

    # w_image = Image.open('C:\Users\speedyj1\Documents\water_hazard_for_csse120.svg')
    # background_label = ttk.Label(my_frame, w_image)
    # background_label.place(x=250, y=250, relwidth=1, relheight=2)

    objective = 'Make the ball/robot go to the hole/beacon'
    label = ttk.Label(my_frame, text=objective)
    label.grid(columnspan=2)

    strokes = 0
    score_counter = 'Strokes: ' + str(strokes)
    scoreboard = ttk.Label(my_frame, text=score_counter)
    scoreboard.grid(row=1, columnspan=2)

    canvas = tkinter.Canvas(my_frame, background='lightgray', width=500, height=600)
    canvas.grid(columnspan=2)

    restart_button = ttk.Button(my_frame, text='Restart')
    restart_button.grid(row=3, column=0)
    restart_button['command'] = lambda: restart_game(mqtt_client)

    quit_button = ttk.Button(my_frame, text='Quit')
    quit_button.grid(row=3, column=1)
    quit_button['command'] = lambda: quit_game(mqtt_client)

    root.mainloop()


def restart_game(mqtt_client):
    mqtt_client.strokes = 0
    print('Please return to the start')


def quit_game(mqtt_client):
    if mqtt_client:
        mqtt_client.close()
    exit()

main()