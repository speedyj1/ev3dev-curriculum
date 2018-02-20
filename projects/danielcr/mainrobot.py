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
        print("(X, Y)=({}), {}) Width = {} Height={}".format(robot.pixy.value(1), robot.pixy.value(2),
                                                             robot.pixy.value(3), robot.pixy.value(4)))

        mqtt_client.send_message('on_rectangle_update', [robot.pixy.value(1), robot.pixy.value(2), robot.pixy.value(3),
                                                         robot.pixy.value(4)])
        time.sleep(0.25)

    print("Goodbye!")
    ev3.Sound.speak("Goodbye").wait()
    mqtt_client.close()
    robot.loop_forever()  # Calls a function that has a while True: loop within it to avoid letting the program end.


main()
