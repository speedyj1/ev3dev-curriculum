"""
This is my CSSE120 final project.
"""

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
from PIL import ImageTk, Image
import ev3dev.ev3 as ev3
left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
right_motor = ev3.LargeMotor(ev3.OUTPUT_C)



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
    restart_button['command'] = lambda: restart_game(mqtt_client, strokes)

    quit_button = ttk.Button(my_frame, text='Quit')
    quit_button.grid(row=3, column=1)
    quit_button['command'] = lambda: quit_game(mqtt_client)

    mqtt_client2 = com.MqttClient()
    mqtt_client2.connect_to_ev3()

    root1 = tkinter.Tk()
    root1.title("MQTT Remote")

    main_frame = ttk.Frame(root1, padding=20, relief='raised')
    main_frame.grid()

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
    forward_button['command'] = lambda: drive_forward(mqtt_client, 600, 600)
    root1.bind('<Up>', lambda event: drive_forward(mqtt_client, 600, 600))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    # left_button and '<Left>' key
    left_button['command'] = lambda: turn_left(mqtt_client, -300, 300)
    root1.bind('<Left>', lambda event: turn_left(mqtt_client, -300, 300))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    # stop_button and '<space>' key (note, does not need left_speed_entry, right_speed_entry)
    stop_button['command'] = lambda: make_stop(mqtt_client)
    root1.bind('<space>', lambda event: make_stop(mqtt_client))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    # right_button and '<Right>' key
    right_button['command'] = lambda: turn_right(mqtt_client, 300, -300)
    root1.bind('<Right>', lambda event: turn_right(mqtt_client, 300, -300))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    # back_button and '<Down>' key
    back_button['command'] = lambda: drive_backward(mqtt_client, -600, -600)
    root1.bind('<Down>', lambda event: drive_backward(mqtt_client, -600, -600))

    root.mainloop()
    root1.mainloop()


def restart_game(mqtt_client, x):
    if mqtt_client:
        x = 0
    print('Please return to the start')


def quit_game(mqtt_client):
    if mqtt_client:
        mqtt_client.close()
    exit()
def drive_forward(button_state, left_speed, right_speed):
    if button_state:
        left_motor.run_forever(speed_sp=left_speed)
        right_motor.run_forever(speed_sp=right_speed)
    else:
        left_motor.stop(stop_action='brake')
        right_motor.run_forever(stop_action='brake')

def drive_backward(button_state, left_speed, right_speed):
    if button_state:
        left_motor.run_forever(speed_sp=left_speed)
        right_motor.run_forever(speed_sp=right_speed)
    else:
        left_motor.stop(stop_action='brake')
        right_motor.stop(stop_action='brake')

def turn_left(button_state, left_speed, right_speed):
    if button_state:
        left_motor.run_forever(speed_sp=left_speed)
        right_motor.run_forever(speed_sp=right_speed)
    else:
        left_motor.stop(stop_action='brake')
        right_motor.stop(stop_action='brake')

def turn_right(button_state, left_speed, right_speed):
    if button_state:
        left_motor.run_forever(speed_sp=left_speed)
        right_motor.run_forever(speed_sp=right_speed)
    else:
        left_motor.stop(stop_action='brake')
        right_motor.stop(stop_action='brake')

def make_stop(button_state):
    if button_state:
        left_motor.stop(stop_action='brake')
        right_motor.stop(stop_action='brake')


main()