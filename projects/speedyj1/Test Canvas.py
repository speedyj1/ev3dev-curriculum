import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
import ev3dev.ev3 as ev3
import time
import robot_controller as robo
import mqtt_remote_method_calls as com

def main():


    mqtt_client2 = com.MqttClient()
    mqtt_client2.connect_to_ev3()

    root1 = tkinter.Tk()
    root1.title("MQTT Remote")

    main_frame = ttk.Frame(root1, padding=20, relief='raised')
    main_frame.grid()

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    # forward_button and '<Up>' key is done for your here...
    forward_button['command'] = lambda: send_forward(mqtt_client, 600, 600)
    root1.bind('<Up>', lambda event: send_forward(mqtt_client, 600, 600))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=3, column=0)
    # left_button and '<Left>' key
    left_button['command'] = lambda: send_left(mqtt_client, -600, 600)
    root1.bind('<Left>', lambda event: send_left(mqtt_client, -600, 600))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=3, column=1)
    # stop_button and '<space>' key (note, does not need left_speed_entry, right_speed_entry)
    stop_button['command'] = lambda: send_stop(mqtt_client)
    root1.bind('<space>', lambda event: send_stop(mqtt_client))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=3, column=2)
    # right_button and '<Right>' key
    right_button['command'] = lambda: send_right(mqtt_client, 600, -600)
    root1.bind('<Right>', lambda event: send_right(mqtt_client, 600, -600))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=4, column=1)
    # back_button and '<Down>' key
    back_button['command'] = lambda: send_back(mqtt_client, -600, -600)
    root1.bind('<Down>', lambda event: send_back(mqtt_client, -600, -600))

    root1.mainloop()

main()