# This code is made for solar panels on Pins 0 and 1 and Servos on Pins 2 and 3
# The Constants may be modified to change what pins the solar panels and the servos are on
# Coded by Austin Dixon github.com/theblur4900


# Constants
SolarPanel_0 = AnalogPin.P0
SolarPanel_1 = AnalogPin.P1
Servo_0 = AnalogPin.P2
Servo_1 = AnalogPin.P3

# Variables
light_list = []
max_val = 0
best_angle = 0

# Set Pin Frequency
pins.analog_set_period(Servo_0, 20000)
pins.analog_set_period(Servo_1, 20000)

# Actual Logic
def on_button_pressed_a():
    global light_list, max_val, best_angle
    light_list = []
    max_val = 0
    best_angle = 0
    for i in range(181):
    
        pins.servo_write_pin(Servo_0, i)
        pins.servo_write_pin(Servo_1, i)
        
        pause(40)
        current_voltage = (pins.analog_read_pin(SolarPanel_0) + pins.analog_read_pin(SolarPanel_1))/2
        print("Current Voltage: ~" + int((current_voltage/1023)*3.3)+ "V (" + current_voltage + "/1023)")
        light_list.append(current_voltage)

    for i in range(len(light_list)):
        if light_list[i] > max_val:
            max_val = light_list[i]
            best_angle = i

    pins.servo_write_pin(Servo_0, best_angle)
    pins.servo_write_pin(Servo_1, best_angle)

    print("Best Angle Found! " + best_angle + " Degrees")
input.on_button_pressed(Button.A, on_button_pressed_a)

# Zeroing
def on_button_pressed_b():
    pins.servo_write_pin(Servo_0, 0)
    pins.servo_write_pin(Servo_1, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)
