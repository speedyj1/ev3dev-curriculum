"""
This is my CSSE120 final project.
"""

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import time
import robot_controller as robo

left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
# assert left_motor.connected
# assert right_motor.connected


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title = 'Golf hole'

    my_frame = ttk.Frame(root, padding=5)
    my_frame.grid()

    objective = 'Make the ball/robot go to the hole/beacon'
    label = ttk.Label(my_frame, text=objective)
    label.grid(columnspan=2)

    canvas = tkinter.Canvas(my_frame, background='lightgray', width=500, height=600)
    canvas.grid(columnspan=2)

    restart_button = ttk.Button(my_frame, text='Restart')
    restart_button.grid(row=3, column=0)

    quit_button = ttk.Button(my_frame, text='Quit')
    quit_button.grid(row=3, column=1)
    quit_button['command'] = lambda: quit_game(mqtt_client)

    robot = robo.Snatch3r()
    dc = DataContainer()

    rc1 = ev3.RemoteControl(channel=1)

    while dc.running:
        rc1.process()
        rc2.process()
        btn.process()
        time.sleep(0.01)

    rc1.on_red_up = lambda state: left_forward(state)
    rc1.on_red_down = lambda state: left_backward(state)
    rc1.on_blue_up = lambda state: right_forward(state)
    rc1.on_blue_down = lambda state: right_backward(state)

    root.mainloop()


def restart(canvas):
    canvas.delete('all')

def quit_game(mqtt_client):
    if mqtt_client:
        mqtt_client.close()
    exit()

def left_forward(button_state):
    if button_state:
        left_motor.run_forever(speed_sp=600)
    else:
        left_motor.stop(stop_action='brake')

def right_forward(button_state):
    if button_state:
        right_motor.run_forever(speed_sp=600)
    else:
        right_motor.stop(stop_action='brake')

def left_backward(button_state):
    if button_state:
        left_motor.run_forever(speed_sp=-600)
    else:
        left_motor.stop(stop_action='brake')

def right_backward(button_state):
    if button_state:
        right_motor.run_forever(speed_sp=-600)
    else:
        right_motor.stop(stop_action='brake')
main()