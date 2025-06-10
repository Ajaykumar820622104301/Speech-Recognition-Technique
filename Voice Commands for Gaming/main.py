import time
from voice_listener import VoiceListener
from command_mapper import execute_command

def main():
    listener = VoiceListener()
    print("Voice Command Controller for Gaming - Ready!")

    while True:
        command = listener.listen()
        if command:
            execute_command(command)
        time.sleep(0.5)  # Adjust delay to control frequency

if __name__ == "__main__":
    main()
