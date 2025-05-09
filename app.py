from flask import Flask, render_template, request
import pyautogui
import time
import pygetwindow as gw

app = Flask(__name__)

def send_hi_message(contact_name, times):
    # Locate and bring WhatsApp to the front
    windows = gw.getWindowsWithTitle("WhatsApp")
    if windows:
        whatsapp_window = windows[0]
        whatsapp_window.activate()
    else:
        return "WhatsApp is not running. Please open WhatsApp Desktop."

    # Wait for the window to become active
    time.sleep(2)

    # Search for the contact
    pyautogui.hotkey("win", "s") 
    pyautogui.typewrite("WhatsApp")
    time.sleep(2)
    pyautogui.press("enter")  # Type message with increasing repetitions
 # Open search bar in WhatsApp
    time.sleep(1)
    pyautogui.hotkey("ctrl", "f")  # Open search bar in WhatsApp
    time.sleep(1)
    pyautogui.typewrite(contact_name)  # Type the contact's name
    time.sleep(2)
    pyautogui.click(x=357, y=221)  # Select the contact
    # Type and send the message multiple times
    for i in range(1, times + 1):
        time.sleep(1)  # Adjust delay as needed
        pyautogui.typewrite("i😒i")  # Type message with increasing repetitions
        pyautogui.press("enter")  # Send the message

  # Send the message

    return "Messages sent successfully."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    contact_name = request.form.get('contact_name')
    times = request.form.get('times')

    if not contact_name or not times:
        return "Please provide both contact name and times."

    try:
        times = int(times)
    except ValueError:
        return "Times must be a valid number."

    result = send_hi_message(contact_name, times)
    return result

if __name__ == "__main__":
    app.run(debug=True)
