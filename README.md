## Usage

To use the gantry, you can enter commands at the terminal. The following commands are supported:

* `move <x>, <y>`: Move the gantry to the specified coordinates.
* `quit`: Quit the program.

For example, to move the gantry to the coordinates (10, 20), you would enter the following command:
move 10, 20
## Tips

* The gantry travel limits are defined by the stepper motor steps per revolution and the gantry dimensions.
* The stepper motor speed is defined by the stepper motor steps per second.
* To move the gantry smoothly, you can use a PID controller.

## License

This software is released under the GPLv3 license.
