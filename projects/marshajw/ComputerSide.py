import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import robot_controller as robo


def main():
    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main = ttk.Frame(root, padding=20, relief='raised')
    main.grid()

    button_1 = ttk.Button(main, text='Manual Drive')
    button_1.grid(row=0, column=0)
    button_1['command'] = lambda: drive(mqtt_client)

    button_2 = ttk.Button(main, text='Manual Color Drive')
    button_2.grid(row=1, column=0)
    button_2['command'] = lambda: drive_color(mqtt_client)

    button_3 = ttk.Button(main, text='Button 3')
    button_3.grid(row=2, column=0)

    button_4 = ttk.Button(main, text='Button 4')
    button_4.grid(row=3, column=0)

    # Buttons for quit and exit
    q_button = ttk.Button(main, text="Quit")
    q_button.grid(row=1, column=2)
    q_button['command'] = (lambda: quit_program(mqtt_client, False))

    e_button = ttk.Button(main, text="Exit")
    e_button.grid(row=2, column=2)
    e_button['command'] = (lambda: quit_program(mqtt_client, True))

    root.mainloop()


def drive(mqtt_client):
    root = tkinter.Tk()
    root.title("Manual Drive")

    main_drive = ttk.Frame(root, padding=20, relief='raised')
    main_drive.grid()
    left_speed_label = ttk.Label(main_drive, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Scale(main_drive, from_=0, to=900)
    left_speed_entry.set(600)
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_drive, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Scale(main_drive, from_=0, to=900)
    right_speed_entry.grid(row=1, column=2)
    right_speed_entry.set(600)

    forward_button = ttk.Button(main_drive, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: send_forward(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: send_forward(mqtt_client, left_speed_entry, right_speed_entry))

    left_button = ttk.Button(main_drive, text="Left")
    left_button.grid(row=3, column=0)
    left_button['command'] = lambda: send_left(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Left>', lambda event: send_left(mqtt_client, left_speed_entry, right_speed_entry))

    stop_button = ttk.Button(main_drive, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: send_stop(mqtt_client)
    root.bind('<space>', lambda event: send_stop(mqtt_client))

    right_button = ttk.Button(main_drive, text="Right")
    right_button.grid(row=3, column=2)
    right_button['command'] = lambda: send_right(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Right>', lambda event: send_right(mqtt_client, left_speed_entry, right_speed_entry))

    back_button = ttk.Button(main_drive, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: send_back(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Down>', lambda event: send_back(mqtt_client, left_speed_entry, right_speed_entry))

    up_button = ttk.Button(main_drive, text="Up")
    up_button.grid(row=5, column=0)
    up_button['command'] = lambda: send_up(mqtt_client)
    root.bind('<u>', lambda event: send_up(mqtt_client))

    down_button = ttk.Button(main_drive, text="Down")
    down_button.grid(row=6, column=0)
    down_button['command'] = lambda: send_down(mqtt_client)
    root.bind('<j>', lambda event: send_down(mqtt_client))

    root.mainloop()


def drive_color(mqtt_client):
    root = tkinter.Tk()
    root.title("Manual Color Drive")

    color = ttk.Frame(root, padding=20, relief='raised')
    color.grid()
    left_speed_label = ttk.Label(color, text="Left")
    left_speed_label.grid(row=0, column=0)
    left_speed_entry = ttk.Entry(color, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(color, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(color, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(color, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: send_forward(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Up>', lambda event: send_forward(mqtt_client, left_speed_entry, right_speed_entry))

    left_button = ttk.Button(color, text="Left")
    left_button.grid(row=3, column=0)
    left_button['command'] = lambda: send_left(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Left>', lambda event: send_left(mqtt_client, left_speed_entry, right_speed_entry))

    stop_button = ttk.Button(color, text="Stop")
    stop_button.grid(row=3, column=1)
    stop_button['command'] = lambda: send_stop(mqtt_client)
    root.bind('<space>', lambda event: send_stop(mqtt_client))

    right_button = ttk.Button(color, text="Right")
    right_button.grid(row=3, column=2)
    right_button['command'] = lambda: send_right(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Right>', lambda event: send_right(mqtt_client, left_speed_entry, right_speed_entry))

    back_button = ttk.Button(color, text="Back")
    back_button.grid(row=4, column=1)
    back_button['command'] = lambda: send_back(mqtt_client, left_speed_entry, right_speed_entry)
    root.bind('<Down>', lambda event: send_back(mqtt_client, left_speed_entry, right_speed_entry))

    robot = robo.Snatch3r()

    root.mainloop()


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
    mqtt_client.send_message("drive", [int(left_speed_entry.get()), int(right_speed_entry.get())])


def send_back(mqtt_client, left_speed_entry, right_speed_entry):
    print("backward")
    mqtt_client.send_message("backward", [int(left_speed_entry.get()), int(right_speed_entry.get())])


def send_stop(mqtt_client):
    print("stop")
    mqtt_client.send_message("stop")


def quit_program(mqtt_client, shutdown_ev3):
    if shutdown_ev3:
        print("shutdown")
        mqtt_client.send_message("shutdown")
    mqtt_client.close()
    exit()


main()
