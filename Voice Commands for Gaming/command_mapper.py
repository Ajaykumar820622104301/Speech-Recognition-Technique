import pyautogui

# Maps spoken words to keyboard keys
COMMANDS = {
    "jump": "space",
    "shoot": "ctrl",
    "reload": "r",
    "crouch": "c",
    "forward": "w",
    "back": "s",
    "left": "a",
    "right": "d",
    "sprint": "shift",
    "pause": "esc"
}

def execute_command(command):
    key = COMMANDS.get(command.lower())
    if key:
        print(f"Executing: {command} -> {key}")
        pyautogui.press(key)
    else:
        print(f"Command not recognized: {command}")
