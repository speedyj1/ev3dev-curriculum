"""
This is my CSSE120 final project.
"""

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import robot_controller as robo
robot = robo.Snatch3r


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

    strokes = 0
    score_counter = 'Strokes: ' + str(strokes)
    scoreboard = ttk.Label(my_frame, text=score_counter)
    scoreboard.grid(row=1, columnspan=2)

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
    forward_button['command'] = lambda: send_forward(mqtt_client2, 600, 600)
    root1.bind('<Up>', lambda event: send_forward(mqtt_client2, 600, 600))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    # left_button and '<Left>' key
    left_button['command'] = lambda: send_left(mqtt_client2, -300, 300)
    root1.bind('<Left>', lambda event: send_left(mqtt_client2, -300, 300))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    # stop_button and '<space>' key (note, does not need left_speed_entry, right_speed_entry)
    stop_button['command'] = lambda: send_stop(mqtt_client2)
    root1.bind('<space>', lambda event: send_stop(mqtt_client2))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    # right_button and '<Right>' key
    right_button['command'] = lambda: send_right(mqtt_client2, 300, -300)
    root1.bind('<Right>', lambda event: send_right(mqtt_client2, 300, -300))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    # back_button and '<Down>' key
    back_button['command'] = lambda: send_back(mqtt_client2, -600, -600)
    root1.bind('<Down>', lambda event: send_back(mqtt_client2, -600, -600))

    root.mainloop()
    root1.mainloop()

    # game = True
    # while game == True:
    #     if ev3.ColorSensor.color == ev3.ColorSensor.COLOR_BLUE:
    #         make_stop()
    #         ev3.Sound.speak("You are in the water. You lose.")
    #         game = False

# def restart_game(mqtt_client, x):
#     if mqtt_client:
#         x = 0
#     print('Please return to the start')


def quit_game(mqtt_client):
    if mqtt_client:
        mqtt_client.close()
    exit()

def send_forward(mqtt_client, left_speed, right_speed):
    print("forward")
    mqtt_client.send_message("drive_forward",[int(left_speed),
                                      int(right_speed)])

def send_left(mqtt_client, left_speed, right_speed):
    print("left")
    mqtt_client.send_message("turn_left",[int(left_speed),
                                      int(right_speed)])

def send_right(mqtt_client, left_speed, right_speed):
    print("right")
    mqtt_client.send_message("turn_right",[int(left_speed),
                                      int(right_speed)])

def send_back(mqtt_client,left_speed,right_speed):
    print("backward")
    mqtt_client.send_message("drive_backward",[int(left_speed),
                                         int(right_speed)])

def send_stop(mqtt_client):
    print("stop")
    mqtt_client.send_message("make_stop")


main()