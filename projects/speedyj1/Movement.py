import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3


def main():
    robot = robo.Snatch3r
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.loop_forever()

    # if robot.ir_sensor.proximity < 20:
    #     ev3.Sound.beep()
    #     print(robot.ir_sensor.proximity)
    #     time.sleep(1.5)

main()