import mqtt_remote_method_calls as com
import robot_controller as robo
import ev3dev.ev3 as ev3
robot = robo.Snatch3r

def main():
    mqtt_client = com.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.loop_forever()
    game = True
    while game == True:
        if ev3.ColorSensor.color == ev3.ColorSensor.COLOR_BLUE:
            send_stop(mqtt_client)
            ev3.Sound.speak("You are in the water. You lose.")
            game = False

def send_stop(mqtt_client):
    print("stop")
    mqtt_client.send_message("stop")
# def drive_forward(button_state, left_speed, right_speed):
#     if button_state:
#         robot.left_motor.run_forever(speed_sp=left_speed)
#         robot.right_motor.run_forever(speed_sp=right_speed)
#     else:
#         robot.left_motor.stop(stop_action='brake')
#         robot.right_motor.run_forever(stop_action='brake')
#
# def drive_backward(button_state, left_speed, right_speed):
#     if button_state:
#         robot.left_motor.run_forever(speed_sp=left_speed)
#         robot.right_motor.run_forever(speed_sp=right_speed)
#     else:
#         robot.left_motor.stop(stop_action='brake')
#         robot.right_motor.stop(stop_action='brake')
#
# def turn_left(button_state, left_speed, right_speed):
#     if button_state:
#         robot.left_motor.run_forever(speed_sp=left_speed)
#         robot.right_motor.run_forever(speed_sp=right_speed)
#     else:
#         robot.left_motor.stop(stop_action='brake')
#         robot.right_motor.stop(stop_action='brake')
#
# def turn_right(button_state, left_speed, right_speed):
#     if button_state:
#         robot.left_motor.run_forever(speed_sp=left_speed)
#         robot.right_motor.run_forever(speed_sp=right_speed)
#     else:
#         robot.left_motor.stop(stop_action='brake')
#         robot.right_motor.stop(stop_action='brake')
#
# def make_stop(button_state):
#     if button_state:
#         robot.left_motor.stop(stop_action='brake')
#         robot.right_motor.stop(stop_action='brake')

main()