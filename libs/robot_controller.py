"""
  Library of EV3 robot functions that are useful in many different applications. For example things
  like arm_up, arm_down, driving around, or doing things with the Pixy camera.

  Add commands as needed to support the features you'd like to implement.  For organizational
  purposes try to only write methods into this library that are NOT specific to one tasks, but
  rather methods that would be useful regardless of the activity.  For example, don't make
  a connection to the remote control that sends the arm up if the ir remote control up button
  is pressed.  That's a specific input --> output task.  Maybe some other task would want to use
  the IR remote up button for something different.  Instead just make a method called arm_up that
  could be called.  That way it's a generic action that could be used in any task.
"""

import ev3dev.ev3 as ev3
import math
import time


class Snatch3r(object):

    def __init__(self):
        self.left_motor = ev3.LargeMotor(ev3.OUTPUT_B)
        self.right_motor = ev3.LargeMotor(ev3.OUTPUT_C)
        assert self.left_motor.connected
        assert self.right_motor.connected
        self.arm_motor = ev3.MediumMotor(ev3.OUTPUT_A)
        self.touch_sensor = ev3.TouchSensor(ev3.INPUT_1)
        assert self.touch_sensor.connected
        assert self.arm_motor.connected
        self.max_speed = 900

    def drive_inches(self, inches_target, speed_deg_per_second):
        """
            drive_inches takes in a distance in inches and converts it to degrees for the motor to turn. This function runs both
            motors the same distance at the same speed. This function beeps when it is finished.
            """
        degrees_per_inch = 90
        rotations_in_degrees = inches_target * degrees_per_inch
        if speed_deg_per_second != 0:
            self.left_motor.run_to_rel_pos(position_sp=rotations_in_degrees, speed_sp=speed_deg_per_second)
            self.right_motor.run_to_rel_pos(position_sp=rotations_in_degrees, speed_sp=speed_deg_per_second)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

    def turn_degrees(self, degrees_to_turn, turn_speed_sp):
        """
        turn_degrees is made to take input on degrees to turn. It moves the motors in opposite directions depending on if
        the input is positive or negative. The function will beep when it has finished.
        """
        degrees_per_turning_degree = 4
        degrees_per_wheel = degrees_to_turn * degrees_per_turning_degree
        if turn_speed_sp < 0:
            self.left_motor.run_to_rel_pos(position_sp=degrees_per_wheel, speed_sp=turn_speed_sp)
            self.right_motor.run_to_rel_pos(position_sp=-degrees_per_wheel, speed_sp=turn_speed_sp)
        if turn_speed_sp > 0:
            self.left_motor.run_to_rel_pos(position_sp=-degrees_per_wheel, speed_sp=turn_speed_sp)
            self.right_motor.run_to_rel_pos(position_sp=degrees_per_wheel, speed_sp=turn_speed_sp)
        self.left_motor.wait_while(ev3.Motor.STATE_RUNNING)
        self.right_motor.wait_while(ev3.Motor.STATE_RUNNING)

    def arm_calibration(self):
        ""
        self.arm_motor.run_forever(speed_sp=self.max_speed)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action="brake")
        self.arm_motor.stop()
        ev3.Sound.beep().wait()
        arm_revolutions_for_full_range = 14.2 * 360
        self.arm_motor.run_to_rel_pos(
            position_sp=-arm_revolutions_for_full_range)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()
        self.arm_motor.position = 0

    def arm_up(self):
        """
        arm_up is made to raise the arm up when the desired button is pressed. This function will always raise the
        arm as fast as possible and will beep when it is fully raised.
        """
        self.arm_motor.run_forever(speed_sp=self.max_speed)
        while not self.touch_sensor.is_pressed:
            time.sleep(0.01)
        self.arm_motor.stop(stop_action="brake")
        self.arm_motor.stop()
        ev3.Sound.beep().wait()

    def arm_down(self):
        """
        arm_down is made to lower the arm down when the desired button is pressed. This function will always lower the
        arm as fast as possible and will beep when it is fully lowered.
        """
        self.arm_motor.run_to_abs_pos(position_sp=0, speed_sp=self.max_speed)
        self.arm_motor.wait_while(ev3.Motor.STATE_RUNNING)
        ev3.Sound.beep().wait()

    def shutdown(self):
        """
        shutdown is made to stop all movement of the robot and finish running code when the desired button is pressed.
        This function changes the LEDs to Green and says 'Goodbye' before after everything is stopped.
        """
        :return:
        self.arm_motor.stop()
        self.left_motor.stop()
        self.right_motor.stop()
        ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
        ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
        print('Goodbye!')
        ev3.Sound.speak("Goodbye").wait()

