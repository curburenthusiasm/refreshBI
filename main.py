import pyautogui
import time
import logging
from pywinauto import Desktop

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

try:
    # Get list of all open windows
    desktop = Desktop(backend='uia')
    windows = desktop.windows()

    # Filter list to include only the Power BI window
    pbix_windows = [w for w in windows if w.window_text().startswith('Mattress')]

    if not pbix_windows:
        logging.error('No open Power BI reports named "Mattress" found')
        print('No open Power BI reports named "Mattress" found')
    else:
        for pbix_window in pbix_windows:
            # Bring the Power BI window to the foreground
            pbix_window.set_focus()
            time.sleep(1)  # Adding a delay after activation

            if pbix_window.is_active():
                print(f'Activated Power BI Desktop - {pbix_window.window_text()}')

                # Perform your actions here
                print("Pressing Alt")
                pyautogui.keyDown('alt')
                time.sleep(3)
                print("Releasing Alt")
                pyautogui.keyUp('alt')
                time.sleep(3)
                print("Pressing H")
                pyautogui.keyDown('h')
                time.sleep(3)
                print("Releasing H")
                pyautogui.keyUp('h')
                time.sleep(3)
                print("Pressing R")
                pyautogui.keyDown('r')
                time.sleep(3)
                print("Releasing R")
                pyautogui.keyUp('r')
                time.sleep(3)
                print("Done with actions")

            else:
                print(f'Failed to activate Power BI Desktop - {pbix_window.window_text()}')
                logging.error(f'Failed to activate Power BI Desktop - {pbix_window.window_text()}')

except Exception as e:
    print(f'An error occurred: {e}')
    logging.exception("An unhandled error occurred:")

# Now press Enter every 90 seconds indefinitely
while True:
    try:
        print("Pressing Enter")
        pyautogui.press('enter')  # Simulate pressing the Enter key
        print("Enter pressed")
        time.sleep(90)  # Wait for 90 seconds before pressing Enter again
    except Exception as e:
        print(f'An error occurred when pressing Enter: {e}')
        logging.exception("An unhandled error occurred when pressing Enter:")

