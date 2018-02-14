import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import time
import robot_controller as robo

left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
assert left_motor.connected
assert right_motor.connected

robot = robo.Snatch3r()
    dc = DataContainer()

    rc1 = ev3.RemoteControl(channel=1)

    while dc.running:
        btn.process()
        time.sleep(0.01)

    root.bind('<Up>', lambda event: drive_forward(button_state=True))
    root.bind('<Left>', lambda event: turn_left(button_state=True))
    root.bind('<Right>', lambda event: turn_right(button_state=True))
    root.bind('<Down>', lambda event: turn_right(button_state=True))

    if robot.color_sensor.color == ev3.ColorSensor.COLOR_BLUE:
        strokes = 100
        quit_button['command'] = lambda: quit_game(mqtt_client)




def drive_forward(button_state):
    if button_state:
        left_motor.run_forever(speed_sp=600)
        right_motor.run_forever(speed_sp=600)
    else:
        left_motor.stop(stop_action='brake')
        right_motor.run_forever(stop_action='brake')

def drive_backward(button_state):
    if button_state:
        left_motor.run_forever(speed_sp=-600)
        right_motor.run_forever(speed_sp=-600)
    else:
        left_motor.stop(stop_action='brake')
        right_motor.stop(stop_action='brake')

def turn_left(button_state):
    if button_state:
        robot.turn_degrees(45, 600)
    else:
        left_motor.stop(stop_action='brake')
        right_motor.stop(stop_action='brake')

def turn_right(button_state):
    if button_state:
        robot.turn_degrees(-45, 600)
    else:
        left_motor.stop(stop_action='brake')
        right_motor.stop(stop_action='brake')