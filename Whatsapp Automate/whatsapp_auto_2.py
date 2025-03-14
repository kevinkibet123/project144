import pyautogui
import time
import webbrowser


webbrowser.open("https://web.whatsapp.com")
time.sleep(13)  # Wait for WhatsApp Web to load. You can adjust time accordingly.

contact_name = "Recipient's name"  # Change to the group or contact name
pyautogui.click(200, 200)  # Clicks on the search bar (adjust coordinates)
time.sleep(2)
pyautogui.write(contact_name)
time.sleep(2)
pyautogui.press("enter")


message = "Your message here"# In my case, output of the text extraction script
time.sleep(4)
pyautogui.write(message)
pyautogui.press("enter")
time.sleep(2)
#pyautogui.hotkey('ctrl', 'w')# Closes  the current WhatsApp tab on Chrome

print("Message sent successfully!")

