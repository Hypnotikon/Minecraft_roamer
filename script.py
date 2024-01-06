import keyboard
import time
import pyautogui


def mouse(interval):   #Use a food item from the hotbar every 3 minutes.
    if interval % 1800 == 0:
        pyautogui.mouseDown(button='right')
        for i in range(50):
            keyboard.press('w')
            time.sleep(0.1)
        pyautogui.mouseUp(button='right')



def type_w_for_duration(duration_seconds):
    interval = 1
    print(f"i for start, i again for pause, o for end")

    while True:
        if keyboard.is_pressed('o'):  # Check if 'o' key is pressed to exit before starting
            print("end")
            return

        if keyboard.is_pressed('i'):
            time.sleep(0.3)  # Wait for 'i' key press to start
            print(f"start")
            start_time = time.time()

            while (time.time() - start_time) < duration_seconds:
                if keyboard.is_pressed('i'):  # Check if 'k' key is pressed to stop
                    time.sleep(0.3)
                    print("pause")
                    break

                if keyboard.is_pressed('o'):  # Check if 'o' key is pressed to exit
                    print("Exiting...")
                    return

                keyboard.press('w')
                time.sleep(0.1)  # Adjust this delay if needed
                keyboard.release('w')
                interval = interval + 1
                mouse(interval)

if __name__ == "__main__":
    duration = 999999999999  # Duration in seconds to type 'w'
    type_w_for_duration(duration)