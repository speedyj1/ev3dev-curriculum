import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3
import time


def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    # mqtt_client.connect_to_pc("35.194.247.175")  # Off campus IP address of a GCP broker
    robot.pixy.mode = "SIG1"

    while not robot.touch_sensor.is_pressed:
        # DONE: 3. Read the Pixy values for x, y, width, and height
        # Print the values (much like the print_pixy_readings example)
        print("(X, Y)=({}), {}) Width = {} Height={}".format(robot.pixy.value(1), robot.pixy.value(2),
                                                             robot.pixy.value(3), robot.pixy.value(4)))

        # DONE: 4. Send the Pixy values to the PC by calling the on_rectangle_update method
        # If you open m2_pc_pixy_display you can see the parameters for that method [x, y, width, height]

        mqtt_client.send_message('on_rectangle_update', [robot.pixy.value(1), robot.pixy.value(2), robot.pixy.value(3),
                                                         robot.pixy.value(4)])

        time.sleep(0.25)

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()
    mqtt_client.close()
    robot.loop_forever()  # Calls a function that has a while True: loop within it to avoid letting the program end.

#
# def search():
#     robot = robo.Snatch3r()
#     robot.pixy.mode = "SIG1"
#     turn_speed = 200
#     while not robot.touch_sensor.is_pressed:
#
#         print("(X, Y)=({}), {}) Width = {} Height={}".format(robot.pixy.value(1), robot.pixy.value(2),
#                                                          robot.pixy.value(3), robot.pixy.value(4)))
#
#         if robot.pixy.value(1) > 200:
#             robot.drive(turn_speed, -turn_speed)
#         elif robot.pixy.value(1) < 100:
#             robot.drive(-turn_speed, turn_speed)
#         elif robot.pixy.value(1) > 100 and robot.pixy.value(1) < 200:
#             robot.stop()
#         else:
#             robot.stop()
#
#         time.sleep(0.25)


main()
