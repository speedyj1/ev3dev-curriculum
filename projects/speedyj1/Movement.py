import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import robot_controller as robo

left_motor = ev3.LargeMotor(ev3.OUTPUT_D)
right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
assert left_motor.connected
assert right_motor.connected

def main():
    robot = robo.Snatch3r()
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.loop_forever()


main()