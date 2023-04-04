#rpi powered 2d gantry by cmd/Sam T
# A gpl license should be distributed witht his software
#for inquiries/suggestions/bugs check uwuimapewson on github or email me


import time
import RPi.GPIO as GPIO

# Define the stepper motor pins
stepper_x_pin_1 = 17
stepper_x_pin_2 = 27
stepper_y_pin_1 = 22
stepper_y_pin_2 = 23

# Define the stepper motor steps per revolution
stepper_x_steps_per_revolution = 200
stepper_y_steps_per_revolution = 200

# Define the gantry travel limits
gantry_x_min = 0
gantry_x_max = 100
gantry_y_min = 0
gantry_y_max = 100

# Initialize the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(stepper_x_pin_1, GPIO.OUT)
GPIO.setup(stepper_x_pin_2, GPIO.OUT)
GPIO.setup(stepper_y_pin_1, GPIO.OUT)
GPIO.setup(stepper_y_pin_2, GPIO.OUT)

# Set the stepper motor speed
stepper_x_speed = 100
stepper_y_speed = 100

# Define the function to move the gantry to a specific coordinate
def move_gantry(x, y):
  # Move the X-axis stepper motor
  for i in range(x):
    GPIO.output(stepper_x_pin_1, True)
    GPIO.output(stepper_x_pin_2, False)
    time.sleep(stepper_x_speed / 1000.0)
    GPIO.output(stepper_x_pin_1, False)
    GPIO.output(stepper_x_pin_2, True)

  # Move the Y-axis stepper motor
  for i in range(y):
    GPIO.output(stepper_y_pin_1, True)
    GPIO.output(stepper_y_pin_2, False)
    time.sleep(stepper_y_speed / 1000.0)
    GPIO.output(stepper_y_pin_1, False)
    GPIO.output(stepper_y_pin_2, True)

# Start the main loop
while True:
  # Get the next command from the terminal
  command = raw_input("Enter a command: ")

  # If the command is "move", move the gantry to the specified coordinates
  if command == "move":
    x, y = map(int, command.split(","))
    if x > 0 and y > 0:
      if x > gantry_x_max or y > gantry_y_max:
        print("Cannot move gantry to outside boundaries.")
      else:
        move_gantry(x, y)
    elif x > 0:
      move_gantry(x, 0)
    elif y > 0:
      move_gantry(0, y)
    else:
      print("Cannot move gantry to negative coordinates.")

  # If the command is "quit", exit the program
  if command == "quit":
    break
