"""
This is the tkinter side of the code.
"""

import tkinter
from tkinter import ttk
import time

import mqtt_remote_method_calls as com

mqtt_client = com.MqttClient()
mqtt_client.connect_to_ev3()


class MyDelegate(object):
    def __init__(self, canvas, rectangle_tag):
        self.canvas = canvas
        self.rectangle_tag = rectangle_tag

    def on_rectangle_update(self, x, y, width, height):
        self.canvas.coords(self.rectangle_tag, [x, y, x + width, y + height])


def main():
    window1link()


def window1link():
    root = tkinter.Tk()  # makes window

    window1 = ttk.Frame(root, padding=20)
    window1.grid()

    button_1 = ttk.Button(window1, text='Manual Mode')
    button_1.grid(row=0, column=0)
    button_1['command'] = lambda: window2link()

    button_2 = ttk.Button(window1, text='Pixy Graph')
    button_2.grid(row=1, column=0)
    button_2['command'] = lambda: window3link()

    button_3 = ttk.Button(window1, text='Draw Shapes')
    button_3.grid(row=2, column=0)
    button_3['command'] = lambda: window4link()

    button_4 = ttk.Button(window1, text='Check Color')
    button_4.grid(row=3, column=0)
    button_4['command'] = lambda: window5link()

    root.mainloop()


def window2link():
    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20, relief='raised')
    main_frame.grid()

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
    forward_button['command'] = lambda: send_forward(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: send_forward(mqtt_client, left_speed_entry, right_speed_entry))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    # left_button and '<Left>' key
    left_button['command'] = lambda: send_left(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Left>', lambda event: send_left(mqtt_client, left_speed_entry, right_speed_entry))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    # stop_button and '<space>' key (note, does not need left_speed_entry, right_speed_entry)
    stop_button['command'] = lambda: send_stop(mqtt_client)
    root.bind('<space>', lambda event: send_stop(mqtt_client))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    # right_button and '<Right>' key
    right_button['command'] = lambda: send_right(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Right>', lambda event: send_right(mqtt_client, left_speed_entry, right_speed_entry))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    # back_button and '<Down>' key
    back_button['command'] = lambda: send_back(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Down>', lambda event: send_back(mqtt_client, left_speed_entry, right_speed_entry))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)
    root.bind('<u>', lambda event: send_up(mqtt_client))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<j>', lambda event: send_down(mqtt_client))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=5, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=6, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


def window3link():
    root = tkinter.Tk()
    root.title = "Pixy display"

    main_frame = ttk.Frame(root, padding=5)
    main_frame.grid()

    # The values from the Pixy range from 0 to 319 for the x and 0 to 199 for the y.
    canvas = tkinter.Canvas(main_frame, background="lightgray", width=320, height=200)
    canvas.grid(columnspan=2)

    rect_tag = canvas.create_rectangle(150, 90, 170, 110, fill="blue")

    # Create an MQTT connection
    my_delegate = MyDelegate(canvas, rect_tag)
    mqtt_client = com.MqttClient(my_delegate)
    mqtt_client.connect_to_ev3()
    # mqtt_client.connect_to_ev3("35.194.247.175")  # Off campus IP address of a GCP broker

    # Buttons for quit and exit
    quit_button = ttk.Button(main_frame, text="Quit")
    quit_button.grid(row=4, column=1)
    quit_button["command"] = lambda: quit_program(mqtt_client, shutdown_ev3=True)

    root.mainloop()


def window4link():
    root = tkinter.Tk()
    root.title = "Draw Shapes"

    main_frame = ttk.Frame(root, padding=5)
    main_frame.grid()

    speed = ttk.Label(main_frame, text="Right")
    speed.grid(row=0, column=2)
    speed = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    speed.insert(0, "600")
    speed.grid(row=1, column=2)

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=0, column=0)
    stop_button['command'] = lambda: send_stop(mqtt_client)

    draw_square_button = ttk.Button(main_frame, text='Square')
    draw_square_button.grid(row=3, column=0)
    draw_square_button['command'] = lambda: draw_square(mqtt_client, speed)

    draw_circle_button = ttk.Button(main_frame, text='Circle')
    draw_circle_button.grid(row=1, column=0)
    draw_circle_button['command'] = lambda: draw_circle(mqtt_client, speed)

    root.mainloop()

def window5link():
    check_color(mqtt_client)


def send_up(mqtt_client):
    print("arm_up")
    mqtt_client.send_message("arm_up")


def send_down(mqtt_client):
    print("arm_down")
    mqtt_client.send_message("arm_down")


def send_forward(mqtt_client, left_speed_entry, right_speed_entry):
    print("forward")
    mqtt_client.send_message("drive", [int(left_speed_entry.get()), int(right_speed_entry.get())])


def send_left(mqtt_client, left_speed_entry, right_speed_entry):
    print("left")
    mqtt_client.send_message("drive", [-int(left_speed_entry.get()), int(right_speed_entry.get())])


def send_right(mqtt_client, left_speed_entry, right_speed_entry):
    print("right")
    mqtt_client.send_message("drive", [int(left_speed_entry.get()), -int(right_speed_entry.get())])


def send_back(mqtt_client, left_speed_entry, right_speed_entry):
    print("backward")
    mqtt_client.send_message("drive", [-int(left_speed_entry.get()), -int(right_speed_entry.get())])


def send_stop(mqtt_client):
    print("stop")
    mqtt_client.send_message("stop")


# Quit and Exit button callbacks
def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    # mqtt_client.close()
    exit()


def search_color(mqtt_client):
    mqtt_client.send_message("search1")


def check_color(mqtt_client):
    mqtt_client.send_message("currentcolor")


def draw_circle(mqtt_client, speed):
    print("draw circle")
    speed = int(speed.get())
    halfspeed = speed/2
    mqtt_client.send_message("drive", [int(speed), int(halfspeed)])


def draw_square(mqtt_client, speed):
    print("draw square")
    for k in range(5):
        print("side", k)
        mqtt_client.send_message("drive", [int(speed.get()), int(speed.get())])
        time.sleep(3)
        mqtt_client.send_message("stop")
        mqtt_client.send_message("turn_degrees", [int(90), int(speed.get())])
        mqtt_client.send_message("stop")


def draw_triangle(mqtt_client, speed):
    for k in range(4):
        print("side", k)
        mqtt_client.send_message("drive", [int(speed.get()), int(speed.get())])
        time.sleep(3)
        mqtt_client.send_message("stop")
        mqtt_client.send_message("turn_degrees", [int(120), int(speed.get())])
        mqtt_client.send_message("stop")




main()
