from src.constants import ValidUserInput as UserInput
from pynput import keyboard


class PlayerInput():
    """Detect and process player input from keyboard"""

    def __init__(self) -> None:
        """Constructor."""
        self._reset_object_vars()

    def wait_for_user_input(self):
        """Wait for user input. Return tuple with key and flag
        to make other modules update"""

        self._reset_object_vars()

        # Collect events until released
        with keyboard.Listener(on_press=self._on_press) as listener:
            listener.join()

        return (self.key_press_detected, self.key_pressed)

    def _on_press(self, key):
        """Process user input and update object variables accordingly."""

        self.key_press_detected = True

        if "char" in dir(key):
            # handle alphanumeric keys
            switcher = {
                "r": UserInput.KEY_R,
                "q": UserInput.KEY_Q
            }
            self.key_pressed = switcher.get(key.char, UserInput.OTHER)
        else:
            # handle special keys
            switcher = {
                keyboard.Key.left: UserInput.ARROW_LEFT,
                keyboard.Key.right: UserInput.ARROW_RIGHT,
                keyboard.Key.enter: UserInput.ENTER,
            }
            self.key_pressed = switcher.get(key, UserInput.OTHER)

        # stop listener and exit loop
        return False

    def _reset_object_vars(self):
        """Reset object variables back to default values"""

        self.key_press_detected = False
        self.key_pressed = UserInput.OTHER